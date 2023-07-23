from langchain.document_loaders import TextLoader
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Import the raw md files
markdown_path = "merged_raw_docs.md"
loader = UnstructuredMarkdownLoader(markdown_path)
pg_docs = loader.load()

# This is a long document we can split up.
with open('merged_raw_docs.md') as f:
    docs_pg = f.read()

# perform transformations
text_splitter = CharacterTextSplitter(        
    separator = "\n\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)

texts = text_splitter.create_documents([docs_pg])
print(texts[0])
print(texts[1])
print(texts[99])
print(texts[100])


# documents = SimpleDirectoryReader('merged_raw_docs.md').load_data()

# embed_model = LangchainEmbedding(HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
# llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0, model_kwargs={'api_key': os.getenv('OPENAI_API_KEY')})
# llm_predictor = LLMPredictor(llm=llm)
# service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, chunk_size_limit=512)

# graph_store = SimpleGraphStore()
# storage_context = StorageContext.from_defaults(graph_store=graph_store)

# index = VectorStoreIndex.from_documents(
#     documents,
#     service_context=service_context,
#     show_progress=True
# )

# query_engine = index.as_query_engine(
#     include_text=True, 
#     response_mode="tree_summarize",
#     embedding_mode='hybrid', 
#     retriever_mode='llm',
#     similarity_top_k=5
# )
# response = query_engine.query(
#     "Tell me more about pagination", 
# )

# print(response)