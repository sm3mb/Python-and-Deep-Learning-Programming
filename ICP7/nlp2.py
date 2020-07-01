import requests
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://en.wikipedia.org/wiki/Google'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# finding text content
text = soup.find_all('p')

output_file = open("output.txt", "w")

result = ''
for t in text:
	result = str(result) + t.text

output_file.write(str(result))
output_file.close()
