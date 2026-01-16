import streamlit as st
from utils import (
    extract_text_from_pdf,
    summarize_text,
    generate_qa_from_summary,
)

# Page configuration
st.set_page_config(
    page_title="PDF Summarization & Q&A",
    layout="centered"
)

st.title("📄 PDF Summarization & Intelligent Q&A System")
st.write("Upload a PDF to generate summary and questions using AI.")

# File upload
uploaded_file = st.file_uploader(
    "Upload your PDF file",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("PDF uploaded successfully!")

    # Extract text
    with st.spinner("Extracting text from PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    if not pdf_text.strip():
        st.error("No readable text found in the PDF.")
    else:
        # Summarization
        if st.button("Generate Summary"):
            with st.spinner("Generating summary using AI..."):
                summary = summarize_text(pdf_text)

            st.subheader("📌 PDF Summary")
            st.write(summary)

            # Store summary in session
            st.session_state["summary"] = summary

        # Generate Q&A
        if "summary" in st.session_state:
            if st.button("Generate Q&A"):
                with st.spinner("Generating questions and answers..."):
                    qa = generate_qa_from_summary(st.session_state["summary"])

                st.subheader("❓ Auto Generated Questions & Answers")
                st.text(qa)

# Footer
st.markdown("---")
st.caption("ML Project | PDF Summarization & Q&A using Cohere API and Streamlit")
