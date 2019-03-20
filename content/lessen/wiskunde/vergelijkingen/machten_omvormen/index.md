---
title: "Machten en wortels omvormen"
date: 2019-01-15T11:16:02+01:00
weight: 5
draft: false
tags: ["vergelijkingen", "algebra"]
categories: ["wiskunde", "algebra"]
level: "2M"
course: "wiskunde"
topic: "algebra"
---
Een [vergelijking](../intro) oplossen betekent dat we de waarden van de
onbekende(n) vinden waarvoor de gelijkheid klopt. Vaak is er maar één
onbekende, namelijk $x$.

Door een vergelijking [om te vormen](../omvormen) naar de vorm $x = \text{(een
getal)}$ kunnen we de vergelijking oplossen. In deze les zien we hoe we
vergelijkingen van de vorm $x^2 = a$ en $x^3 = a$ kunnen omvormen naar $x
= \text{(een getal)}$. Ten slotte zullen we ook de vergelijkingen $\sqrt{x} =
a$ en $\sqrt[3]{x} = a$ omvormen.

## Omvormen van $x^2 = a$
Om een vergelijking van de vorm $x^2 = a$ {{% mute "(met $a \in \mathbb{R}^+$)" %}} om te vormen naar $x = \text{(een getal)}$, moeten we enkel het **kwadraat** weg krijgen uit het linkerlid. We willen dat er links $x$ staat in plaats van $x^2$. We kunnen het kwadraat weg krijgen door de **wortel te nemen van het linker- en rechterlid**:
$$x^2 = a$$
$$\Leftrightarrow \orange{\sqrt{\normal{x^2}}} = \orange{\pm\sqrt{\normal{a}}}$$
$$\Leftrightarrow x = \pm\sqrt{a}$$

Bijvoorbeeld: stel dat we de vergelijking
$$x^2 = 10$$
moeten oplossen. We willen het kwadraat aan de linkerkant weg krijgen zodat er links gewoon $x$ staat. Dat kunnen we doen door van de vergelijking de **vierkantswortel** te nemen:
$$x^2 = 10$$
$$\Leftrightarrow \orange{\sqrt{\normal{x^2}}} = \orange{\pm\sqrt{\normal{10}}}$$
$$\Leftrightarrow x = \pm \sqrt{10}$$
$$\Leftrightarrow x = \pm 3.162\ldots$$


We controleren door de $x$ in de oorspronkelijke vergelijking $\blue{x}^2 = 10$ eens te vervangen door $\blue{(3.162\ldots)}$ en eens door $\blue{(-3.162\ldots)}$:
$$\blue{(3.162\ldots)}^2 = 10$$ Check! :white_check_mark:
$$\blue{(-3.162\ldots)}^2 = 10$$
Klopt! :facepunch:

{{% expand "Uitbreiding: waarom die $\pm$?" %}}
Waar komt die $\orange{\pm}$ plots vandaan? :scream:

Het probleem is dat we enkel het *kwadraat* van $x$ kennen. Wanneer je een
reëel getal kwadrateert, zal het echter **altijd positief zijn**. Je kan het
teken van een getal dus niet meer weten nadat het gekwadrateerd is.

Stel dat ik een getal in mijn hoofd heb waarvan het kwadraat gelijk is aan $9$.
Welk getal heb ik dan in mijn hoofd? Je zou misschien eerst denken dat het $3$
is omdat $3^2 = 9$, maar het zou even goed $-3$ kunnen zijn want ook
$(-3)^2=9$. Het getal in mijn hoofd kan dus $+3$ of $-3$ zijn. We schrijven de
vergelijkingen die hierbij horen als volgt:
$$x^2 = 9$$
$$\Leftrightarrow \sqrt{x^2} = \sqrt{9}$$
$$\Leftrightarrow x = \pm \sqrt{9}$$
$$\Leftrightarrow x=\pm 3$$.

Als het **kwadraat** van een getal *positief* is, kan het getal zelf **zowel
positief als negatief** zijn.
{{% /expand %}}

## Omvormen van $x^3 = a$
Voor een vergelijking als $x^3 = a$ doen we iets heel gelijkaardigs als bij
$x^2 = a$, maar nu gebruiken we de **derdemachtswortel**:
$$x^3 = a$$
$$\Leftrightarrow \orange{\sqrt[3]{\normal{x^3}}} = \orange{\sqrt[3]{\normal{a}}}$$
$$\Leftrightarrow x = \sqrt[3]{a}$$

