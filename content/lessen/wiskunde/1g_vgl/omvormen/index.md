---
title: "Vergelijkingen omvormen"
date: 2019-01-10T18:10:30+01:00
weight: 2
draft: false
wiski: "http://wiski.be/oefenen/eerstegraadsvergelijkingen/take"
tags: ["vergelijkingen", "algebra"]
categories: ["wiskunde", "algebra"]
level: "2M"
course: "wiskunde"
topic: "algebra"
images: []
---
Een [vergelijking](../intro) is de gelijkheid van een *linkerlid* en een *rechterlid* waarbij het linkerlid en/of het rechterlid een of meerdere onbekenden bevat. Vaak is er maar één onbekende, namelijk $x$.

Het is meestal de bedoeling om te zoeken naar die waarden voor de onbekende(n) waarvoor de gelijkheid klopt.

## Van de ene vergelijking naar de andere
Veel vergelijkingen kunnen we oplossen door de vergelijking **om te vormen**. Een vergelijking omvormen betekent dat je er een nieuwe vergelijking van maakt door in het linker- en rechterlid **dezelfde bewerking** te doen. De vergelijking die je krijgt na het omvormen is **even juist als de oorspronkelijke vergelijking**.

Stel dat
\begin{equation}\label{eq:1}
x + 2 = -3x - 1
\end{equation}
Aan wat is $x + 2 \orange{- 6}$
dan gelijk? Wel uit de eerste vergelijking weten we dat $x + 2 = - 3x - 1$. Dan is
$$x + 2 \orange{- 6} = -3x - 1 \orange{- 6}$$
Uitrekenen geeft dus dat
\begin{equation}\label{eq:2}
x \orange{- 4} = - 3x \orange{- 7}
\end{equation}


We zeggen dat we vergelijking \ref{eq:1} hebben *omgevormd* naar vergelijking \ref{eq:2} door in het linker- en rechterlid *dezelfde bewerking* te doen (namelijk links en rechts $\orange{6}$ aftrekken).
Achter elkaar schrijven we de omvorming als volgt:
\begin{split}
&x + &2 &= \quad &-3x - &1\\\\\
\Leftrightarrow\quad &x + &2 \orange{- 6} &= &-3x - &1 \orange{- 6}\\\\\
\Leftrightarrow\quad &x - &4 &= &-3x - &7
\end{split}

{{< expand "Uitbreiding: dubbele pijlen" >}}
Er staat niet voor niets een *dubbele pijl* ($\Leftrightarrow$) tussen de vergelijkingen in plaats van een enkele pijl ($\Rightarrow$ of $\Leftarrow$). Je kan namelijk van de laatste vergelijking ook terug naar de eerste vergelijking gaan. De omvorming is *omkeerbaar*:
\begin{split}
&x - &4 &= \quad &-3x - &7\\\\\
\Leftrightarrow\quad &x + &1 \orange{+ 6} &= &-3x - &2 \orange{+ 6}\\\\\
\Leftrightarrow\quad &x + &2 &= &-3x - &1
\end{split}

Zulke pijlen zijn symbolen uit de logica. Een dubbele pijl wijst op een equivalentie, een enkele pijl op een implicatie.
{{< /expand >}}

## Vergelijkingen oplossen door om te vormen
We zagen hierboven hoe we een vergelijking kunnen omvormen naar nieuwe vergelijkingen door links en rechts dezelfde bewerking toe te voegen. Het trucje is nu om de vergelijking om te vormen naar een vergelijking van de vorm

$$x= \text{(een getal)}$$

waar er in het linkerlid gewoon een $x$ staat en in het rechterlid gewoon een getal. Als we de oorspronkelijke vergelijking naar die vorm kunnen omvormen, weten we waar $x$ aan gelijk moet zijn en is de vergelijking opgelost.

