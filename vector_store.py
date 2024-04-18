from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS


class VectorStore:

    def __init__(self):
        pass


    def text_split(self, data):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            length_function=len
        )
        splits = text_splitter.split_documents(data)
        return splits

    def embed_documents(self, splits):
        embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        self.vectorstore = FAISS.from_documents(documents=splits, embedding=embedding_model)
        return self.vectorstore
\

    def store(self, splits):
        splits = self.text_split(source)
        self.vectorstore = self.embed_documents(splits)
        return self.vectorstore


# # Example usage

# crawl = Crawler
# source = crawl.get_data_from_url()
# vector_store = VectorStore()
# vectordb = vector_store.store(source)
# print(vectordb.index_to_docstore_id)