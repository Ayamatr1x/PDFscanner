from pdf2image import convert_from_path
import pytesseract
import cv2
from PIL import Image

# Path to Tesseract (only if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load PDF
pdf_file = "sample-local-pdf.pdf"
pages = convert_from_path(pdf_file, dpi=300)

# Ask user which page
page_num = int(input(f"Enter page number (1 - {len(pages)}): "))

if 1 <= page_num <= len(pages):
    page = pages[page_num - 1]  # because index starts from 0
    page.save(f'page_{page_num}.jpg', 'JPEG')

    # Preprocess
    image_path = f'page_{page_num}.jpg'
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    processed_path = f"processed_{page_num}.jpg"
    cv2.imwrite(processed_path, thresh)

    # OCR
    text = pytesseract.image_to_string(Image.open(processed_path))
    print(f"\n--- Text from Page {page_num} ---\n")
    print(text)

    # Save text
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- Page {page_num} ---\n")
        f.write(text + "\n")
else:
    print("❌ Invalid page number!")
