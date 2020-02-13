---
title: "Eentermen vereenvoudigen"
date: 2019-12-04T08:20:36+02:00
weight: 3
draft: true
images: []
---

Een eenterm bestaat in principe enkel uit een [coëfficiënt en een
lettergedeelte](../eenterm/#coëfficiënt-en-lettergedeelte). Toch kan een
eenterm er soms wat ingewikkeld uitzien. Om een eenterm er zo minst
angstaanjagend mogelijk te laten uitzien, moeten we de eenterm
**vereenvoudigen**.

(illustratie met angstaanjagende eenterm en zijn vereenvoudigd equivalent)

Het vereenvoudigen van een eenterm gaat als volgt:

1. Werk de haakjes weg;
2. Reken de [coëfficiënt](../eenterm/#coëfficiënt-en-lettergedeelte) uit;
3. Reken het [lettergedeelte](../eenterm/#coëfficiënt-en-lettergedeelte) uit;
4. Rangschik de factoren.

## Haakjes wegwerken

Wanneer een eenterm haakjes bevat, zullen we die eerst wegwerken. Er zijn
verschillende manieren waarop haakjes kunnen voorkomen in een eenterm:

1. Haakjes die factoren tot een bepaalde macht verheffen
2. Haakjes rond factoren met een minteken

(illustratie)

In de twee gevallen werk je de haakjes anders uit.


### Haakjes met een macht uitwerken

Als er een **macht bij de haakjes** staat, **verhef je elke factor binnen de
haakjes** tot die macht.

(illustratie)

Als er binnen de haakjes een minteken staat, moet je die ook tot de macht
verheffen. Dat doe je door in gedachten het **minteken te vervangen door
$(-1)$** en die te verheffen tot de macht.

(illustratie)

{{% expand "Waarom mogen we een minteken vervangen door $(-1)$?" %}}
We mogen een minteken altijd vervangen door $(-1)$ omdat een minteken voor een
factor hetzelfde betekent als "*vermenigvuldig met $-1$*".

Bijvoorbeeld, $-1 \cdot 2 = - 2$. Dus of we nu $-2$ schrijven, of $-1 \cdot 2$
of $(-1)\cdot 2$, dat is allemaal hetzelfde. Eén pot nat. 🍯
{{% /expand %}}

### Haakjes met een minteken uitwerken

Wanneer er haakjes rond een **factor met een minteken** staan, kan je weer in
gedachte **ieder minteken vervangen door $(-1)$**. Alle $(-1)-$en kan je
vervolgens voorop zetten en met elkaar vermenigvuldigen.

(illustratie)


{{% expand "Waarom mag je alle $(-1)-$en voorop zetten?" %}}
De vermenigvuldiging van rationale getallen is **commutatief**.
{{% mute "(Hetzelfde geldt voor reële getallen.)" %}} Dat betekent dat de
volgorde waarin je een vermenigvuldiging uitrekent, niet uitmaakt:

\begin{split}
    5\cdot 2 \cdot 3 = 30\\\\\
    3 \cdot 2  \cdot 5 = 30\\\\\
    2 \cdot 5 \cdot 3 = 30\\\\\
\end{split}

Je mag in een vermenigvuldiging van rationale getallen de **factoren dus altijd
van plaats veranderen**.

We hebben daarnet al gezien dat een minteken hetzelfde is als vermenigvuldigen
met $(-1)$. Een minteken is dus hetzelfde als een **factor $(-1)$**. Hierboven
zeiden we dat we in een vermenigvuldiging de factoren altijd van plaats mogen
veranderen, dus we mogen gerust alle $(-1)-$en voorop zetten.

\begin{split}
    \orange{-}5\cdot (\orange{-}2) \cdot (\orange{-}3) &= - 30\\\\\
    \orange{-}2\cdot (\orange{-}3) \cdot (\orange{-}5) &= - 30\\\\\
    \orange{-}2\cdot (\orange{-}5) \cdot (\orange{-}3) &= - 30\\\\\
    \orange{(-1)} \cdot 2 \cdot \orange{(-1)} \cdot 5 \cdot \orange{(-1)} \cdot 3 &= - 30\\\\\
    \orange{(-1)} \cdot \orange{(-1)} \cdot \orange{(-1)} \cdot 2\cdot 5 \cdot 3 &= - 30\\\\\
\end{split}

{{% /expand %}}

## Coëfficiënt uitrekenen

Om de [coëfficiënt](../eenterm/#coëfficiënt-en-lettergedeelte), of het
*cijfergedeelte*, van een eenterm uit te rekenen, kan je in gedachte alle
[variabelen](../variabele) even weglaten. Vervolgens reken je de bewerking die
er staat gewoon uit.

(illustratie)


{{% expand "Waarom mag je de coëfficiënt apart uitrekenen?" %}}
De vermenigvuldiging van rationale getallen is **commutatief**.
{{% mute "(Dat is ook zo voor reële getallen.)" %}} Dat betekent dat de
volgorde waarin je een vermenigvuldiging uitrekent, niet uitmaakt:

\begin{split}
    4\cdot 5 \cdot 7 = 140\\\\\
    7 \cdot 4  \cdot 5 = 140\\\\\
    5 \cdot 4 \cdot 7 = 140\\\\\
\end{split}

Je mag in een vermenigvuldiging van rationale getallen de **factoren dus altijd
van plaats veranderen**. Omdat zowel de variabelen als de getallen in onze
eenterm *rationaal* zijn {{% mute "(reëel mag ook)" %}}, mogen we ze dus van
plaats veranderen.

\begin{split}
    4 \cdot a \cdot b \cdot 3 \\\\\
    = 3 \cdot  a \cdot 4 \cdot b\\\\\
    = b \cdot 3 \cdot a \cdot 4\\\\\
\end{split}

We kiezen ervoor om het volledige
[cijfergedeelte](../eenterm/#coëfficiënt-en-lettergedeelte) vooraan te zetten
en al eerste uit te rekenen.

\begin{split}
    \orange{4} \cdot a \cdot b \cdot \orange{3} \\\\\
    = \orange{4 \cdot 3} \cdot a \cdot b \\\\\
    = \orange{12} \cdot a \cdot b \\\\\
\end{split}

Dat geeft ons de {{% class "coëfficiënt" "orange" %}}.

{{% /expand %}}

## Lettergedeelte uitrekenen

Eens het cijfergedeelte van de eenterm is opgekuist, pakken we het
lettergedeelte aan. Om het lettergedeelte te vereenvoudigen, ga je op zoek naar
de factoren met **dezelfde variabele** in hun grondtal.

(illustratie die grondtal en exponent toont van verschillende factoren)

Voor elke variabele tel je de exponenten bij elkaar op. Zo krijg je de nieuwe
exponent voor die variabele.

(illustratie)


{{% expand "Waarom tellen we de exponenten bij elkaar op?" %}}
Stel dat we de volgende eenterm hebben:

$$\orange{a^4} \cdot \blue{a^2} \cdot b^3$$

Dan kunnen we die eenterm languit schrijven als

$$\orange{a \cdot a \cdot a \cdot a} \cdot \blue{a \cdot a} \cdot b \cdot b \cdot b$$

We vermenigvuldigen $a$ dus 6 keer met zichzelf en vervolgens vermenigvuldigen
we $b$ 3 keer met zichzelf. Dat is hetzelfde als

$$a^6\cdot b^3$$

Vanwaar komt die $6$ van $a^6$ nu? Wel de $\orange{a^4}$ gaf ons 4 $a$'s en de
$\blue{a^2}$ gaf er ons nog eens 2. In totaal kregen we dus $\orange{4} +
\blue{2} = 6$ $a$'s. We kunnen bijgevolg zeggen dat:

$$\orange{a^4} \cdot \blue{a^2} \cdot b^3 = a^{\orange{4} + \blue{2}}\cdot b^3$$

In het algemeen is de regel dat je in een vermenigvuldiging **exponenten bij
elkaar mag optellen** wanneer ze **hetzelfde grondtal hebben**:

$$\orange{a^n} \cdot \blue{a^m} = a^{\orange{n} + \blue{m}}$$

Waarbij $a, \orange{n}, \blue{m} \in \mathbb{Q}$. {{% mute "(of $\mathbb{R}$ mag ook)" %}}
{{% /expand %}}

## Factoren rangschikken
Vanaf we de coëfficiënt en het lettergedeelte hebben vereenvoudigd, zijn alle
factoren van onze eenterm vereenvoudigd. Vaak gaan we echter nog als laatste
stap de **factoren van de eenterm rangschikken**. De meest gebruikelijke manier
van rangschikken is:

1. Zet de coëfficiënt en het toestandsteken voorop;
2. Rangschik de variabelen alfabetisch.

Enkele voorbeelden:

(illustratie)

## Samengevat

{{% attention "Eentermen vereenvoudigen" %}}
Het vereenvoudigen van eentermen doe je als volgt:

1. Werk de **haakjes weg** door machten en mintekens uit te werken;
2. Vermenigvuldig alle **factoren in het cijfergedeelte** met elkaar;
3. Combineer de **factoren in het lettergedeelte** per soort en reken hun nieuwe macht uit;
4. Zet het **toestandsteken en de coëfficiënt voorop** en rangschik de **variabelen alfabetisch**.
{{% /attention %}}
