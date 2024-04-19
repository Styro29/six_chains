#README_Crawler.md

def get_data_from_url(self, url_file="urls.txt", save_dir=os.path.dirname(__file__)):

	- Data crawling을 위해 url들이 명시된 urls.txt 파일을 이용해서 URL로더에 입력 파라메터로 넘겨서 로딩을 해줍니다.

	- 크롤링이 진행되면 현재 디렉토리 내에 text_data가 있는지 확인 후, 
		1. 데이터가 없으면 UnstructuredURLLoader를 이용하여 download 후, 다운로드한 데이터를 pickle을 이용하여 {text_data} binary file 로 저장해 줍니다.
		2. 이때 동시에 생성된 {text_data_check.txt} 파일은 테스트시, 받아온 데이터 확인용으로 사용됩니다. 

	- 만약, 이전에 받았던 crawling data가 이미 있을 경우에는 다시 url crawling을 하지않고, saved 된 text_data를 로딩하여 더 빠르게 user input을 받게 실행 됩니다.

	- 이렇게 다운로드 받거나 로딩된 raw data 를 최종적으로 return 해줍니다.

	- 만약, url에 문제가 있거나 다운로드 과정에서 문제가 발생하여 데이터를 못 받아오게 되면,
		1. "Error: Failed to load text data from URLS." 를 출력하게 됩니다.