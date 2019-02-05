---
title: "Prefixen"
date: 2019-01-28T08:05:35+01:00
weight: 3
draft: true
tags: []
categories: []
level: ""
course: ""
topic: ""
---
We kunnen grootheden zoals *lengte* beschrijven met eenheden zoals *meter*. In een vorige les zagen we dat elke [grootheid een officiële SI-eenheid heeft](../intro#si-eenheden-maken-duidelijke-afspraken). De officiële eenheid van *tijd* is bijvoorbeeld de seconde.

In een [andere les](../machten_van_10) zagen we hoe we machten van 10 kunnen gebruiken om heel grote of heel kleine getallen korter en leesbaarder te schrijven.

Om alles nog korter en leesbaarder te schrijven, gebruiken we vaak **prefixen**. Een prefix
{{% mute "(of voorvoegsel)" %}}
schrijf je telkens *vóór* de eenheid. Elke prefix stelt een bepaalde macht van 10 voor. Je bent ongetwijfeld al veel prefixen tegengekomen. De $\si{k}$
{{% mute "(kilo)" %}}
in $\si{kg}$
{{% mute "(kilogram)" %}}, bijvoorbeeld, is een prefix. Of de $\si{c}$
{{% mute "(centi)" %}}
in $\si{cm}$
{{% mute "(centimeter)" %}}.

## De belangrijkste prefixen
Elke prefix komt overeen met een macht van 10. Hieronder vind je een tabel met de belangrijkste prefixen.

| Symbool 	| Naam  	| Macht van 10 	|
|---------	|-------	|--------------	|
| $\si{T}$       	| Terra 	| $10^{12}   $    	|
| $\si{G}$       	| Giga  	| $10^9    $    	|
| $\si{M}$       	| Mega  	| $10^6    $    	|
| $\si{k}$       	| kilo  	| $10^3    $    	|
| $\si{h}$       	| hecto 	| $10^2    $    	|
| $\si{da}$      	| deca  	| $10^1    $    	|
|              	|       	| $        $    	|
| $\si{d}$       	| deci  	| $10^{-1} $    	|
| $\si{c}$       	| centi 	| $10^{-2} $    	|
| $\si{m}$       	| milli 	| $10^{-3} $    	|
| $\mu$   	| micro 	| $10^{-6} $    	|
| $\si{n}$       	| nano  	| $10^{-9} $    	|
| $\si{p}$       	| pico  	| $10^{-12}$    	|

## Prefixen omzetten
Eens je weet welke prefix overeenkomt met welke macht van 10 (en omgekeerd), is het omzetten van prefixen hetzelfde als het [omzetten van machten van 10](../machten_van_10#machten-van-10-omzetten).
Het enige wat je extra moet doen is prefixen omzetten naar machten van 10 en terug.

Stel dat we $5{,}2 \green{\si{ k}}\si{m}$ willen omzetten naar $\blue{\si{d}}\si{m}$. Dat kan je doen als volgt:

1. Zet alle prefixen om naar een macht van 10. De opgave wordt dan:
"Zet $5{,}2 \cdot \green{10^{3}} \si{ m}$ om naar $\ldots\text{iets}\ldots\cdot \blue{10^{-1}}\si{ m}$"
2. Los op volgens de methode van het [omzetten van machten van 10](../machten_van_10#machten-van-10-omzetten)
\begin{split}
5{,}2 \cdot \green{10^{3}} \si{ m}
&= 5{,}2 \cdot \green{10^{3}} \cdot \orange{10^1} \cdot \blue{10^{-1}}\si{ m}\\\\\
&= 5{,}2\cdot 10^{\green{3} + \orange{1}} \cdot \blue{10^{-1}} \si{ m}\\\\\
&= 5{,}2\cdot 10^4 \cdot \blue{10^{-1}}\si{ m}
\end{split}
3. Vervang de bijhorende macht van 10 terug door de prefix:
$$5{,}2\cdot 10^4 \cdot \blue{\si{d}}\si{m}$$

## Kubieke- en vierkante-
De eenheid van volume is $\si{m}^3$
{{% mute "(kubieke meter)" %}}. 
Als er een prefix voor zo'n eenheid staat, bijvoorbeeld $\orange{\si{c}} \si{m}^3$, wordt die prefix ook tot de derde macht verheven. Er staat dus eigenlijk

\begin{split}
\orange{\si{c}}\si{m}^3
&= \orange{\si{c}}^3\si{m}^3\\\\\
&= (\orange{10^{-2}})^3\si{m}^3\\\\\
&= 10^{\orange{-2}\cdot 3}\si{m}^3\\\\\
&= 10^{-6}\si{m}^3
\end{split}

Voor prefixen van een oppervlakte (eenheid $\si{m}^2$) doen we net hetzelfde, maar nu met een kwadraat:

\begin{split}
\orange{\si{c}}\si{m}^2
&= \orange{\si{c}}^2\si{m}^2\\\\\
&= (\orange{10^{-2}})^2\si{m}^2\\\\\
&= 10^{\orange{-2}\cdot 2} \si{m}^2\\\\\
&= 10^{-4}\si{m}^2
\end{split}
