---
title: "Tools"
layout: single
type: pages
excerpt: "Tools built to answer specific security questions."
author_profile: false
sitemap: true
permalink: /tools/
---

Things I've built to answer questions I kept running into at work. Free to use.

<ul class="tools-list">
{% for tool in site.data.tools %}
  <li class="tools-list__item">
    <h2 class="tools-list__name"><a href="{{ tool.url }}">{{ tool.name }}</a></h2>
    <p class="tools-list__description">{{ tool.description }}</p>
    <p class="tools-list__cta"><a href="{{ tool.url }}">Open {{ tool.name }} &rarr;</a></p>
  </li>
{% endfor %}
</ul>
