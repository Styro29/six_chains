
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
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

        vectorstore = FAISS.from_documents(documents=splits, embedding=embedding_model)
        return vectorstore # * vectorstore: 생성된 벡터 저장소 객체 (FAISS)


