from flask import Flask, render_template, request
import pytesseract
from pdf2image import convert_from_path
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['IMAGES_FOLDER'] = 'images'  # New folder for converted images

# Create directories if they don't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['IMAGES_FOLDER'], exist_ok=True)

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = None
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        text_result = ""
        
        # Handle PDF
        if file.filename.lower().endswith(".pdf"):
            pages = convert_from_path(filepath, 300)  # 300 DPI
            base_filename = os.path.splitext(file.filename)[0]
            
            for i, page in enumerate(pages):
                # Save each page as an image
                image_filename = f"{base_filename}_page_{i+1}.png"
                image_path = os.path.join(app.config['IMAGES_FOLDER'], image_filename)
                page.save(image_path, 'PNG')
                
                # Extract text from the image
                text_result += pytesseract.image_to_string(page) + "\n"
        else:
            return "Only PDF files are supported"
        
        extracted_text = text_result
    
    return render_template("index.html", extracted_text=extracted_text)

if __name__ == "__main__":
    app.run(debug=True)