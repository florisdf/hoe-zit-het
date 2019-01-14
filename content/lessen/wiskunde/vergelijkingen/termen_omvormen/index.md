---
title: "Optellingen en aftrekkingen omvormen"
date: 2019-01-13T13:33:15+01:00
weight: 3
draft: false
tags: ["vergelijkingen", "algebra"]
categories: ["wiskunde", "algebra"]
level: "2M"
course: "wiskunde"
topic: "algebra"
---
Een [vergelijking](../intro) oplossen betekent dat we de waarden van de onbekende(n) vinden waarvoor de gelijkheid klopt. Vaak is er maar één onbekende, namelijk $x$.

Door een vergelijking [om te vormen](../omvormen) naar de vorm 
$x = \text{(een getal)}$
kunnen we de vergelijking oplossen. In deze les zien we hoe we een vergelijking van de vorm $x + a = b$ en $x - a = b$ (waarbij $a$ en $b$ [reële getallen](../../verzamelingen/reele_getallen) zijn)" kunnen omvormen naar $x = \text{(een getal)}$.

## Omvormen van $x + a = b$
Om een vergelijking van de vorm $x + a = b$ {{% mute "(met $a, b \in \mathbb{R}$)" %}} om te vormen naar $x = \text{(een getal)}$, moeten we enkel de $+ a$ weg krijgen uit het linkerlid. We willen dat er links $x + 0$ staat in plaats van $x + a$. We kunnen van de $a$ een $0$ maken door van het linker- en rechterlid $a$ af te trekken:
$$x + a = b$$
$$\Leftrightarrow x + a \orange{- a} = b \orange{- a}$$
$$\Leftrightarrow x + \orange{0} = b \orange{- a}$$
$$\Leftrightarrow x = b - a$$

## Een voorbeeld
Nu eens zonder al die letters. We zullen het eens toepassen op de vergelijking
$$x + 3 = -8$$
De $a$ is hier $3$ en de $b$ is hier $-8$. Om die vergelijking om te zetten naar de vorm $x = \text{(een getal)}$, moeten we van het linker- en rechterlid $3$ aftrekken:
$$x + 3 = -8$$
$$\Leftrightarrow x + 3 \orange{-3} = -8 \orange{-3}$$
$$\Leftrightarrow x + \orange{0} = \orange{-11}$$
$$\Leftrightarrow x = -11$$

Ziezo! We hebben $x$ gevonden!:champagne::clap: 

## En wat met $x - a = b$?
We hebben weer hetzelfde doel: de vegelijking omvormen naar $x = \text{(een getal)}$. We willen dus dat er in het linkerlid $0$ staat in plaats van $a$. Die $0$ kunnen we daar krijgen door bij de linker- en rechterkant **$a$ op te tellen**.
$$x - a = b$$
$$\Leftrightarrow x - a \orange{+a} = b \orange{+a}$$
$$\Leftrightarrow x \orange{+0} = b \orange{+a}$$
$$\Leftrightarrow x = b + a$$

Bijvoorbeeld
$$x - 6 = 2$$
$$\Leftrightarrow x - 6 \orange{+6} = 2 \orange{+6}$$
$$\Leftrightarrow x \orange{+0} = \orange{8}$$
$$\Leftrightarrow x = 8$$

{{% expand "Uitbreiding" %}}
Eigenlijk is $x - a = b$ dezelfde vorm als $x + a = b$, want
$$x - a = b$$
$$\Leftrightarrow x + (-a) = b$$
waarbij we nu $(-a)$ hebben in plaats van $a$. We moeten nu dus aan beide kanten $(-a)$ aftrekken in plaats van gewoon $a$.
$$x + (-a) = b$$
$$\Leftrightarrow x + (-a) \orange{- (-a)} = b \orange{- (-a)}$$
Dat komt echter neer op het **optellen van $a$** bij het linker- en rechterlid, zoals we hierboven gezien hadden.
$$x + (-a) \orange{- (-a)} = b \orange{- (-a)}$$
$$\Leftrightarrow x - a \orange{+a} = b \orange{+a}$$
$$\Leftrightarrow x \orange{+0} = b \orange{+a}$$
$$\Leftrightarrow x = b + a$$
{{% /expand %}}

## Samengevat
{{% attention "Oplossen van $x + a = b$" %}}
Een vergelijking van de vorm
$$x + a = b$$
met $a, b \in \mathbb{R}$ los je op door van het linker- en rechterlid $a$ **af te trekken**:
$$x + a = b$$
$$\Leftrightarrow x + a \orange{- a} = b \orange{- a}$$
$$\Leftrightarrow x + \orange{0} = b \orange{- a}$$
$$\Leftrightarrow x = b - a$$
{{% /attention %}}

{{% attention "Oplossen van $x - a = b$" %}}
Een vergelijking van de vorm
$$x - a = b$$
met $a, b \in \mathbb{R}$ los je op door bij het linker- en rechterlid $a$ **op te tellen**:
$$x - a = b$$
$$\Leftrightarrow x - a \orange{+a} = b \orange{+ a}$$
$$\Leftrightarrow x \orange{+ 0} = b \orange{+ a}$$
$$\Leftrightarrow x = b + a$$
{{% /attention %}}