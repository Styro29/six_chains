# 이어드림 스쿨 4기 5팀의 LangChain 프로젝트 six_chains
### 김아민, 김지연, 길기현, 박우열, 전성환, 한지원

![6-chains](https://github.com/Styro29/six_chains/assets/133292854/232724ea-af0a-4465-aa85-459e78e4f662)


# 서비스 요약
직군선택에 방황하는 동기들을 위해 데이터 관련 직군 정보를 한 곳에 모았다!
- 사용자에게 관련 데이터 관련 직군의 정보 제공
- 현재 지원자들이 갖춰야 할 역량을 설명해줌
- 취업사이트의 지원 공고 소개  

# 기획 이유  


<br/> 

# 소프트웨어 기능 소개
![Class diagram](https://github.com/Styro29/six_chains/assets/133292854/1ce8c041-7bef-416d-bf2a-96f6dc5a3544)

<br/> 

# 모듈별 기능
## main.py
 - 사용자에게 질문을 받고 응답 반환 후 히스토리에 저장
 - 다섯개의 각 모듈을 import하고 모듈별로 내장된 함수를 호출하여 기능 구현
 - 함수 실행 결과를 app.log 파일에 저장


## crawler.py
`get_data_from_url(self, url_file="urls.txt", save_dir=os.path.dirname(__file__)):`<br>

1. Data crawling을 위해 명시된 url을 urls.txt 파일을 이용하여 url_loader에 입력 후 파라미터로 넘겨서 로딩

2. 크롤링이 진행되면 현재 디렉토리 내에 text_data가 있는지 확인 후 
	- 데이터가 없으면 UnstructuredURLLoader를 이용하여 download 후, 다운로드한 데이터를 pickle을 이용하여 {text_data} binary file 로 저장
	- 이때 동시에 생성된 {text_data_check.txt} 파일은 테스트시, 받아온 데이터 확인용으로 사용

3. 만약 이전에 받았던 crawling data가 이미 있을 경우에는 다시 url crawling을 하지 않고 saved 된 text_data를 로딩하여 더 빠르게 user input을 받게<br>실행

4. 이렇게 다운받거나 로딩된 raw data를 최종적으로 return

5. 만약 url에 문제가 있거나 다운로드 과정에서 문제가 발생하여 데이터를 못 받아오게 되면
	"Error: Failed to load text data from URLS." 를 출력


## gemini.py
1. `AI_Model(self, model, temperature):`<br>
	- 'AI_Model' 클래스는 객체 생성 시, model 종류와 모델의 temperature 값을 입력 받아 클래스 내부 변수 'chat_model'에 ChatGoogleGenerativeAI 인스턴스를 할당
	- 클래스 내부 변수로 'chat_history'에는 사용자 입력 질문 'user_input', 'get_response()' 함수에서 생성된 답변을 str 형식으로 저장
	- 'last_question_no'는 현재 사용자가 마지막으로 입력한 질문과 답변의 순서를 int 형식으로 저장
	- 클래스 내장 함수 'get_response()'는 language chain을 입력 받고, 사용자 입력 질문인 'user_input'과 기존 질의응답 내역인 'chat_history'를 결합하여<br>language chain에 invoke를 수행 
	- invoke 수행 후 생성된 답변 'response'와 'user_input'을 클래스 내장 변수 'chat_history'에 저장

	Arguments:
	- `model` (str) -> optional : *Google Gemini의 세부 모델명(기본값: 'gemini-1.5-pro-latest')*
	- `temperature` (float) -> optional : *언어 모델의 temperature(기본값: 0.7)*
	
	Internal variables:
	- `self.chat_history` (str) : *사용자의 질문(user_input)과 모델의 답변(response)을 저장*
	- `self.last_question_no` (int) : *현재 사용자가 마지막으로 입력한 질문과 답변의 순서를 저장*
	- `self.chat_model` (obj) : *ChatGoogleGenerativeAI 인스턴스 객체*

<br/> 

2. `get_response(self, chain, user_input):`<br>
	Arguments:
	- `chain` (obj) :  *invoke를 수행할 생성된 chain*
	- `user_input` (str) : *사용자가 입력한 질문*
	
	Returns:
	- `response` (str) : *Gemini API를 통해 생성된 답변 내용*


## vector-store.py
1. `text_split(self, data)`: 
	crawling한 data를 청크 단위로 split

	Arguments
	- `data`: 채용 공고를 crawling한 raw data

	Return
	- `splits`: data를 chunk 단위로 분할한 문장


2. `embed_documents(self, splits):`
	split한 텍스트 청크를 embedding

	- `splits`: 고차원 벡터 데이터의 유사성 검색을 수행하는 FAISS를 사용하여 인덱스를 생성한 data
	- `vectorstore`: FAISS를 통해 생성된 벡터 저장소


## retriever.py
'retrieve.py' 모듈은 vector DB 생성 라이브러리로 생성된 vector DB를 입력 받아 LangChain의 vectorstores 라이브러리의 as_retriever 메서드 함수를<br>호출하여 vector DB가 retriever로 사용될 수 있도록 retriever 인스턴스를 반환하며, retrieve 함수의 'result_num' 인자를 통해 retriever가 검색하는 chunk의 개수를 지정

**`Retriever(self)`:** <br>
'Retriever' 클래스는 객체 생성 후, 클래스 내장 함수인 'retrieve()' 함수를 통해 vector DB를 retriever로 사용할 수 있도록 인스턴스를 생성<br>

<br/> 

***`retrieve(self, vec_db, result_num)`***<br>
Arguments:
- `vec_db` (obj) :  *생성된 vector DB 객체*
- `result_num` (int) : *retriever가 유사도 검색을 통해 찾을 chunck의 개수(as_retriever 메서드의 arg 'k')*

Returns:
- `retriever` (obj) : *입력 받은 vector DB에 대해 생성된 retriever 인스턴스*


## chain.py
'chain.py' 모듈은 언어 모델의 retrieved context data를 반영한 Prompt를 설정하고, Gemini AI chain과 결합하여 언어 모델에서 목적에 맞는 답변을 유도할 수 있는 chain을 생성하고 반환

**`Chain(self)`:** <br>
- 'Chain' 클래스는 객체 생성 시, model의 default prompt를 설정하고, 'create_chain()' 함수를 통해 사용자의 질문에 대한 답변을 invoke할 수 있도록 language chain을 구성하여 반환<br>
- 클래스 내장 함수인 'create_chain()' 함수는 chat_model 객체와 retriever 객체를 입력으로 받아, default prompt의 context로 사용자 질문과<br>가장 유사한 data chunk를 가져와서
  복수의 data chunk를 하나의 문서로 병합하는 'format_docs()' 함수를 이용하여 context를 구성하는 runnable<br>인스턴스를 chain 요소의 하나로 구성
- 이후 invoke 시, 'user_input' 변수를 통해 추가되는 'question' 항목은 LangChain의 RunnablePassthrough() 인스턴스를 이용하여 통과하도록 구현
- 다음 체인 요소로 default prompt를 두어 목적에 맞는 답변을 생성하도록 구성
- 이후 'chat_model' 인스턴스를 구성하여 Google Gemini API 통해 답변을 생성할 수 있도록 구성하였으며, <br>'StrOutputParser()'를 이용하여 답변 내용을
  str 형식으로 출력할 수 있도록 체인을 구성하여 체인 객체를 반환하도록 함수를 구현<br>

<br/> 

***`create_chain(self, chat, retrieve)`***<br>
Arguments:
- `chat` (obj) : *Language model 객체*
- `retrieve` (obj) : *Retriever 객체*

Returns:
- `chain` (obj) : *default prompt가 반영된 chain 객체*
<br>
<br>
