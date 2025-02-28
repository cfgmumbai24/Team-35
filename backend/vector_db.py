# from pprint import pprint
# import pandas as pd
# import chromadb
# from chromadb import Documents, EmbeddingFunction, Embeddings
# import google.generativeai as genai
# from chromadb.api.types import Embeddings
# import time
# from tqdm import tqdm
# from google.generativeai import GenerationConfig, GenerativeModel
# import os
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# import PyPDF2
# import asyncio
# from chromadb.utils import embedding_functions

# async def extract_text(pdf_path):
#     try:
#         extracted_text = ""
#         with open(pdf_path, 'rb') as file:
#             pdf_reader = PyPDF2.PdfReader(file)
#             num_pages = len(pdf_reader.pages)
#             for page_number in range(num_pages):
#                 page = pdf_reader.pages[page_number]
#                 extracted_text += page.extract_text()
#         return extracted_text
#     except Exception as e:
#         print(f"The exception has occurred at: {e}")
#         return e

# def chunking(data):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=5000,
#         chunk_overlap=100,
#         length_function=len,
#         add_start_index=True
#     )
#     texts = text_splitter.create_documents([data])
#     docs = [content.page_content for content in texts]  # Extracting only the page content
#     return docs

# gemini_key = ""

# genai.configure(api_key=gemini_key)

# sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# class MyEmbeddingFunction(EmbeddingFunction):
#     def __call__(self, input: Documents) -> Embeddings:
#         embeddings = sentence_transformer_ef(input)
#         return embeddings

# def create_content_embeddings_db(data: str, db_name: str) -> chromadb.Collection:
#     docs = chunking(data)
#     embedding_function = sentence_transformer_ef
#     embeddings = embedding_function(docs)
#     db = create_chroma_db(docs, embeddings, db_name)
#     return db

# def create_chroma_db(docs, embeddings: Embeddings, name) -> chromadb.Collection:
#     class MyEmbeddingFunction(EmbeddingFunction):
#         def __call__(self, input: Documents) -> Embeddings:
#             embeddings_list = sentence_transformer_ef(input)
#             return embeddings_list

#     chroma_client = chromadb.PersistentClient(path="D:/Competitions/KLEOS/backend/backend/parth/apps/database")
#     db = chroma_client.get_or_create_collection(name=name, embedding_function=sentence_transformer_ef)

#     initial_size = db.count()
#     for i, (doc, emb) in tqdm(enumerate(zip(docs, embeddings)), total=len(docs), desc="Creating Chroma DB"):
#         db.add(documents=[doc], embeddings=[emb], ids=[str(i + initial_size)])
#         time.sleep(0.5)
#     return db

# async def get_chroma_db(name):
#     chroma_client = chromadb.PersistentClient(path="D:/Competitions/KLEOS/backend/backend/parth/apps/database")
#     return chroma_client.get_collection(name=name, function=MyEmbeddingFunction())

# async def generating_db(pdf_path):
#     text = await extract_text(pdf_path)
#     docs = chunking(text)
#     print(f"\n\nDocs:\n{docs}\n\n")
#     db = create_chroma_db(docs, sentence_transformer_ef(docs), 'valid_data')
#     return db

# async def return_db():
#     pdf_path = './cyber_learn.pdf'
#     op = await generating_db(pdf_path)
#     print(op)
#     return op

# # asyncio.run(return_db())



import PyPDF2
from dotenv import load_dotenv
from pprint import pprint
import pandas as pd
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
import google.generativeai as genai
from IPython.display import Markdown
from chromadb.api.types import Embeddings
import time
from tqdm import tqdm
from google.generativeai import GenerationConfig, GenerativeModel
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chunking
from dotenv import load_dotenv

# gemini_key = ""

gemini_key = load_dotenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_key)

class GeminiEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input: Documents) -> Embeddings:
        model = 'models/embedding-001'
        title = 'API'
        return genai.embed_content(
            model=model,
            content=input,
            task_type="retrieval_document",
            title=title)["embedding"]

def create_chroma_db(docs, name, path):
    chroma_client = chromadb.PersistentClient(path=path) 
    db = chroma_client.get_or_create_collection(
        name=name, embedding_function=GeminiEmbeddingFunction())
    
    initial_size = db.count()
    for i, d in tqdm(enumerate(docs), total=len(docs), desc="Creating ChromaDB"):
        db.add(
            documents=d,
            ids=str(i + initial_size)
        )
        time.sleep(0.5)
    return db

# Example usage
pdf_path = './rbi_data.pdf'
db_path = "/Users/mihiresh/Mihiresh/Work/cfg/Team-35/backend/vector_database"
db_name = "finance_rbi_vector_db"
docs = chunking.generate_docs_from_pdf(pdf_path)
create_chroma_db(docs, db_name, db_path)