import streamlit as st
import os 

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_community.llms import ollama

# step 1 --> Page configuration 

st.set_page_config(page_title="C++ Rag Chatbot", layout="wide")
st.title(" ☠️ C++ RAG chatbot using ollama ")