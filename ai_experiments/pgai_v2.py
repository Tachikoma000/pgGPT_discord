import os
import getpass
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA

class AILangChain:
    def __init__(self):
        load_dotenv()
        OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
        if not OPENAI_API_KEY:
            raise ValueError("Missing OpenAI API key!")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        lib_docs_path = os.path.join(current_dir, "lib_docs.md")
        loader = TextLoader(lib_docs_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        embeddings = OpenAIEmbeddings()

        # Check if FAISS index exists, if not create it
        if not os.path.exists("faiss_index"):
            db = FAISS.from_documents(docs, embeddings)
            db.save_local("faiss_index")

        # Load the FAISS vector store
        vectorStore = FAISS.load_local("faiss_index", embeddings)

        llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.2)

        # Use the FAISS vector store to search the local document
        retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k":6})

        TEACHING_PROMPT_TEXT = ("Instructions: As an AI with expertise in 'Subgrounds', your primary goal is to assist and educate users. Generate "
    "queries or provide information based on the Subgrounds document given below, strictly adhering to its guidance. Your responses "
    "should balance accuracy and consistency.\n"
    "---------------------\n"
    "{chat_history}"
    "\n---------------------\n"
    "Consider a user query such as: {question}. Depending on the nature of the request, you should respond in one of two ways:\n\n"
    
    "1. If the user seeks information available in the Subgrounds document, present a detailed explanation using "
    "the document's language. Reference the source as 'Document: [Doc Number], Relevance: [Relevance score]' to allow users "
    "to review the original context. Include the documentation website link: "
    "https://docs.playgrounds.network/subgrounds/ in your response.\n\n"

    "2. If the user needs help crafting a Subgrounds query, generate code emulating the document's examples. Use sg.query_df "
    "to retrieve query results unless instructed otherwise. Again, cite the relevant document references and include the website link "
    "in your response.\n\n"
    
    "Your objective is to provide accurate and consistent information, aiding in the understanding of Subgrounds. Remember, "
    "adherence to the document examples and knowledge is crucial.")


        # QUESTION_PROMPT_TEXT = (
        #     "Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.\n"
        #     "Chat History:\n"
        #     "{chat_history}\n"
        #     "Follow Up Input: {question}\n"
        #     "Standalone question:\n"
        # )

        FULL_PROMPT_TEMPLATE = PromptTemplate.from_template(
            TEACHING_PROMPT_TEXT
        )


        self.qa = ConversationalRetrievalChain.from_llm(llm=llm,
                                                        retriever=retriever, 
                                                        condense_question_prompt=FULL_PROMPT_TEMPLATE, 
                                                        return_source_documents=True, 
                                                        verbose=True)
    
    def ask(self, query):
        chat_history = []
        return self.ask_question_with_context(query, chat_history)
    
    def ask_question_with_context(self, question, chat_history):
        result = self.qa({"question": question, "chat_history": chat_history})
        chat_history = [(question, result["answer"])]
        return chat_history
