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

Eentermen zijn belangrijke functies en dus zijn hun afgeleiden dat ook. In de les [afgeleide van een functie](../../afgeleiden_1/afgeleide_functie/) werd de algemene formule voor de afgeleide uitgelegd. Eventjes opfrissen:

$$ f'(x) = \lim_{\Delta x \rightarrow 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}$$

Als we nu de functie $f$ vervangen door de eenterm wordt die formule:
$$ f'(x) = \lim_{\Delta x \rightarrow 0} \frac{ (x + \Delta x)^n - x^n}{\Delta x} $$

Hmm. Dit algemeen uitwerken ziet er niet simpel uit. De term $(x + \Delta x)^n$ is niet zo eenvoudig te veralgemenen. Maar we kunnen slimmer zijn. Als we de limiet van iets dat naar nul gaat moeten berekenen, volstaat het om te kijken naar de termen met $\Delta x$ in de breuk met de kleinste exponent. Als $\Delta x$ heel klein wordt, zullen die nog veel grooter zijn dan termen met een grotere exponent. 

Voor $n$ gelijk aan 2, 3 en 4 krijgen we, door de distributieve eigenschap toe te passen, het volgende resultaat:

$$
\begin{align*}
(x + \Delta x)^\red{2} &= (x + \Delta x) (x + \Delta x) = \green{x^2} + \orange{2 x \Delta x} + \Delta x^2 \\\\
(x + \Delta x)^\red{3} &= \cdots  = \green{x^3} + \orange{3 x^2 \Delta x} + 3 x \Delta x^2 + \Delta x^3 \\\\
(x + \Delta x)^\red{4} &= \cdots  = \green{x^4} + \orange{4  x^3 \Delta x} + 6 x^2 \Delta x^2 + 4 x \Delta x^3 + \Delta x^4 \\\\
\end{align*}
$$

De uitgewerkte versies kan je best bekijken als veeltermen in de variabele $\Delta x$. Alles wat niet $\Delta x$ is, zijn de coëfficienten van die veelterm. In elke uitgewerkte veelterm is een term zonder $\Delta x$. Die heeft als coëfficient $x^n$. De volgende term bevat $\Delta x$ tot de 'eerste' macht. De coëfficient van deze term volgt ook een, op het eerste zicht minder duidelijk, patroon: $n x^{n-1}$. Als je ons niet gelooft dat dit altijd geldt, kijk dan eens op deze [site](http://www.wikiwand.com/nl/Binomium_van_Newton) over het binomium van Newton

Gebruiken we nu die twee kleinste graads termen in de formule van de afgeleide:

$$
\begin{align*}
f'(x) &= \lim_{\Delta x \rightarrow 0} \frac{ x^n + n x ^ {n -1} \Delta x - x^n  }{\Delta x} \\\\
f'(x) &= \lim_{\Delta x \rightarrow 0} \frac{n x ^ {n -1} \Delta x }{\Delta x} \\\\
f'(x) &= \lim_{\Delta x \rightarrow 0} n x ^ {n -1} \\\\
f'(x) &= nx^{n-1}
\end{align*}
$$

In de laatste regel zijn alle termen met $\Delta x$ weggevallen, en dus ook de limiet. Dit beketent dat we een uitdrukking hebben gevonden voor de afgeleide van $x^n$, namelijk $nx^{n-1}$. Hoera!

De formule geldt voor positieve en negatieve exponenten. Eentermen met negatieve exponenten worden meestal als een breuk geschreven. Denk er dus aan om die breuk eerst als een eenterm te schrijven! Bijvoorbeeld de eenterm $x^{-2}$ zal je sneller tegen komen als $\frac{1}{x^2}$. De formule werkt alleen voor eentermen in de vorm $x^n$, dus moet je de breuk eerst omvormen.
# Voorbeelden
In de tabel hieronder staan enkele voorbeelden. In de eerste kolom staat de functie $f(x)$, in de tweede kolom de exponent van de eenterm $n$ en in de derde kolom de afgeleide $f'(x)$. Test je door de tweede en derde kolom of te dekken en probeer zelf het antwoord te vinden door de formule toe te passen!

| $\quad f(x) \quad$ | $\quad n \quad$   | $\quad f'(x) \quad$ |
| ---------------- | ---------------- | ------------ |
| $x^5$ |   $5$   | $5x^4$ |
| $x^{42}$ |   $42$   | $42x^{41}$ |
| $x$ | $1$ | $1$ |
| $\frac{1}{x} = x^{-1}$ | $-1$ | $-x^{-2}$ |
| $\frac{1}{x^3} = x^{-3}$ | $-3$ | $-3x^{-4}$ |

# Truckje
Om de formule zeker niet te vergeten, kan je het berekenen van een de afgeleide van een eenterm ook bekijken als het 'naar beneden halen van de exponent, en er daarna een van aftrekken in de exponent'. Zoals hier: 
{{< svg "img/trick.svg" "Truckje" >}}
De rode tekst is wat je moet toevoegen aan de eenterm om zijn afgeleide te vinden!

# Samengevat

{{< attention "De afgeleide van $x^n$" >}}
De afgeleide van een eenterm kan snel gevonden worden door de formule te gebruiken:

| $\quad f(x) \quad$ | $\quad f'(x) \quad$ |
| -------| ------- |
| $x^n$  | $nx^{n-1}$ |

{{< /attention >}}