---
title: "Machten van 10"
date: 2019-01-28T08:06:49+01:00
weight: 2
draft: true
tags: []
categories: []
level: ""
course: ""
topic: ""
---

Het wordt snel lastig om heel grote of heel kleine getallen te lezen of te schrijven. De afstand tussen de aarde en de zon, bijvoorbeeld, is ongeveer $150\ 000\ 000\ 000 \si{ m}$.
De tijd die het licht nodig
heeft om $1 \si{ m}$ ver te reizen, bedraagt dan weer $0{,}00000000334 \si{ s}$.

**Machten van 10** zorgen ervoor dat we zulke getallen korter kunnen voorstellen. Door die macht van 10 kunnen we namelijk de **komma van een getal eender waar zetten**. Zo kunnen we kiezen om de komma van $0{,}00000000334$ na de eerste 3 te zetten door nadien terug te vermenigvuldigen met $\orange{10^{-9}}$:
$$0{,}00000000334 = 3{,}34\cdot \orange{10^{-9}}$$
Of je kan met een andere macht van 10 ook kiezen om de komma na de tweede 3 te zetten: 
$$0{,}00000000334 = 33{,}4\cdot \orange{10^{-10}}$$
Of na de 4:
$$0{,}00000000334 = 334\cdot \orange{10^{-11}}$$
Merk op hoe de macht van 10 telkens verandert voor een andere keuze van waar we de komma willen zetten.

Hetzelfde kunnen we doen om $150\ 000\ 000\ 000$ korter te schrijven. Bijvoorbeeld de komma na de 1:
$$150\ 000\ 000\ 000 = 1{,}500 \cdot 10^{11}$$
Of na de 5:
$$150\ 000\ 000\ 000 = 15{,}00 \cdot 10^{10}$$
Of na de eerste 0:
$$150\ 000\ 000\ 000 = 150{,}0 \cdot 10^{9}$$

{{% expand "Uitbreiding: beduidende cijfers" %}}
$150\ 000\ 000\ 000$ heeft 12
[beduidende cijfers](../beduidende_cijfers/index.md), terwijl $1{,}500 \cdot 10^{11}$ en $15{,}00 \cdot 10^{10}$ en $150{,}0 \cdot 10^{9}$ elk 4 beduidende cijfers hebben. Het eindresultaat heeft dus minder beduidende cijfers. Normaal gesproken laten we beduidende cijfers niet zomaar wegvallen. Hier deed ik het omdat $1{,}50000000000\cdot 10^{11}$ nogal lang is om te schrijven.

In de meeste oefeningen zullen we nooit meer dan 4 beduidende cijfers hebben. Als we dan een getal hebben dat uit meer dan 4 cijfers bestaat, is een macht van 10 de *enige* manier om dat getal te kunnen schrijven met het juiste aantal beduidende cijfers.
{{% /expand %}}

## Machten van 10 uitrekenen
Hoe komen we bij het voorbeeld van $0{,}00000000334 = 3{,}34\cdot \orange{10^{-9}}$ aan die $\orange{10^{-9}}$? 
Voor we tonen waar die vandaan komt, bespreken we eerst hoe we een macht van 10 terug uitrekenen. Enkele voorbeelden:
$$2{,}621\cdot \orange{10^2} = 2{,}621 \cdot \orange{100} = 262{,}1$$
$$75{,}0411\cdot \orange{10^3} = 75{,}0411 \cdot \orange{1000} = 75\ 041{,}1$$
$$6{,}3\cdot \orange{10^{-3}} = 6{,}3 \cdot \orange{0{,}001} = 0{,}0063$$
$$405{,}9\cdot \orange{10^{-2}} = 405{,}9 \cdot \orange{0{,}01} = 4{,}059$$
$$51\cdot \orange{10^{3}} = 51 \cdot \orange{1000} = 51\ 000$$

