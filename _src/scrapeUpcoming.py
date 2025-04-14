import requests
from bs4 import BeautifulSoup
import csv
import json

url = "https://www.imdb.com/list/ls528329180/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

json_ld_scripts = soup.find_all("script", type="application/ld+json")

movies = []

for script in json_ld_scripts:
    try:
        data = json.loads(script.string)
        if data.get("@type") == "ItemList":
            for item in data["itemListElement"]:
                movie = item["item"]
                image_url = movie.get("image", {}).get("url", "")
                movies.append({
                    "title": movie.get("name"),
                    "description": movie.get("description"),
                    "genre": movie.get("genre"),
                    "duration": movie.get("duration"),
                    "rating": movie.get("aggregateRating", {}).get("ratingValue", "N/A"),
                    "image_url": image_url
                })
    except Exception as e:
        continue

csv_filename = "horror_movies.csv"

with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["title", "description", "genre", "duration", "rating", "image_url"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for movie in movies:
        writer.writerow(movie)

print(f"✅ CSV file '{csv_filename}' created successfully with {len(movies)} movies.")
