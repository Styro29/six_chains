from crawler import Crawler
from vector_store import VectorStore
# import os

# if "GOOGLE_API_KEY" not in os.environ:
#     os.environ["GOOGLE_API_KEY"] = "AIzaSyCA-bUfCd1Y5A9UDZkDUmsoGKvpnVa4Gmc"

def main():

    # 크롤링 함수 실행
    URL = Crawler()
    crawled_data = URL.get_data_from_url()
    
    # 스플릿 함수 실행
    vector_store = VectorStore()
    splited_data = vector_store.text_split(crawled_data)

    # 임베드 실행
    embeded_data = vector_store.embed_documents(splited_data)

    # 임베딩 된 벡터를 vectordb에 저장
    vectordb = vector_store.store(embeded_data)

    print(vectordb)


if __name__ == "__main__":
    main()