---
title: "Building the AI-Ready SOC"
type: pages
excerpt: "A series on turning analyst expertise into something AI can apply at scale."
sitemap: true
permalink: /series/ai-ready-soc/
---

{{ site.data.series['ai-ready-soc'].argument }}

{% assign series_posts = site.posts | where: "series", "ai-ready-soc" | sort: "series_part" %}
<ol class="series-landing__list">
  {% for post in series_posts %}
    <li>
      <a href="{{ post.url | relative_url }}">Part {{ post.series_part }}: {{ post.title }}</a>
      {% if post.excerpt %}<p>{{ post.excerpt | strip_html }}</p>{% endif %}
    </li>
  {% endfor %}
</ol>
