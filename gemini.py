from langchain_google_genai import ChatGoogleGenerativeAI

class AI_Model:
    def __init__(self, api_key, model = 'gemini-1.5-pro-latest', temperature = 0.7):   # AI_Model class의 객체 지정 시, model 종류, temperature, api_key를 attribute로 받음
        self.model = model      # Google Gemini: 'gemini-pro'
        self.temperature = temperature      # 기본값: 0.7
        self.api_key = api_key      # API key(예시): "AIzaSyDtPYcEmBSCBmwJdiKHzcJZoLG2zL33KQE"
        self.chat_history = str("")     # 질의응답 내역을 저장하는 str 형식 변수
        self.last_question_no = 0       # 직전 질의응답의 순서를 저장하는 int 변수

    def prepare(self):      # Google Gemini API key 설정 후 ChatGoogleGenerativeAI instance 반환
        self.chat_model = ChatGoogleGenerativeAI(model=self.model, temperature=self.temperature)

    def get_response(self, chain, user_input):      # chain.py 모듈에서 받아온 chain과 user_input을 이용해 Gemini 모델의 답변을 리턴하는 함수
        fin_user_input = "제가 궁금한 점은 다음과 같습니다." + user_input + "과거의 질의응답은 아래와 같으니, 참고하여 답변해주세요. 질문의 번호는 1번 부터 숫자가 커질 수록 최신 질문과 답변입니다. 가능한 숫자가 큰 질문과 답변을 기반으로 답변을 해주세요. \n" + self.chat_history       # chat_history에 저장된 내용을 불러와 user_input에 concat후 invoke

        response = chain.invoke(fin_user_input)     # user_input과 chat_history를 결합한 fin_user_input을 가지고 invoke 수행 -> response 변수로 저장

        self.last_question_no += 1      # 프로그램 실행 중 마지막 질의응답 번호를 기억 후, 새 질문이 입력될 때마다, 1 증가
        self.chat_history += "{self.last_question_no}. 질문: {user_input} \n"       # chat_history에 마지막 질문 번호와 함께 현재 질문 내용 concate 수행
        self.chat_history += "답변: {response} \n\n"        # chat_history에 현재 답변 내용 concate 수행

        return response