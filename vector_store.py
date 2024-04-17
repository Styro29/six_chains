import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma


# 만약 컴퓨터에 GOOGLE_API_KEY가 저장되어있지 않다면 새로 저장하라는 코드
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = ""

loader = WebBaseLoader("")
text = loader.load()
print(text)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=, chunk_overlap=)
splits = text_splitter.split_documents(text)
print(splits)