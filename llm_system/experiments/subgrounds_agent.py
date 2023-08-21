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
    "Instructions: As an AI with expertise in 'Subgrounds', your primary goal is to assist and educate users. Generate "
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
    "adherence to the document examples and knowledge is crucial."
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
llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.2, streaming=True)
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
# query_engine = index.as_query_engine(text_qa_template=TEACHING_PROMPT, streaming=True)
# response = query_engine.query("Teach me about subgrounds, the various way to qury with subgrounds and how to use synthetic fields. Give me code examples as well.")
# response.print_response_stream()

# Use the created index to query data
# Here the AI is asked to teach about subgrounds, the various ways to query with subgrounds and how to use synthetic fields
# The query engine uses the custom prompt defined earlier and streams the response
# chat_engine = index.as_chat_engine(text_qa_template=TEACHING_PROMPT, streaming=True)
# response = chat_engine.chat("write me a subgrounds query to query the mochi_mochi subgraph to query the mochiEarns entiy and the mochiCustomer field. used synthetic fields to divide mochiCustomer by 2")
# response.print_response_stream()

def generate_query(query_str):
    # Use the created index to query data
    # The query engine uses the custom prompt defined earlier and streams the response
    chat_engine = index.as_chat_engine(text_qa_template=TEACHING_PROMPT, streaming=True)
    response = chat_engine.chat(query_str)
    response.print_response_stream()
    return response
