from pdf2image import convert_from_path
from numpy import asarray
import pytesseract

filename = 'nomeFile.pdf'
img = convert_from_path(filename)

ocr_text = []
    
for image in img:
    # Convert the page intto a numpy array, then perform OCR recognition
    img1 = asarray(image)
    text = pytesseract.image_to_string(img1)        
    ocr_text.append(text)

# Create a unique string from array of text
unique_string = '. '.join(ocr_text)

prompt: f"riassumi questo testo {unique_string}"