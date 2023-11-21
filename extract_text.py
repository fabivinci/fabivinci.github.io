import os
import pytesseract
import re
from PIL import Image
from tqdm import tqdm
import zipfile  # Importa la libreria zipfile
 
input_folder = "uploads/"
 
def remove_special_characters(text):
    # Utilizziamo un'espressione regolare per trovare e sostituire i caratteri speciali con uno spazio vuoto
    text = re.sub(r'[^\w\s]', ' ', text)
    return text
 
def ocr_images_in_folder(input_folder):

    input_path = os.path.join(input_folder, filename)

    # Esegui l'OCR sull'immagine
    image = Image.open(input_path)
    text = pytesseract.image_to_string(image, lang='ita')  # Cambia 'ita' con la lingua desiderata

    # Rimuovi i caratteri speciali dal testo
    text = remove_special_characters(text)

    print(text)
 
# Utilizzo della funzione con il tuo percorso specifico
ocr_images_in_folder(input_folder)
