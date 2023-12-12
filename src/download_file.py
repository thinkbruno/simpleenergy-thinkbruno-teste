import requests
import sys

def download(url, destiny_path, test_number):
    print(url)
    print(destiny_path)
    print(test_number)
    response = requests.get(url)
    
    if response.status_code == 200:
            with open(destiny_path, 'wb') as arquivo:
                arquivo.write(response.content)
            print(f"The file has been successfully downloaded to {destiny_path} path.")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")
        sys.exit("The script will terminate due to download failure.")

test_number = "1234"
file_url = f"https://simpleenergy.com.br/teste/{test_number}"
destiny_path = ".\download" 

download(file_url, destiny_path, test_number)