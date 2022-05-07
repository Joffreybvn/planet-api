---
layout: default
title: Planets
front: true
order: 1
permalink: /planets/
---


-------------------
# {{page.title}}

The planet generator API is based on a suite of noise generation algorithms. He is totally random and won't produce two time the same planet. So, better save the ones you like.

The API produces two kind of sprites:
- **Sprite 512x512 masked**: Transparent background, with lighting and solar effect. Ideal to get ready-to-use planet sprites.
- **Sprite 1080x1080 unmasked**: Basic sprite with no effect. It requires further processing from your side (apply your own masks, shadows, light effects, ...).

The API produce more than 10 different kind of planets (Ice, Gaz, Sand, Plasma, Barren, Lava, Moon, ...), but due to the random nature of the system, it is not currently possible to choose a specific one.