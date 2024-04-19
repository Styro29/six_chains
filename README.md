# six_chains
## 이어드림 스쿨 4기 5팀의 LangChain 프로젝트입니다.
- 참여자: 김아민, 김지연, 길기현, 박우열, 전성환, 한지원

## [소프트웨어 기능 소개]

### main.py

LangChain 라이브러리를 이용하여 ~를하는 소프트웨어입니다.

‘main.py’ 파일에서는 ..., ..., ...기능을 수행하는 각 모듈을 import하고 모듈별로 내장된 함수를 호출하여 기능을 구현합니다.

## [모듈별 기능]

### gemini.py
'gemini.py' 모듈은 LangChain 라이브러리를 이용하여 Google Gemini API를 이용할 수 있도록 'AI_Model' 클래스에서 ChatGoogleGenerativeAI 인스턴스를 생성하고, <br>
클래스에 내장된 함수 'get_response()'를 통해 'chain.py' 모듈에서 생성한 language chain과 사용자가 입력한 질문 'user_input'을 입력 받고, <br>
기존의 질문과 답변을 결합하여 Gemini API에 응답을 요청하고 생성된 답변을 반환합니다.

**`AI_Model(self, model, temperature)`:** <br>
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
- `self.chat_model' (obj) : *ChatGoogleGenerativeAI 인스턴스 객체*

***`get_response(self, chain, user_input)`***<<br>
Arguments:
- `chain` (obj) :  *invoke를 수행할 생성된 chain*
- `user_input` (str) : *사용자가 입력한 질문*

Returns:
- `response` (str) : *Gemini API를 통해 생성된 답변 내용*
<br>
<br>
### retrieve.py
'retrieve.py' 모듈은 vector DB 생성 라이브러리로 생성된 vector DB를 입력 받아 LangChain의 vectorstores 라이브러리의 as_retriever 메서드 함수를 호출하여 vector DB가 retriever로 사용될 수 있도록 retriever 인스턴스를 반환하며, retrieve 함수의 'result_num' 인자를 통해 retriever가 검색하는 chunk의 개수를 지정합니다.

**`Retriever(self)`:** <br>
'Retriever' 클래스는 객체 생성 후, 클래스 내장 함수인 'retrieve()' 함수를 통해 vector DB를 retriever로 사용할 수 있도록 인스턴스를 생성합니다.<br>


***`retrieve(self, vec_db, result_num)`***<<br>
Arguments:
- `vec_db` (obj) :  *생성된 vector DB 객체*
- `result_num` (int) : *retriever가 유사도 검색을 통해 찾을 chunck의 개수(as_retriever 메서드의 arg 'k')*

Returns:
- `retriever` (obj) : *입력 받은 vector DB에 대해 생성된 retriever 인스턴스*
<br>
<br>

### chain.py
'chain.py' 모듈은 언어 모델의 retrieved context data를 반영한 Prompt를 설정하고, Gemini AI chain과 결합하여 언어 모델에서 목적에 맞는 답변을 유도할 수 있는 chain을 생성하고 반환합니다. 

**`Retriever(self)`:** <br>
'Retriever' 클래스는 객체 생성 후, 클래스 내장 함수인 'retrieve()' 함수를 통해 vector DB를 retriever로 사용할 수 있도록 인스턴스를 생성합니다.<br>


***`retrieve(self, vec_db, result_num)`***<<br>
'retrieve()' 함수는 생성된 vector DB를 입력 받아 'mmr' 방식으로 50회의 fetch 후 연관성 상위 result_num개의 chunck를 반환할 수 있는 인스턴스를 생성합니다.<br>
Arguments:
- `vec_db` (obj) :  *생성된 vector DB 객체*
- `result_num` (int) : *retriever가 'mmr' 방식 검색을 통해 찾을 chunck의 개수*

Returns:
- `retriever` (obj) : *입력 받은 vector DB에 대해 생성된 retriever 인스턴스*