We willen bijvoorbeeld de vergelijking $x^3 = -16$ oplossen.
$$x^3 = -16$$
$$\Leftrightarrow \orange{\sqrt[3]{\normal{x^3}}} = \orange{\sqrt[3]{\normal{-16}}}$$
$$\Leftrightarrow x = \sqrt[3]{-16}$$
$$\Leftrightarrow x = -2.520\ldots$$

Controle:
$$\blue{(-2.520\ldots)}^3 = -16$$

{{% expand "Uitbreiding: waarom nu plots geen $\pm$?" %}}
Merk op dat er deze keer géén $\pm$ voor de wortel staat. Dat komt omdat de
derde macht van een getal altijd hetzelfde teken heeft als het getal
zelf. Bijvoorbeeld $(\orange{-}2)^3 = (-2)\cdot(-2)\cdot(-2) = \orange{-}8$.

Als de **derde macht** van een getal *negatief* is, is het getal zelf *ook*
negatief.  Als de **derde macht** van een getal *postitief* is, is het getal
zelf *ook* positief.
{{% /expand %}}

## Omvormen van $\sqrt{x} = a$
Om een vergelijking van de vorm $\sqrt{x} = a$
{{% mute "(met $a \in \mathbb{R}^+$)" %}}
om te vormen naar $x = \text{(een getal)}$, moeten we enkel
de **vierkantswortel** weg krijgen uit het linkerlid. We kunnen hiervoor zorgen
door het **linker- en rechterlid te kwadrateren**:

$$\sqrt{x} = a$$
$$\Leftrightarrow \orange{(}\sqrt{x}\orange{)^2} = \orange{(}a\orange{)^2}$$
$$\Leftrightarrow x = a^2$$

Bijvoorbeeld:
$$\sqrt{x} = 5$$
$$\Leftrightarrow \orange{(}\sqrt{x}\orange{)^2} = \orange{(}5\orange{)^2}$$
$$\Leftrightarrow x = 5^2$$
$$\Leftrightarrow x = 25$$

Controle:
$$\sqrt{\blue{25}} = 5$$
Perfect! :ok_hand:

{{% expand "Uitbreiding: Waarom niet $\pm a^2$?" %}}
Omdat we de vierkantswortel nemen van $x$, is $x$ sowieso een positief (reëel)
getal.

{{% mute "(De vierkantswortel van een negatief getal bestaat niet in $\mathbb{R}$.)" %}}
{{% /expand %}}

## Omvormen van $\sqrt[3]{x} = a$
Ook voor $\sqrt[3]{x} = a$ doen we iets gelijkaardigs als bij $\sqrt{x} = a$,
maar nu dan met een derde macht. Merk op dat $a$ nu zowel positief als negatief
kan zijn ($a \in \mathbb{R}$), want een derdemachtswortel kan ook negatief zijn.

$$\sqrt[3]{x} = a$$
$$\Leftrightarrow \orange{(}\sqrt[3]{x}\orange{)^3} = \orange{(}a\orange{)^3}$$
$$\Leftrightarrow x = a^3$$

Bijvoorbeeld $\sqrt[3]{x} = -2$
$$\sqrt[3]{x} = -2$$
$$\Leftrightarrow \orange{(}\sqrt[3]{x}\orange{)^3} = \orange{(}-2\orange{)^3}$$
$$\Leftrightarrow x = (-2)^3$$
$$\Leftrightarrow x = -8$$

Controle:
$$\sqrt[3]{\blue{-8}} = -2$$
OK!

## Samengevat
| Vergelijking      | Tussenstap                                                              | Oplossing                            | {{% mute "Voorwaarden" %}}                                |
|-------------------|-------------------------------------------------------------------------|--------------------------------------|-----------------------------------------------------------|
| $x^2 = a$         | $\orange{\sqrt{\normal{x^2}}} = \orange{\sqrt{\normal{a}}}$             | $x = \pm \orange{\sqrt{\normal{a}}}$ | {{% mute "$a \in \mathbb{R}^+$" %}}                       |
| $\sqrt{x} = a$    | $\orange{(\normal{\sqrt{x}})^2} = a^\orange{2}$                         | $x = a^\orange{2}$                   | {{% mute "$a \in \mathbb{R}^+$" %}}                       |
| $x^3 = a$         | $\orange{\sqrt[3]{\normal{x^3}}} = \orange{\sqrt[3]{\normal{a}}}$       | $x = \orange{\sqrt[3]{\normal{a}}}$  | {{% mute "$a \in \mathbb{R}$" %}}                         |
| $\sqrt[3]{x} = a$ | $\orange{(\normal{\sqrt[3]{x}})^3} = a^\orange{3}$                      | $x = a^\orange{3}$                   | {{% mute "$a \in \mathbb{R}$" %}}                         |
