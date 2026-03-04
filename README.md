# OmniDoc-RAG: Production-Ready Document Intelligence API

​**OmniDoc-RAG is a high-performance**, scalable Retrieval-Augmented Generation (RAG) system. It enables users to interact with large PDF documents through a natural language interface, leveraging LangChain for orchestration, FastAPI for high-speed serving, and Docker for seamless deployment.
​🚀 Key Features
**​Intelligent Text Splitting:** Utilizes RecursiveCharacterTextSplitter with optimized chunk sizes and overlap to maintain semantic context.
**​Vectorized Search:** Powered by ChromaDB for fast and accurate document retrieval.
**​Asynchronous API:** Built with FastAPI to ensure low-latency responses and high concurrency.
**​Containerized Architecture:** Fully Dockerized to ensure "plug-and-play" deployment across any environment.
​Source Transparency: The system doesn't just answer; it points back to the specific source documents used for the response.

# Tech Stack
​- Language: Python 3.9+
- ​Orchestration: LangChain
- ​LLM: OpenAI GPT (Compatible with Gemini/Anthropic)
- ​Vector DB: ChromaDB
- ​API Framework: FastAPI & Pydantic
- ​DevOps: Docker

# ⚙️ Installation & Setup
**​Using Docker (Recommended)**
**1-Build the Image:**
- docker build -t omnidoc-rag-api .
**Run the Container:**
- docker run -d -p 8000:8000 --env OPENAI_API_KEY="your_api_key_here" omnidoc-rag-api
**Manual Setup**
**Install Dependencies:**
- pip install -r requirements.txt
**Run the Server:**
- uvicorn main:app --reload


# 👨‍💻 Developed By
**-​Yassin Sanad**
**-AI Systems & Machine Learning Engineer**
