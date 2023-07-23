# ai_system.py
import chromadb
from chromadb.config import Settings
from langchain.chat_models import ChatOpenAI
from llama_index.vector_stores import ChromaVectorStore
from llama_index import Prompt, VectorStoreIndex, SimpleDirectoryReader
from llama_index.storage.storage_context import StorageContext
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import LangchainEmbedding, ServiceContext, LLMPredictor
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

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
    "{context_str}\n"
    "---------------------\n"
    "You are an AI with expertise in 'Subgrounds'. Your task is to assist and educate users based on the context provided above. "
    "For a user query such as: '{query_str}', you should respond as follows:\n\n"

    "1. If the user seeks information available in the context, use what you learn from the context to provide meaningful explanation. "
    "Cite the source as 'Document: [Doc Number], Relevance: [Relevance score]' "
    "and include the documentation website link: https://docs.playgrounds.network/subgrounds/ in your response.\n\n"

    "2. If the user needs help crafting a Subgrounds query, use the context as a guide to generate subgrounds code. "
    "Use sg.query_df to retrieve query results unless instructed otherwise. Cite the relevant document references "
    "and include the website link in your response.\n\n"

    "Your objective is to provide accurate and consistent information, aiding in the understanding of Subgrounds. "
    "Your responses should be as concise as possible. Now, respond to the user query."
)

def setup_chat_engine():
    try:
        chroma_client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory="../chroma_db"
        ))

        collection = chroma_client.get_or_create_collection("subgrounds_collection")
        embed_model = LangchainEmbedding(HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
        llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.2, model_kwargs={'api_key': os.getenv('OPENAI_API_KEY')})
        llm_predictor = LLMPredictor(llm=llm)
        service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

        if collection.count() == 0:
            # Load documents from context_store.md
            documents = SimpleDirectoryReader(input_files=['../raw_files/merged_raw_docs.md']).load_data()

            # Get vector store, storage context, and index and populate the database
            vector_store, storage_context, index = get_vector_store_index(collection, documents, embed_model)
            chroma_client.persist()

        vector_store, storage_context, index = get_vector_store_index(collection, embed_model=embed_model, service_context=service_context)

        chat_engine = index.as_chat_engine(text_qa_template=TEACHING_PROMPT)

        return chat_engine

    except Exception as e:
        print(f"An error occurred while setting up the AI system: {e}")
        raise  # Re-raise the exception after logging it

