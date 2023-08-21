import os
from dotenv import load_dotenv
from pathlib import Path
import chromadb
from langchain.chat_models import ChatOpenAI
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.llms import ChatMessage, MessageRole
from llama_index import VectorStoreIndex, ServiceContext, download_loader, LLMPredictor, Prompt, SimpleDirectoryReader
from llama_index.embeddings import LangchainEmbedding


class AIChatSystemV2:

    def __init__(self):
        # Initialize the environment variables
        self.load_environment()
        # Initialize the chat system
        self.init_chat_system()

    def load_environment(self):
        """Loads environment variables and checks if the OpenAI API key is present."""
        load_dotenv()
        self.OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
        if not self.OPENAI_API_KEY:
            raise ValueError("Missing OpenAI API key!")
        else:
            # Set the OpenAI API key here
            import openai
            openai.api_key = self.OPENAI_API_KEY

        # Set the source path for the documents
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.source_path = os.path.join(current_dir, "playgrounds_docs_cleaned.md")

    def init_chat_system(self):
        """Initializes the AI chat system components."""
        # Create ChromaDB persistent client with a directory for persistence
        self.chroma_client = chromadb.PersistentClient(path="./chroma_db")
        self.chroma_collection = self.chroma_client.get_or_create_collection("playgrounds_knowledge_base")

        # Define embedding model using a HuggingFace transformer model
        self.embed_model = LangchainEmbedding(
            HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        )

        # Set up ChatOpenAI and LLMPredictor
        self.llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.2, streaming=True)
        self.llm_predictor = LLMPredictor(self.llm)
        
        # Define service context which holds the AI language model and the language model predictor
        self.service_context = ServiceContext.from_defaults(llm_predictor=self.llm_predictor)

        # Check if the collection is empty; if it is, then populate it
        if self.chroma_collection.count() == 0:
            print("Chroma collection is empty. Loading documents...")
            # Load the knowledge base into memory
            self.documents = self.load_knowledge_base()
            # Set up vector store, storage context, and index
            self.vector_store, self.storage_context, self.service_context, self.index = self.setup_indexing()
        else:
            # If the collection is not empty, retrieve the existing vector store and index
            self.vector_store, self.storage_context, self.index = self.get_vector_store_index(self.chroma_collection, embed_model=self.embed_model, service_context=self.service_context)

        # Use the created index to query data
        self.chat_engine = self.index.as_chat_engine(text_qa_template=self.get_teaching_prompt(), streaming=True)

    def load_knowledge_base(self):
        """Load knowledge base data using SimpleDirectoryReader."""
        # Load the knowledge base into memory using SimpleDirectoryReader
        documents = SimpleDirectoryReader(input_files=[self.source_path]).load_data()
        # Print the first few entries for verification
        print(documents[:5])
        return documents


    def setup_indexing(self):
        """Set up ChromaVectorStore, contexts, embed data, and create an index."""
        # Create a Vector Store using the collection
        vector_store = ChromaVectorStore(chroma_collection=self.chroma_collection)
        # Create storage and service contexts
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        service_context = ServiceContext.from_defaults(embed_model=self.embed_model, llm_predictor=self.llm_predictor)
        # Create the index from the documents or directly from the vector store if the documents are empty
        if self.documents:
            index = VectorStoreIndex.from_documents(
                self.documents, storage_context=storage_context, service_context=service_context
            )
        else:
            index = VectorStoreIndex.from_vector_store(vector_store=vector_store, storage_context=storage_context, embed_model=self.embed_model, service_context=service_context)
            
        return vector_store, storage_context, service_context, index

    def get_vector_store_index(self, chroma_collection, embed_model=None, service_context=None):
        """Retrieve the Vector Store and Index from an existing collection."""
        # Create a Vector Store using the collection
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        # Create a storage context for the vector store
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        # Create the index directly from the vector store
        index = VectorStoreIndex.from_vector_store(vector_store=vector_store, storage_context=storage_context, embed_model=embed_model, service_context=service_context)
        # Return all three items
        return vector_store, storage_context, index

    def get_teaching_prompt(self):
        return Prompt(
            "Instructions: You have access to a knowledge base about 'Playgrounds' and 'Subgrounds'. Adhere strictly to this "
            "knowledge base when answering questions. \n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n"
            "Given the user query: {query_str}, provide a detailed and accurate response based on the above context. "
            "If the answer can be derived from the context, reference it as 'Document: [Doc Number], Relevance: [Relevance score]' "
            "and include the documentation website link: https://docs.playgrounds.network/ in your response."
        )

    def chat(self, message):
        """Query the chat engine and return the best response."""
        response = self.chat_engine.chat(message)
        return response.response

        # TEACHING_PROMPT_TEXT = (
        #     "INSTRUCTIONS:\n"
        #     "-------------\n"
        #     "You are an AI expert on 'Subgrounds'. Your mission is to assist, educate, and provide accurate, "
        #     "detailed explanations based on the subgrounds docs:\n"
        #     "---------------------\n"
        #     "Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.\n"
        #     "Chat History:\n"
        #     "{chat_history}\n"
        #     "Follow Up Input: {question}\n"
        #     "Standalone question:\n"
        # )