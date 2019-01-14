---
title: "Vermenigvuldigingen en delingen omvormen"
date: 2019-01-13T13:33:28+01:00
weight: 4
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
kunnen we de vergelijking oplossen. In deze les zien we hoe we vergelijkingen van de vorm $a\cdot x = b$ en $\frac{x}{a} = b$ kunnen omvormen naar $x = \text{(een getal)}$. Daarbij zijn $a$ en $b$ [reële getallen](../../verzamelingen/reele_getallen) en $a \neq 0$.

{{% expand "Uitbreiding: Waarom moet $a \neq 0$?" %}}
Zowel bij de vergelijking $a\cdot x = b$ als bij $\frac{x}{a} = b$ moet $a \neq 0$.

Bij $a\cdot x = b$ moet dat omdat als $a = 0$ de vgl. wordt
$0\cdot x = b$. Dit is een speciale soort vergelijking waar we het [later](../aantal_oplossingen) over zullen hebben.

Bij $\frac{x}{a} = b$ moet $a \neq 0$ omdat we anders zouden delen door $0$. En delen door $0$, dat [levert alleen maar problemen op](../../rekenen/delingen#delen_door_nul).
{{% /expand %}}

## Omvormen van $a\cdot x = b$
Om een vergelijking van de vorm $a \cdot x = b$ {{% mute "(met $a \in \mathbb{R}_0$ en $b \in \mathbb{R}$)" %}} om te vormen naar $x = \text{(een getal)}$, moeten we enkel de $a$ weg krijgen uit het linkerlid. We willen dat er links $1\cdot x$ staat in plaats van $a\cdot x$. We kunnen van de $a$ een $1$ maken door het linker- en rechterlid **te delen door $a$**:
$$a \cdot x = b$$
$$\Leftrightarrow \frac{a \cdot x}{\orange{a}} = \frac{b}{\orange{a}}$$
$$\Leftrightarrow \frac{a}{\orange{a}}\cdot x = \frac{b}{\orange{a}}$$
$$\Leftrightarrow \orange{1}\cdot x = \frac{b}{\orange{a}}$$
$$\Leftrightarrow x = \frac{b}{a}$$

{{% expand "Uitbreiding" %}} 
Zorg dat je goed begrijpt waarom we bij het omvormen van een vergelijking telkens dezelfde bewerking aan **beide** kanten van de vergelijking moeten doen. We doen dat om de **gelijkheid te kunnen behouden**.

Als we weten dat
$$\blue{3x} = \blue{-6}$$
Waar is $\frac{\blue{3x}}{3}$ dan aan gelijk? Omdat we weten dat $\blue{3x} = \blue{- 6}$ is
$$\frac{\blue{3x}}{3} = \frac{\blue{-6}}{3}$$
Enkel door beide kanten van de vergelijking te delen door $3$, zijn we zeker dat we opnieuw een **gelijkheid krijgen**.
{{% /expand %}}

## Voorbeeld voor $a\cdot x = b$
Nu eens met echte getallen in plaats van al die letters. Stel dat we de vergelijking
$$-3x = 6$$
moeten oplossen. We willen de $-3$ aan de linkerkant weg krijgen zodat er links gewoon $x$ staat. Dat kunnen we doen door de vergelijking te delen door $\orange{-3}$:
$$-3\cdot x = 6$$
$$\Leftrightarrow \frac{-3\cdot x}{\orange{-3}} = \frac{6}{\orange{-3}}$$
$$\Leftrightarrow \frac{-3}{\orange{-3}}\cdot x = \frac{6}{\orange{-3}}$$
$$\Leftrightarrow \orange{1}\cdot x = \orange{-2}$$
$$\Leftrightarrow x = -2$$

Controle door de $x$ in de oorspronkelijke vergelijking $-3\cdot \blue{x} = 6$ te vervangen door $\blue{(-2)}$:
$$-3\cdot \blue{(-2)} = 6$$

Feest! :tada: We hebben $x$ gevonden!

## Omvormen van $\frac{x}{a} = b$
Om een vergelijking van de vorm $\frac{x}{a} = b$ {{% mute "(met $a \in \mathbb{R}_0$ en $b \in \mathbb{R}$)" %}} om te vormen naar $x = \text{(een getal)}$, moeten we enkel de $a$ weg krijgen uit het linkerlid. We willen dat er links $x\cdot 1$ staat in plaats van $\frac{x}{a}$. We kunnen hiervoor zorgen door het linker- en rechterlid **te vermenigvuldigen met $a$**:
$$\frac{x}{a} = b$$
$$\Leftrightarrow \frac{x}{a} \cdot \orange{a} = b\cdot \orange{a}$$
$$\Leftrightarrow x \cdot \frac{\orange{a}}{a} = b\cdot \orange{a}$$
$$\Leftrightarrow x \cdot \orange{1} = b\cdot \orange{a}$$
$$\Leftrightarrow x = b\cdot a$$

## Voorbeeld voor $\frac{x}{a} = b$
$$\frac{x}{5} = -2$$
$$\Leftrightarrow \frac{x}{5}\cdot \orange{5} = -2\cdot \orange{5}$$
$$\Leftrightarrow x\cdot \frac{\orange{5}}{5} = -2\cdot \orange{5}$$
$$\Leftrightarrow x\cdot \orange{1} = \orange{-10}$$
$$\Leftrightarrow x = -10$$

Controle:
$$\frac{\blue{-10}}{5} = - 2$$
Yes! :muscle:
## Samengevat
{{% attention "Oplossen van $a\cdot x = b$" %}}
Een vergelijking van de vorm
$$a\cdot x = b$$
met $a \in \mathbb{R}_0$ en $b \in \mathbb{R}$ los je op door het linker- en
rechterlid te **delen door $a$**:
$$a\cdot x = b$$
$$\Leftrightarrow \frac{a\cdot x}{\orange{a}} = \frac{b}{\orange{a}}$$
$$\Leftrightarrow x = \frac{b}{a}$$
{{% /attention %}}

{{% attention "Oplossen van $\frac{x}{a} = b$" %}}
Een vergelijking van de vorm
$$\frac{x}{a} = b$$
met $a \in \mathbb{R}_0$ en $b \in \mathbb{R}$ los je op door het linker- en
rechterlid te **vermenigvuldigen met $a$**:
$$\frac{x}{a} = b$$
$$\Leftrightarrow \frac{x}{a}\orange{\cdot a} = b\orange{\cdot a}$$
$$\Leftrightarrow x = b \cdot a$$
{{% /attention %}}
