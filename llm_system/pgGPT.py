import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import GPT4All
from langchain.chat_models import ChatOpenAI


class AILangChain:
    def __init__(self):
        load_dotenv()
        OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
        if not OPENAI_API_KEY:
            raise ValueError("Missing OpenAI API key!")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        lib_docs_path = os.path.join(current_dir, "data/playgrounds_docs_with_code_cleaned.md")
        loader = TextLoader(lib_docs_path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
        docs = text_splitter.split_documents(documents)

        embeddings = OpenAIEmbeddings()

        # Check if FAISS index exists, if not create it
        if not os.path.exists("faiss_index"):
            db = FAISS.from_documents(docs, embeddings)
            db.save_local("faiss_index")

        # Load the FAISS vector store
        vectorStore = FAISS.load_local("faiss_index", embeddings)

        # model_path = os.path.join(current_dir, "models/wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin")
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)


        # Define the custom prompt template
        TEACHING_PROMPT_TEXT = (
            "Instructions: As an AI with expertise in 'Subgrounds', your primary goal is to assist and educate users. Generate "
            "queries or provide information based on the Subgrounds document given below, strictly adhering to its guidance. Your responses "
            "should balance accuracy and consistency.\n"
            "---------------------\n"
            "{context}"
            "\n---------------------\n"
            "Consider a user query such as: {question}. Depending on the nature of the request, you should respond in one of two ways:\n\n"
            "1. If the user seeks information available in the Subgrounds document, present a detailed explanation using "
            "the document's language. Reference the source as 'Document: [Doc Number], Relevance: [Relevance score]' to allow users "
            "to review the original context. Include the documentation website link: "
            "https://docs.playgrounds.network/subgrounds/ in your response. Ensure your response is as concise as possible, keeping word count low\n\n"
            "2. If the user needs help crafting a Subgrounds query, generate code emulating the document's examples. Use sg.query_df "
            "to retrieve query results unless instructed otherwise. Again, cite the relevant document references and include the website link "
            "in your response. Ensure your response is as concise as possible, keeping word count low\n\n"
            "Your objective is to provide accurate and consistent information, aiding in the understanding of Subgrounds. Remember, "
            "adherence to the document examples and knowledge is crucial.Ensure your response is as concise as possible, keeping word count low"
        )

        FULL_PROMPT = PromptTemplate.from_template(TEACHING_PROMPT_TEXT)

        # Pass the custom prompt template to RetrievalQA
        self.qa = RetrievalQA.from_chain_type(
            llm, 
            retriever=vectorStore.as_retriever(),
            chain_type_kwargs={"prompt": FULL_PROMPT}
        )

    def ask(self, query):
        context = ""  # Initial context is empty
        return self.ask_question_with_context(query, context)
        
    def ask_question_with_context(self, question, context=None):
        context = context or ""  # Set a default value if context is None
        result = self.qa({"query": question, "context": context})
        answer = result.get("result", "Sorry, I couldn't find an answer.")  # Extract the answer from the "result" key
        return [(question, answer)]



