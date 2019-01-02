---
title: "Domein en beeld"
date: 2018-07-01T22:13:11+02:00
draft: true
weight: 5
tags: ["Functies", "Analyse"]
categories: ["wiskunde", "analyse", "3e middelbaar"]
---
Een functie kunnen we [voorstellen als een machientje](../intro) waar we een
waarde voor $x$ in stoppen en waar [hoogstens één](../intro#samengevat) waarde
voor $y$ uit komt.

{{% img "img/conveyor_plain.svg" "" %}}

Voor een bepaalde $x-$waarde kan er dus **één of géén** $y-$waarde uit de
functie komen.

## Domein van een functie
Het domein van een functie is de [verzameling](../../algemeen/verzamelingen)
van $x-$waarden waarvoor er een $y-$waarde uit de functie komt.

* Voor de $x-$waarden die **niet in het domein** zitten, bestaat er dus **géén
$y-$waarde**.
* Voor de $x-$waarden die **wel in het domein** zitten, bestaat er **één
$y-$waarde**.

Een typisch voorbeeld is de [reële functie](../reele_functies) die als
[functievoorschrift](../voorschrift) heeft

$$f(x) = \sqrt{x}$$

Omdat de [wortel van een negatief
getal](../../algemeen/vierkantswortel#vierkantswortel-van-een-negatief-getal)
geen [reëel getal](../../algemeen/reele_getallen) is, bestaat er enkel een
reële $y-$waarde voor $x-$waarden die groter of gelijk zijn aan $0$. Het domein
van deze functie $f$ is dus alle positieve reële getallen. We schrijven:
$$dom f = \mathbb{R}^+$$

## Beeld van een functie
Stel dat we nu een oranje machientje hebben waar $y=x^2$ uit komt.

{{% img "img/conveyor_voorschrift_3.svg" "" %}}

Wat is hiervan het domein? Je kan ieder getal kwadrateren, dus we mogen eender welke $x$ kiezen.
Het domein bevat dus alle getallen, net zoals bij het blauwe machientje.

{{% img "img/conveyor_in_domain_oranje_1.svg" "" %}}
{{% img "img/conveyor_in_domain_oranje_2.svg" "" %}}

Stel dat we nu **alle** getallen van het oranje domein eens in het oranje machientje stoppen. Dus niet alleen $-1$ en $2$
maar ook $-128$ en $0,5$ en $324758,948...$ enzovoort; echt **alle** getallen die je maar kan
bedenken want het oranje domein bevat nu eenmaal **alle** getallen.

{{% img "img/range_oranje.svg" "" %}}

De $y-$waarden die telkens uit het oranje machientje komen, verzamelen we in een aparte doos.
Eens we alle $x-$waarden van het oranje domein in het machientje hebben gestopt,
hebben we aan de uitgang een hele hoop $y-$waarden verzameld. Die verzameling
van $y-$waarden noemen we **het beeld** van de oranje functie.

Het beeld bevat dus de $y-$waarden die uit de functie komen wanneer je alle $x-$waarden van het domein één voor één in de functie stopt.
Nu is de vraag natuurlijk: welke getallen zitten er allemaal in het oranje beeld?
Wel als we $2$ in het oranje machientje stoppen, komt er $4$ uit. Als we
$-2$ in het oranje machientje stoppen, komt er *ook* $4$ uit.

{{% img "img/conveyor_in_domain_oranje_3.svg" "" %}}
{{% img "img/conveyor_in_domain_oranje_4.svg" "" %}}

En als $x=1$ dan is $y=1$ en als $x=-1$ dan is weer $y=1$. Het lijkt alsof er uit het oranje machientje
enkel positieve getallen kunnen komen! Zo is het ook. Welk getal je ook in het
oranje machientje stopt, er komt **altijd een positief getal uit**. Het beeld
van de oranje functie bevat dus alle *positieve* getallen.

Je kan dezelfde oefening eens proberen maken voor het blauwe en het groene
machientje. Probeer zelf na te gaan waarom het blauwe beeld alle getallen

## Domein en beeld op een grafiek

## Samengevat
{{% attention "Definitie domein" %}}
Het **domein van een functie** is de verzameling van alle mogelijke $x-$waarden
waarvoor er een $y-$waarde bestaat.
{{% /attention %}}

{{% attention "Definitie beeld" %}}
Het **beeld van een functie** is de verzameling van alle $y-$waarden die uit de
functie kunnen komen.
{{% /attention %}}

