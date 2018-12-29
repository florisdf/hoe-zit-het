---
title: "Grafieken van functies"
date: 2018-10-01T22:13:11+02:00
weight: 4
draft: true
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
$\orange{-2}$          |    $\green{-21}$
$\orange{-1}$          |    $\green{-10}$
$\orange{0}$           |    $\green{-5}$
$\orange{\frac{1}{3}}$ |    $\green{\frac{-14}{3}}$
$\orange{\frac{2}{3}}$ |    $\green{-5}$
$\orange{1}$           |    $\green{-6}$
$\orange{2}$           |    $\green{-13}$

## $x$ en $y$ als coördinaten
We kunnen de waarden voor $\orange{x}$ en $\green{y}$ in de bovenstaande tabel
zien als coördinaten van punten op een
[assenstelsel](../../algemeen/assenstelsel). In de eerste rij van de
waardentabel is $\orange{x = -2}$ en $\green{y = -21}$. We kunnen dit
voorstellen door een puntje met coördinaten $(\orange{-2}, \green{-21})$.

{{% html "plt/single_x.html" %}}

Zo kunnen we alle rijen in onze waardentabel voorstellen als puntjes in een
assenstelsel.

## Veel puntjes vormen een curve
We laten ons even gaan en we zoeken $f(\orange{x})$ voor waanzinnig veel
waarden van $\orange{x}$. Bijvoorbeeld voor alle waarden tussen $\orange{-2}$
en $\orange{2}$ in stapjes van $0.01$ (dus $\orange{-2}$, $\orange{-1.99}$,
$\orange{-1.98}$, $\orange{-1.97}$ enzovoort tot $\orange{2}$). Wat gebeurt
er als we die enorme hoeveelheid puntjes nu op een assenstelsel zetten? We
krijgen deze mooie figuur:

We hebben nu zoveel puntjes op ons assenstelsel dat we eigenlijk niet meer zien
dat het *aparte* puntjes zijn. We zien één **curve**. Deze curve noemen we de
**grafiek van de functie**.

## Hoogstens één $y$ voor elke $x$
We weten dat er bij een functie voor een bepaalde waarde van $x$ [hoogstens
één](../intro#samengevat) waarde van $y$ bestaat. Grafisch betekent dit dat er op
de curve van een functie **nooit twee punten boven elkaar liggen**. Vergelijk
hieronder de grafieken van "wel functie" en "geen functie".
