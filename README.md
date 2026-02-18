# 🤖 C++ RAG Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.1%2B-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Store-0078D4?style=for-the-badge&logo=meta&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**_Where Documents Meet Intelligence — Powered by Retrieval_**

🔵 Retrieve Smart &nbsp;·&nbsp; 🟡 Generate Accurately &nbsp;·&nbsp; 🟢 Answer Confidently


[Features](#-features) · [Architecture](#-architecture) · [Installation](#-installation) · [Usage](#-usage) · [Project Structure](#-project-structure) · [Tech Stack](#-tech-stack) · [Author](#-author)

</div>

---

## 📌 Overview

**C++ RAG Chatbot** is a locally-runnable, document-grounded question-answering system built with **Streamlit**, **LangChain**, **FAISS**, and **HuggingFace Embeddings**. It answers questions strictly based on a C++ reference document — eliminating hallucinations by anchoring every response in retrieved context.

The project ships as two progressive implementations — a pure retrieval stage and a full generation stage — making it an ideal hands-on project for anyone stepping into the world of Retrieval-Augmented Generation.

> *"I didn't build this to impress anyone. I built it because 2 AM said — one more function."*
> — **Samruddha Belsare**, Developer 🇮🇳

---

## ✨ Features

### 🔍 Section 01 — rag.py : Retrieval Engine
- Loads `C++_Introduction.txt` using LangChain's `TextLoader`
- Splits the document into semantic chunks using `RecursiveCharacterTextSplitter` (chunk size: 200, overlap: 20)
- Generates dense vector embeddings using `sentence-transformers/all-MiniLM-L6-v2` from HuggingFace
- Indexes all chunks into a **FAISS** in-memory vector store for lightning-fast lookup
- Caches the entire pipeline using `@st.cache_resource` — runs only once per session, never on refresh
- Accepts a user query and retrieves the **top 3 most semantically similar document chunks**
- Displays each retrieved chunk in a clean, numbered result card with dividers

### 🤖 Section 02 — ragbot.py : Full RAG Chatbot
- Inherits the complete retrieval pipeline from `rag.py`
- Integrates **Ollama** with the `gemma2:2b` model as the fully local LLM — no API key needed
- Constructs a grounded prompt by injecting retrieved context directly above the user question
- Sends the structured prompt to the LLM and returns a generated final answer
- Uses a strict prompt template that prevents the model from answering beyond the provided document
- Displays a spinner with a human touch ("Ruk ja bhai, sochne de.....") while generating

### ⚙️ Section 03 — Shared Core (Both Files)
- Zero cloud dependency — runs entirely on your local machine
- No OpenAI key required — embeddings and LLM are both fully local
- Streamlit-powered UI — clean, minimal, and snappy
- `.env` support via `python-dotenv` for environment variable management
- `@st.cache_resource` ensures the heavy embedding step never repeats unnecessarily

---

## 🏗️ Architecture

```
╔══════════════════════════════════════════════════════════════════════════╗
║                    C++ RAG CHATBOT — SYSTEM PIPELINE                    ║
║  ──────────────────────────────────────────────────────────────────────  ║
║                                                                          ║
║   📄 [C++_Introduction.txt]                                             ║
║           |                                                              ║
║           v                                                              ║
║   📥 [TextLoader]                                                       ║
║           |                                                              ║
║           v                                                              ║
║   ✂️  [RecursiveCharacterTextSplitter]   chunk=200   overlap=20         ║
║           |                                                              ║
║           v                                                              ║
║   🧠 [HuggingFace Embeddings]   all-MiniLM-L6-v2   (384 dimensions)   ║
║           |                                                              ║
║           v                                                              ║
║   🗄️  [FAISS Vector Store]  ←──────── @st.cache_resource               ║
║           |                                                              ║
║           v                                                              ║
║   💬 User Query ──► similarity_search(k=3) ──► Top 3 Chunks            ║
║                                                      |                   ║
║                                    (ragbot.py only)  v                   ║
║                              📝 [Prompt Engineering]                    ║
║                              "Answer using only the context below"      ║
║                                      |                                   ║
║                                      v                                   ║
║                         🦙 [Ollama — gemma2:2b]  (runs locally)       ║
║                                      |                                   ║
║                                      v                                   ║
║                              ✅ Final Grounded Answer                   ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 🖥️ Demo

```
╔══════════════════════════════════════════════════════════════════╗
║  🤖 C++ RAG CHATBOT                                             ║
║  ─────────────────────────────────────────────────────────────  ║
║  🔍 rag.py — Retrieval  ·  🤖 ragbot.py — Full Chatbot         ║
╚══════════════════════════════════════════════════════════════════╝
```

> Run the app locally — see [Installation](#-installation) below.

---

## 🗂️ Project Structure

```
cpp-rag-chatbot/
│
├── rag.py                      # Stage 1 — Pure retrieval, no LLM generation
├── ragbot.py                   # Stage 2 — Full RAG chatbot with Ollama LLM
├── C++_Introduction.txt        # Knowledge base document (you provide this)
├── .env                        # Environment variables (API keys if needed)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

> This is a **two-file RAG project** — `rag.py` is the foundation and `ragbot.py` builds the complete chatbot on top of it.

---

## 🛠️ Tech Stack

| Library | Version | Purpose |
|---|---|---|
| `streamlit` | >= 1.32 | Web UI framework — input, output, caching, spinner |
| `langchain-community` | >= 0.1 | TextLoader, FAISS vector store, Ollama LLM wrapper |
| `langchain-text-splitters` | >= 0.1 | RecursiveCharacterTextSplitter for document chunking |
| `langchain-huggingface` | >= 0.1 | HuggingFace embeddings interface for LangChain |
| `faiss-cpu` | >= 1.7 | High-speed local vector similarity search |
| `sentence-transformers` | >= 2.2 | `all-MiniLM-L6-v2` — 384-dimensional dense embeddings |
| `ollama` | >= 0.1 | Local LLM runtime — serves Gemma 2B entirely on-device |
| `python-dotenv` | >= 1.0 | Loads environment variables from `.env` |

---

## 📦 Installation

### Prerequisites

- Python **3.8 or higher**
- `pip` package manager
- **Ollama** installed and running locally *(for `ragbot.py` only)*

### Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/cpp-rag-chatbot.git
cd cpp-rag-chatbot
```

### Step 2 — Create a Virtual Environment *(Recommended)*

```bash
# Create virtual environment
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — macOS / Linux
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit langchain-community langchain-text-splitters langchain-huggingface faiss-cpu sentence-transformers python-dotenv
```

### Step 4 — Install Ollama and Pull Gemma 2B *(ragbot.py only)*

Download Ollama from [https://ollama.com](https://ollama.com), then run:

```bash
ollama pull gemma2:2b
ollama serve
```

### Step 5 — Add Your Knowledge Base

Place `C++_Introduction.txt` in the root project directory. Both apps load this file at startup.

### Step 6 — Run the App

```bash
# Stage 1 — Retrieval only
streamlit run rag.py

# Stage 2 — Full RAG chatbot
streamlit run ragbot.py
```

The app will open automatically at **`http://localhost:8501`** in your browser.

---

## 📋 requirements.txt

```
streamlit>=1.32.0
langchain-community>=0.1.0
langchain-text-splitters>=0.1.0
langchain-huggingface>=0.1.0
faiss-cpu>=1.7.0
sentence-transformers>=2.2.0
python-dotenv>=1.0.0
```

---

## 🚀 Usage

### Running rag.py for the First Time

1. Launch the app with `streamlit run rag.py`
2. The browser opens at `http://localhost:8501`
3. The knowledge base is chunked, embedded, and indexed on first load (cached afterwards)
4. Type any C++ question into the text input
5. The **top 3 most semantically similar document chunks** are displayed instantly

### Running ragbot.py for the First Time

1. Ensure `ollama serve` is running in a separate terminal window
2. Launch with `streamlit run ragbot.py`
3. Type a C++ question in the input box
4. The spinner activates while retrieval and LLM generation occur
5. A grounded, document-based answer appears in the output area

### How the Pipeline Works Step by Step

| Step | What Happens | Which File |
|---|---|---|
| Load | `TextLoader` reads `C++_Introduction.txt` into memory | Both |
| Chunk | Document split into 200-token chunks with 20-token overlap | Both |
| Embed | Each chunk converted to a 384-dim vector via `all-MiniLM-L6-v2` | Both |
| Index | All vectors stored in FAISS for fast similarity lookup | Both |
| Cache | `@st.cache_resource` ensures steps 1–4 run only once per session | Both |
| Retrieve | User query embedded → top 3 most similar chunks fetched | Both |
| Generate | Chunks injected into prompt → Ollama LLM produces the final answer | ragbot.py only |

---

## 📊 Prompt Engineering — ragbot.py

The prompt template used to keep the model grounded and prevent hallucination:

```
Answer the question using only the context below.

Context: {retrieved_chunks}

Question: {user_question}

Answer:
```

| Prompt Element | Purpose |
|---|---|
| `"only the context below"` | Hard-constrains the LLM to retrieved document content only |
| `Context: {chunks}` | Injects the 3 retrieved chunks as the model's sole knowledge source |
| `Question: {user_question}` | Passes the exact user query to the model |
| `Answer:` | Signals the model exactly where to begin its response |

---

## 🔮 Future Improvements

- [ ] Support multiple file formats — PDF, DOCX, Markdown, HTML
- [ ] Add multi-turn chat history using `st.session_state`
- [ ] Display source citations — show which chunk each answer came from
- [ ] Allow users to upload their own knowledge base via the Streamlit UI
- [ ] Add a model selector — switch between installed Ollama models at runtime
- [ ] Persist the FAISS index to disk to avoid re-embedding on every restart
- [ ] Add chunk size and overlap sliders for advanced configuration in the sidebar
- [ ] Add a confidence score display alongside each retrieved result
- [ ] OpenAI API support as an optional alternative to local Ollama
- [ ] Dark / Light theme toggle

---

## ⚠️ Known Limitations

- `C++_Introduction.txt` must exist in the project root before launching — the app will crash without it
- The FAISS index lives in memory only — it is fully rebuilt on every server restart
- `ragbot.py` requires Ollama to be actively running before the Streamlit app is launched
- The system only answers questions grounded in the provided document — general C++ questions not covered in the text may receive incomplete answers
- A chunk size of 200 tokens may be too small for some complex C++ topics — tuning may be needed for better retrieval quality

---

## 🤝 Contributing

Contributions are welcome! If you want to add features or fix bugs:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes in `rag.py` and / or `ragbot.py`
4. Test both apps thoroughly before submitting
5. Commit: `git commit -m "Add: your feature description"`
6. Push: `git push origin feature/your-feature-name`
7. Open a **Pull Request**

Please maintain the local-first, no-cloud-dependency philosophy of this project in all contributions.

---

## 📄 License

```
MIT License

Copyright (c) 2026 Samruddha Belsare

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👨‍💻 Author

<div align="center">

**Samruddha Belsare**

🇮🇳 &nbsp; India &nbsp; · &nbsp; 📅 Built on 18 February 2026

*"I didn't build this to impress anyone. I built it because 2 AM said — one more function."*

Developed with ❤️ and Large Language Models (LLMs)

---

*Built for every developer who stays up late not because they have to — but because the code is almost working.* 🤖

</div>

---

<div align="center">

```
◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
   🤖  C++ RAG CHATBOT  ·  Powered by Retrieval-Augmented Generation
   Built with  Streamlit  ·  LangChain  ·  FAISS  ·  Ollama
   ────────────────────────────────────────────────────────────
        🔵 Retrieve Smart   🟡 Generate Accurately   🟢 Answer Confidently
◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
```

*© 2026 · C++ RAG Chatbot · For every developer who dares to build AI from scratch 🇮🇳*

⭐ If this project helped you, please give it a star on GitHub!

</div>