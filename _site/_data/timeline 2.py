
import requests
import json
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/list/ls062634338/"

# Send request to IMDb
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract movie details
movies = []
for item in soup.select(".lister-item")[:25]:  # Limit to top 25 movies
title_tag = item.select_one(".lister-item-header a")
year_tag = item.select_one(".lister-item-year")
image_tag = item.select_one(".loadlate")

if title_tag and year_tag and image_tag:
title = title_tag.text.strip()
year = year_tag.text.strip("()")
image_url = image_tag["loadlate"]

movies.append({"title": title, "year": year, "image_url": image_url})

# Save to JSON
with open("_src/_data/timeline.json", "w", encoding="utf-8") as f:
json.dump(data, f, indent=4)



print("Movie data saved to src/_data/timeline.json!")
