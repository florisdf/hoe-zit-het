---
title: "Kwadraten en vierkantswortels omvormen"
date: 2019-01-15T11:16:02+01:00
weight: 5
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
kunnen we de vergelijking oplossen. In deze les zien we hoe we vergelijkingen van de vorm $x^2 = a$ en $\sqrt{x} = a$ kunnen omvormen naar $x = \text{(een getal)}$. Daarbij is $a$ een positief [reële getal](../../verzamelingen/reele_getallen).

{{% expand "Uitbreiding: waarom moet $a\geq 0$?" %}}
{{% /expand %}}

## Omvormen van $x^2 = a$
Om een vergelijking van de vorm $x^2 = a$ {{% mute "(met $a \in \mathbb{R}^+$)" %}} om te vormen naar $x = \text{(een getal)}$, moeten we enkel het **kwadraat** weg krijgen uit het linkerlid. We willen dat er links $x$ staat in plaats van $x^2$. We kunnen het kwadraat weg krijgen door de **wortel te nemen van het linker- en rechterlid**:
$$x^2 = a$$
$$\Leftrightarrow \orange{\sqrt{\black{x^2}}} = \orange{\pm\sqrt{\black{a}}}$$
$$\Leftrightarrow x = \pm\sqrt{a}$$

{{% expand "Uitbreiding: waarom die $\pm$?" %}}
Waar komt die $\orange{\pm}$ plots vandaan? :scream:

Het probleem is dat we enkel het *kwadraat* van $x$ kennen. Wanneer je een reëel getal kwadrateert, zal het echter **altijd positief zijn**. Je kan het teken van een getal dus niet meer weten nadat het gekwadrateerd is.

Stel dat ik een getal in mijn hoofd heb waarvan het kwadraat gelijk is aan $9$. Welk getal heb ik dan in mijn hoofd? Je zou misschien eerst denken dat het $3$ is omdat $3^2 = 9$, maar het zou even goed $-3$ kunnen zijn want ook $(-3)^2=9$. Het getal in mijn hoofd kan dus $+3$ of $-3$ zijn. We schrijven de vergelijkingen die hierbij horen als volgt:
$$x^2 = 9$$
$$\Leftrightarrow \sqrt{x^2} = \pm \sqrt{9}$$
$$\Leftrightarrow x=\pm 3$$.
{{% /expand %}}


## Voorbeeld voor $x^2 = a$
Stel dat we de vergelijking
$$x^2 = 10$$
moeten oplossen. We willen het kwadraat aan de linkerkant weg krijgen zodat er links gewoon $x$ staat. Dat kunnen we doen door van de vergelijking de **vierkantswortel** te nemen:
$$x^2 = 10$$
$$\Leftrightarrow \orange{\sqrt{\black{x^2}}} = \orange{\pm\sqrt{\black{10}}}$$
$$\Leftrightarrow x = \pm \sqrt{10}$$
$$\Leftrightarrow x = \pm 3.162\ldots$$


We controlen door de $x$ in de oorspronkelijke vergelijking $\blue{x}^2 = 10$ eens te vervangen door $\blue{(3.162\ldots)}$ en eens door $\blue{(-3.162\ldots)}$:
$$\blue{(3.162\ldots)}^2 = 10$$ Check! :white_check_mark:
$$\blue{(-3.162\ldots)}^2 = 10$$
Klopt! :facepunch:

## Omvormen van $\sqrt{x} = a$
Om een vergelijking van de vorm $\sqrt{x} = a$ {{% mute "(met $a \in \mathbb{R}^+$" %}} om te vormen naar $x = \text{(een getal)}$, moeten we enkel de **vierkantswortel** weg krijgen uit het linkerlid. We willen dat er links $x$ staat in plaats van $\sqrt{x}$. We kunnen hiervoor zorgen door het **linker- en rechterlid te kwadrateren**:
$$\sqrt{x} = a$$
$$\Leftrightarrow \orange{(}\sqrt{x}\orange{)^2} = \orange{(}a\orange{)^2}$$
$$\Leftrightarrow x = a^2$$

{{% expand "Uitbreiding: Waarom niet $\pm a^2$?" %}}
Omdat we de vierkantswortel nemen van $x$, kan $x$ geen negatief (reëel) getal zijn.
{{% /expand %}}

## Voorbeeld voor $\sqrt{x} = a$
$$\sqrt{x} = 5$$
$$\Leftrightarrow \orange{(}\sqrt{x}\orange{)^2} = \orange{(}5\orange{)^2}$$
$$\Leftrightarrow x = 5^2$$
$$\Leftrightarrow x = 25^2$$

Controle:
$$\sqrt{25} = 5$$
Perfect! :ok_hand:
## Samengevat
{{% attention "Oplossen van $x^2 = a$" %}}
Een vergelijking van de vorm
$$x^2 = a$$
met $a \in \mathbb{R}^+$ los je op door de **wortel te nemen van het linker- en rechterlid**:
$$x^2 = a$$
$$\Leftrightarrow \orange{\sqrt{\black{x^2}}} = \orange{\pm\sqrt{\black{a}}}$$
$$\Leftrightarrow x = \pm\sqrt{a}$$
{{% /attention %}}

{{% attention "Oplossen van $\sqrt{x} = a$" %}}
Een vergelijking van de vorm
$$\sqrt{x} = a$$
met $a \in \mathbb{R}^+$ los je op door het **linker- en rechterlid te kwadrateren**:
$$\sqrt{x} = a$$
$$\Leftrightarrow \orange{(}\sqrt{x}\orange{)^2} = \orange{(}a\orange{)^2}$$
$$\Leftrightarrow x = a^2$$
{{% /attention %}}