import gemini
import crawler
import vector_store
import retriever
import chat
# import sql
# import logger

def main():
    # Gemini API 설정
    gemini_client = gemini.GeminiClient("AIzaSyDs0DbM3ns9rM-KvXfEoVTAcwmlBNMYkc4")

    # KB 구축
    crawler_module = crawler.Crawler()
    documents = crawler_module.crawl_data()  # 문서 데이터 수집 (예: arXiv PDF 다운로드)

    vector_store_module = vector_store.VectorStore()
    vector_store_module.save_documents(documents)  # Vector DB에 문서 저장 (RAG 학습용)

    # QA Engine 실행
    retriever_module = retriever.Retriever(vector_store_module)
    chat_module = chat.Chat(gemini_client, retriever_module, sql.SQLClient())

    while True:
        # 사용자 입력 받기
        user_input = input("사용자 입력: ")

        # LLM 답변 생성
        system_prompt = chat_module.generate_system_prompt(user_input)
        l_response = gemini_client.predict(system_prompt)

        # Retrieve 결과와 함께 LLM 답변 조합
        r_response = retriever_module.retrieve(user_input)
        combined_response = chat_module.combine_responses(l_response, r_response)

        # Chat History 유지
        chat_module.update_chat_history(user_input, combined_response)

        # 답변 출력
        print(f"답변: {combined_response}")

if __name__ == "__main__":
    main()