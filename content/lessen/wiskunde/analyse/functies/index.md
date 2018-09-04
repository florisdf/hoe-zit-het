---
title: "Functies - een intro"
date: 2018-07-01T22:13:11+02:00
draft: false
tags: ["Functies", "Analyse"]
categories: ["wiskunde", "analyse", "3e middelbaar"]
---
## Een functie is een machientje
Je kan een functie zien als een *machientje* waar je een getal $x$ instopt en een getal $y$ uitkomt. Jij kiest de $x$. Het machientje bepaalt de $y$ afhankelijk van jouw $x$.

{{< img "img/conveyor_plain.svg" "" >}}

Bijvoorbeeld: we hebben een blauw machientje dat altijd twee optelt bij jouw $x$. Je kan
zeggen dat de $y$ die uit het machientje komt gelijkt is aan $x+2$:

$$y = x + 2$$

Als we het getal $1$ in het machientje stoppen ($x$), geeft die het getal $3$ terug ($y$), want $1 + 2 = 3$. En als $x = -1$, is $y = 1$; als $x = 8$, is $y = 10$ enzovoort.

{{< img "img/conveyor_voorschrift_1.svg" "" >}}

## Domein van een functie
Het blauwe machientje stelt maar een heel eenvoudige functie voor. Stel dat we een ingewikkelder,
groen machientje hebben. Uit het groene machientje komt een $y$ die gelijk is aan de *vierkantswortel* van onze $x$.
Dat betekent dus dat als we een $x$ in ons machientje stoppen, $\sqrt{x}$ uit
het machientje zal komen.

{{< img "img/conveyor_voorschrift_2.svg" "" >}}

Belangrijke vraag: **Kunnen we eender welke $x$ in de machientjes stoppen?**

In het blauwe machientje kunnen we alle getallen stoppen want het blauwe
machientje maakte van onze $x$ simpelweg $x + 2$ en gewoon $2$ ergens bij
optellen, lukt met ieder getal.
Bijvoorbeeld:

{{< img "img/conveyor_in_domain_3.svg" "" >}}
{{< img "img/conveyor_in_domain_4.svg" "" >}}

In het groene machientje kunnen we echter **niet ieder getal**
stoppen. Welke getallen dan niet? Bijvoorbeeld $x = -1$ gaat niet omdat $\sqrt{-1}$ niet bestaat.
Dat is omdat je geen vierkantswortel
van negatieve getallen kan berekenen. In het **groene machientje** mogen we dus
alle getallen stoppen die **niet negatief** zijn, of dus alle **positieve
getallen**. Even illustreren:

{{< img "img/conveyor_in_domain_1.svg" "" >}}
{{< img "img/conveyor_in_domain_2.svg" "" >}}
{{< img "img/conveyor_not_in_domain.svg" "" >}}

*Het domein van een functie is de verzameling van alle mogelijke $x$-waarden (ingangen) waarvoor de functie een $y$-waarde kan berekenen.
Voor de $x$-waarden die niet in het domein zitten, bestaat er géén $y$-waarde.*

We zeggen dat **het domein** van het *blauwe* machientje alle getallen bevat,
terwijl het domein van het *groene* machientje enkel alle *positieve* getallen
bevat.

## Beeld van een functie
Stel dat we nu een oranje machientje hebben waar $y=x^2$ uit komt.

{{< img "img/conveyor_voorschrift_3.svg" "" >}}

Wat is hiervan het domein? Je kan ieder getal kwadrateren, dus we mogen eender welke $x$ kiezen.
Het domein bevat dus alle getallen, net zoals bij het blauwe machientje.

{{< img "img/conveyor_in_domain_oranje_1.svg" "" >}}
{{< img "img/conveyor_in_domain_oranje_2.svg" "" >}}

Stel dat we nu **alle** getallen van het oranje domein eens in het oranje machientje stoppen. Dus niet alleen $-1$ en $2$
maar ook $-128$ en $0,5$ en $324758,948...$ enzovoort; echt **alle** getallen die je maar kan
bedenken want het oranje domein bevat nu eenmaal **alle** getallen.

{{< img "img/range_oranje.svg" "" >}}

De $y$-waarden die telkens uit het oranje machientje komen, verzamelen we in een aparte doos.
Eens we alle $x$-waarden van het oranje domein in het machientje hebben gestopt,
hebben we aan de uitgang een hele hoop $y$-waarden verzameld. Die verzameling
van $y$-waarden noemen we **het beeld** van de oranje functie.

*Het beeld van een functie is de verzameling van alle mogelijke $y$-waarden (uitgangen) die uit de functie kunnen komen. Ze zijn de $y$-waarden die uit de functie komen wanneer je alle $x$-waarden van het domein één voor één in de functie stopt.*

Nu is de vraag natuurlijk: welke getallen zitten er allemaal in het oranje beeld?
Wel als we $2$ in het oranje machientje stoppen, komt er $4$ uit. Als we
$-2$ in het oranje machientje stoppen, komt er *ook* $4$ uit.

{{< img "img/conveyor_in_domain_oranje_3.svg" "" >}}
{{< img "img/conveyor_in_domain_oranje_4.svg" "" >}}

En als $x=1$ dan is $y=1$ en als $x=-1$ dan is weer $y=1$. Het lijkt alsof er uit het oranje machientje
enkel positieve getallen kunnen komen! Zo is het ook. Welk getal je ook in het
oranje machientje stopt, er komt **altijd een positief getal uit**. Het beeld
van de oranje functie bevat dus alle *positieve* getallen.

## Nulpunten van een functie
Je kan je inbeelden dat er soms $x$-waarden zullen zijn waarvoor de $y$-waarden
$0$ zijn. Deze $x$-waarden noemen we **nulpunten**. De functie $y = x + 2$
heeft als nulpunt $x = -2$. De functie $y = \sqrt{x}$ heeft als nulpunt $x = 0$
en de functie $y = x^2 - 9$ heeft de nulpunten $x = -3$ en $x = 3$.

{{< img "img/conveyor_zero.svg" "" >}}

[^1]: Eigenlijk kan dit wel, maar de uitkomst is geen reëel getal.
