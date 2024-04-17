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
CHAT_HISTORY = "chat_history.txt"

def get_response(question, prompt):
    # gemini.py에서 질문에 대한 응답을 가져오는 함수 # 나중에 gemini보고 수정하기
    return gemini.get_response(question, prompt)

def load_chat_history():
    # 대화 기록 파일이 있는 경우, 파일에서 읽어옴
    if os.path.exists(CHAT_HISTORY):
        with open(CHAT_HISTORY, 'r') as file:
            chat_history = file.readlines()
        return chat_history
    else:
        return []

def save_chat_history(chat_history):
    # 대화 기록을 파일에 저장
    with open(CHAT_HISTORY, 'a') as file:
        file.writelines(chat_history)

def main():
    # 기존 대화 기록 불러오기
    chat_history = load_chat_history()

    print("Welcome to ChatBot!")

    while True:
        # 사용자 질문 입력 받기
        user_question = input("이어드림 스쿨에 대해 궁금한 점을 입력하세요!")

        # 사용자가 종료하고자 할 때까지 반복
        if user_question.lower() == 'exit':
            print("대화를 종료합니다.")
            break

        # 프롬포트 설정
        prompt = ("system", "At first, Answer only syntax. And then add explanation.")

        # gemini.py를 사용하여 사용자 질문에 대한 응답 가져오기
        response = get_response(user_question, prompt)

        # 대화 기록에 추가
        chat_history.append(f"User: {user_question}\n")
        chat_history.append(f"ChatBot: {response}\n")

        # 대화 출력
        print("ChatBot:", response)

        # 대화 기록 저장
        save_chat_history(chat_history)

if __name__ == "__main__":
    main()
