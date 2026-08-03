import os
import tempfile
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore, RetrievalMode
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="PDF RAG ASSISTANT",
    page_icon="📖",
    layout="centered",
)
st.title("📄 PDF RAG Chatbot")
st.write("I am you PDF RAG ASSISTANT. YOU CAN UPLOAD YOUR FILES AND RETRIEVE DATA FROM THE FILES YOU UPLOADED.")

GOOGLE_API_KEY = "your_gemini_api_key"

llm_client = OpenAI(
    api_key=GOOGLE_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

qdrant_client = QdrantClient(
    url="http://localhost:6333/"
)

# PDF UPLOAD

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("PDF Uploaded Successfully!")

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    loader = PyPDFLoader(temp_path)
    docs = loader.load()

    st.write("Total Pages :", len(docs))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    st.write("Total Chunks :", len(chunks))


    collections = qdrant_client.get_collections().collections
    collection_names = [c.name for c in collections]

    if "my_documents" not in collection_names:

        qdrant_client.create_collection(
            collection_name="my_documents",
            vectors_config=VectorParams(
                size=3072,
                distance=Distance.COSINE
            )
        )

    embedding_model = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview",
        google_api_key=GOOGLE_API_KEY
    )

    qdrant = QdrantVectorStore(
        client=qdrant_client,
        collection_name="my_documents",
        embedding=embedding_model,
        retrieval_mode=RetrievalMode.DENSE
    )

    qdrant.add_documents(chunks)

    st.success("Document Stored in Qdrant Successfully!")

    st.divider()


    query = st.text_input("Ask a question from the PDF")

    if st.button("Search"):

        if query:

            found_docs = qdrant.similarity_search(query)

            st.subheader("Retrieved Chunks")


            SYSTEM_PROMPT = f"""You are a PDF RAG Assistant. You need analyse the pdf carefully and answer only from the pdf uploaded. You must give concise and
            content aware answers from the pdf only"""
Context:
{found_docs}
"""
            response = llm_client.chat.completions.create(
                model="gemini-3.6-flash",
                reasoning_effort="low",
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            )

            st.subheader("Answer")

            st.write(response.choices[0].message.content)
