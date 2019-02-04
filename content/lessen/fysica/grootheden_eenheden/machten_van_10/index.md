---
title: "Machten van 10"
date: 2019-01-28T08:06:49+01:00
weight: 2
draft: false
tags: ["grootheden_eenheden", "machten_van_10"]
categories: ["grootheden_eenheden", "machten_van_10"]
level: "3M"
course: "Fysica"
topic: "grootheden_eenheden"
---

Het wordt snel lastig om heel grote of heel kleine getallen te lezen of te 
schrijven.
De tijd die het licht nodig
heeft om $1 \si{ m}$ ver te reizen, bijvoorbeeld, bedraagt $0{,}00000000334 
\si{ s}$. We kunnen dit getal veel korter schrijven door de komma na de eerste 
3 te zetten en nadien terug te vermenigvuldigen met $\orange{10^{-9}}$:
$$0{,}00000000334 = 3{,}34\cdot \orange{10^{-9}}$$

Machten van 10 zullen ons toelaten om heel kleine getallen en heel grote 
getallen op een korte, leesbare manier te noteren.

Het is voor deze les belangrijk dat je de volgende rekenregels kent en begrijpt 
($a, b, c \in \mathbb{R}$):

$$a^{-b} = \frac{1}{a^{b}} \quad \text{waarbij }a \ne 0$$
$$a^b \cdot a^c = a^{b+c}$$

