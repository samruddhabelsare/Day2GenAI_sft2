from dotenv import load_dotenv
import streamlit as st
import os 

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_community.llms import Ollama

# step 1 --> Page configuration 

st.set_page_config(page_title="C++ Rag Chatbot", layout="wide")
st.title(" ☠️ C++ RAG chatbot using ollama ")

# step 2 --> load environment variables
load_dotenv()

# step 3 --> use cache (importance for performance) to load and process documents
@st.cache_resource
# streamlit decorator - run this function only once , not every refresh
# this is very important for embeddings + FAISS speed

# MAIN RAG PIPELINE
def load_vectorstore():
    
    # load documents 
    loader = TextLoader("C++_Introduction.txt", encoding="utf-8")
    documents = loader.load()
    
    # split documents into chunks 
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )
    final_docs = text_splitter.split_documents(documents)
    
    # create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    # create FAISS vector store
    db = FAISS.from_documents(final_docs, embeddings)
    
    return db

db= load_vectorstore()

# extra stop - load LLM
llm=Ollama(model="gemma2:2b")

# last step - chat interface 
user_question=st.text_input("Ask question about C++")

if user_question:
    with st.spinner("Ruk ja bhai , sochne de ....."):
        docs=db.similarity_search(user_question)
        
        # combine cotext (construction)
        # 1. Extract text from retrived documents
        # 2. Joins them into single string 
        # 3. this becomes context of LLM 
        
        context = "\n ".join([doc.page_content for doc in docs])
        
        # prompt enggenering
        prompt = f""" answer the question using only context below.
        
        context :{context}
        
        Question : {user_question}
        
        Answer : 
        """
        
        # created structure prompts 
        # 1. provides context
        # 2. provides question
        # 3. ask for answer 
        
        # This is how hallucinations effect is reduced 
        
        response = llm.invoke(prompt)
        st.subheader("Answer : ")
        st.write(response) 
    