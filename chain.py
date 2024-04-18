from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# To do List : Input, 프롬포트, 벡터값 받아서 chain 으로 연결해주기

class Chain:
    def __init__(self):       
        self.default_prompt = ChatPromptTemplate(
            input_variables = [ 'context', 'question' ],
            messages = [ HumanMessagePromptTemplate(prompt = PromptTemplate(input_variables = [ 'context', 'question'], \
                                                                            template = "You are a data specialist for over 20 years. \
                                                                                Please give advice as seniors to new employees who are thinking about their career path with data jobs. \
                                                                                    It is especially important to present the direction of the problem")),
                         SystemMessagePromptTemplate(prompt = PromptTemplate(template = "Enter your answer in the first line, followed by any additional explanation."))   # 오류 생기면 줄 삭제
            ]
        )
    
    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def create_chain(self, user_input, chat, retrieve):
        chain = ({"context": retrieve | self.format_docs, "question" : RunnablePassthrough()}
                 | self.default_prompt
                 | chat
                 | StrOutputParser()
                 )

        return chain


