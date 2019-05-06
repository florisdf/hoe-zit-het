---
title: "Vergelijkingen van de eerste graad"
date: 2019-01-10T18:10:30+01:00
weight: 2
draft: true
tags: ["vergelijkingen", "algebra"]
categories: ["wiskunde", "algebra"]
level: "2M"
course: "wiskunde"
topic: "algebra"
---
Een [vergelijking](../intro) van de eerste graad in $x$ is een vergelijking
waarvan de **hoogste macht van $x$ gelijk is aan $1$**. Bijvoorbeeld de
vergelijking

$$-3x - 2 + x = 15 - 6x + 9x -3$$

is een eerstegraadsvergelijking omdat elke $x$ een macht $1$ heeft.
De volgende vergelijking is **geen** eerstegraadsvergelijking

$$2 - 9x^\red{2} + 6x = 15 - 6x$$

omdat de hoogste macht van $x$ hier $\red{2}$ is.

In deze les zien we hoe we eerstegraadsvergelijkingen kunnen oplossen in drie
stappen. Tijdens deze stappen zullen we de vergelijking
[omvormen](../omvormen). 
De drie stappen zijn:

1. **Schoonmaakwerk**: vereenvoudig het linker- en rechterlid zodat er langs
beide kanten iets staat van de vorm $a x + b$
{{% mute "(met $a, b \in \mathbb{R}$)" %}};
2. **Alle $x$-en naar links**: vorm de vergelijking om zodat enkel het
linkerlid nog $x$-en bevat;
3. **Alle getallen naar rechts**: vorm de vergelijking om zodat alle getallen in
het rechterlid staan.

## Schoonmaakwerk
De eerste stap in het oplossen van een eerstegraadsvergelijking is de
vergelijking *opkuisen* tot zowel de linker- als rechterkant de vorm $ax + b$
heeft.

$$-3x - 2 + x = 15 - 6x + 9x -3$$

Dit doen we door links en rechts de termen met hetzelfde lettergedeelte samen
te nemen.

\begin{split}
    \red{-3x} - 2 \red{+ x} &= \blue{15}
    \green{- 6x}
    \green{+ 9x} \blue{-3}\\\\\
    \Leftrightarrow \red{-2x} - 2 &= \green{3x} + \blue{12}
\end{split}

We krijgen nu een vergelijking van de vorm
$$\red{a\_{links}\cdot x} + b\_{links} = \green{a\_{rechts}\cdot x} + \blue{b\_{rechts}}$$

Waarbij
\begin{split}
    \red{a\_{links}} &= \red{-2}\\\\\
    b\_{links} &= -2\\\\\
    \green{a\_{rechts}} &= \green{3} \\\\\
    \blue{b\_{rechts}} &= \blue{12}
\end{split}

## Alle $x$-en naar links
De volgende stap is om alle termen met een $x$ als lettergedeelte naar de
linkerkant te brengen. We [vormen de vergelijking om](../omvormen) door de
$a\_{rechts}x$
uit het **rechter**lid van de vergelijking af te trekken. Dan zal de
$a\_{rechts}x$ uit het
rechterlid wegvallen en hebben we enkel in het linkerlid nog een $x$.
In ons voorbeeld is de $ax$ uit het rechterlid $3x$.

\begin{split}
    \Leftrightarrow -2x - 2 &= 3x + 12\\\\\
    \Leftrightarrow -2x - 2 \orange{- 3x} &= 3x + 12 \orange{- 3x}\\\\\
    \Leftrightarrow \green{-2x} - 2 \green{- 3x} &= \blue{3x} + 12 \blue{- 3x}\\\\\
    \Leftrightarrow \green{-5x} - 2 &= 12\\\\\
\end{split}

We zien dat de $3x$ inderdaad is verdwenen uit het rechterlid.
We krijgen een vergelijking met enkel nog in het linkerlid een $x$.

## Alle getallen naar rechts
In de laatste stap brengen we de getallen die in het linkerlid nog overblijven 
naar het rechterlid. Dat doen we zelf best in twee stappen.

1. Trek links en rechts de $b_{links}$ uit het **linker**lid af van de vergelijking
2. Deel door de $a$ van het

\begin{split}
    \Leftrightarrow -5x - 2 &= 12\\\\\
\end{split}
