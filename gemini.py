import os
# from langchain_community.document_loaders import WebBaseLoader
from langchain.chains import ConversationChain  # 대화형 체인을 생성하는 라이브러리
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
# from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser   # response의 content 내용만 추출하는 외부 라이브러리
from langchain_core.runnables import RunnablePassthrough
from langchain.memory import ConversationBufferMemory   # 기존 질문과 답변을 누적하여 저장하는 외부 라이브러리

class AI_Model:
    def __init__(self, api_key, model = 'gemini-1.5-pro-latest', temperature = 0.7):   # AI_Model class의 객체 지정 시, model 종류, temperature, api_key를 attribute로 받음
        self.model = model      # Google Gemini: 'gemini-pro'
        self.temperature = temperature      # 기본값: 0.7
        self.api_key = api_key      # API key(예시): "AIzaSyDtPYcEmBSCBmwJdiKHzcJZoLG2zL33KQE"

    def prepare(self):      # Google Gemini API key 설정 후 ChatGoogleGenerativeAI class 반환
        if "GOOGLE_API_KEY" not in os.environ:
            os.environ["GOOGLE_API_KEY"] = self.api_key

        self.chat = ChatGoogleGenerativeAI(model=self.model, temperature=self.temperature)

    def get_response(self, default_prompt, user_input, retriever):
        output_parser = StrOutputParser()
        
        chat_memory = ConversationBufferMemory()
        conv_chain = ConversationChain(
            memory=chat_memory, 
            prompt=default_prompt, 
            retriever=retriever, 
            verbose=False
        )

        response = conv_chain.predict(user_input)

        return response
    
################ 테스트용 코드 ##################
gemini = AI_Model("AIzaSyDtPYcEmBSCBmwJdiKHzcJZoLG2zL33KQE", 'gemini-pro', 0.7)
gemini.prepare()
response = gemini.get_response(("system", "At first, Answer only syntax. And then add explanation."), "Which color does an apple have?")