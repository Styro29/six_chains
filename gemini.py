from langchain_google_genai import ChatGoogleGenerativeAI

class AI_Model:
    def __init__(self, model = 'gemini-1.5-pro-latest', temperature = 0.7):   # AI_Model class의 객체 지정 시, model 종류, temperature, api_key를 attribute로 받음
        self.model = model      # Google Gemini: 'gemini-pro'
        self.temperature = temperature      # 기본값: 0.7
        self.chat_history = str("")     # 질의응답 내역을 저장하는 str 형식 변수
        self.last_question_no = 0       # 직전 질의응답의 순서를 저장하는 int 변수
        self.chat_model = ChatGoogleGenerativeAI(model=self.model, temperature=self.temperature)    # Google Gemini API key 설정 후 ChatGoogleGenerativeAI instance 반환

    def get_response(self, chain, user_input):      # chain.py 모듈에서 받아온 chain과 user_input을 이용해 Gemini 모델의 답변을 리턴하는 함수
        fin_user_input = "My questions are as follows." + user_input + \
            "Q&A in the past is as follows, so please refer to it and answer it. \
                The number of questions is the latest questions and answers as the number increases from number 1. \
                    Please answer based on the questions and answers with the largest possible number. \n" + self.chat_history       # chat_history에 저장된 내용을 불러와 user_input에 concat후 invoke

        response = chain.invoke(fin_user_input)     # user_input과 chat_history를 결합한 fin_user_input을 가지고 invoke 수행 -> response 변수로 저장

        self.last_question_no += 1      # 프로그램 실행 중 마지막 질의응답 번호를 기억 후, 새 질문이 입력될 때마다, 1 증가
        self.chat_history += "{self.last_question_no}. 질문: {user_input} \n"       # chat_history에 마지막 질문 번호와 함께 현재 질문 내용 concate 수행
        self.chat_history += "답변: {response} \n\n"        # chat_history에 현재 답변 내용 concate 수행

        return response