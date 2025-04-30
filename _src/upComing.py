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

    # Get movie rating
    rating_tag = movie.find('span', class_='ipc-rating-star--rating')
    rating = rating_tag.text.strip() if rating_tag else "N/A"

    # Get movie poster image
    img_tag = movie.find('img', class_='ipc-image')
    img_url = img_tag['src'] if img_tag else "N/A"

    # Get plot (from within each movie block)
    plot_tag = movie.select_one('div.ipc-html-content-inner-div')
    plot = plot_tag.get_text(strip=True) if plot_tag else "No plot available"

    # Find the director
    director_span = soup.select_one('span.sc-7746c29e-3.hBzOQe:contains("Director") + span.sc-7746c29e-2.fQnBdG')
    director = director_span.get_text(strip=True) if director_span else "No director available"

    # Find the stars
    stars_spans = soup.select('span.sc-7746c29e-3.hBzOQe:contains("Stars") + span.sc-7746c29e-2.fQnBdG a')
    stars = [star.get_text(strip=True) for star in stars_spans] if stars_spans else ["No stars available"]

    # Store movie information in a dictionary
    movie_info = {
        'title': title,
        'year': year,
        'rating': rating,
        'img_url': img_url,
        'plot': plot,
        'director': director,
        'stars': stars
    }
    movie_data.append(movie_info)


for movie in movie_data:
    print(f"{movie['title']} ({movie['year']}) - Rating: {movie['rating']}")
    print(f"Plot: {movie['plot']}")
    print(f"Director: {movie['director']}")
    print(f"Stars: {', '.join(movie['stars'])}")
    print(f"Poster URL: {movie['img_url']}")
    print()


import json

with open('moviesUp.json', 'w') as f:
    json.dump(movie_data, f, indent=2)

print("Scraping complete.")
