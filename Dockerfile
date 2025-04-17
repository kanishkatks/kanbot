FROM python:3.10-slim

WORKDIR /app
COPY . /app
COPY kanbot_key.json /app/kanbot_key.json

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE port 4000

CMD uvicorn rag_chatbot:app --host 0.0.0.0 --port 4000
