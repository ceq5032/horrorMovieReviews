---
title: Upcoming Horror Movies
layout: layouts/about.html
permalink: latest.html
---

## Upcoming Horror Movies

{% for movie in upComing %}
### {{ movie.title }}
- **Genre**: {{ movie.genre }}
- **Rating**: {{ movie.rating }}
- **Description**: {{ movie.description }}
- **Duration**: {{ movie.duration }}
  {% endfor %}

## Links to Scripts

- [upComing.py](./upComing.py) – Python script to generate `upComing.json`.
- [scrapeUpcoming.py](./scrapeUpcoming.py) – Python script for scraping the IMDb list.
- [upComing.json](./_data/upComing.json) – The generated JSON data.

You can run these scripts to regenerate the data if needed.

