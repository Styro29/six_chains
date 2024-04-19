**이어드림 스쿨 4기 Langchain 활용 LLM 애플리케이션개발 Project**
- 오프라인 5조 : 김아민, 김지연, 길기현, 박우열, 전성환, 한지원
- 개발 기간 : 24.04.17~ 24.04.19
  
## [소프트웨어 기능 소개]



	**기반 기술**
	1.   text_split(self, data): 
	crawling한 data를 청크 단위로 split 합니다.
		Arguments: 
		- data: 채용 공고를 crawling한 raw data입니다.
		Return
		- splits: data를 chunk 단위로 분할한 문장입니다.

	2.embed_documents(self, splits):
	split한 텍스트 청크를 embedding합니다.
		Arguments: 
		- splits: 고차원 벡터 데이터의 유사성 검색을 수행하는 FAISS를 사용하여 인덱스를 생성한 data입니다.
		Return
		- vectorstore: FAISS를 통해 생성된 벡터 저장소입니다.
