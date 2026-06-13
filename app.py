import streamlit as st

from pdf_reader import read_pdf
from text_splitter import split_text
from vector_store import create_vector_store
from chatbot import ask_question

st.title("AI PDF Chatbot")

pdf = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if pdf is not None:

    if st.button("Process PDF"):

        with st.spinner("Processing PDF..."):

            text = read_pdf(pdf)
            chunks = split_text(text)
            vector_store = create_vector_store(chunks)

            st.session_state["vector_store"] = vector_store

        st.success("PDF Processed Successfully!")

if "vector_store" in st.session_state:

    question = st.text_input(
        "Ask a question about the PDF"
    )

    if question:

        answer = ask_question(
            question,
            st.session_state["vector_store"]
        )

        st.write(answer)