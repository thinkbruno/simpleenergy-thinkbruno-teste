import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup

from dotenv import load_dotenv #work with ambient var
load_dotenv()

def extract(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser") # analyzing html
        text_elements = soup.find_all("p") # find all text
        extracted_text = "\n".join(text_element.get_text() for text_element in text_elements) # organizing all texts
        return extracted_text
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

    except Exception as e:
        print(f"An error has occurred: {e}")
        return None

def save_text(text, filename=f"{datetime.now().strftime("%Y-%m-%d")}_text.txt"):
    try:
        if os.path.exists(filename): # If exists, add a counter to the file name
            count = 1
            base_name, extension = os.path.splitext(filename)
            while os.path.exists(filename):
                filename = f"{base_name}({count}){extension}"
                count += 1
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Extracted text saved in {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")
    
file_url = os.getenv("FILE_URL")
extracted_text = extract(file_url)

if extracted_text:
    save_text(extracted_text)