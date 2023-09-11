"""
This module integrates a custom AI language model chain (AILangChainV2) to assist and educate users about 'Subgrounds'. 
The core functionality lies in querying a database of documents using a combination of vector-based and knowledge graph-based 
retrieval methods. The results are then processed through an AI language model to provide human-readable responses.

The AILangChainV2 class initializes the necessary components, including:
1. Loading the document corpus from a file.
2. Setting up embedding functions and node parsers to create a structured representation of the documents.
3. Initializing the language model using OpenAI's API.
4. Loading or creating vector and knowledge graph indices of the documents.
5. Setting up retrievers for vector and knowledge graph searches.
6. Defining a custom prompt template for instructing the language model.
7. Initializing a query engine that combines the retrievers and the AI language model to provide responses to user queries.

Developers should ensure the environment has the 'OPENAI_API_KEY' set up, and be aware of the underlying data structures 
and retrieval mechanisms to effectively utilize and extend the functionalities of this module.
"""

import os
import logging
from llama_hub.file.unstructured.base import UnstructuredReader
from llama_index.node_parser import SimpleNodeParser
from llama_index.llms import OpenAI
from llama_index import (LLMPredictor, StorageContext, SimpleDirectoryReader, 
                         load_index_from_storage, VectorStoreIndex, KnowledgeGraphIndex, 
                         SummaryIndex, get_response_synthesizer, VectorStoreIndex, 
                         ServiceContext, set_global_service_context, QueryBundle, 
                         PromptTemplate)
from llama_index.graph_stores import SimpleGraphStore
from llama_index.vector_stores import ChromaVectorStore
from llama_index.retrievers import (BaseRetriever, VectorIndexRetriever, KGTableRetriever)
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import SentenceTransformerRerank
import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path
from dotenv import load_dotenv
from llama_index.schema import NodeWithScore
from typing import List

# ===================== Logging Setup ======================

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the logging level to DEBUG for detailed logs

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
file_handler = logging.FileHandler('./loggers/pggpt_llm_layer.log')  # Save logs to file
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# ===================== Constants ======================

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        
# ===================== Main Class ======================

