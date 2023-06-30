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

from config import OPENAI_API_KEY # API key for OpenAI model

# This function is used to create and return a vector store, a storage context and an index 
# The index can be created from documents or from an existing vector store
def get_vector_store_index(chroma_collection, documents=None, embed_model=None, service_context=None):
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

# The teaching prompt is a pre-written prompt used to instruct the AI in how to interact with the user
# It's flexible and can be used to shape the AI's response to a wide variety of questions
# It's a helpful tool for creating more context-aware responses from the AI
TEACHING_PROMPT = Prompt(
    "Instructions: As an AI, your role is to provide expert assistance and education on 'Subgrounds' "
    "based on the document information provided below:\n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "When you are asked a question: {query_str}, you should provide detailed explanations, code examples, "
    "and solutions using this knowledge. Strictly adhere to the information, structures, and syntax "
    "present in these documents. Do not create new Fields, Entities, or filter arguments - use only "
    "the ones provided by the user or present in the documents."
    "\n\n"
    "In case of code examples, follow the syntax found in the documents. Do not invent your own examples "
    "or extrapolate beyond the information provided. "
    "Whenever you provide information or code, reference the part of the documentation it was "
    "derived from using the format [Doc Number], Relevance: [Relevance score]'. This way, users can "
    "refer back to the original documents for context and further learning."
    "\n\n"
    "If you provide Subgrounds code or examples, follow the structure and syntax as provided in the documents. "
    "Your role is to assist and educate - avoid inventing or creating new concepts or structures. "
    "Avoid adding any information not present in the documents or provided by the user (hallucinations)."
    "\n\n"
    "Always provide the reference documentation website: https://docs.playgrounds.network/subgrounds/ ."
    "\n\n"
    "Remember your goal: assist, educate, and provide accurate information based on the given documents.\n"
)

# Create a ChromaDB client with settings to use DuckDB implementation and persist data in a directory named "chroma_db"
chroma_client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db"
))

# Retrieve an existing collection or create a new one if it doesn't exist
collection = chroma_client.get_or_create_collection("subgrounds_collection")

# Define embedding model using a HuggingFace transformer model
embed_model = LangchainEmbedding(HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))

# Define the Language Model and its predictor
llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.3, streaming=True)
llm_predictor = LLMPredictor(llm=llm)

# Define service context which holds the AI language model and the language model predictor
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# Check if the collection is empty, if it is then populate it
if collection.count() == 0:
    # Load documents from context_store.md
    documents = SimpleDirectoryReader(input_files=['context_store.md']).load_data()
    
    # Get vector store, storage context, and index and populate the database
    vector_store, storage_context, index = get_vector_store_index(collection, documents, embed_model)
    
    # Persist the data to disk
    chroma_client.persist()

# Get vector store, storage context, and index from the collection
vector_store, storage_context, index = get_vector_store_index(collection, embed_model=embed_model, service_context=service_context)

# Use the created index to query data
# Here the AI is asked to teach about subgrounds, the various ways to query with subgrounds and how to use synthetic fields
# The query engine uses the custom prompt defined earlier and streams the response
query_engine = index.as_query_engine(text_qa_template=TEACHING_PROMPT, streaming=True)
response = query_engine.query("Teach me about subgrounds, the various way to qury with subgrounds and how to use synthetic fields. Give me code examples as well.")
response.print_response_stream()

