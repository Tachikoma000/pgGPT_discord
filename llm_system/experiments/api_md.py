# Import necessary libraries and modules
import os
import re
import numpy as np
import openai
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors
from uuid import uuid4
from config import OPENAI_API_KEY

# Import required classes from llama_index
from llama_index import SimpleDirectoryReader, Document
from llama_index.node_parser import SimpleNodeParser
from llama_index import VectorStoreIndex, ServiceContext, SimpleDirectoryReader, Document

# Suppress TensorFlow logging messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Define the SemanticSearch class which utilizes the SentenceTransformer library
'''
The SemanticSearch class is used to create a semantic search engine using the SentenceTransformer library.
The fit method takes the data and fits it to a K-nearest neighbors model. The __call__ method encodes the input
text and finds the nearest neighbors for this encoding in the fitted data. The number of neighbors is determined 
by the n_neighbors parameter. 
'''
class SemanticSearch:
    # Initialize the transformer model on class instantiation
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.fitted = False

    # Fit method for training the model
    def fit(self, data, n_neighbors=5):
        self.data = data
        self.embeddings = self.model.encode(data)
        n_neighbors = min(n_neighbors, len(self.embeddings))
        self.nn = NearestNeighbors(n_neighbors=n_neighbors)
        self.nn.fit(self.embeddings)
        self.fitted = True

    # Define call method for the class
    def __call__(self, text, return_data=True):
        inp_emb = self.model.encode([text])
        neighbors = self.nn.kneighbors(inp_emb, return_distance=False)[0]

        if return_data:
            return [self.data[i] for i in neighbors]
        else:
            return neighbors
        
# Define a child class of SemanticSearch that uses the Llama Index library
'''
The SemanticSearchLlamaIndex class is a subclass of SemanticSearch that utilizes the Llama
Index library to read documents, parse them into nodes, and build an index from these nodes.
'''
class SemanticSearchLlamaIndex(SemanticSearch):
    def __init__(self, docs):
        super().__init__()
        # Configure a node parser
        parser = SimpleNodeParser.from_defaults(
            chunk_size=512, 
            include_metadata=False, 
            include_prev_next_rel=False
        )

        # Parse document into Node objects
        nodes = parser.get_nodes_from_documents(docs)

        # Build index from Node objects
        index = VectorStoreIndex(nodes)
        self.data = [node.text for node in nodes]

    def fit(self, n_neighbors=5):
        self.embeddings = self.model.encode(self.data)
        n_neighbors = min(n_neighbors, len(self.embeddings))
        self.nn = NearestNeighbors(n_neighbors=n_neighbors)
        self.nn.fit(self.embeddings)
        self.fitted = True

# Preprocess text by replacing newline characters and condensing multiple spaces into one
'''
The preprocess function replaces newline characters with spaces and condenses multiple spaces
into a single space.
'''
def preprocess(text):
    text = text.replace('\n', ' ')
    text = re.sub('\s+', ' ', text)
    return text

# Read a markdown file, preprocess the text, and return a Document object
'''
The read_md_file function opens a Markdown file, preprocesses the text inside, and 
returns a Document object.
'''
def read_md_file(path):
    with open(path, 'r') as file:
        text = preprocess(file.read())
    # Assuming the title of the document is the filename without the extension
    title = os.path.basename(path).split('.')[0]
    return Document(
        id=str(uuid4()),  # Generate a unique ID
        title=title,
        text=text,
    )

# Load a recommender model from a markdown file
# The load_recommender function creates a semantic search model from a given Markdown file.
def load_recommender(md_file_path):
    # Here, documents is a list of Document objects
    documents = [read_md_file(md_file_path)]
    recommender = SemanticSearchLlamaIndex(documents)
    recommender.fit()
    return recommender

# Generate text using OpenAI's API
def generate_text(openAI_key, prompt, engine="gpt-3.5-turbo"):
    openai.api_key = openAI_key
    try:
        response = openai.ChatCompletion.create(
            model=engine,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        if 'choices' in response and len(response['choices']) > 0:
            message = response['choices'][0]['message']['content']
    except Exception as e:
        message = f'API Error: {str(e)}'
    return message

# Generate an answer to a question using a recommender model and OpenAI
# The generate_answer function uses the semantic search model to find relevant information and feeds this to OpenAI to generate an answer.
def generate_answer(question, recommender, openAI_key):
    topn_chunks = recommender(question)
    prompt = ""
    prompt += 'search results:\n\n'
    for c in topn_chunks:
        prompt += c + '\n\n'
        
    prompt += (
        "Instructions: As an AI, your role is to assist and educate users about Subgrounds. You possess expert "
        "knowledge based on the information contained in the provided search results. When asked questions, use "
        "this knowledge to provide detailed explanations, code examples, and solutions. It's important to stick "
        "strictly to the information, structures, and syntax present in the documents. This includes not creating "
        "new Fields, Entities, or filter arguments on your own. Instead, only use the ones that the user provides. "
        "\When asked for code examples, it's essential that you follow the examples and syntax found in the search "
        "results. Do not invent your own examples or extrapolate beyond the information provided in the search "
        "results. "
        "\Whenever you provide information or code, ensure you reference the part of the documentation it was "
        "derived from using [Reference Number] notation. This way, the user can study the original document to "
        "understand the context and gain more knowledge. "
        "When providing subgrounds code examples or subgrounds code, ensure you follow the structure as provided below:"
        "\n code "
        "Your goal is to assist and educate, not to invent or create new concepts or structures. Please remember to "
        "avoid adding any information not present in the documents or provided by the user (hallucinations)."
        "When referencing the docs website, iy must be https://docs.playgrounds.network/subgrounds/"
        "\n\n"
    )

    prompt += f"Query: {question}\nAnswer:"
    answer = generate_text(openAI_key, prompt, "gpt-3.5-turbo")
    return answer

# Load the OpenAI API key
def load_openai_key() -> str:
    if OPENAI_API_KEY is None:
        raise ValueError(
            "[ERROR]: Please pass your OPENAI_API_KEY. Get your key here : https://platform.openai.com/account/api-keys"
        )
    return OPENAI_API_KEY

# Generate an answer to a query using a markdown file as a knowledge base
# The get_markdown function creates a semantic search model from a Markdown file and uses it to generate an answer to a query using OpenAI.
def get_markdown(query):
    md_file_path = 'context_store.md'
    recommender = load_recommender(md_file_path)
    openAI_key = load_openai_key()
    answer = generate_answer(query, recommender, openAI_key)
    return answer

query = "what is subgrounds? how can i use synthetic fields? what are some pagination strategies when using subgrounds?"
answer = get_markdown(query)
print(answer)
