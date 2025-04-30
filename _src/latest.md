---
title: Latest Horror Movie Rumors 
layout: layouts/about.html
permalink: latest.html
---
<script>
  const moviesData = {{ moviesUP | json }};
  console.log(moviesData);
</script>

<h3><a href="https://www.imdb.com/list/ls056154538/">IMDb </a>Upcoming Horror Movies</h3>

{% for movie in moviesUP %}
  <div class="containerL">
    <span>{{ loop.index }}</span> 
    <h3>{{ movie.title }} ({{ movie.year }})</h3>
    <img src="{{ movie.img_url }}" alt="Poster for {{ movie.title }}">
    <h4>Rating: {{ movie.rating }}</h4>
  </div>
{% endfor %}


