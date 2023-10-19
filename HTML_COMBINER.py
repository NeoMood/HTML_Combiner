import requests
from bs4 import BeautifulSoup

urls = [
    'https://www.lipsum.com/',
    'https://www.lipsum.com/',
    'https://www.lipsum.com/',
    'https://www.lipsum.com/',
]

with open('output.html', 'a', encoding='utf-8') as file:
    for url in urls:
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        file.write(soup.prettify())

print("HTML saved to file: output.html")

