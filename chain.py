from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# To do List : Input, 프롬포트, 벡터값 받아서 chain 으로 연결해주기

class Chain:
    def __init__(self):       
        self.default_prompt = ChatPromptTemplate(
            input_variables = [ 'context', 'question' ],
            messages = [ HumanMessagePromptTemplate(prompt = PromptTemplate(input_variables = [ 'context', 'question'], \
                                                                            template = "You are a data specialist with over 20 years of experience helping people find their dream jobs. \
                                                                                Please give advice as seniors to new employees who are thinking about their career path with data jobs. \
                                                                                you can recommend recruitment or give loadmap of specific jobs. \
                                                                                    It is especially important to present the direction of the problem. \
                                                                                        Based on the previous conversation(chat_history) and context data, \
                                                                                            provide thoughtful and insightful advice about the user's career path in Korean. \
                                                                                            \n Qustion: {question} \n Context: {context} \n Answer:"))
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


