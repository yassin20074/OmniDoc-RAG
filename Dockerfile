# Choosing a light breeze from Python for speed 
FROM python:3.9-slim

# Identifying the work folder 
WORKDIR /app

# Copy the requirements file 
COPY requirements.txt .

# Install the required libraries 
RUN pip install --no-cache-dir -r requirements.txt

# Copying project files 
COPY main.py
Copy Ai_Rag.FastAPI

# Opening the port 
EXPOSE 8000

# Run command using uvicorn 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