class AILangChainV2:
    """The main class that integrates the retrievers and the AI language model."""

    def __init__(self):
        """Initialize components for document retrieval and AI language model interactions."""
        
        if not OPENAI_API_KEY:
            logger.error("Missing OpenAI API key!")
            raise ValueError("Missing OpenAI API key!")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        lib_docs_path = os.path.join(current_dir, "data/playgrounds_docs_with_code_cleaned.txt")
        
        # Load the documents
        loader = UnstructuredReader()
        documents = loader.load_data(file=Path(lib_docs_path))

        # Set up the embedding function and the node parser
        ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name='all-mpnet-base-v2')
        parser = SimpleNodeParser.from_defaults(chunk_size=1024, chunk_overlap=50)
        nodes = parser.get_nodes_from_documents(documents)

        # Initialize the AI language model
        llm = OpenAI(model="gpt-3.5-turbo-16k", temperature=0.3, api_key=OPENAI_API_KEY)
        service_context = ServiceContext.from_defaults(llm=llm, chunk_size=1024, chunk_overlap=50)
        set_global_service_context(service_context)

        # Set up ChromaDB for vector storage
        chroma_client = chromadb.EphemeralClient()
        chroma_collection = chroma_client.get_or_create_collection("playgrounds_body_of_knowledge")
        vector_store = ChromaVectorStore(
            chroma_collection=chroma_collection, 
            embedding_function=ef
        )
        graph_store = SimpleGraphStore()

        # Try to load persisted indexes or create them if they don't exist
        try:
            # Load persisted knowledge graph index
            kg_storage_context = StorageContext(
                docstore=SimpleDocumentStore.from_persist_dir('kg_storage'),
                vector_store=SimpleVectorStore.from_persist_dir('kg_storage'),
                index_store=SimpleIndexStore.from_persist_dir('kg_storage'),
                graph_store=SimpleGraphStore.from_persist_dir('kg_storage')
            )
            self.kg_index = load_index_from_storage(kg_storage_context)

            # Load persisted vector index
            vector_storage_context = StorageContext(
                docstore=SimpleDocumentStore.from_persist_dir('vector_storage'),
                vector_store=SimpleVectorStore.from_persist_dir('vector_storage'),
                index_store=SimpleIndexStore.from_persist_dir('vector_storage'),
                graph_store=SimpleGraphStore.from_persist_dir('vector_storage')
            )
            self.vector_index = load_index_from_storage(vector_storage_context)

        except:
            # If not persisted, create the indexes
            graph_storage_context = StorageContext.from_defaults(graph_store=graph_store)
            vector_storage_context = StorageContext.from_defaults(vector_store=vector_store)

            # Create knowledge graph index
            self.kg_index = KnowledgeGraphIndex.from_documents(
                documents,
                max_triplets_per_chunk=10,
                storage_context=graph_storage_context,
                service_context=service_context,
                include_embeddings=True,
            )

            # Create vector index
            self.vector_index = VectorStoreIndex.from_documents(
                documents,
                storage_context=vector_storage_context,
                service_context=service_context
            )
            # Persist the created indexes
            self.kg_index.storage_context.persist(persist_dir="./storage/kg_storage")
            self.vector_index.storage_context.persist(persist_dir="./storage/vector_storage")

        # Set up retrievers
        vector_retriever = VectorIndexRetriever(index=self.vector_index, similarity_top_k=2)
        kg_retriever = KGTableRetriever(index=self.kg_index, retriever_mode="hybrid", include_text=True)
        custom_retriever = CustomRetriever(vector_retriever, kg_retriever, mode="OR")

        # Define a custom prompt template for instructing the AI language model
        teaching_prompt_text = (
            "As an AI expert in 'Subgrounds', assist and educate users using the Subgrounds document below. Ensure accurate, consistent, and concise responses.\n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n"
            "For a user query like: {query_str}, respond as:\n"
            "1. If seeking document information, explain using its language. Cite as 'Document: [Doc Number], Relevance: [Relevance score]' and include "
            "https://docs.playgrounds.network/subgrounds/.\n"
            "2. If needing a Subgrounds query, emulate document examples using sg.query_df for results. Cite relevant references and include the website link.\n"
            "Adhere closely to the document's content and examples."
        )

        qa_template = PromptTemplate(teaching_prompt_text)
        rerank = SentenceTransformerRerank(model="cross-encoder/ms-marco-TinyBERT-L-2-v2", top_n=5)
        response_synthesizer = get_response_synthesizer(service_context=service_context, text_qa_template=qa_template)
        self.query_engine = RetrieverQueryEngine.from_args(retriever=custom_retriever, response_synthesizer=response_synthesizer)
        logger.info("AILangChainV2 initialized successfully.")

    def ask(self, query):
        """Process a user query using the query engine and return the AI's response."""
        try:
            response = self.query_engine.query(query)
            
            # Ensure the response is structured as expected
            if response is None or not hasattr(response, 'response'):
                error_message = "The AI's response is not structured as expected."
                logger.error(error_message)
                raise ValueError("The AI's response is not structured as expected.")
            
            logger.debug(f"Query: {query} | Response: {response.response}")
            return response.response

        except Exception as e:
            # Handle any exceptions and return a specific error message
            error_message = f"Error occurred while processing the query: {query}. Error: {str(e)}"
            logger.error(error_message)
            return error_message

# ===================== Dependent Classes ======================

class CustomRetriever(BaseRetriever):
    """Custom retriever that performs both Vector search and Knowledge Graph search."""

    def __init__(
        self,
        vector_retriever: VectorIndexRetriever,
        kg_retriever: KGTableRetriever,
        mode: str = "OR",
    ) -> None:
        """Initialize the custom retriever with the given vector and knowledge graph retrievers."""
        self._vector_retriever = vector_retriever
        self._kg_retriever = kg_retriever
        if mode not in ("AND", "OR"):
            raise ValueError("Invalid mode.")
        self._mode = mode

    def _retrieve(self, query_bundle: QueryBundle) -> List[NodeWithScore]:
        """Retrieve nodes given a query bundle using both vector and knowledge graph retrievers."""
        vector_nodes = self._vector_retriever.retrieve(query_bundle)
        kg_nodes = self._kg_retriever.retrieve(query_bundle)

        vector_ids = {n.node.node_id for n in vector_nodes}
        kg_ids = {n.node.node_id for n in kg_nodes}

        combined_dict = {n.node.node_id: n for n in vector_nodes}
        combined_dict.update({n.node.node_id: n for n in kg_nodes})

        if self._mode == "AND":
            retrieve_ids = vector_ids.intersection(kg_ids)
        else:
            retrieve_ids = vector_ids.union(kg_ids)

        retrieve_nodes = [combined_dict[rid] for rid in retrieve_ids]
        logger.debug(f"Retrieved nodes for query: {query_bundle.query}. Node IDs: {retrieve_ids}")
        return retrieve_nodes