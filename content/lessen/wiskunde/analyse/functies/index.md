---
title: "Functies - een intro"
date: 2018-07-01T22:13:11+02:00
draft: false
tags: ["Functies", "Analyse"]
categories: ["wiskunde", "analyse", "3e middelbaar"]
---
Genoeg gerekend. Tijd voor echte wiskunde. Je had het misschien niet gedacht,
maar rekenen is bijzaak in wiskunde. Hier leggen we de basis uit van
*functies*.

## Een functie is een machientje
Je kan een functie zien als een *machientje* waar je een getal $x$ instopt en een getal $y$ uitkomt. Jij kiest de $x$. Het machientje bepaalt de $y$ afhankelijk van de $x$ die jij koos.

{{< img "img/conveyor_plain.svg" "" >}}

Bijvoorbeeld: ons machientje telt altijd twee op bij wat je erin stopt. Je kan
zeggen dat de $y$ die uit het machientje komt gelijkt is aan $x+2$:

$$y = x + 2$$

Als we het getal $1$ in het machientje stoppen ($x$), geeft die het getal $3$ terug ($y$). En als $x = -1$, is $y = 1$; als $x = 8$, is $y = 10$ enzovoort.

{{< img "img/conveyor_voorschrift.svg" "" >}}

## Domein van een functie
$y = x + 2$ is een heel eenvoudige functie. Je kan ook ingewikkeldere functies
bedenken. Bijvoorbeeld: $y = \sqrt{x}$. Dit is meteen een speciaal geval, want
in die functie past niet zomaar eender welke $x$-waarde. Je kan enkel positieve
getallen als $x$-waarde gebruiken, omdat je van een negatief getal de
vierkantswortel niet kan berekenen[^1]. We zeggen dat **het domein van de
functie** alle positieve reële getallen bevat. Of in symbolen:

$$dom~f = \mathbb{R}^+$$

Het domein van een functie is dus de verzameling van alle mogelijke $x$-waarden (ingangen) waarvoor de functie een $y$-waarde kan berekenen. Voor de $x$-waarden die niet in het domein zitten, bestaat er géén $y$-waarde.

{{< img "img/conveyor_not_in_domain.svg" "" >}}

## Beeld van een functie
Stel dat we de functie $y=x^2$ hebben. Je kan elk reëel getal kwadrateren, dus iedere $x \in \mathbb{R}$ kan in de functie worden gestopt. Het domein is dus $dom~f = \mathbb{R}$. Stel dat we nu alle $x$-waarden verzamelen die in het domein zitten (dus alle reële getallen). Die stoppen we één voor één in onze functie. De $y$-waarden die uit de functie komen, verzamelen we in een aparte doos. Eens we alle $x$-waarden van het domein in de functie hebben gestopt, hebben we aan de uitgang een hele hoop $y$-waarden verzameld. Het kwadraat van een (reëel) getal is altijd positief: bv. $(-2)^2=4$ en $3^2=9$. De $y$-waarden aan de uitgang van de functie $y = x^2$, zullen dus ook altijd positief zijn. We zeggen dat **het beeld van de functie** alle positieve reële getallen bevat. Of in symbolen:

$$bld~f = \mathbb{R}^+$$

Het beeld van een functie is dus de verzameling van alle mogelijke $y$-waarden (uitgangen) die uit de functie kunnen komen. Ze zijn de $y$-waarden die uit de functie komen wanneer je alle $x$-waarden van het domein één voor één in de functie stopt.

{{< img "img/conveyor_domain_image.svg" "" >}}

## Nulpunten van een functie
Je kan je inbeelden dat er soms $x$-waarden zullen zijn waarvoor de $y$-waarden
$0$ zijn. Deze $x$-waarden noemen we **nulpunten**. De functie $y = x + 2$
heeft als nulpunt $x = -2$. De functie $y = \sqrt{x}$ heeft als nulpunt $x = 0$
en de functie $y = x^2 - 9$ heeft de nulpunten $x = -3$ en $x = 3$.

{{< img "img/conveyor_zero.svg" "" >}}

## Oké... En waarom hebben we dat nodig?
TODO

[^1]: Eigenlijk kan dit wel, maar de uitkomst is geen reëel getal.
