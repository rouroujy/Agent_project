from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.tools import tool

from rag.langchain_rag import chunk_text, load_document
from langchain_core.documents import Document

import pathlib
import os

BASE_MODEL_DIR = "/mnt/d/ai_models"
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
CACHE_DIR = os.path.join(BASE_MODEL_DIR,"hf_cache")

# =========================
# 初始化（只做一次！）
# =========================

data_path = pathlib.Path("data/chunk_test.md")
text = load_document(data_path)
chunks = chunk_text(text)

documents = [Document(page_content=doc) for doc in chunks]

embedding_model = HuggingFaceEmbeddings(
    model_name=EMBED_MODEL_NAME,
    cache_folder=CACHE_DIR
)

vectorstore = FAISS.from_documents(
    documents,
    embedding_model
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k":3}
)

# =========================
# Tool
# =========================

@tool
def knowledge_base_search(query: str) -> str:
    """
    用于查询知识库中的相关内容。
    输入应该是一个完整的问题。
    """
    docs = retriever.invoke(query)

    if not docs:
        return "未找到相关内容"

    return "\n\n".join(doc.page_content for doc in docs)
