import requests
import json
import os
from bs4 import BeautifulSoup

# Define the correct project root dynamically
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# data path
data_dir = os.path.join(project_root, "_src", "_data")
save_path = os.path.join(data_dir, "movies.json")

# check _src/_data directory exists
os.makedirs(data_dir, exist_ok=True)

# URL to scrape
URL = "https://horror.fandom.com/wiki/Chronological_List_of_Horror_Films"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)

# Check response status
if response.status_code != 200:
    print("Failed to fetch the page.")
    exit()

soup = BeautifulSoup(response.text, "html.parser")
movies = []

# Locate the movie tables
tables = soup.find_all("table", class_="wikitable")

for table in tables:
    rows = table.find_all("tr")[1:]
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:
            year = cols[0].text.strip()
            title = cols[1].text.strip()
            img_tag = cols[1].find("img")
            image_url = img_tag["src"] if img_tag else "No image available"

            movies.append({"title": title, "year": year, "image_url": image_url})

# Save JSON data
with open(save_path, "w", encoding="utf-8") as f:
    json.dump(movies, f, indent=4)

print(f" Movie data saved correctly to: {save_path}")
