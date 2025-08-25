# 📄 PDF OCR Extractor

A simple Flask web application that extracts text from PDF files using OCR (Optical Character Recognition) technology.

## ✨ Features

- Upload PDF files via web interface
- Extract text from scanned documents and images within PDFs
- Clean, responsive web interface with drag & drop support
- Copy extracted text to clipboard
- Handles multi-page PDFs

## 🛠️ Requirements

- Python 3.7+
- Tesseract OCR engine
- Poppler (for PDF processing)

## 📦 Installation

1. **Install Python dependencies:**
   ```bash
   pip install flask pytesseract pdf2image pillow
   ```

2. **Install Tesseract OCR:**
   - **Windows:** Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS:** `brew install tesseract`
   - **Ubuntu:** `sudo apt install tesseract-ocr`

3. **Install Poppler:**
   - **Windows:** Download from [GitHub](https://github.com/oschwartz10612/poppler-windows/releases/)
   - **macOS:** `brew install poppler`
   - **Ubuntu:** `sudo apt install poppler-utils`

## 🚀 Usage

1. **Run the application:**
   ```bash
   python app.py
   ```

2. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

3. **Upload a PDF file and extract text!**
