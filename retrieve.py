from langchain_chroma import Chroma

class Retriever:
    def __init__(self):
        pass

    def retrieve(self, vec_db, input_prompt, result_num):     # 필요한 변수: vectorDB, chat 모듈에서의 input_prompt
        retr_set = vec_db.as_retriever(k=result_num)        # VectorDB를 변수로 받아 사용자 질문과 가까운 result_num개의 결과 찾기
        retr_result = retr_set.invoke(input_prompt)         # input_prompt와 가까운 답변 invoke
        return retr_result                                  # retrieve 완료된 결과값 반환