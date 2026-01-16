import os
import cohere
from dotenv import load_dotenv
import pdfplumber
from pdf2image import convert_from_path
import pytesseract

# Load environment variables
load_dotenv()

# Cohere API Key
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise ValueError("Cohere API key not found. Please check your .env file.")

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)


def extract_text_from_pdf(pdf_file):
    """
    Extract text from a PDF.
    1. Try pdfplumber first (normal text PDFs)
    2. Fallback to OCR using pytesseract (scanned/image PDFs)
    """
    # --- Step 1: pdfplumber ---
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # --- Step 2: OCR fallback if pdfplumber fails ---
    if not text.strip():
        # Convert PDF pages to images
        pages = convert_from_path(pdf_file)
        for page_image in pages:
            page_text = pytesseract.image_to_string(page_image)
            text += page_text + "\n"

    return text


def summarize_text(text):
    """
    Summarize PDF text using Cohere Chat API.
    """
    if not text.strip():
        return "No text found in PDF."

    # Limit text length for safety
    text = text[:4000]

    response = co.chat(
        model="command-a-03-2025",
        message=f"""
Summarize the following text clearly and concisely.
Focus on key points and important concepts.

TEXT:
{text}
"""
    )

    return response.text


def generate_qa_from_summary(summary, num_questions=5):
    """
    Generate question-answer pairs from summary using Cohere Chat API.
    """
    if not summary.strip():
        return "No summary available."

    response = co.chat(
        model="command-a-03-2025",
        message=f"""
Based on the summary below, generate {num_questions} important
questions with their answers.

SUMMARY:
{summary}

Format:
Q1: ...
A1: ...
Q2: ...
A2: ...
"""
    )

    return response.text
