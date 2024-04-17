# # from tiktoken import TikTokenEncoder

# import bs4

# from langchain_community.document_loaders import WebBaseLoader
# from langchain_text_splitters import CharacterTextSplitter
# # from vertexai.preview.generative_models import GenerativeModel


# url1 = "https://www.boannews.com/media/view.asp?idx=125971&kind="
# url2 = "https://www.aitimes.kr/news/articleView.html?idxno=30090"
# url1 = "https://n.news.naver.com/mnews/article/138/0002165311?sid=105"
# url2 = "https://n.news.naver.com/mnews/article/005/0001668469?sid=101"

# loader = WebBaseLoader(
#     web_paths=(url1, url2),
#     # web_paths=(url2),
#     bs_kwargs=dict(
#         parse_only=bs4.SoupStrainer(
#             class_=("article-header", "article-content")
#         )
#     ),
# )

import bs4
import os 
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings


if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = "AIzaSyCA-bUfCd1Y5A9UDZkDUmsoGKvpnVa4Gmc"

# 뉴스기사 내용을 로드하고, 청크로 나누고, 인덱싱합니다.
loader = WebBaseLoader(
    web_paths=("https://n.news.naver.com/mnews/article/138/0002165311?sid=105",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            "div",
            attrs={"class": ["newsct_article _article_body"]},
        )
    ),
)

docs = loader.load()
print(docs)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap  = 100,
    length_function = len,
)

splits = text_splitter.split_documents(docs)
print(f"분할한 길이 : {len(splits)}")

vectorstore = FAISS.from_documents(documents=splits, embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
vectorstore
print(splits)

