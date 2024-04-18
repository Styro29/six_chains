from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS


class VectorStore:

    def __init__(self):
        pass


    def text_split(self, data): #크롤링한 데이터를 청크 단위로 split 합니다.
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            length_function=len
        )
        splits = text_splitter.split_documents(data)
        return splits

    def embed_documents(self, splits): #split한 텍스트 청크를 embedding합니다.
        embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        self.vectorstore = FAISS.from_documents(documents=splits, embedding=embedding_model)
        return self.vectorstore # * vectorstore: 생성된 벡터 저장소 객체 (FAISS)

    def store(self, source): # 상위 두개의 함수를 진행하는 함수로, 크롤링한 원본 데이터를 분할하고 임베딩하여 벡터 저장소에 저장합니다.
        splits = self.text_split(source)
        self.vectorstore = self.embed_documents(splits)
        return self.vectorstore


# # Example usage

# crawl = Crawler
# source = crawl.get_data_from_url()
# vector_store = VectorStore()
# vectordb = vector_store.store(source)
# print(vectordb.index_to_docstore_id)