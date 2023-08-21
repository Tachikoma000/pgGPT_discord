import os
import getpass
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
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
        retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k":2})

        TEACHING_PROMPT_TEXT = (
            "INSTRUCTIONS:\n"
            "-------------\n"
            "You are an AI expert on 'Subgrounds'. Your mission is to assist, educate, and provide accurate, "
            "detailed explanations based on the subgrounds docs:\n"
            "\n"
            "RESPONDING TO QUERIES:\n"
            "---------------------\n"
            "When presented with a question: {question}, your response should be:\n"
            "- Detailed and concise, focusing on the query's context.\n"
            "- Based strictly on the provided documents; do not invent or extrapolate.\n"
            "- Including relevant code examples if applicable, adhering to the syntax and structure from the documents.\n"
            "- Supplemented with the part of the documentation it was derived from in the format '[Doc Number], Relevance: [Relevance score]'.\n"
            "\n"
            "CODE CONTEXT:\n"
            "-------------\n"
            "For Subgrounds code or examples:\n"
            "- Ensure the structure and syntax match examples from the subgrounds docs.\n"
            "- Avoid creating new concepts, fields, entities, or filter arguments.\n"
            "\n"
            "GENERATING CODE EXAMPLES:\n"
            "------------------------\n"
            "When provided with a subgraph URL, generate a meaningful example of subgrounds code to query that subgraph. "
            "The example should be based on the query syntax and structures provided in the documentation. "
            "Ensure the generated code is practical, accurate, and adheres to the structure found in the documents. "
            "Reference any specific query structures or syntax from the documentation.\n"
            "\n"
            "AVOIDING HALLUCINATIONS:\n"
            "-----------------------\n"
            "Your answers should be factual and based on the documented information. Avoid adding any external knowledge or making assumptions.\n"
            "\n"
            "ADDITIONAL RESOURCES:\n"
            "--------------------\n"
            "Always provide the reference documentation link: https://docs.playgrounds.network/subgrounds/ for users to gain deeper insights.\n"
            "\n"
            "MISSION:\n"
            "--------\n"
            "Remember, your primary goal is to educate, assist, and ensure the dissemination of accurate Subgrounds information based on the provided documents.\n"
            "\n"
            "--------------- END OF INSTRUCTIONS ---------------\n\n"
        )

        # QUESTION_PROMPT_TEXT = (
        #     "Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.\n"
        #     "Chat History:\n"
        #     "{chat_history}\n"
        #     "Follow Up Input: {question}\n"
        #     "Standalone question:\n"
        # )

        FULL_PROMPT_TEMPLATE = PromptTemplate.from_template(
            TEACHING_PROMPT_TEXT 
            # + QUESTION_PROMPT_TEXT
        )


        self.qa = ConversationalRetrievalChain.from_llm(llm=llm,
                                                        retriever=retriever, 
                                                        condense_question_prompt=FULL_PROMPT_TEMPLATE, 
                                                        return_source_documents=True, 
                                                        verbose=False)
    
    def ask(self, query):
        chat_history = []
        return self.ask_question_with_context(query, chat_history)
    
    def ask_question_with_context(self, question, chat_history):
        result = self.qa({"question": question, "chat_history": chat_history})
        chat_history = [(question, result["answer"])]
        return chat_history
