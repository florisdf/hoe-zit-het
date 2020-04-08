---
title: "Wat is een afgeleide?"
date: 2020-03-10T16:35:11+02:00
weight: 1
draft: true
tags: ["afgeleide", "differentiequotiënt", "gemiddelde verandering",
"ogenblikkelijke verandering", "snelheid"]
description: "Met afgeleiden berekenen we ogenblikkelijke veranderingen. In
deze les leren we de formule om zo'n afgeleide te berekenen. We bouwen stap per
stap op naar deze definitie en gaan van gemiddelde snelheid naar
differentiequotiënt om ten slotte bij afgeleiden te eindigen. Zodat begrijp je
aan het einde van de les helemaal waar de definitie van afgeleiden vandaan
komt."
images: []
---

Je kan waarschijnlijk al een gemiddelde snelheid berekenen. Een wagen rijdt
bijvoorbeeld $100~\si{km}$ in $2~\si{h}$, dan reed hij gemiddeld
$50~\si{km/h}$. Dat betekent echter **niet dat de wagen voortdurend
$50~\si{km/h}$ reed**. Soms reed hij waarschijnlijk iets sneller, soms iets
trager, soms stond de wagen misschien even stil voor een rood licht... Die
gemiddelde snelheid leert ons niets over hoe snel de wagen bijvoorbeeld reed om
16u30. Soms zijn we echter wel geïnteresseerd in de **snelheid op een bepaald
tijdstip**. In deze les leren we voor het eerst over **afgeleiden**. Een
afgeleide is eigenlijk een veralgemening van die **ogenblikkelijke snelheid**.
Met behulp van een afgeleide zullen we vragen als "Hoe snel reed de wagen om
16u30?" wél kunnen beantwoorden.


# Dragracen met Maria en Dirk

Als voorbeeld voor deze les, gaan we een van de favoriete hobby's van Maria en
Dirk gebruiken: dragracen.  Bij dragracen vertrekken twee wagens vanuit
stilstand en racen ze $300~\si{m}$ in een rechte lijn. De eerste aan de finish
wint.

{{< svg "img/drag_racing.svg" "Maria en Dirk die tegen elkaar dragracen en bijna aan de finish zijn." >}}

De wagens halen enorme snelheden tot meer dan $500~\si{km/h}$. Hieronder zie je
enkele luchtfoto's van Maria in haar *Top Fuel dragster* tijdens het dragracen.

(functie $f(x) = 20x^2$ met x in seconden en y in meter)

In deze les gaan we twee vragen proberen beantwoorden: wat was de **gemiddelde
snelheid** van Maria en **met welke snelheid reed ze over de eindmeet**?


## Gemiddelde snelheid

Door het verschil van de eindtijd en de begintijd te nemen, kunnen we voor
Dirk en Maria berekenen **hoe lang** ze beiden hebben gelopen:

(illustratie)

We noteren dit voor Dirk als:

$$t\_{eind,D} - t\_{begin,D} = 45~\si{s} - 20~\si{s} = 25~\si{s}$$


En voor Maria als:
$$t\_{eind,M} - t\_{begin,M} = 48~\si{s} - 20~\si{s} = 28~\si{s}$$

Of korter:

$$\Delta t\_D = 45~\si{s} - 20~\si{s} = 25~\si{s}$$
$$\Delta t\_{M} = 48~\si{s} - 20~\si{s} = 28~\si{s}$$


{{< expand "Wat is die $\Delta$?" >}}

Het symbool "$\Delta$" (een Griekse *delta*), gebruiken we om een *verschil*
korter te schrijven. Het betekent gewoon "het verschil van het einde en het
begin".

In plaats van $t\_{eind} - t\_{begin}$ kunnen we dus veel korter schrijven $\Delta t$:


$t\_{eind} - t\_{begin} = \Delta t$

{{< /expand >}}

Dirk liep dus $100~\si{m}$ in $25~\si{s}$ en Maria liep $100~\si{m}$ in
$28~\si{s}$.

Hun **gemiddelde snelheid** vinden we door hun **afgelegde
afstand te delen door de tijd** die ze nodig hadden:

$$v\_{gem} = \frac{x\_{einde} - x\_{begin}}{t\_{einde} - t\_{begin}}$$

Voor Dirk wordt dit:

$$v_{gem, D} = \frac{100~\si{m} - 0~\si{m}}{25~\si{s}}$$

Als Dirk zijn gemiddelde snelheid berekent doet hij dit over een tijdsinterval, bijvoorbeeld tussen de starttijd en de eindtijd. Maar met de formule kan je over elk tijdsinterval de gemiddelde snelheid berekenen.

Als we nu dit tijdsinterval heel klein maken spreken we niet meer van een gemiddelde snelheid, maar van een **ogenblikkelijke snelheid**. De snelheid die onze lopers op een bepaald tijdstip hadden.

## Gemiddeld vs. ogenblikkelijk

De **gemiddelde verandering** van een functie is zoals de gemiddelde snelheid. Je wilt te weten komen hoeveel een functie veranderd is over een interval. Dit kan je zelf kiezen: bijvoorbeeld $a = 2$ tot $b = 5$. De gemiddelde verandering vind je dan door ook de functie waarden op deze positie te gebruiken:

$$ \frac{\Delta f(x)}{\Delta x} = \frac {f(b) - f(a)}{b - a} $$

De **ogenblikkelijke verandering** van een functie is zoals de ogenblikkelijke snelheid. Het geeft weer hoe snel een functie op die plaats veranderd. Die vind je door het tijdsinterval in de vorige formule heel klein te maken. In wiskunde termen: de limiet van $\Delta x$ naar $0$. Dit is ook de definitie van **de afgeleide**, aangegeven met het symbool $f'(x)$.

$$ f'(x) = \lim_{\Delta x \rightarrow 0} \frac{\Delta f(x)}{\Delta x} $$


## Samengevat

{{% attention "Wat is een afgeleide?" %}}
Dit is een afgeleide!
{{% /attention %}}
