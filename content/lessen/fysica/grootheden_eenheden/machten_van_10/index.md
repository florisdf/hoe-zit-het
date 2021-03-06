---
title: "Machten van 10"
date: 2019-01-28T08:06:49+01:00
weight: 2
draft: false
tags: ["macht van 10", "machtsverheffing"]
description: "Warvoor gebruiken we machten van 10? Deze les legt uit waarom we machten van 10 nodig hebben en hoe je ermee kan rekenen. De concepten worden heel visueel uitgelegd aan de hand van kleurtjes etc."
images: []
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
we eerst hoe we een macht van 10 ook al weer uitrekenen. Enkele voorbeelden:

\begin{split}
    2{,}6211\cdot \orange{10^2} = 2{,}6211 \cdot \orange{100} = 262{,}11\\\\\
    -0{,}0075\cdot \orange{10^3} = -0{,}0075\cdot \orange{1000} = -7{,}5\\\\\
    6{,}3\cdot \orange{10^{-3}} = 6{,}3 \cdot \orange{0{,}001} = 0{,}0063\\\\\
    405{,}9\cdot \orange{10^{-2}} = 405{,}9 \cdot \orange{0{,}01} = 4{,}059\\\\\
    51\cdot \orange{10^{3}} = 51 \cdot \orange{1000} = 51\ 000\\\\\
\end{split}

Je ziet dat vermenigvuldigen met een macht van 10
ervoor zorgt dat de **komma verschuift**.
De komma verschuift **naar links bij negatieve machten** en ze verschuift **naar rechts bij positieve machten**.

Vermenigvuldigingen met $10^{\orange{2}}$, bijvoorbeeld, verschuift de komma {{< class "2 plaatsen naar rechts" "orange" >}}.
Vermenigvuldigingen met $10^{\orange{-3}}$, verschuift de komma {{< class "3 plaatsen naar links" "orange" >}}.

## Getallen omzetten naar een macht van 10
Nu zullen we zien hoe we aan die $\orange{10^{-9}}$ kwamen bij het voorbeeld 
van $0{,}00000000334 = 3{,}34\cdot \orange{10^{-9}}$.
We willen de komma van $0{,}00000000334$ met
**{{< class "9 plaatsen naar rechts" "blue" >}}** verschuiven tot na de eerste
3. Dat zouden we kunnen doen door te
**{{< class "vermenigvuldigen met $10^9$" "blue" >}}**.
**Maar** we willen dat onze uitkomst
**{{< class "nog steeds gelijk is" "orange" >}}** aan $0{,}00000000334$. Daarom
moeten we ook terug
**{{< class "delen door $10^9$" "orange" >}}**.

\begin{split}
    0{,}00000000334 &= 0{,}00000000334 \cdot \frac{\blue{10^9}}{\orange{10^9}} \\\\\
                    &= 0{,}00000000334 \cdot \blue{10^9} \cdot \frac{1}{\orange{10^9}} \\\\\
                    &= \udotblue{0{,}00000000334 \cdot \blue{10^{9}}} \cdot \orange{10^{-9}} \\\\\
                    &= \udotblue{3{,}34} \cdot \orange{10^{-9}}
\end{split}

Het **{{< class "delen door $10^9$" "orange" >}}** komt neer op
een **{{< class "vermenigvuldigen met $10^{-9}$" "orange" >}}**. We kunnen dus ook
zeggen dat we
**{{< class "vermenigvuldigen met $10^9$" "blue" >}}** om de komma
**{{< class "9 plaatsen naar rechts" "blue" >}}** te verschuiven en vervolgens
**{{< class "vermenigvuldigen met $10^{-9}$" "orange" >}}** om alles
**{{< class "gelijk te houden" "orange" >}}**.

