---
title: "Bewerkingen met veeltermen"
date: 2020-06-04T09:29:43+02:00
weight: 4
draft: true
description: "In deze les leggen we uit hoe je kan rekenen met veeltermen. Hoe
tel je veeltermen bij elkaar op of vermenigvuldig je ze? Hoe deel je een
veelterm door een eenterm? En hoe vermenigvuldig je een veelterm met een
eenterm?"
tags: ["veeltermen", "veelterm", "bewerkingen met veeltermen", "veeltermen
optellen", "veeltermen aftrekken", "veeltermen vermenigvuldigen", "veelterm
vermenigvuldigen met een eenterm", "veelterm delen door een eenterm", "som van
veeltermen", "verschil van veeltermen", "product van veeltermen", "product van
een veelterm en een eenterm", "quotient van een veelterm en een eenterm"]
images: []
---

Net zoals je op getallen bewerkingen kan uitvoeren (optellen, aftrekken,
vermenigvuldigen,...), kan je dat ook met veeltermen. In principe kan je eender
welke bewerking die je met getallen kan doen, ook met veeltermen doen wanneer
de variabelen van de veelterm reële of rationale getallen zijn. We gaan ons
voorlopig echter tot vier basisbewerkingen beperken:

* Veeltermen optellen (en aftrekken)
* Een eenterm vermenigvuldigen met een veelterm
* Veeltermen vermenigvuldigen
* Een veelterm delen door een eenterm

We bespreken deze bewerkingen hieronder apart.

{{< expand "Alle variabelen in deze zijn $\in \mathbb{R}$ (of $\in\mathbb{Q}$)" >}}

We gaan ervan uit dat alle variabelen in deze les een element zijn van de reële
getallen.  Als je nog niet weet wat reële getallen zijn, mag je ook aannemen
dat de variabelen een element zijn van de rationale, gehele of zelfs natuurlijk
getallen. Voor al die verzamelingen gelden dezelfde rekenregels wat
betreft bewerkingen met veeltermen.
{{< /expand >}}

## Veeltermen optellen en aftrekken

Het **optellen** van twee veeltermen doe je zo:

1. Laat de **haakjes weg**.
2. Je krijgt nu één lange veelterm. **Vereenvoudig en herleid** die veelterm.

Twee veeltermen die bij elkaar moeten opgeteld worden, dat ziet er bijvoorbeeld
zo uit:

$(2a^2b - 4ab^3) + (2ab^3 - 3a^2b)$

We gaan ervan uit dat de variabelen {{< mute "($a$ en $b$)" >}} reële getallen
zijn {{< mute "(of rationale getallen, maakt niet uit)" >}}. We mogen dus de
rekenregels voor reële getallen toepassen. Die zeggen dat de **optelling in
$\mathbb{R}$ associatief is**. Dat betekent dat het niet uitmaakt of we al dan
niet haakjes zetten in een optelling en dat het niet uitmaakt waar we dan wel
die haakjes zouden zetten. We kunnen alle **haakjes dus gewoon weglaten**:

\begin{split}
    \orange{(}2a^2b - 4ab^3\orange{)} + \orange{(}2ab^3 - 3a^2b\orange{)} &=
    2a^2b - 4ab^3 + 2ab^3 - 3a^2b
\end{split}

Nu krijgen we een veelterm die we eenvoudig kunnen **herleiden** door de
gelijksoortige eentermen bij elkaar op te tellen:

\begin{split}
    \orange{2a^2b} \green{- 4ab^3} \green{+ 2ab^3} \orange{- 3a^2b} &= \orange{(2 - 3)\cdot a^2b} + \green{(-4 + 2)\cdot ab^3}\\\\\
    &= \orange{-a^2b} - \green{2\cdot ab^3}\\\\\
\end{split}

> Als je niet meer goed weet wat het juist betekent om een veelterm te
> *"herleiden"*, lees dan zeker onze les over het [vereenvoudigen en herleiden
> van een veelterm](../vereenvoudigen) eens na.

Het **aftrekken** van twee veeltermen gaat zo:

1. Laat de **haakjes weg** en **verander de toestandstekens**
   {{< mute "($+$ en $-$)" >}} van de termen van de veelterm die **na het
   minteken** stond.
2. Je krijgt nu één lange veelterm. **Vereenvoudig en herleid** die veelterm.

Bij het **aftrekken van veeltermen** gaan we ook de haakjes weglaten, maar dan
moeten we **opletten dat we het minteken correct binnen de haakjes brengen**.
Stel dat we de volgende berekening voorgeschoteld krijgen:

$(-2x^3 + 3y - 5x^2y + 6) - (2x^2y + 3 - 5y - 6x^3)$

Bij het weglaten van de haakjes, vermenigvuldigen we eigenlijk elke term in de
tweede veelterm met het minteken. Net zoals $-(-3) = +3$. Dat betekent dat
**alle tekens van die veelterm moeten veranderen**:

\begin{split}
    (-2x^3 - 5x^2y + 6) - (\orange{2x^2y + 3 - 6x^3}) &=
    -2x^3 - 5x^2y + 6 \orange{- 2x^2y - 3 + 6x^3}
\end{split}

Vervolgens is het weer een kwestie van de veelterm te **herleiden**, net als
bij het optellen van veeltermen:

\begin{split}
    \orange{-2x^3} \green{- 5x^2y} \blue{+ 6} \green{- 2x^2y} \blue{- 3} \orange{+ 6x^3}
    &= \orange{(-2 + 6)\cdot x^3} + \green{(- 5 - 2)\cdot x^2y} + \blue{(6 - 3)}\\\\\
    &= \orange{4\cdot x^3} -\green{7\cdot x^2y} + \blue{3}\\\\\
\end{split}

## Een eenterm vermenigvuldigen met een veelterm

Het vermenigvuldigen van een eenterm met een veelterm gaat als volgt:

1. **Vermenigvuldig de coëfficiënt** van elke term in de veelterm met de
   coëfficiënt van de eenterm
2. **Vermenigvuldig het lettergedeelte** van elke term in de veelterm met elke
   factor in het lettergedeelte van de eenterm

> Ben je even vergeten wat nu wee de *"coëfficiënt"* en het *"lettergedeelte"*
> was van een eenterm? Lees dan zeker onze [les over
> eentermen](../../eentermen/eenterm) even na.

Stel bijvoorbeeld dat we de volgende berekening moeten maken:

$$-2x y^2\cdot (3x^2 + 4y^3 -6)$$

We zien dat de eenterm $-2xy^2$ wordt vermenigvuldigd met een veelterm. Eerst
gaan we de $-2$ van de eenterm vermenigvuldigen met alle **coëfficiënten** van
de veelterm ($3$, $4$ en $-6$). We passen dus eigenlijk gewoon de
**distributieve eigenschap** toe:

$$\orange{-2}x y^2\cdot (\orange{3}x^2 \orange{+ 4}y^3 \orange{-6}) = x y^2\cdot (\orange{-6}x^2 \orange{- 8}y^3 \orange{+ 12})$$

Nu staan er enkel nog variabelen buiten de haakjes. We zullen eerste de $x$
naar binnen brengen door weer gebruik te maken van de distributieve eigenschap:

$$\orange{x} y^2\cdot (-6x^2 - 8y^3 + 12) = y^2\cdot (-6\orange{x^3} - 8\orange{x} y^3 + 12 \orange{x})$$

> Merk op dat de $-6x^2$ na de vermenigvuldiging met $x$ veranderd is naar
> $-6x^\orange{3}$. We passen de rekenregel toe van het **vermenigvuldigen van
> machten met hetzelfde grondtal**. Zowel $x$ als $x^2$ hebben namelijk een
> grondtal $x$. Daarom moeten we bij de vermenigvuldigingen de **exponenten bij
> elkaar optellen**: $x \cdot x^2 = x^{1 + 2} = x^3$.

Goed! Nu staat er nog enkel $y^2$ buiten de haakjes. We kunnen ook hier weer de
distributieve eigenschap gebruiken om die binnen de haakjes te krijgen:

$$\orange{y^2}\cdot (-6x^3 - 8x y^3 + 12 x) = (-6x^3\orange{y^2} - 8x \orange{y^5} + 12 x\orange{y^2})$$

> Merk weer op dat we de rekenregel van het vermenigvuldigen van machten met
> hetzelfde grondtal hebben toegepast: $y^2 \cdot y^3 = y^{2 + 3} = y^5$.

De haakjes rond onze uitkomst mogen we natuurlijk gewoon weglaten. We krijgen
de volgende veelterm:

$$-6x^3y^2 - 8x y^5 + 12 xy^2$$

## Een veelterm delen door een eenterm

Bij het **delen van een veelterm door een eenterm**, gaan we gelijkaardig te
werk als bij het *vermenigvuldigen* van een veelterm met een eenterm:

1. **Deel de coëfficiënt** van elke term in de veelterm door de
   coëfficiënt van de eenterm
2. **Deel het lettergedeelte** van elke term in de veelterm door elke
   factor in het lettergedeelte van de eenterm

Stel bijvoorbeeld dat we de volgende deling moeten maken:

$$(21u^2v^3 - 14u^2v^2 + 28uv^3):(-7uv^2)$$

Dan beginnen we eerst met het delen van **alle coëfficiënten** van de veelterm
door de $-7$:

$$(\orange{21}u^2v^3 \orange{- 14}u^2v^2 \orange{+ 28}uv^3):(\orange{-7}uv^2) = (\orange{-3}u^2v^3 \orange{+ 2}u^2v^2 \orange{- 4}uv^3):(uv^2)$$

Vervolgens gaan we de factoren van de eentermen één per één weghalen. We
beginnen met de $u$:

$$(-3u^2v^3 + 2u^2v^2 - 4uv^3):(orange{u}v^2) = (-3\orange{u}v^3 + 2\orange{u}v^2 - 4v^3):(v^2)$$

## Veeltermen met elkaar vermenigvuldigen

## Veeltermen met letterexponenten vermenigvuldigen

## Samengevat

{{< attention "Het optellen van veeltermen" >}}
Het **optellen** van twee veeltermen doe je zo:

1. Laat de **haakjes weg**.
2. Je krijgt nu één lange veelterm. **Vereenvoudig en herleid** die veelterm.
{{< /attention >}}

{{< attention "Het aftrekken van veeltermen" >}}
Het **aftrekken** van twee veeltermen gaat zo:

1. Laat de **haakjes weg** en **verander de toestandstekens**
   {{< mute "($+$ en $-$)" >}} van de termen van de veelterm die **na het
   minteken** stond.
2. Je krijgt nu één lange veelterm. **Vereenvoudig en herleid** die veelterm.
{{< /attention >}}

