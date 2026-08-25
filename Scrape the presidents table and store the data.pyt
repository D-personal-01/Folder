from bs4 import BeautifulSoup
import requests
import json

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Failed to fetch page: {e}")
    exit(1)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find("table", class_="wikitable sortable")
if not table:
    table = soup.find("table", class_="wikitable")

data = []
for row in table.find_all("tr"):
   
    cells = row.find_all(["th", "td"])
    row_data = [cell.get_text(strip=True) for cell in cells]
    if row_data:
        data.append(row_data)

output_file = 'presidents.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"Table saved to {output_file}")