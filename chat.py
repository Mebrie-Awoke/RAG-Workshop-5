import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

if "history" not in st.session_state:
    st.session_state.history = []

st.title("📚 RAG Assistant")


uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    # Proper file formatting from Code 1
    files = {"file": (uploaded_file.name,
                      uploaded_file.getvalue(), 
                      "application/pdf")}
    
    # Error handling from Code 1
    response = requests.post(f"{BACKEND_URL}/upload", files=files)
    
    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error(response.text)

# Ask Question with validation (from Code 1)
question = st.text_input("Ask a question")

# Button with condition check from Code 1
if st.button("Ask") and question:  # Only triggers if question exists
    response = requests.post(
        f"{BACKEND_URL}/ask",
        json={"question": question}
    )
    
    answer = response.json()["answer"]
    
    # Display answer
    st.write("### Answer")
    st.write(answer)
    
    # Save to history with proper formatting (from Code 1)
    st.session_state.history.insert(0, {
        "question": question,
        "answer": answer
    })
    
    # Keep only last 10 items (from Code 1)
    st.session_state.history = st.session_state.history[:10]

# Display history section (from Code 1)
st.divider()
st.subheader("🕘 Search History (Last 10)")

# Display history with expanders (from Code 1)
for item in st.session_state.history:
    with st.expander(item["question"]):
        st.write(item["answer"])
