---
title: "De afgeleide van $x^n$"
date: 2020-04-03T15:34:59+02:00
weight: 1
draft: true
tags: []
images: []
description: ""
---

# De afgeleide van $x^n$
Een belangrijke familie van functies zijn de eentermen. Een eenterm bestaat uit een onbekende, meestal $x$. Die onbekende wordt tot een macht verheft. De macht kan heel algemeen als $n$ worden aangeduid. Voor bijvoorbeeld $x^2$ is $n$ dan gelijk aan $2$. Het algemene functie voorschrift van deze functies is:

$$ f(x) = x^n $$

Eentermen zijn belangrijke functies en dus zijn hun afgeleiden dat ook. In de les [afgeleide van een functie](../../afgeleiden_1/afgeleide_functie/) werd de algemene formule voor de afgeleide uitgelegd. Die formule ziet er als volgt uit:

$$ f'(x) = \lim_{\Delta x \rightarrow 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}$$

Als we nu de algemene formule voor een eenterm invullen in die limiet, vinden we de volgende formule
$$ f'(x) = \lim_{\Delta x \rightarrow 0} \frac{ (x + \Delta x)^n - x^n}{\Delta x} $$

Hmm. Dit algemeen uitwerken ziet er niet eenvoudig uit. De term $(x + \Delta x)^n$ is niet zo eenvoudig te veralgemenen. Maar we kunnen slimmer zijn. Als we de limiet van iets naar nul moeten berekenen, volstaat het om te kijken naar de laagste graads termen in een breuk. Hier nemen we de limiet van $\Delta x$ naar $0$. 

*Dilemma. Die macht met n uitwerken met binomium is niet echt makkelijk als ge dat niet kent. Twee eerste termen zijn $x^n$ en $n x^{n-1} \Delta x$. Wat het wel duidelijk maakt. Moet zelfs geen limiet meer uitgerekend worden.*

# De afgeleide van $x^n$, maar dan snel en praktisch
