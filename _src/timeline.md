---
title: Top 25
layout: layouts/about.html
permalink: timeline.html
---

<div class="timeline">
  <h1><a href="https://www.imdb.com/list/ls003174642/"> IMDb </a> Top 25 Horror Movies</h1>
  {% for movie in movies %}
    <div class="event">
      <span>{{ loop.index }}</span> 
      <h3>{{ movie.title }} ({{ movie.year }})</h3>
      <p>Rating: {{ movie.rating }}</p>
      <div class="popup">
        <img src="{{ movie.img_url }}" alt="Poster for {{ movie.title }}">
        <p>{{ movie.title }}</p>
      </div>
    </div>
  {% endfor %}
</div>

