# 🧠 MCP Server: Model Context Prototyping with Gemini + MySQL + FastAPI

## 📌 Project Overview

**MCP Server** is a lightweight, extendable API server that:
- Accepts a natural language `prompt`
- Sends the prompt to **Gemini (Google's LLM)** via API
- Stores both the prompt and the AI-generated response into a **MySQL database**
- Built using **FastAPI**, **Google Generative AI SDK**, and **MySQL**

## ⚙️ Features

- 🌐 REST API Endpoint: `/get-context/`
- 🧠 LLM Integration: Gemini via `google-generativeai`
- 🗃️ Database Logging: Stores prompt & response
- 🔐 API key secured via `.env`
- 🚀 Easy to deploy on local or cloud (Render, Railway, etc.)

## 📁 Folder Structure

```
mcp-server/
│
├── app.py                  # Main FastAPI server
├── gemini_integration.py   # Gemini API integration
├── schema.sql              # SQL for DB setup
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
└── README.md               # Project documentation
```

## 🏁 Getting Started

### ✅ 1. Clone or Unzip the Project

```bash
unzip mcp_server.zip
cd mcp-server
```

### ✅ 2. Install Requirements

```bash
pip install -r requirements.txt
```

### ✅ 3. Configure Environment Variables

Create or edit the `.env` file:

```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

You can get your key from [Google AI Studio](https://makersuite.google.com/app).

### ✅ 4. Setup MySQL Database

#### Option A: Use `schema.sql`

Run this SQL file in MySQL:

```sql
CREATE DATABASE IF NOT EXISTS mcp_db;
USE mcp_db;

CREATE TABLE IF NOT EXISTS responses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prompt TEXT,
    response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### ✅ 5. Run the FastAPI Server

```bash
uvicorn app:app --reload
```

Access it at:  
📍 `http://127.0.0.1:8000`

## 🧪 How to Use

### 🚀 API Endpoint

**POST** `/get-context/`  
**Content-Type:** `application/json`

#### 📥 Request Body

```json
{
  "prompt": "What is quantum computing?"
}
```

#### 📤 Response

```json
{
  "status": "success",
  "response": "Quantum computing is a field of computing that..."
}
```

## 🔐 Security Notes

- API key stored securely in `.env`
- Use HTTPS if deploying online

## ☁️ Cloud Deployment

Deploy on:
- [Render.com](https://render.com)
- [Railway.app](https://railway.app)

## 📦 Postman Test

```bash
curl --location --request POST 'http://127.0.0.1:8000/get-context/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "prompt": "What is quantum computing?"
}'
```

## 📜 License

Open-source for research, learning, and educational purposes.
