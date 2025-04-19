FROM python:3.11-slim

WORKDIR /app
COPY . /app
COPY kanbot_key.json /app/kanbot_key.json

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD uvicorn rag_chatbot:app --host 0.0.0.0 --port $PORT