Je ziet dat vermenigvuldigen met een macht van 10
ervoor zorgt dat de **komma verschuift**.
De komma verschuift **naar links bij negatieve machten** en ze verschuift **naar rechts bij positieve machten**.

Vermenigvuldigingen met $10^{\orange{2}}$, bijvoorbeeld, verschuift de komma {{% class "2 plaatsen naar rechts" "orange" %}}.
Vermenigvuldigingen met $10^{\orange{-3}}$, verschuift de komma {{% class "3 plaatsen naar links" "orange" %}}.

## Getallen omzetten naar een macht van 10
Nu zullen we zien hoe we met een macht van 10 de komma van een getal op eender welke plek kunnen zetten. We willen bijvoorbeeld de komma van $1{,}530$ na de 3 krijgen. Dat betekent dat we de komma **2 plaatsen naar rechts** moeten schuiven. Dat kunnen we doen door te vermenigvuldigen met $\orange{10^2}$:
$$1{,}530 \cdot \orange{10^2} = 153{,}0$$

Maar pas op! Nu hebben we gevonden waar $1{,}530 \cdot 10^2$ aan gelijk is, en nog niet waar $1{,}530$ *zelf* aan gelijk is. We willen zowel de **komma verschuiven** als de **gelijkheid behouden** met $1{,}530$.

Om die gelijkheid te kunnen behouden, is het belangrijk in te zien dat $\orange{10^2} \cdot \blue{10^{-2}} = 1$ en dat we dus perfect mogen zeggen dat
\begin{split}
1{,}530 &= 1{,}530 \cdot 1\\\\\
&= 1{,}530 \cdot \orange{10^2} \cdot \blue{10^{-2}}
\end{split}

En zo kunnen we zowel de **{{% class "komma verschuiven" "orange" %}}** als de **{{% class "gelijkheid behouden" "blue" %}}**. Samengevat is onze tactiek als volgt:

1. Tel hoeveel plaatsen we de komma willen opschuiven, hier **2 plaatsen naar rechts**;
1. Vermenigvuldig met $\orange{10^2}$ om de **komma te verschuiven** naar de plek die we wouden;
2. Vermenigvuldig met $\blue{10^{-2}}$ om de vorige macht te compenseren en om 
   zo de **gelijkheid te behouden**.

Concreet gaat dat dan als volgt:
\begin{split}
1{,}530 &= 1{,}530 \cdot 1 \\\\\
&= 1{,}530 \cdot \orange{10^2} \cdot \blue{10^{-2}}\\\\\
&= \orange{1{,}530 \cdot 10^{2}} \cdot \blue{10^{-2}}\\\\\
&= \orange{153{,}0} \cdot \blue{10^{-2}}\\\\\
&= 153{,}0 \cdot 10^{-2}
\end{split}


## Machten van 10 omzetten naar andere machten van 10
Soms zullen we ook machten van 10 moeten omzetten naar andere machten van 10. We willen bijvoorbeeld $4{,}0881 \cdot 10^{5}$ omzetten naar $\ldots\text{iets}\ldots\orange{\cdot 10^{3}}$.

\begin{split}
4{,}0881 \cdot 10^{5} &= 4{,}0881 \cdot 10^{5} \cdot 1\\\\\
&= 4{,}0881 \cdot 10^{5} \cdot \orange{10^{3}} \cdot \blue{10^{-3}}\\\\\
&= 4{,}0881 \cdot 10^{5} \cdot \blue{10^{-3}} \cdot \orange{10^{3}}\\\\\
&= 4{,}0881 \blue{\cdot 10^{5} \cdot 10^{-3}} \cdot \orange{10^{3}}\\\\\
&= 4{,}0881 \blue{\cdot 10^{2}} \cdot \orange{10^{3}}\\\\\
&= \blue{4{,}0881 \cdot 10^{2}} \cdot \orange{10^{3}}\\\\\
&= \blue{408{,}81}\cdot \orange{10^{3}}\\\\\
&= 408{,}81\cdot 10^{3}\\\\\
\end{split}
