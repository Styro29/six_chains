import os
import logging
from crawler import Crawler
from vector_store import VectorStore
from retrieve import Retriever
from gemini import AI_Model
from chain import Chain

# 로그 설정
logging.basicConfig(filename='app.log', level = logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyCA-bUfCd1Y5A9UDZkDUmsoGKvpnVa4Gmc"
api_key = "AIzaSyCA-bUfCd1Y5A9UDZkDUmsoGKvpnVa4Gmc"

def main():
    try:
        # 크롤링 실행
        logging.info('Crawling started')
        URL = Crawler()
        crawled_data = URL.get_data_from_url()
        logging.info('Crawling completed')

        # 스플릿 실행
        logging.info('Splitting data')
        vector_store = VectorStore()
        splited_data = vector_store.text_split(crawled_data)
        logging.info('Data split completed')

        # 임베드 실행
        logging.info('Embedding documents')
        embeded_data = vector_store.embed_documents(splited_data)
        logging.info('Embedding completed')

        # 임베드 데이터를 가공하여 retriever에 보냄
        logging.info('Retrieving documents')
        retr_creator = Retriever()
        retriever = retr_creator.retrieve(embeded_data, 5)
        logging.info('Retrieving completed')

        # gemini 호출
        logging.info('Initializing Gemini model')
        gemini = AI_Model()

        # 프롬프트 호출하고 체인 만들기
        logging.info('Creating chat chain')
        chain = Chain()
        created_chain = chain.create_chain(gemini.chat_model, retriever)
        logging.info('Chat chain creation completed')

        # while 문으로 계속해서 질문할 수 있도록 구현
        
        while True:
            user_input = input('User: ')
            if user_input == "quit":
                break
            logging.info(f'User input : {user_input}')
            chat_history = gemini.get_response(created_chain, user_input)
            logging.info(f'Gemini response : {chat_history}')
            print(chat_history)

    except Exception as e:
        logging.exception("Exception occured")

if __name__ == "__main__":
    main()