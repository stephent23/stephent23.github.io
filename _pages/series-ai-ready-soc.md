---
title: "Building the AI-Ready SOC"
layout: single
type: pages
excerpt: "A series on turning analyst expertise into something AI can apply at scale."
author_profile: false
sitemap: true
permalink: /series/ai-ready-soc/
---

<p class="series-landing__argument">{{ site.data.series['ai-ready-soc'].argument }}</p>

{% assign series_posts = site.posts | where: "series", "ai-ready-soc" | sort: "series_part" %}
<ol class="series-landing__list">
  {% for post in series_posts %}
    <li class="series-landing__item">
      <p class="series-landing__part">Part {{ post.series_part }}</p>
      <h2 class="series-landing__title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      {% if post.description %}<p class="series-landing__description">{{ post.description }}</p>{% endif %}
    </li>
  {% endfor %}
</ol>

{% include subscribe.html copy="The next part covers how expertise actually gets captured. Sent when it publishes, nothing else." %}
