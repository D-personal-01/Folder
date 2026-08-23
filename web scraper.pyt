import requests
from bs4 import BeautifulSoup

url = "https://archive.ics.uci.edu/dataset/2/adult"

# 1. Get the webpage
response = requests.get(url)

# 2. Check whether the request worked
print("Status:", response.status_code)

# 3. Convert HTML into a BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# 4. Get the page title
print("Title:", soup.title.get_text(strip=True))

# 5. Find all links on the page
links = soup.find_all("a")

for link in links:
    text = link.get_text(strip=True)
    href = link.get("href")

    if text:
        print(text, "->", href)