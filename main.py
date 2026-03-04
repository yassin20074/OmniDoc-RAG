#Requesting the required libraries 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Ai_Rag import setup_rag_system
import os

app = FastAPI(title="OmniDoc-RAG")

# You can modify the path to be dynamic according to your needs
PDF_PATH = "data/my_document.pdf"
rag_bot = setup_rag_system(PDF_PATH)

class Question(BaseModel):
    text: str

@app.post("/ask")
async def ask_ai(question: Question):
    try:
        response = rag_bot.invoke({"query": question.text})
        return {"answer": response["result"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"message": "RAG API is running!"}
