---
title: top 25 upcoming
layout: layouts/about.html
permalink: latest.html
---

<div class="containerL">

  <h3><a href="https://www.imdb.com/list/ls056154538/">IMDb </a> Upcoming Horror Movies</h3>

  {% for movie in upcoming_movies %}
    
    <h3>{{ movie.title }} ({{ movie.year }})</h3>
    <img src="{{ movie.img_url }}" alt="Poster for {{ movie.title }}">
  {% endfor %}

</div>