Stel dat we de volgende vergelijking willen oplossen.
$$2x - 6 = 8 - x$$
Om die om te zetten naar de vorm die we willen {{< mute "(namelijk $x= \text{(een getal)}$)" >}}, mag er in het rechterlid geen $x$ staan. De eenvoudigste manier om die weg te krijgen is door een vergelijking te maken met $8 - x \orange{+ x}$ in het rechterlid:

\begin{split}
    2x - 6 &= 8 - x\\\\\
    \Leftrightarrow 2x - 6 \orange{+ x} &= 8 - x \orange{+ x}\\\\\
    \Leftrightarrow \udot{2x} - 6 \udot{\orange{+ x}} &= 8 \cancelto{0}{- x \orange{+ x}}\\\\\
    \Leftrightarrow \udot{\orange{3}x} - 6 &= 8\\\\\
\end{split}

Door aan beide kanten van de vergelijking $\orange{x}$ op te tellen, valt de $-x$ uit het rechterlid weg en is er enkel in het linkerlid nog een $x$.

In de vorm $x= \text{(een getal)}$ staan er in het linkerlid geen getallen meer. De $\orange{3}$ en de $-6$ moeten dus weg links. Je mag kiezen met welke je begint, maar eerst de $-6$ weg krijgen is het eenvoudigst:
\begin{split}
    3x - 6 &= 8\\\\\
    \Leftrightarrow 3x - 6 \orange{+ 6} &= 8 \orange{+6}\\\\\
    \Leftrightarrow 3x \cancelto{0}{- 6 \orange{+ 6}} &= \udot{8 \orange{+6}}\\\\\
    \Leftrightarrow 3x &= \udot{14}\\\\\
\end{split}

Vervolgens moeten we enkel nog de $3$ weg krijgen. Dat kan als volgt:

\begin{split}
    3x &= 14\\\\\
    \Leftrightarrow \frac{3x}{\orange{3}} &= \frac{14}{\orange{3}}\\\\\
    \Leftrightarrow \cancelto{1}{\frac{3}{\orange{3}}}\cdot x &= \frac{14}{\orange{3}}\\\\\
    \Leftrightarrow x &= \frac{14}{3}\\\\\
\end{split}
**En we hebben $x$ gevonden!!!** 🎉💃💪

{{< expand "Uitbreiding: via een andere weg" >}}
Als we in de stap met de keuze tussen $\orange{3}$ en $-6$, kiezen om eerst de $\orange{3}$ weg te werken in plaats van de $6$, vinden we natuurlijk hetzelfde:

\begin{split}
    3x - 6 &= 8\\\\\
    \Leftrightarrow\frac{3x - 6}{\orange{3}} &= \frac{8}{\orange{3}}\\\\\
    \Leftrightarrow x - 2 &= \frac{8}{3}\\\\\
    \Leftrightarrow x - 2 \orange{+2} &= \frac{8}{3} \orange{+2}\\\\\
    \Leftrightarrow x &= \frac{8}{3} +2\\\\\
    \Leftrightarrow x &= \frac{8}{3} +\frac{6}{3}\\\\\
    \Leftrightarrow x &= \frac{14}{3}\\\\\
\end{split}

Maar zoals je ziet, maken we het ons zo onnodig moeilijk.
{{< /expand >}}

## En wat nu?
Daar komt het oplossen van vergelijkingen op neer: de vergelijking stap per stap omvormen naar $x=\text{(een getal)}$. De volgende lessen geven enkele tips van hoe je het snelst naar $x=\text{(een getal)}$ kan omvormen.

## Samengevat
{{< attention "Omvormen" >}}
Door op het linker- en rechterlid van een vergelijking **dezelfde bewerking** uit te voeren, **vormen we een vergelijking om** naar een nieuwe vergelijking die even juist is als de oorspronkelijke vergelijking.
{{< /attention >}}

{{< attention "Oplossen door om te vormen" >}}
We kunnen een vergelijking met onbekende $x$ oplossen door die vergelijking **om te vormen naar $x = \text{(een getal)} $.**
{{< /attention >}}
