---
title: Timeline of Best Horror Movies
layout: layouts/about.html
permalink: timeline.html
---

<div class="timeline">
  <script>
    console.log({{ movies | json }});
  </script>
<h1> Rotten Tomatoes Best Horror Movies of All Times </h1>
<p>Below is a timeline of Rotten Tomatoes' best horror movies of all time. The movies are ranked in order, starting with number 1. What are your thoughts on this timeline? Do you agree with their rankings? </p>
{% for movie in movies %}
<div class="event">
<span>{{ loop.index }}</span> 
<h3>{{ movie.title }} ({{ movie.year }})</h3>
<div class="popup">
<img src="{{ movie.image_url }}" alt="Poster for {{ movie.title }}">
<p>{{ movie.title }}</p>
</div>
</div>
{% endfor %}
</div>


