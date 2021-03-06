---
title: "Prefixen"
date: 2019-01-28T08:05:35+01:00
weight: 3
draft: false
tags: ["eenheid", "grootheid", "prefix", "SI-prefix", "SI-voorvoegsel", "voorvoegsel"]
description: "Wat zijn voorzetsels of prefixen en waarom we ze nodig hebben? Deze les legt het uit en toont hoe je voorvoegsels kan wegwerken, toevoegen en omzetten. We vertellen ook wat er gebeurt met eenheden die een exponent hebben (kubieke en vierkante)."
images: []
---
We kunnen grootheden zoals *lengte* beschrijven met eenheden zoals *meter*. In een vorige les zagen we dat elke [grootheid een officiële SI-eenheid heeft](../intro#si-eenheden-maken-duidelijke-afspraken). De officiële eenheid van *tijd* is bijvoorbeeld de seconde.

In een [andere les](../machten_van_10) zagen we hoe we machten van 10 kunnen gebruiken om heel grote of heel kleine getallen korter en leesbaarder te schrijven.

Om alles nog korter en leesbaarder te schrijven, gebruiken we vaak **prefixen**. Een prefix
{{< mute "(of voorvoegsel)" >}}
schrijf je telkens *vóór* de eenheid. Elke prefix stelt een bepaalde macht van 10 voor. Je bent ongetwijfeld al veel prefixen tegengekomen. De $\si{k}$
{{< mute "(kilo)" >}}
in $\si{kg}$
{{< mute "(kilogram)" >}}, bijvoorbeeld, is een prefix. Of de $\si{c}$
{{< mute "(centi)" >}}
in $\si{cm}$
{{< mute "(centimeter)" >}}.

## De belangrijkste prefixen
Elke prefix komt overeen met een macht van 10. Hieronder vind je een tabel met de belangrijkste prefixen.

| Symbool   | Naam    | Macht van 10   |
| --------- | ------- | -------------- |
| $\si{T}$  | Tera   | $10^{12}   $   |
| $\si{G}$  | Giga    | $10^9    $     |
| $\si{M}$  | Mega    | $10^6    $     |
| $\si{k}$  | kilo    | $10^3    $     |
| $\si{h}$  | hecto   | $10^2    $     |
| $\si{da}$ | deca    | $10^1    $     |
|           |         | $        $     |
| $\si{d}$  | deci    | $10^{-1} $     |
| $\si{c}$  | centi   | $10^{-2} $     |
| $\si{m}$  | milli   | $10^{-3} $     |
| $\mu$     | micro   | $10^{-6} $     |
| $\si{n}$  | nano    | $10^{-9} $     |
| $\si{p}$  | pico    | $10^{-12}$     |

Deze tabel **moet je uit je hoofd kennen**... Je moet voor elke prefix weten
welke macht van 10 ermee overeenkomt en voor elke macht van 10 moet je weten
welke prefix ermee overeenkomt. Je moet dus bijvoorbeeld weten dat je $-0{,}53
\orange{\si{ h}} \si{N}$ ook kan schrijven als $-0{,}53 \cdot \orange{10^2}
\si{ N}$. En dat je $184 \cdot \orange{10^{-12}} \si{ m}$ kan schrijven als
$184 \orange{\si{ p}} \si{m}$.

## Prefixen wegwerken
Voor grote afstanden maken we vaak gebruik van de kilometer ($\si{km}$). De [SI-eenheid](../intro#si-eenheden-maken-duidelijke-afspraken) van afstand is echter de meter ($\si{m}$). We moeten daarom vaak $\si{km}$ omzetten naar $\si{m}$. In de tabel hierboven zien we dat die $\si{k}$ hetzelfde is als $10^{3}$. Voor het omzetten van $\si{km}$ naar $\si{m}$ moet je dan gewoon de $\si{k}$ vervangen door $10^{3}$.

Bijvoorbeeld: de afstand tussen Brussel en Amsterdam is ongeveer $173{,}89 \si{ km}$ in vogelvlucht. Zet dit om naar de juiste SI-eenheid.

\begin{split}
173{,}89 \orange{\si{ k}}\si{m}
= 173{,}89 \cdot \orange{10^3}\si{ m}
\end{split}

## Prefixen toevoegen
De [SI-eenheid](../intro#si-eenheden-maken-duidelijke-afspraken) van massa is de kilogram ($\si{kg}$). Vaak wordt een massa echter ook uitgedrukt in gram ($\si{g}$). Als we een massa in $\si{g}$ moeten omzetten naar de SI-eenheid $\si{kg}$, zullen we dus een prefix moeten *toevoegen*. Omdat elke prefix een macht van 10 voorstelt, is het toevoegen van een prefix hetzelfde als het toevoegen van een macht van 10. In het geval van $\si{g}$ omzetten naar $\si{kg}$, moeten we een $\si{k}$ toevoegen of dus $10^3$. In de [les over machten van 10](../machten_van_10#machten-van-10-omzetten) zagen we hoe we zo'n $10^3$ konden toevoegen zonder de waarde van een getal te veranderen.

Bijvoorbeeld: voor een bepaald recept heb je $250 \si{ g}$ bloem nodig. Zet dit om naar de juiste SI-eenheid.

\begin{split}
250\si{ g}
&= 250 \cdot \orange{10^{-3}} \cdot \blue{10^3} \si{ g}\\\\\
&= 250 \cdot \orange{10^{-3}} \blue{\si{ k}} \si{g}\\\\\
&= \orange{0{,}250} \blue{\si{ k}} \si{g}\\\\\
\end{split}


## Prefixen omzetten
Eens je weet welke prefix overeenkomt met welke macht van 10 (en omgekeerd), is het omzetten van prefixen hetzelfde als het [omzetten van machten van 10](../machten_van_10#machten-van-10-omzetten).
Het enige wat je extra moet doen is het omzetten van prefixen naar machten van 10 en terug.

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
{{< mute "(kubieke meter)" >}}. 
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
