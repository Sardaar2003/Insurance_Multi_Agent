# 🏦 Enterprise Insurance Multi-Agent AI Platform

An **enterprise-grade multi-agent insurance assistant** built using:

* **LangGraph orchestration**
* **RAG (Retrieval Augmented Generation)**
* **LangChain**
* **Vector Database (ChromaDB)**
* **Streamlit UI**
* **Role-Based Access Control (RBAC)**
* **Audit Logging + Metrics Monitoring**

This system simulates a **FAANG-style AI architecture** for insurance operations including policy queries, knowledge retrieval, and enterprise governance.

---

# 🚀 Features

## 👤 User Features

* Login authentication
* Ask insurance-related questions
* Retrieve personal profile information
* AI-powered responses from knowledge base
* Secure session management

## 👑 Admin Features

* Upload multiple documents (PDF/DOCX/TXT)
* Knowledge indexing using RAG pipeline
* Audit log monitoring
* System metrics dashboard
* Role-based access control

## 🤖 AI Capabilities

* Multi-agent orchestration
* Knowledge retrieval (RAG)
* Semantic search
* Document chunking & embeddings
* LLM-based answer generation
* Persistent vector storage

---

# 🧠 System Architecture

```
User Query
   ↓
Authentication
   ↓
Intent Processing
   ↓
Knowledge Service (RAG)
   ↓
Vector Database Retrieval
   ↓
LLM Response Generation
   ↓
Decision + Output Guardrails
```

---

# 📂 Project Structure

```
insurance_multiagent/
│
├── app.py                     # Streamlit UI
│
├── agents/                    # AI agents
│   ├── general_agent.py
│   ├── executor_agent.py
│
├── rag/                       # Retrieval pipeline
│   ├── vector_store.py
│   ├── retriever.py
│   ├── document_loader.py
│
├── services/                  # Business services
│   ├── auth_service.py
│
├── database/                  # SQLite storage
│   ├── sqlite_store.py
│   ├── seed_data.py
│
├── vector_db/                 # Persistent embeddings (ignored in git)
├── .env                       # API keys (ignored in git)
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <repo-url>
cd Insurance_Multi_Agent
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```
venv\Scripts\activate
```

### Mac/Linux

```
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Setup

Create `.env` in project root:

```
OPENAI_API_KEY=your_api_key_here
```

⚠️ Never commit `.env`.

---

# 🗄 Initialize Database

```bash
python database/seed_data.py
```

Creates:

* users
* profiles
* system tables

---

# ▶ Run Application

```bash
streamlit run app.py
```

---

# 🔑 Default Credentials

### Admin

```
username: admin
password: admin@123
```

### User

```
username: user1
password: pass123
```

---

# 📚 Knowledge Upload (Admin)

1. Login as admin
2. Upload policy documents
3. Documents are:

   * chunked
   * embedded
   * stored in vector database
4. Users can query knowledge

---

# 🧩 RAG Pipeline

```
Document Upload
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embedding Generation
   ↓
Vector Storage
   ↓
Semantic Retrieval
```

---

# 📊 Observability

* Audit logging
* System metrics
* Session tracking
* Query monitoring

---

# 🔒 Security

* Role-based access control
* Environment-based secrets
* Data privacy enforcement
* Admin restrictions

---

# 🛠 Tech Stack

* Python
* Streamlit
* LangChain
* LangGraph
* ChromaDB
* SQLite
* Sentence Transformers
* OpenAI / Local LLM

---

# 📈 Future Improvements

* Multi-agent collaboration workflow
* Model routing gateway
* Confidence scoring
* Human-in-the-loop review
* Policy recommendation engine
* Enterprise dashboard analytics
* Cloud deployment

---

# 🤝 Contributing

Pull requests welcome.

---
