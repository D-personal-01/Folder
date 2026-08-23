import requests
from bs4 import BeautifulSoup
url=input("Enter the URL of the website you want to scrape: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

