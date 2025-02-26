import pytesseract
from PIL import Image

image = Image.open("Image20250225173532.png")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(image)

print(text)