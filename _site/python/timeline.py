import requests
from bs4 import BeautifulSoup

# URL of IMDb's Top Horror Movies (You can change this)
URL = "https://www.imdb.com/list/ls062634338/"

# Send a request to IMDb
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract movie details
movies = []
for item in soup.select(".lister-item"):
    title_tag = item.select_one(".lister-item-header a")
    year_tag = item.select_one(".lister-item-year")
    image_tag = item.select_one(".loadlate")

    if title_tag and year_tag and image_tag:
        title = title_tag.text.strip()
        year = year_tag.text.strip("()")  # Removing parentheses
        image_url = image_tag["loadlate"]

        movies.append({"title": title, "year": year, "image_url": image_url})

# Generate the HTML file
    <div class="timeline">
        <h1>Horror Movie Timeline</h1>
        <h2>UNDER CONSTRUCTION</h2>
"""

# Append movie details to HTML
for movie in movies[:30]:  # Limit to top 10 movies
    html_content += f"""
    <div class="event">
        <p>{movie['title']}</p>
        <span class="date">Year: {movie['year']}</span>
        <div class="popup">
            <img src="{movie['image_url']}" alt="{movie['title']} poster">
            <p>{movie['title']}</p>
        </div>
    </div>
    """

html_content += """
    </div>


# Save to a file
with open("timeline.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Horror movie timeline generated successfully!")
