# Product_search tool for searching cars in a catalog of cars. 
from typing import List
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain.tools import tool

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import CSVLoader

from app.config import Config


@tool
def product_search_tool(query: str) -> List[str]:
    """Search for cars in the catalog by make, model, version, or year."""
    loader = CSVLoader(file_path=Config.CSV_FILE_PATH, encoding="utf-8", csv_args={'delimiter': ','})
    data = loader.load()

    text_splitter = CharacterTextSplitter(separator='\n')
    text_chunks = text_splitter.split_documents(data)

    embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    vector_store = InMemoryVectorStore(embeddings)
    ids = vector_store.add_documents(documents=text_chunks)

    retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={'k': 5, "lambda_mult": 1})
    response = retriever.invoke(query, filter={"source": Config.CSV_FILE_PATH})
    return response
