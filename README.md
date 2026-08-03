AI PDF RAG Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that enables users to upload PDF documents and interact with them using natural language. The application extracts text from PDFs, splits it into semantic chunks, generates vector embeddings using Google's Gemini Embedding model, stores them in a Qdrant Vector Database, retrieves the most relevant information based on user queries, and generates context-aware responses using the Gemini LLM.

Features
--> Upload PDF documents through a Streamlit web interface
--> Automatic document chunking using LangChain
--> Semantic search with vector embeddings
--> Store and retrieve embeddings using Qdrant Vector Database
--> AI-powered question answering with Google's Gemini LLM
--> Fast and intuitive Streamlit interface
--> Context-aware responses using Retrieval-Augmented Generation (RAG)

Tech Stack
Frontend: Streamlit
LLM: Google Gemini
Embeddings: Gemini Embedding Model
Framework: LangChain
Vector Database: Qdrant
Language: Python

Workflow
Upload a PDF document.
Extract text from the PDF.
Split the document into overlapping chunks.
Generate embeddings for each chunk.
Store embeddings in the Qdrant Vector Database.
Retrieve relevant chunks for user queries.
Generate accurate responses using the Gemini LLM.
