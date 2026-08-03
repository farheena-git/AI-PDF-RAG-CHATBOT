# 📄 AI PDF RAG Chatbot

An AI-powered **Retrieval-Augmented Generation (RAG)** chatbot that enables users to upload PDF documents and interact with them using natural language. The application extracts text from PDFs, splits it into semantic chunks, generates vector embeddings using Google's **Gemini Embedding** model, stores them in a **Qdrant Vector Database**, retrieves the most relevant information based on user queries, and generates context-aware responses using the **Gemini LLM**.

---

##  Features

-  Upload PDF documents through a Streamlit web interface
-  Automatic document chunking using LangChain
-  Semantic search with vector embeddings
-  Store and retrieve embeddings using Qdrant Vector Database
-  AI-powered question answering using Google's Gemini LLM
-  Fast and intuitive Streamlit interface
-  Context-aware responses using Retrieval-Augmented Generation (RAG)

---

##  Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit |
| **Framework** | LangChain |
| **LLM** | Google Gemini |
| **Embeddings** | Gemini Embedding Model |
| **Vector Database** | Qdrant |
| **Programming Language** | Python |

---

## 🔄 Workflow

```text
           PDF Upload
                │
                ▼
        PDF Text Extraction
                │
                ▼
     Recursive Text Chunking
                │
                ▼
      Gemini Embeddings
                │
                ▼
     Qdrant Vector Database
                │
                ▼
      Similarity Search
                │
                ▼
      Relevant Chunks
                │
                ▼
         Gemini LLM
                │
                ▼
      Context-Aware Answer
```

---

## How It Works

1. Upload a PDF document using the Streamlit interface.
2. Extract text from the uploaded PDF.
3. Split the document into overlapping semantic chunks.
4. Generate embeddings for each chunk using the Gemini Embedding model.
5. Store the embeddings in the Qdrant Vector Database.
6. Perform similarity search to retrieve the most relevant chunks based on the user's query.
7. Pass the retrieved context to the Gemini LLM.
8. Generate an accurate and context-aware response.

---

