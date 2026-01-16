# 📄 PDF Summarization & Q&A System

An interactive Python application that extracts text from PDFs, generates concise summaries, and creates intelligent question-answer pairs using AI. Built with **Streamlit**, **Cohere API**, and supports **OCR for scanned PDFs**.

---

## 🌟 Features

- Upload **any PDF** (text-based or scanned)
- Automatic **text extraction**:
  - Uses **pdfplumber** for normal PDFs
  - Falls back to **OCR (Tesseract)** for scanned PDFs
- **Summarization** of PDF content using Cohere Chat API
- **Automatic Q&A generation** from the summary
- Interactive **Streamlit UI**
- College/project-ready and demo-friendly

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **Streamlit** – Frontend UI
- **Cohere API** – NLP summarization & Q&A
- **pdfplumber** – PDF text extraction
- **pytesseract + pdf2image** – OCR for scanned PDFs
- **dotenv** – Manage API keys securely

---

## 🛠 Installation

1. Clone the repository:

2. Create a virtual environment:

python -m venv venv


3. Activate virtual environment:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

4. Install dependencies:

pip install -r requirements.txt


Create a .env file in the project root and add your Cohere API key:

5. COHERE_API_KEY=your_api_key_here

6. 
🚀 Running the App
streamlit run app.py


Upload a PDF

Click Generate Summary

Click Generate Q&A
git clone https://github.com/amanverma95/pdf-ai-summarizer.git
cd pdf-ai-summarizer
