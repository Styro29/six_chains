import os
# from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
# from langchain_core.messages import HumanMessage, SystemMessage
# from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_chroma import Chroma

class AI_Model:
    def __init__(self, model: str, temperature: float, api_key: str):   # AI_Model class의 객체 지정 시, model 종류, temperature, api_key를 attribute로 받음
        self.model = model      # Google Gemini: 'gemini-pro'
        self.temperature = temperature      # 기본값: 0.7
        self.api_key = api_key      # API key(예시): "AIzaSyDtPYcEmBSCBmwJdiKHzcJZoLG2zL33KQE"

    def prepare(self):      # Google Gemini API key 설정 후 ChatGoogleGenerativeAI class 반환
        if "GOOGLE_API_KEY" not in os.environ:
            os.environ["GOOGLE_API_KEY"] = self.api_key

        self.chat = ChatGoogleGenerativeAI(model=self.model, temperature=self.temperature)

        # return ChatGoogleGenerativeAI(model=self.model, temperature=self.temperature)
    
################ 테스트용 코드 ##################

# gemini = AI_Model('gemini-pro', 0.7, "AIzaSyDtPYcEmBSCBmwJdiKHzcJZoLG2zL33KQE")
# gemini.prepare()
# response = gemini.chat.invoke(input=input("User: "))
# print(response.content)