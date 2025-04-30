import requests
from bs4 import BeautifulSoup
import csv

url = "https://editorial.rottentomatoes.com/guide/best-horror-movies-of-all-time/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movie_cards = soup.select(".row.countdown-item")


output_file = "_src/horror.csv"


with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["title", "year", "image_url"])

    for card in movie_cards:
        title_tag = card.select_one(".article_movie_title a")
        if not title_tag:
            continue

        title = title_tag.get_text(strip=True)


        year_tag = card.find("span", class_="subtle start-year")
        year = year_tag.get_text(strip=True).strip("()") if year_tag else ""


        image = card.select_one("img")
        image_url = image["data-src"] if image and "data-src" in image.attrs else image["src"]

        writer.writerow([title, year, image_url])

print(" horror.csv has been created!")

