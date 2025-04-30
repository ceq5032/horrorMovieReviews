---
title: Latest Horror Movie Rumors 
layout: layouts/about.html
permalink: latest.html
---
<div class="timeline">
  <script>
    const moviesData = {{ moviesUP | jsonify }};
    console.log(moviesData);
  </script>
  <h1> Rotten Tomatoes Upcoming Movies </h1>
  <p> Here is a list of Upcoming Horror Movies! </p>

  {% for movie in moviesUP %}
  <div class="event">
    <span>{{ loop.index }}</span> 
    <h3>{{ movie.title }} ({{ movie.critic_score }})</h3>
    <div class="popup">
      <img src="{{ movie.image_url }}" alt="Poster for {{ movie.title }}">
      <p>{{ movie.title }}</p>
    </div>
  </div>
  {% endfor %}
</div>
