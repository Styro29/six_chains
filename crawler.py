# crawler.py
import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain.document_loaders import UnstructuredURLLoader


class Crawler:
    def get_data_from_url():
        urls = [
            "https://www.catch.co.kr/NCS/RecruitInfoDetails/297693",
            "https://www.catch.co.kr/NCS/RecruitInfoDetails/297678",
            "https://www.wanted.co.kr/wd/166369",
            "https://www.wanted.co.kr/wd/148653",
            "https://www.wanted.co.kr/wd/65223",
            "https://about.daangn.com/jobs/5248527003",
            "https://about.daangn.com/jobs/4300801003",
            "https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=45614720&recommend_ids=eJxdjsERw0AIA6vJHw4hxDuFuP8uck7GNpPnsiCE7ICbDnm%2F6o1syYMb%2FYfwytvSVpB5aP3jgXOAhhzjWiTrQosAnOPanPEse8ntstldQT2WSK4LaWawHHZ167Fr472cLEWOqFw9UNqffUSVerQybwzcreqLHxBhRFk%3D&view_type=search&searchword=%EC%95%BC%EB%86%80%EC%9E%90&searchType=search&gz=1&t_ref_content=generic&t_ref=search&paid_fl=n&search_uuid=a8f591c7-3e93-4fd3-af1a-1a478033d13c&immediately_apply_layer_open=n#seq=0",
            "https://www.wanted.co.kr/wd/162018",
            "https://www.wanted.co.kr/wd/135256",
            "https://job.incruit.com/jobdb_info/jobpost.asp?job=2209080002003",
            "https://www.wanted.co.kr/wd/167203",
            "https://www.wanted.co.kr/wd/155240",
            "https://www.wanted.co.kr/wd/153864",
            "https://job.incruit.com/jobdb_info/jobpost.asp?job=2302090004407",
            "https://medium.com/naver-dna-tech-blog/dna%ED%8C%80%EA%B3%BC-%ED%95%A8%EA%BB%98-%EC%84%B1%EC%9E%A5%ED%95%A0-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%94%8C%EB%9E%AB%ED%8F%BC-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A5%BC-%EB%AA%A8%EC%8B%AD%EB%8B%88%EB%8B%A4-8373d96f3626",
            "https://naver-career.gitbook.io/kr/service/search/vision",
            "https://naver-career.gitbook.io/kr/service/search/websearch",
            "https://naver-career.gitbook.io/kr/service/search/undefined-2",
            "https://naver-career.gitbook.io/kr/service/search/undefined-3/product-recommendation-aitems",
            "https://naver-career.gitbook.io/kr/service/search/recommendation-airs/al-ml",
            "https://naver-career.gitbook.io/kr/service/search/recommendation-airs/al-ml-1",
            "https://naver-career.gitbook.io/kr/service/search/ai-and-data-platform",
            "https://naver-career.gitbook.io/kr/service/biz-cic/ai-ml",
            "https://naver-career.gitbook.io/kr/service/shopping/shopping-aggregation-platform#ai-ml",
            "https://naver-career.gitbook.io/kr/service/music/music-ai-and-data-tech",
            "https://naver-career.gitbook.io/kr/service/band/ml-data-engineering",
            "https://naver-career.gitbook.io/kr/service/clova/speech-recognition",
            "https://naver-career.gitbook.io/kr/service/clova/ai-ml",
            "https://naver-career.gitbook.io/kr/service/clova/clova-vision-kit/face-ai",
            "https://naver-career.gitbook.io/kr/service/clova/clova-vision-kit/video-ai",
            "https://naver-career.gitbook.io/kr/service/clova/clova-vision-kit/avatar-ai",
            "https://naver-career.gitbook.io/kr/service/clova/clova-vision-kit/edge-ai",
            "https://naver-career.gitbook.io/kr/service/clova/clova-vision-kit/data-engineer",
            "https://naver-career.gitbook.io/kr/service/clova/hci-x-ai",
            "https://naver-career.gitbook.io/kr/service/clova/conversation",
            "https://naver-career.gitbook.io/kr/service/clova/ai-assistant",
            "https://naver-career.gitbook.io/kr/service/clova/ai",
            "https://naver-career.gitbook.io/kr/service/papago/ai-ml",
            "https://naver-career.gitbook.io/kr/service/clova/and-and",
            "https://www.wanted.co.kr/wd/215303",
            "https://www.wanted.co.kr/wd/215669",
            "https://www.wanted.co.kr/wd/215440",
            "https://www.wanted.co.kr/wd/214287",
            "https://www.wanted.co.kr/wd/214463",
            "https://www.wanted.co.kr/wd/160748",
            "https://www.wanted.co.kr/wd/201396",
            "https://www.wanted.co.kr/wd/215835",
        ]
        loader = UnstructuredURLLoader(urls=urls)
        data = loader.load()
        return data
    
    # print(len(get_data_from_url()))