Extra uitleg vind je in de les over [rekenen met 
machten](../../../wiskunde/rekenen/machten/#producten-van-machten).

## Machten van 10 uitrekenen
Hoe komen we aan die $\orange{10^{-9}}$ bij het voorbeeld van $0{,}00000000334 
= 3{,}34\cdot \orange{10^{-9}}$? Voor we tonen waar die vandaan komt, bespreken 
we eerst hoe we een macht van 10 terug uitrekenen. Enkele voorbeelden:

$$2{,}6211\cdot \orange{10^2} = 2{,}6211 \cdot \orange{100} = 262{,}11$$
$$-0{,}0075\cdot \orange{10^3} = -0{,}0075\cdot \orange{1000} = -7{,}5$$
$$6{,}3\cdot \orange{10^{-3}} = 6{,}3 \cdot \orange{0{,}001} = 0{,}0063$$
$$405{,}9\cdot \orange{10^{-2}} = 405{,}9 \cdot \orange{0{,}01} = 4{,}059$$
$$51\cdot \orange{10^{3}} = 51 \cdot \orange{1000} = 51\ 000$$

Je ziet dat vermenigvuldigen met een macht van 10
ervoor zorgt dat de **komma verschuift**.
De komma verschuift **naar links bij negatieve machten** en ze verschuift **naar rechts bij positieve machten**.

Vermenigvuldigingen met $10^{\orange{2}}$, bijvoorbeeld, verschuift de komma {{% class "2 plaatsen naar rechts" "orange" %}}.
Vermenigvuldigingen met $10^{\orange{-3}}$, verschuift de komma {{% class "3 plaatsen naar links" "orange" %}}.

## Getallen omzetten naar een macht van 10
Nu zullen we zien hoe we aan die $\orange{10^{-9}}$ kwamen bij het voorbeeld 
van $0{,}00000000334 = 3{,}34\cdot \orange{10^{-9}}$.
We willen de komma van $0{,}00000000334$ met
**{{% class "9 plaatsen naar rechts" "blue" %}}**
verschuiven tot na de eerste 3. Dat zouden we kunnen doen door te
**{{% class "vermenigvuldigen met $10^9$" "blue" %}}**.
**Maar** we willen dat onze uitkomst
**{{% class "nog steeds gelijk is" "orange" %}}**
aan $0{,}00000000334$. Daarom moeten we ook terug
**{{% class "delen door $10^9$" "orange" %}}**.

\begin{split}
0{,}00000000334 &= 0{,}00000000334 \cdot \frac{\blue{10^9}}{\orange{10^9}} \\\\\
&= 0{,}00000000334 \cdot \blue{10^9} \cdot \frac{1}{\orange{10^9}} \\\\\
&= 0{,}00000000334 \cdot \blue{10^{9}} \cdot \orange{10^{-9}} \\\\\
&= \blue{3{,}34} \cdot \orange{10^{-9}}
\end{split}

Het **{{% class "delen door $10^9$" "orange" %}}**, komt neer op
**{{% class "vermenigvuldigen met $10^{-9}$" "orange" %}}**.

{{% attention "Omzetten naar macht van 10" %}}
* Als je de komma $N$ plaatsen **naar rechts** wilt opschuiven:
Vermenigvuldig met {{% class "$10^{N}$ om de komma op te schuiven" "blue" %}} en met {{% class "$10^{-N}$ om het getal gelijk te houden" "orange" %}}.
* Als je de komma $N$ plaatsen **naar links** wilt opschuiven:
Vermenigvuldig met {{% class "$10^{-N}$ om de komma op te schuiven" "blue" %}} en met {{% class "$10^N$ om het getal gelijk te houden" "orange" %}}.
{{% /attention %}}

In ons voorbeeld willen we de komma 9 plaatsen **naar rechts** opschuiven. We 
moeten dus vermenigvuldigen met
{{% class "$10^{9}$ om de komma op te schuiven" "blue" %}} en met
{{% class "$10^{-9}$ om het getal gelijk te houden" "orange" %}}. We krijgen:

\begin{split}
0{,}00000000334 &= 0{,}00000000334 \cdot \blue{10^{9}} \cdot \orange{10^{-9}} \\\\\
&= \blue{3{,}34} \cdot \orange{10^{-9}}
\end{split}

## Machten van 10 omzetten
Soms zullen we ook machten van 10 moeten omzetten naar andere machten van 10.
We willen onze $3{,}34 \cdot 10^{-9}$ bijvoorbeeld omzetten naar 
$\orange{\ldots\text{iets}\ldots} \cdot \blue{10^{-11}}$. Om dat te doen, 
zullen we de $3{,}34 \cdot 10^{-9}$ vermenigvuldigen met
{{% class "$10^{-11}$ om de juiste macht van 10 te hebben" "blue" %}}
en met
{{% class "$10^{11}$ om het getal gelijk te houden" "orange" %}}.

{{% attention "Macht van 10 omzetten" %}}
Als je $a \cdot 10^b$ wilt omzetten naar $\ldots\text{iets}\ldots \cdot \blue{10^c}$
{{% mute "(met $a, b, c \in \mathbb{R}$)" %}}:

Vermenigvuldig $a \cdot 10^b$ met
{{% class "$10^{c}$ om de juiste macht van 10 te hebben" "blue" %}} en met
{{% class "$10^{-c}$ om alles gelijk te houden" "orange" %}} aan $a \cdot 10^b$.

{{% /attention %}}

In ons voorbeeld willen we $3{,}34 \cdot 10^{-9}$ omzetten naar 
$\ldots\text{iets}\ldots \cdot \blue{10^{-11}}$. Daarvoor moeten we $3{,}34 
\cdot 10^{-9}$ vermenigvuldigen met
{{% class "$10^{-11}$ om de juiste macht van 10 te hebben" "blue" %}} en met
{{% class "$10^{-(-11)}$ om alles gelijk te houden" "orange" %}}.

\begin{split}
3{,}34 \cdot 10^{-9} &= 3{,}34 \cdot 10^{-9} \cdot \blue{10^{-11}} \cdot \orange{10^{-(-11)}} \\\\\
&= 3{,}34 \cdot 10^{-9} \cdot \orange{10^{11}} \cdot \blue{10^{-11}} \\\\\
&= 3{,}34 \cdot \orange{10^{-9 + 11}} \cdot \blue{10^{-11}} \\\\\
&= 3{,}34 \cdot \orange{10^{2}} \cdot \blue{10^{-11}} \\\\\
&= \orange{334} \cdot \blue{10^{-11}} \\\\\
\end{split}
