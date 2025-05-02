import requests
from bs4 import BeautifulSoup

# IMDb list URL
url = "https://www.imdb.com/list/ls056154538/"

# Add headers to simulate a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send HTTP request to the IMDb list page with headers
response = requests.get(url, headers=headers)
response.raise_for_status()  # Check if the request was successful

# Parse the content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')


# Find the section containing the movies in the list
movies = soup.find_all('div', class_='sc-995e3276-0')

# Extract movie data
movie_data = []
for movie in movies:
    # Get movie title
    title_tag = movie.find('h3', class_='ipc-title__text')
    title = title_tag.text.strip() if title_tag else "N/A"

    # Get movie year
    year_tag = movie.find('span', class_='idrYgr')
    year = year_tag.text.strip() if year_tag else "N/A"

    # Get movie poster image
    img_tag = movie.find('img', class_='ipc-image')
    img_url = img_tag['src'] if img_tag else "N/A"

    # Store movie information in a dictionary
    movie_info = {
        'title': title,
        'year': year,
        'img_url': img_url,

    }
    movie_data.append(movie_info)


for movie in movie_data:
    print(f"{movie['title']} ({movie['year']})")
    print(f"Poster URL: {movie['img_url']}")
    print()


import json

with open('upcoming_movies.json', 'w') as f:
    json.dump(movie_data, f, indent=2)

print("Scraping complete.")
