# Chatbot with Search Tools 🔎🤖

A Streamlit chatbot powered by **Groq LLM** and **LangChain** that can search **Arxiv, Wikipedia, and the web**. This assistant is capable of answering questions and fetching relevant information from multiple sources.

---

## Features

- LLM (Groq API with LLaMA-4 Scout)
- Arxiv integration for research papers
- Wikipedia integration for general knowledge
- DuckDuckGo search for web queries
- Streamlit chat UI with persistent conversation

---

## Installation

###Clone the repository:

```bash
git clone https://github.com/your-username/chatbot-search-agent.git
cd chatbot-search-agent
```

### Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Create a ```.env``` file in the root directory with your Groq API key:

```bash
GROQ_API_KEY=your_api_key_here
```

## Usage

### Run the app with Streamlit:

```bash
streamlit run app.py
```
Enter your Groq API key in the sidebar and start chatting! The bot can answer questions and fetch data from Arxiv, Wikipedia, and the web.









