# ai_chat_system.py

# Importing necessary libraries and modules
import os
import chromadb  # Database management library
from chromadb.config import Settings  # Configuration settings for ChromaDB
from langchain.chat_models import ChatOpenAI  # OpenAI model for conversational AI
from llama_index.vector_stores import ChromaVectorStore  # Vector store for embeddings
from llama_index import Prompt, VectorStoreIndex, SimpleDirectoryReader  # Data indexing and reading modules
from llama_index.storage.storage_context import StorageContext  # Storage context for vector stores
from langchain.embeddings.huggingface import HuggingFaceEmbeddings  # HuggingFace based embedding models
from llama_index import LangchainEmbedding, ServiceContext, LLMPredictor  # Context, prediction and embedding models for Langchain
from dotenv import load_dotenv
# from config import OPENAI_API_KEY # API key for OpenAI model

class AIChatSystem:

    def __init__(self):
        load_dotenv()
        OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
        if not OPENAI_API_KEY:
            raise ValueError("Missing OpenAI API key!")
        
        self.init_chat_system()

    def init_chat_system(self):
        # Create a ChromaDB client using the new method
        self.chroma_client = chromadb.PersistentClient(path="./chroma_db")

        # Retrieve an existing collection or create a new one if it doesn't exist
        self.collection = self.chroma_client.get_or_create_collection("subgrounds_collection")

        # Define embedding model using a HuggingFace transformer model
        self.embed_model = LangchainEmbedding(HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))

        # Define the Language Model and its predictor
        self.llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.2, streaming=True)
        self.llm_predictor = LLMPredictor(llm=self.llm)

        # Define service context which holds the AI language model and the language model predictor
        self.service_context = ServiceContext.from_defaults(llm_predictor=self.llm_predictor)

        # Check if the collection is empty, if it is then populate it
        if self.collection.count() == 0:
            # Load documents from context_store.md
            documents = SimpleDirectoryReader(input_files=['context_store.md']).load_data()
    
            # Get vector store, storage context, and index and populate the database
            self.vector_store, self.storage_context, self.index = self.get_vector_store_index(self.collection, documents, self.embed_model, self.service_context)
    
            # Persist the data to disk
            self.chroma_client.persist()

        # Get vector store, storage context, and index from the collection
        self.vector_store, self.storage_context, self.index = self.get_vector_store_index(self.collection, embed_model=self.embed_model, service_context=self.service_context)

        # Use the created index to query data
        self.chat_engine = self.index.as_chat_engine(text_qa_template=self.get_teaching_prompt(), streaming=True)

    def get_teaching_prompt(self):
        # The teaching prompt is a pre-written prompt used to instruct the AI in how to interact with the user
        return Prompt("Instructions: As an AI with expertise in 'Subgrounds', your primary goal is to assist and educate users. Generate "
    "queries or provide information based on the Subgrounds document given below, strictly adhering to its guidance. Your responses "
    "should balance accuracy and consistency.\n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Consider a user query such as: {query_str}. Depending on the nature of the request, you should respond in one of two ways:\n\n"
    
    "1. If the user seeks information available in the Subgrounds document, present a detailed explanation using "
    "the document's language. Reference the source as 'Document: [Doc Number], Relevance: [Relevance score]' to allow users "
    "to review the original context. Include the documentation website link: "
    "https://docs.playgrounds.network/subgrounds/ in your response.\n\n"

    "2. If the user needs help crafting a Subgrounds query, generate code emulating the document's examples. Use sg.query_df "
    "to retrieve query results unless instructed otherwise. Again, cite the relevant document references and include the website link "
    "in your response.\n\n"
    
    "Your objective is to provide accurate and consistent information, aiding in the understanding of Subgrounds. Remember, "
    "adherence to the document examples and knowledge is crucial.")

    def get_vector_store_index(self, chroma_collection, documents=None, embed_model=None, service_context=None):
        # Create a Vector Store using the collection
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        # Create a storage context for the vector store
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        # If documents are provided, create an index from the documents
        # If not, create the index directly from the vector store
        if documents:
            index = VectorStoreIndex.from_documents(documents, storage_context=storage_context, embed_model=embed_model, service_context=service_context)
        else:
            index = VectorStoreIndex.from_vector_store(vector_store=vector_store, storage_context=storage_context, embed_model=embed_model, service_context=service_context)
        # Return all three items
        return vector_store, storage_context, index

    def chat(self, message):
        response = self.chat_engine.chat(message)
        return response.get_best_response()
