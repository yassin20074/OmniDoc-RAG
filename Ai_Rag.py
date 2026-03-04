#Retrieve the required libraries 
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
import os

def setup_rag_system(pdf_path):
    # Download files 
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Text segmentation with overlap ensures context is not lost
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=150, # overlap 
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)

    # Create and save the embedding in ChromADB 
    embeddings = OpenAIEmbeddings()
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db" #Save it in the path 
    )

    # Creating the model and setting up the answer system 
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=retriever
    )
    
    return qa_chain
