import os
import getpass
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

def ask_question(qa, question):
    result = qa({"query": question})
    print("Question:", question)
    print("Answer:", result["result"])

def ask_question_with_context(qa, question, chat_history):
    query = "what is Subgrounds?"
    result = qa({"question": question, "chat_history": chat_history})
    print("answer:", result["answer"])
    chat_history = [(query, result["answer"])]
    return chat_history


loader = TextLoader("lib_docs.md")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

db = FAISS.from_documents(docs, embeddings)
db.save_local("faiss_index")

# Initialize gpt-35-turbo and our embedding model
#load the faiss vector store we saved into memory
vectorStore = FAISS.load_local("faiss_index", embeddings)

llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)

#use the faiss vector store we saved to search the local document
retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k":2})

QUESTION_PROMPT = PromptTemplate.from_template(
    """
    Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.
    
    Chat History:
    {chat_history}
    
    Follow Up Input: {question}
    Standalone question:
    """)

qa = ConversationalRetrievalChain.from_llm(llm=llm,
                                           retriever=retriever, 
                                           condense_question_prompt=QUESTION_PROMPT, 
                                           return_source_documents=True, 
                                           verbose=False)

chat_history = []
while True:
    query = input('you: ')
    if query == 'q':
        break
    chat_history = ask_question_with_context(qa, query, chat_history)