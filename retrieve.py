class Retriever:
    def __init__(self):
        pass

    def retrieve(self, vec_db, result_num):     # 필요한 변수: vec_db -> vectorDB, result_nim -> retrieve 출력 개수
        retriever = vec_db.as_retriever(search_type="mmr", search_kwargs={'k': result_num, 'fetch_k': 50})        # VectorDB를 입력받아 retriever 인스턴스 생성
        return retriever                                     # 생성된 retriever 인스턴스 반환