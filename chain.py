from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# To do List : Input, 프롬포트, 벡터값 받아서 chain 으로 연결해주기

class Chain:
    def __init__(self):       
        self.default_prompt = ChatPromptTemplate(
            input_variables = [ 'context', 'question' ],
            messages = [ HumanMessagePromptTemplate(prompt = PromptTemplate(input_variables = [ 'context', 'question'], \
                                                                            template = "You are a job counselor who helps people get a job in the data field. \
                                                                                Please advise as a senior to those who are struggling to get a job with a data-related job.\
                                                                                It mainly analyzes job postings and shows job postings suitable for the job based on crawled data.\
                                                                                If you ask about job postings, they will guide you through job postings. \
                                                                                    If you ask about a specific job, not a job posting, I can give you a roadmap for a specific job. \
                                                                                        It is particularly important to provide a solution to the problem.\
                                                                                            Based on the previous conversation(chat_history) and context data, \
                                                                                                provide thoughtful and insightful advice about the user's career path in Korean. \
                                                                                            \n Qustion: {question} \n Context: {context} \n Answer:"))
            ]
        )
    
    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def create_chain(self, chat, retrieve):
        chain = ({"context": retrieve | self.format_docs, "question" : RunnablePassthrough()}
                 | self.default_prompt
                 | chat
                 | StrOutputParser()
                 )

        return chain


