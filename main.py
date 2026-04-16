import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import xml2epub
import time
import os

# URL da página que você deseja extrair dados
url = input('Enter chapter URL: ')

# Faz a requisição HTTP para a página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (status code 200)
if response.status_code == 200:
    # Cria o objeto BeautifulSoup para fazer o parsing do HTML
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print("Falha ao acessar a página:", response.status_code)
    exit()

ficHeader = soup.find('div', class_='fic-header').a
urlBase = "https://www.royalroad.com"
urlFic = urlBase + ficHeader["href"]
ficTitle = ficHeader.h2.get_text()

response = requests.get(urlFic)

if response.status_code == 200:
    # Cria o objeto BeautifulSoup para fazer o parsing do HTML
    fic_soup = BeautifulSoup(response.text, 'html.parser')
else:
    print("Falha ao acessar a página:", response.status_code)
    exit()

img_url = fic_soup.find('img', class_='thumbnail')['src']
img_data = requests.get(img_url).content

#create folder if it doesn't exist
filename = './covers/cover_img.jpg'
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'wb') as f:
    f.write(img_data)

book = xml2epub.Epub(ficTitle, language='en')
coverChapter = xml2epub.create_chapter_from_string(filename, local=True, title='Cover', strict=False)
book.add_chapter(coverChapter)

def getNextChapter(soup):
    nextBtn = soup.find('div', class_='col-md-offset-4').a
    nextUrl = urlBase + nextBtn["href"]

    # Faz a requisição HTTP para a página
    response = requests.get(nextUrl)

    # Verifica se a requisição foi bem-sucedida (status code 200)
    if response.status_code == 200:
        # Cria o objeto BeautifulSoup para fazer o parsing do HTML
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        print("Falha ao acessar a página:", response.status_code)
        exit()

    return soup

numChapters = int(input('Number of chapters that you want in this book: '))

for i in range(1, numChapters + 1):
    try:
        warning = soup.find('div', class_='chapter-content').div
        # print(warning.text)
        warning.decompose()
    except:
        # print("No warning found")
        pass

    chapterTitle = str(soup.h1)
    chapterText = str(soup.find('div', class_='chapter-content'))
    chapterText = chapterTitle + chapterText

    print(f"{i} - {soup.h1.text}")
    ficChapter = xml2epub.create_chapter_from_string(chapterText, url=url, title=soup.h1.text, strict=False)
    book.add_chapter(ficChapter)

    time.sleep(0.6)
    try:
        soup = getNextChapter(soup)
    except:
        print("There is no next chapter")
        print(f"book finished with {i} chapters")
        break

book.create_epub('./books/')
print(f"Book {ficTitle}")