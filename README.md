# Kanbot Portfolio Assistant: Talk to My Experience & Projects 

A smart, conversational assistant built into my portfolio website that answers questions about my background, projects, and skills in natural language. It feels like chatting with me, even when I'm not available!

![Portfolio Assistant Demo](https://github.com/user-attachments/assets/c2d521b0-7a98-4ece-90e8-b787321e4705)


🌐 Live: [kanishkawaghmare.com](https://kanishkawaghmare.com)

---

## What This Project Does

This assistant helps visitors to my website learn more about:
- My work history and projects
- Education and research background  
- Technical skills and expertise
- Detailed information about specific projects

Instead of reading through my entire portfolio, visitors can simply ask questions like "What experience does Kanishka have with machine learning?" or "Tell me about the Movie Recommender project" and get immediate, accurate answers.




---

## How It Works: Smart Document Search + AI Writing

The assistant combines two powerful technologies:

1. **Smart Document Search**: Finds the most relevant parts of my portfolio based on your question
2. **AI Text Generation**: Creates natural, conversational answers using only the accurate information found

This approach (called "Retrieval-Augmented Generation" or RAG) ensures responses are:
- Accurate and factual
- Based only on my real experience
- Detailed where needed
- Conversational and helpful

![RAG Process Diagram](https://github.com/user-attachments/assets/b4886b87-65ac-4a8c-a7b6-626f59abda33)

---

## Technical Components

### Frontend Interface
- **Clean Chat Interface**: Floating chat bubble expands to a full conversation
- **Mobile Responsive**: Works great on all devices
- **Real-Time Responses**: No page reloads needed
- **Built With**: React, TypeScript, and Tailwind CSS

### Backend Intelligence
- **Smart Search Engine**: Finds the most relevant information from my knowledge base
- **AI Text Generation**: Creates natural-sounding responses using the retrieved information
- **Fast API Server**: Handles requests efficiently
- **Built With**: Python FastAPI, Vector Search (FAISS), and AI models via Hugging Face

### Cloud Deployment
- **Always Available**: Hosted on Google Cloud Run
- **Scalable**: Handles multiple conversations simultaneously
- **Containerized**: Packaged in Docker for consistent deployment

---

## Example Conversations

**User**: "What's his dog's name??"

**Assistant**: "The dog's name is Beau, and he's a four-year-old Boston Terrier. 
Kanishka is very proud of him and would be happy to share his pictures with you!"

**User**: "Where was he born?."

**Assistant**: He was born in India

![Example Chat Screenshot](https://github.com/user-attachments/assets/143303fd-9796-4aa0-93b9-951099ffaedc)

---

## Project Files and Structure

```
.
├── rag_chatbot.py           # The main server with AI search & response logic
├── data/
│   └── kanishka_knowledge.md   # My experience, projects, and background info
├── vectorstore/             # Search index for quick information retrieval
├── components/ChatBot.tsx   # The chat interface for the website
├── Dockerfile               # For cloud deployment
└── requirements.txt         # Python dependencies
```

---

## Setup Instructions

### Option 1: Run Locally

1. **Clone & Install**
```bash
git clone https://github.com/kanishkatks/kanbot.git
cd kanbot
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Set Up AI Access**
Create a `.env` file:
```bash
HF_API_TOKEN=your_token_here  # Get from huggingface.co
```

3. **Start the Server**
```bash
uvicorn rag_chatbot:app --host 0.0.0.0 --port 8080
```

4. **View in Browser**: Open [http://localhost:8080](http://localhost:8080)

### Option 2: Using Docker

```bash
docker build -t kanbot .
docker run -p 8080:8080 -e HF_API_TOKEN=your_token_here kanbot
```

### Option 3: Deploy to Cloud

```bash
# Google Cloud Run deployment
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/kanbot

gcloud run deploy kabot \
  --image gcr.io/YOUR_PROJECT_ID/portfolio-assistant \
  --platform managed \
  --region YOUR_REGION \
  --set-env-vars HF_API_TOKEN=your_token_here \
  --allow-unauthenticated
```

![Deployment Options Diagram](https://via.placeholder.com/650x300?text=Deployment+Options)

---

## Future Enhancements

I'm planning to add these features in upcoming versions:

- **Memory**: Remember previous questions in the same conversation
- **Document Upload**: Upload a resume or job description to get personalized insights
- **Career Advice Mode**: Get customized career guidance based on my experience
- **Multi-language Support**: Chat in different languages

---

## Get In Touch

👤 **Kanishka Waghmare**  
🌐 [kanishkawaghmare.com](https://kanishkawaghmare.com)  
📧 kanishkatks@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/yourprofile)


I'm open to collaboration, feedback, or just a friendly chat about data science and AI!



---

> Built to make my portfolio interactive and showcase my work with practical AI applications!
