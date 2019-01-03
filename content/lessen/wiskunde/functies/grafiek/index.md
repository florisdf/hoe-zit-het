---
title: "Grafieken van functies"
date: 2018-10-01T22:13:11+02:00
weight: 4
draft: false
tags: ["Functies", "grafieken", "plot", "Analyse"]
categories: ["wiskunde", "analyse", "3e middelbaar"]
level: 3M
course: wiskunde
topic: analyse
---
Een functie kunnen we [voorstellen als een machientje](../intro) waar we een
waarde voor $x$ in stoppen en waar [hoogstens één](../intro#samengevat) waarde
voor $y$ uit komt.

{{% img "img/conveyor_plain.svg" "" %}}

Als we [het functievoorschrift](../voorschrift) van de functie hebben, kunnen
we voor verschillende waarden van $\orange{x}$ de bijhorende waarde van
$\green{y} = f(\orange{x})$ zoeken. Die resultaten kunnen we proper noteren in een
[waardentabel](../waardentabel).

{{% img "img/conveyor_functiewaarde.svg" "" %}}

Ingang $\orange{x}$    | Uitgang $\green{y} = f(\orange{x})$
-----------------------|------------
$\orange{-1}$          |    $\green{-10.5}$
$\orange{0}$           |    $\green{-6}$
$\orange{1}$           |    $\green{-2.5}$
$\orange{2}$           |    $\green{0}$
$\orange{3}$           |    $\green{1.5}$
$\orange{4}$           |    $\green{2}$
$\orange{5}$           |    $\green{1.5}$

## $x$ en $y$ als coördinaten
We kunnen de waarden voor $\orange{x}$ en $\green{y}$ in de bovenstaande tabel
zien als coördinaten van punten op een
[assenstelsel](../../algemeen/assenstelsel). Bijvoorbeeld in de laatste rij van
de waardentabel is $\orange{x = 5}$ en $\green{y = 1.5}$. We kunnen dit
voorstellen door een puntje met coördinaten $(\orange{5}, \green{1.5})$.
{{% mute "(Als je met je muis over het puntje in de grafiek beweegt - of erop tikt met je vinger - zie je de coördinaten ervan)" %}}

{{% bokeh "plt/single_x.json" %}}

Zo kunnen we alle rijen in onze waardentabel voorstellen als puntjes in een
assenstelsel.

{{% bokeh "plt/multiple_x.json" %}}

## Veel puntjes vormen een curve
We laten ons even gaan en we zoeken $f(\orange{x})$ voor waanzinnig veel
waarden van $\orange{x}$. Bijvoorbeeld voor alle waarden tussen $\orange{-1}$
en $\orange{9}$ in stapjes van $0.01$ (dus $\orange{-1}$, $\orange{-0.99}$,
$\orange{-0.98}$, $\orange{-0.97}$ enzovoort tot $\orange{9}$). Wat gebeurt
er als we die enorme hoeveelheid puntjes nu op een assenstelsel zetten? We
krijgen deze mooie figuur:

{{% bokeh "plt/loads_of_x.json" %}}

We hebben nu zoveel puntjes op ons assenstelsel dat we eigenlijk niet meer zien
dat het *aparte* puntjes zijn. Het zijn wel degelijk aparte puntjes
{{% mute "(beweeg maar eens over de grafiek)" %}},
maar we zien het als **één doorlopende curve**.
Deze curve noemen we de **grafiek van de functie**.

## Hoogstens één $y$ voor elke $x$
We weten dat er bij een functie voor een bepaalde waarde van $x$ [hoogstens
één](../intro#samengevat) waarde van $y$ bestaat. Grafisch betekent dit dat er op
de curve van een functie **nooit twee punten boven elkaar liggen**. De curve
hieronder is een voorbeeld van een curve waar er voor bepaalde waarden van $x$
**meerdere** waarden van $y$ bestaan. Met andere woorden is hier $y$ **geen
functie van** $x$. Moest het {{% class "oranje" "b orange" %}} stukje er niet
geweest zijn, was $y$ *wel* een functie van $x$.

{{% bokeh "plt/no_fx.json" %}}
