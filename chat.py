import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.title("📚 RAG Assistant")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{BACKEND_URL}/upload", files=files)
    st.success(response.json()["message"])

# Ask Question
question = st.text_input("Ask a question")

if st.button("Ask"):
    response = requests.post(
        f"{BACKEND_URL}/ask",
        json={"question": question}
    )

    st.write("### Answer:")
    st.write(response.json()["answer"])