import streamlit as st 
import os 

# Load environment variables from .env file 
# like API keys and other sensitive informations

from dotenv import load_dotenv

# langchain imports 
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# step 1 --> Page configuration 

st.set_page_config(page_title="C++ Rag Chatbot", page_icon="☠️")
st.title(" ☠️ C++ RAG chatbot")
st.write("Write all questions about C++ only ")

#step 2 last environment variables
load_dotenv()

#step 3 --> use cache (importance for performance) to load and process documents
@st.cache_resource
#streamlit decorator -run this function only once ,not every refresh
#this is very important for embeddings + FAISS speed

#MAIN RAG PIPELINE
def load_vectorstore():
    
    #load documents 
    loader = TextLoader("C++_Introduction.txt",encoding="utf-8")
    documents = loader.load()
    
    # split documents into chunks 
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=20)
    final_docs = text_splitter.split_documents(documents)
    
    # embeddings