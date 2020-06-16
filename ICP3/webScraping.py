import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Deep_learning'

response = requests.get(url) # Connect to the URL

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify())
heading = soup.find(id='firstHeading').string

print(heading)

# print(soup.find_all('a'))
all_links = soup.find_all('a')
f1 = open("output_links.txt", "w")
for link in all_links:
    linkhref = link.get('href')
    f1.write(str(linkhref) + '\n')