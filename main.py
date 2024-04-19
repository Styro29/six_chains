import os
from crawler_old import Crawler
from vector_store import VectorStore
from retrieve import Retriever
from gemini import AI_Model
from chain import Chain

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyCA-bUfCd1Y5A9UDZkDUmsoGKvpnVa4Gmc"
api_key = "AIzaSyCA-bUfCd1Y5A9UDZkDUmsoGKvpnVa4Gmc"

def main():
    # 크롤링 실행
    URL = Crawler()
    crawled_data = URL.get_data_from_url()

    # 스플릿 실행
    vector_store = VectorStore()
    splited_data = vector_store.text_split(crawled_data)

    # 임베드 실행
    embeded_data = vector_store.embed_documents(splited_data)

    # 임베드 데이터를 가공하여 retriever에 보냄
    retr_creator = Retriever()
    retriever = retr_creator.retrieve(embeded_data, 5)

    # gemini 호출
    gemini = AI_Model()

    # 프롬프트 호출하고 체인 만들기
    chain = Chain()
    created_chain = chain.create_chain(gemini.chat_model, retriever)

    # while 문으로 계속해서 질문할 수 있도록 구현
    
    while True:
        user_input = input('User: ')
        if user_input == "quit":
            break
        chat_history = gemini.get_response(created_chain, user_input)
        print(chat_history)



if __name__ == "__main__":
    main()