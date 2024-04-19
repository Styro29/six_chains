# 이어드림 스쿨 4기 5팀의 LangChain 프로젝트 six_chains
### 김아민, 김지연, 길기현, 박우열, 전성환, 한지원

![6-chains](https://github.com/Styro29/six_chains/assets/133292854/232724ea-af0a-4465-aa85-459e78e4f662)


# 소프트웨어 기능 소개
![Class diagram](https://github.com/Styro29/six_chains/assets/133292854/1ce8c041-7bef-416d-bf2a-96f6dc5a3544)



# 모듈별 기능
## main.py
`crawler.py` : urls.txt에서 데이터 크롤링<br> 
`vector_store.py` : 크롤링된 데이터를 chunk 단위로 split하고 임베딩하여 VectorDB에 저장<br>
`gemini.py` : gemini를 호출하고 입출력 데이터의 히스토리를 저장<br> 
`chain.py` : 문자열로 출력하는 랭체인 생성<br> 
`gemini.py` : gemini의 프롬프트를 정해주고 생성된 프롬프트와 Gemini<br> 
다섯개의각 모듈을 import하고 모듈별로 내장된 함수를 호출하여 기능을 구현합니다.


## crawler.py
1. `get_data_from_url(self, url_file="urls.txt", save_dir=os.path.dirname(__file__)):

	- Data crawling을 위해 url들이 명시된 urls.txt 파일을 이용해서 URL로더에 입력 파라메터로 넘겨서 로딩을 해줍니다.

	- 크롤링이 진행되면 현재 디렉토리 내에 text_data가 있는지 확인 후, 
		1. 데이터가 없으면 UnstructuredURLLoader를 이용하여 download 후, 다운로드한 데이터를 pickle을 이용하여 {text_data} binary file 로 저장해 줍니다.
		2. 이때 동시에 생성된 {text_data_check.txt} 파일은 테스트시, 받아온 데이터 확인용으로 사용됩니다. 

	- 만약, 이전에 받았던 crawling data가 이미 있을 경우에는 다시 url crawling을 하지않고, saved 된 text_data를 로딩하여 더 빠르게 user input을 받게 실행 됩니다.

	- 이렇게 다운로드 받거나 로딩된 raw data 를 최종적으로 return 해줍니다.

	- 만약, url에 문제가 있거나 다운로드 과정에서 문제가 발생하여 데이터를 못 받아오게 되면,
		1. "Error: Failed to load text data from URLS." 를 출력하게 됩니다.


## gemini.py
1. `AI_Model(self, model, temperature)`:** <br>
	'AI_Model' 클래스는 객체 생성 시, model 종류와 모델의 temperature 값을 입력 받아 클래스 내부 변수 'chat_model'에 ChatGoogleGenerativeAI 인스턴스를 할당합니다.<br>
	클래스 내부 변수로 'chat_history'에는 사용자 입력 질문 'user_input', 그리고 'get_response()' 함수에서 생성된 답변을 str 형식으로 저장합니다.<br>
	'last_question_no'는 현재 사용자가 마지막으로 입력한 질문과 답변의 순서를 int 형식으로 저장합니다.
	클래스 내장 함수 'get_response()'는 language chain을 입력 받고, 사용자 입력 질문인 'user_input'과 기존 질의응답 내역인 'chat_history'를 결합하여 language chain에 invoke를 수행합니다. <br>
	또한, invoke 수행 후 생성된 답변 'response'와 'user_input'을 클래스 내장 변수 'chat_history'에 저장합니다.

	Arguments:
	- `model` (str) -> optional : *Google Gemini의 세부 모델명(기본값: 'gemini-1.5-pro-latest')*
	- `temperature` (float) -> optional : *언어 모델의 temperature(기본값: 0.7)*
	
	Internal variables:
	- `self.chat_history` (str) : *사용자의 질문(user_input)과 모델의 답변(response)을 저장*
	- `self.last_question_no` (int) : *현재 사용자가 마지막으로 입력한 질문과 답변의 순서를 저장*
	- `self.chat_model` (obj) : *ChatGoogleGenerativeAI 인스턴스 객체*

<br/>

2.`get_response(self, chain, user_input)`:*** <br>
	Arguments:
	- `chain` (obj) :  *invoke를 수행할 생성된 chain*
	- `user_input` (str) : *사용자가 입력한 질문*
	
	Returns:
	- `response` (str) : *Gemini API를 통해 생성된 답변 내용*
	<br>
	<br>


 
## vector-store.py
1. `text_split(self, data)`: 
	crawling한 data를 청크 단위로 split 합니다.

	Arguments
	- `data`: 채용 공고를 crawling한 raw data입니다.

	Return
	- `splits`: data를 chunk 단위로 분할한 문장입니다.
<br>

2. `embed_documents(self, splits):`
	split한 텍스트 청크를 embedding합니다.

	- `splits`: 고차원 벡터 데이터의 유사성 검색을 수행하는 FAISS를 사용하여 인덱스를 생성한 data입니다.
	- `vectorstore`: FAISS를 통해 생성된 벡터 저장소입니다.


## retriever.py
- 기반 기술
    - …
- 예시 입력
    - …
- 예시 결과



## chain.py
- 기반 기술
    - …
- 예시 입력
    - …
- 예시 결과
    - …
