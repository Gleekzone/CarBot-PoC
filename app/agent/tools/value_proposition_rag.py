import bs4
import requests
from typing import Dict

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.tools import tool
from app.config import Config


@tool
def value_prop_rag_tool(query: str) -> Dict:
    """Tool for retrieving value propositions using RAG (Retrieval-Augmented Generation)."""
    # This code is used because the website have a block to prevent scraping
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36" # This can be customized as needed
    session = requests.Session()
    session.headers.update({"User-Agent": user_agent})
    url = Config.WEBSITE_SEARCH_URL

    # Load the website content
    bs4_strainer = bs4.SoupStrainer(class_=("main-content"))
    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs={"parse_only": bs4_strainer},
        session=session
    )
    docs = loader.load()

    # Split the documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100, add_start_index=True)
    all_split_docs = text_splitter.split_documents(docs)

    # Create an in-memory vector store with embeddings
    vector_store = InMemoryVectorStore(HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2'))
    document_ids = vector_store.add_documents(documents=all_split_docs) # Add documents to the vector store

    # Create a retriever for the vector store
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})

    response = retriever.invoke(query)
    session.close()
    return response
