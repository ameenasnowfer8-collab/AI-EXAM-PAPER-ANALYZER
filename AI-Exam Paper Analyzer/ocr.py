import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(uploaded_file):

    image = Image.open(uploaded_file)

    text = pytesseract.image_to_string(image)

    return text