Een ander voorbeeld is dat we een heel groot getal korter willen schrijven. De
afstand tussen de zon en de aarde, bijvoorbeeld, bedraagt ongeveer
$149\ 600\ 000\ 000\ \si{m}$. Dit kunnen we korter schrijven door de komma 
**{{< class "11 plaatsen naar links" "blue" >}}** te schuiven tot net na de 1.
Dat zouden we kunnen doen door te
**{{< class "vermenigvuldigen met $10^{-11}$" "blue" >}}**. **Maar** we willen
natuurlijk dat onze uitkomst
**{{< class "nog steeds gelijk is" "orange" >}}** aan $149\ 600\ 000\ 000$.
Daarom moeten we ook terug delen door $10^{-11}$. Dat is echter hetzelfde als
**{{< class "vermenigvuldigen met $10^{11}$" "orange" >}}**.

\begin{split}
    149\ 600\ 000\ 000 &= \udotblue{149\ 600\ 000\ 000 \cdot \blue{10^{-11}}} \cdot \orange{10^{11}} \\\\\
                       &= \udotblue{1{,}496} \cdot \orange{10^{11}} \\\\\
\end{split}

Merk wel op dat nu het aantal [beduidende cijfers](../beduidende_cijfers) is
veranderd van 12 naar 4. Je kan het juiste aantal beduidende cijfers
verkrijgen door de [benaderingsregels](../benaderingsregels) toe te passen.

## Machten van 10 omzetten
Soms zullen we ook machten van 10 moeten omzetten naar andere machten van 10.
We willen onze $3{,}34 \cdot 10^{-9}$ bijvoorbeeld omzetten naar 
$\orange{\ldots\text{iets}\ldots} \cdot \blue{10^{-11}}$. Om dat te doen, 
zullen we de $3{,}34 \cdot 10^{-9}$
**{{< class "vermenigvuldigen met $10^{-11}$ om de juiste macht van 10 te hebben" "blue" >}}**
en vervolgens 
**{{< class "vermenigvuldigen met $10^{11}$ om het getal gelijk te houden" "orange" >}}**.

\begin{split}
    3{,}34 \cdot 10^{-9} &= 3{,}34 \cdot \udotorange{10^{-9} \cdot \orange{10^{11}}} \cdot \blue{10^{-11}} \\\\\
                         &= 3{,}34 \cdot \udotorange{10^{2}} \cdot \blue{10^{-11}} \\\\\
                         &= \udoubleorange{3{,}34 \cdot 10^{2}} \cdot \blue{10^{-11}} \\\\\
                         &= \udoubleorange{334} \cdot \blue{10^{-11}} \\\\\
\end{split}

## Samengevat
{{< attention "Omzetten naar macht van 10" >}}
* Als je de komma $N$ plaatsen **naar rechts** wilt opschuiven:
Vermenigvuldig met {{< class "$10^{N}$ om de komma op te schuiven" "blue" >}} en met {{< class "$10^{-N}$ om het getal gelijk te houden" "orange" >}}.
* Als je de komma $N$ plaatsen **naar links** wilt opschuiven:
Vermenigvuldig met {{< class "$10^{-N}$ om de komma op te schuiven" "blue" >}} en met {{< class "$10^N$ om het getal gelijk te houden" "orange" >}}.
{{< /attention >}}

{{< attention "Omzetten van een macht van 10" >}}
Als je $a \cdot 10^b$ wilt omzetten naar $\ldots\text{iets}\ldots \cdot \blue{10^c}$
{{< mute "(met $a, b, c \in \mathbb{R}$)" >}}:

Vermenigvuldig $a \cdot 10^b$ met
{{< class "$10^{c}$ om de juiste macht van 10 te hebben" "blue" >}} en met
{{< class "$10^{-c}$ om alles gelijk te houden" "orange" >}} aan $a \cdot 10^b$.
Combineer vervolgens de $a \cdot 10^{b} \cdot \orange{10^{-c}}$ tot één getal en
laat de $\cdot \blue{10^{c}}$ erachter staan.

{{< /attention >}}
