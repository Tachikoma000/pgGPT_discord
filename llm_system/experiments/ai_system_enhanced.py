import os
import chromadb  
from langchain.chat_models import ChatOpenAI  
from llama_index.vector_stores import ChromaVectorStore  
from llama_index import Prompt, VectorStoreIndex, SimpleDirectoryReader
from llama_index.storage.storage_context import StorageContext  
from langchain.embeddings.huggingface import HuggingFaceEmbeddings  
from llama_index import LangchainEmbedding, ServiceContext, LLMPredictor
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import initialize_agent
from llama_index.langchain_helpers.agents import LlamaToolkit, create_llama_chat_agent, IndexToolConfig
from dotenv import load_dotenv
from config import OPENAI_API_KEY 

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

class SubgroundsAgent:

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
    "Remember your goal: assist, educate, and provide accurate information based on the given documents.\n")

    def __init__(self):
        self.chroma_client = self._initialize_chroma_client()
        self.collection = self._get_or_create_collection()
        self.embed_model = self._initialize_embedding_model()
        self.llm, self.llm_predictor = self._initialize_language_model()
        self.service_context = self._initialize_service_context()
        self.vector_store, self.storage_context, self.index = self._initialize_vector_store_index()
        self.memory = self._initialize_memory()
        self.toolkit = self._initialize_toolkit()
        self.agent_chain = self._initialize_agent_chain()

    def _initialize_chroma_client(self):
        return chromadb.PersistentClient(path="./chroma_db")

    def _get_or_create_collection(self):
        return self.chroma_client.get_or_create_collection("subgrounds_collection")

    def _initialize_embedding_model(self):
        return LangchainEmbedding(HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))

    def _initialize_language_model(self):
        if not OPENAI_API_KEY:
            raise ValueError("Please set the OPENAI_API_KEY environment variable.")
        llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.3, streaming=True, openai_api_key=OPENAI_API_KEY)
        llm_predictor = LLMPredictor(llm=llm)
        return llm, llm_predictor

    def _initialize_service_context(self):
        return ServiceContext.from_defaults(llm_predictor=self.llm_predictor)

    def _initialize_vector_store_index(self):
        if self.collection.count() == 0:
            documents = SimpleDirectoryReader(input_files=['merged_raw_docs.md']).load_data()
            vector_store, storage_context, index = get_vector_store_index(self.collection, documents, self.embed_model)
        else:
            vector_store, storage_context, index = get_vector_store_index(self.collection, embed_model=self.embed_model, service_context=self.service_context)
        return vector_store, storage_context, index

    def _initialize_memory(self):
        return ConversationBufferMemory(memory_key="chat_history")

    def _initialize_toolkit(self):
        index_tool_config = IndexToolConfig(
            query_engine=self.index.as_query_engine(text_qa_template=self.TEACHING_PROMPT, streaming=True), 
            name="Subgrounds Index",
            description="Useful for answering questions about Subgrounds",
            tool_kwargs={"return_direct": True}
        )
        return LlamaToolkit(index_configs=[index_tool_config])

    def _initialize_agent_chain(self):
        return create_llama_chat_agent(
            self.toolkit,
            self.llm,
            memory=self.memory,
            verbose=True,
            streaming=True
        )

    def chat(self):
        while True:
            user_input = input("User: ")
            if user_input.lower() == "quit":
                break
            response = self.agent_chain.run(input=user_input)
            print(f'Agent: {response}')


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


if __name__ == "__main__":
    agent = SubgroundsAgent()
    agent.chat()
