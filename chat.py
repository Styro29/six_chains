from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class Chat:
    def __init__(self):
        self.default_prompt = ChatPromptTemplate.from_messages(
            [
                ('system', "Give the answer with syntax in the first line, and then explain it.")
                ('human', "You are a data specialist for over 20 years. \
                 Please give advice as seniors to new employees who are thinking about their career path with data jobs. \
                 It is especially important to present the direction of the problem")
            ]
        )

    def chatting(self): # self를 받는게 맞는지?, MessagesPlaceholder 사용해야되는지?
        self.user_input = ""
        
        print("Welcome to 커리어 상담봇!")

        while True:
            # 사용자 질문 입력 받기
            user_input = input("데이터 직무에 대해 궁금한 점을 말씀해주세요!")

            # 사용자가 종료하고자 할 때까지 반복
            if user_input.lower() == 'exit':
                print("대화를 종료합니다.")
                break

if __name__ == "__main__":
    Chat.chatting()
