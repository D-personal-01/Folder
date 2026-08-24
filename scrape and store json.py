import requests
from bs4 import BeautifulSoup
import json

url = "https://www.bu.edu/president/boston-university-facts-stats/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

data = []

for element in soup.find_all(["h2", "h3", "li"]):
    text = element.get_text(" ", strip=True)

    if text:
        data.append(text)

with open("bu_facts.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Done!")