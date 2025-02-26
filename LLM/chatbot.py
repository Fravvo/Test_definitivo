#  ollama pull llama3.2:1b
from ollama import chat, ChatResponse
from pdf2image import convert_from_path
from numpy import asarray
import pytesseract

def pdf_to_text(filename):
    file = filename
    img = convert_from_path(filename)

    ocr_text = []
        
    for image in img:
        # Convert the page intto a numpy array, then perform OCR recognition
        img1 = asarray(image)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(img1)        
        ocr_text.append(text)

    unique_string = '. '.join(ocr_text)
    return unique_string

print("Benvenuto in questo chatbot")
while True:
    print("Ecco le nostre funzioni:")
    print("[1]Riassunto")
    print("[2]Traduzione")
    print("[3]Domanda")
    input_scelta_funzione = str(input("Di quale vuoi usufruire? ")).capitalize()
    match input_scelta_funzione:
        case "1" | "Riassunto" | "R":
            input_file = input("Inserisci il file da riassumere: ")
            optional = ""
            funzione = f"mi fai il riassunto di {pdf_to_text(input_file)}?"

        case "2" | "Traduzione" | "T":
            input_file = input("Inserisci il file da tradurre: ")
            optional = input("In che lingua vuoi che venga tradotto? ")
            funzione = f"mi fai la traduzione di {pdf_to_text(input_file)} in {optional}?"

        case "3" | "Domanda" | "D":
            input_file = ""
            optional = ""
            funzione = input("Cosa vuoi chiedere? ") 

        case "Exit" | "E" | "Esci":
            print("Arrivederci!")
            break
        case _:
            print("Non valido, riprova")
            continue

    response: ChatResponse = chat(model='llama3.2:1b', messages=[
    {
        'role': 'user',
        'content': f'{funzione}',
    },
    ])
    print(response['message']['content'])

    input_continuo = str(input("Vuoi continuare? ")).capitalize()
    print(input_continuo)
    match input_continuo:
        case "Si" | "Yes" | "S" | "Y":
            continue
        case "No" | "N":
            print("Arrivederci!")
            break
# or access fields directly from the response object
#print(response.message.content)
