'''
chat.py 구현할 기능
1. 사용자 질문 입력
-> 사용자 질문 형태 카테고리로 제한할지?(카테고리화 한다면 벡터 스토어에 저장도 카테고리대로 저장해야 함.)
2. prompt 설정
3. chat history 저장(최소 5개)
-> 질문 데이터 저장 및 response : gemini.py에서 불러온 후 저장 입력 데이터와 출력 데이터 연결해서
'''

import os
import gemini
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import WebBaseLoader

# 대화 기록을 저장할 파일 경로

class Chat:
    def __init__(self, chat_history_file = "chat_history.txt"):
        self.default_prompt = []
        self.user_input = ""
        self.chat_history_file = chat_history_file
        self.chat_history = self.load_chat_history()
        
    def load_chat_history(self):
        # 대화 기록 파일이 있는 경우, 파일에서 읽어옴
        if os.path.exists(self.chat_history_file): # type: ignore
            with open(self.chat_history_file, 'r') as file:
                chat_history = file.readlines()
            return chat_history
        else:
            return []

    def save_chat_history(self, model, last_qna):
        # 대화 기록을 파일에 저장
        with open(self.chat_history_file, 'a') as file:
            file.writelines(str({'user' : self.user_input, 'chatbot' : model.get_response(default_prompt, user_input)}))


def main(model, retriever):
    C = Chat()

    print("Welcome to ChatBot!")

    while True:
        # 사용자 질문 입력 받기
        user_input = input("이어드림 스쿨에 대해 궁금한 점을 입력하세요!")

        # 사용자가 종료하고자 할 때까지 반복
        if user_input.lower() == 'exit':
            print("대화를 종료합니다.")
            break

        # 프롬포트 설정
        default_prompt = ("system", "At first, Answer only syntax. And then add explanation.")

        model.get_response(default_prompt, user_input)
        retriever()


        # 대화 기록에 추가
        

        # 대화 기록 저장
        C.save_chat_history(last_qna)

if __name__ == "__main__":
    main()
