---
title: "Wat is een afgeleide?"
date: 2020-03-10T16:35:11+02:00
weight: 1
draft: true
tags: ["afgeleide", "differentiequotiënt", "gemiddelde verandering",
"ogenblikkelijke verandering", "snelheid", "wat betekent delta"]
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
gemiddelde snelheid leert ons niets over hoe snel de wagen bijvoorbeeld reed
wanneer hij voorbij een flitspaal reed. Soms zijn we echter wel geïnteresseerd
in de **snelheid op een bepaald tijdstip** of de **ogenblikkelijke snelheid**.
In deze les leren we voor het eerst over **afgeleiden**. Een afgeleide is
eigenlijk een veralgemening van die *ogenblikkelijke snelheid*.  Met behulp
van een afgeleide zullen we vragen als "Met welke snelheid reed de wagen
voorbij de flitspaal?" wél kunnen beantwoorden.


## Dragracen met Maria en Dirk

Als voorbeeld voor deze les, gaan we een van de favoriete hobby's van Maria en
Dirk gebruiken: dragracen.  Bij dragracen vertrekken twee wagens vanuit
stilstand en racen ze $300~\si{m}$ in een rechte lijn. De eerste aan de finish
wint.

{{< svg "img/drag_racing.svg" "Maria racet en is bijna aan de finish." >}}

De wagens halen enorme snelheden tot meer dan $500~\si{km/h}$. Hieronder zie je
enkele luchtfoto's van Maria in haar *Top Fuel dragster* tijdens het dragracen.

{{< svg "img/maria_race_top.svg" "Luchtfoto's van Maria tijdens haar race." >}}

We gaan in deze les twee vragen proberen beantwoorden over de dragrace die je
hierboven op de luchtfoto's ziet:

1. Wat was de **gemiddelde snelheid** van Maria?
2. Met welke snelheid reed Maria **over de eindmeet**?


## Gemiddelde snelheid berekenen

We weten al dat we een gemiddelde 
snelheid kunnen berekenen door de **afgelegde afstand**
{{< mute "(hoeveel (kilo)meter?)" >}} te delen door de **tijd die nodig 
was** {{< mute "(hoeveel uur of seconden?)" >}} om die afstand af te leggen:

\begin{split}
    \text{gem. snelheid} &= \frac{\orange{\text{afgelegde afstand} }}{\blue{\text{tijd die nodig was}}}\\\\\
\end{split}

In de volgende paragrafen gaan we deze formule op een iets wiskundigere 
manier leren 
schrijven zodat de formule niet enkel toepasbaar is voor het berekenen van 
*gemiddelde snelheid*, maar ook voor het berekenen van **gemiddelde 
verandering van een functie** in het algemeen. Gemiddelde snelheid is 
namelijk een soort van gemiddelde verandering. We zullen leren dat die formule voor gemiddelde verandering van een functie er zo uitziet:

$$\text{gem. verandering v.e. functie} = \frac{\orange{\Delta y}}{\blue{\Delta x}}$$

Die formule zullen we nadien ook schrijven als:

$$\text{gem. verandering v.e. functie} = \frac{\orange{\Delta f(x)}}{\blue{\Delta x}}$$

Eens we die laatste formule goed begrijpen, gaan we een naadloze overgang 
kunnen maken naar afgeleiden! 🏄‍♀️

## Gemiddelde snelheid als een breuk van twee verschillen

Stel dat we Maria haar gemiddelde snelheid willen berekenen
tussen $1{,}00~\si{s}$ en $3{,}00\si{s}$.

{{< svg "img/maria_avg_speed_last_100.svg" "Gemiddelde snelheid van Maria voor de laatste 100 m berekenen" >}}

Wanneer de chronometer op $\blue{1{,}00~\si{s}}$ stond, was Maria
$\orange{20~\si{m}}$ ver. Bij $\blue{3{,}00~\si{s}}$, was ze
$\orange{180~\si{m}}$ ver. De gemiddelde snelheid tussen $\blue{1{,}00~\si{s}}$ en
$\blue{3{,}00~\si{s}}$ is dus:

\begin{split}
    \text{gem. snelheid} &= \frac{\orange{\text{afgelegde afstand} }}{\blue{\text{tijd die nodig was}}}\\\\\
                         &= \frac{\orange{180~\si{m}} - \orange{20~\si{m}}}{\blue{3{,}00~\si{s}} - \blue{1{,}00~\si{s}}}\\\\\
                         &= \frac{\orange{160~\si{m}}}{\blue{2{,}00~\si{s}}}\\\\\
                         &= 80{,}0~\si{m/s}\\\\\
                         &= 288~\si{km/h}
\end{split}

Lekker snel! 🚀

Je ziet dat we voor de afgelegde afstand en de tijd die nodig was telkens
een **verschil** berekenen. Voor de afstand is dat het **verschil
tussen de tweede positie** ($\orange{180~\si{m}}$) **en de eerste positie**
($\orange{20~\si{m}}$). Voor de tijd is dat het **verschil tussen de 
tweede tijd** ($\blue{3{,}00~\si{s}}$) **en de eerste tijd**
($\blue{1{,}00~\si{s}}$).

We kunnen onze formule voor gemiddelde snelheid dus ook schrijven als:

$$\text{gem. snelheid} = \frac{\orange{\text{positie}\_2} - \orange{\text{positie}\_1}}{\blue{\text{tijd}\_2} - \blue{\text{tijd}\_1}}$$

Dit noemen we een **differentiequotiënt**. Wat een *monster* van een woord! 
🐉 Het woord bestaat uit twee stukken:

1. *differentie-*: iets met een *aftrekking* of *verschil*, denk maar aan het Engelse woord *difference*
2. *-quotiënt*: moeilijk woord voor een *deling* of een *breuk*

Letterlijk "vertaald" is een *differentiequotiënt* dus een *verschilbreuk* of
met andere woorden een **breuk met in de teller en de noemer een verschil**.
Bij gemiddelde snelheid staat er in de teller een verschil van posities en in
de noemer een verschil van tijden. In de volgende paragraaf gaan we dieper in
op *differentiequotiënten*.

## Differentiequotiënt en gemiddelde verandering van een functie

In de vorige paragraaf leerden we dat gemiddelde snelheid een 
**differentiequotiënt** van positie en tijd is en dat we gemiddelde snelheid
als volgt kunnen berekenen:

$$\text{gem. snelheid} = \frac{\orange{\text{positie}\_2} - \orange{\text{positie}\_1}}{\blue{\text{tijd}\_2} - \blue{\text{tijd}\_1}}$$

In deze paragraaf leren we de algemene formule van een differentiequotiënt en
dat we daarmee de **gemiddelde verandering van een functie** kunnen berekenen.
Eerst gaan we even terug naar de dragrace van Maria. Daar berekenden we de
gemiddelde snelheid tussen $\blue{1{,}00\si{s}}$ en $\blue{3{,}00\si{s}}$ als
volgt:

$$\frac{\orange{180~\si{m}} - \orange{20~\si{m}}}{\blue{3{,}00~\si{s}} - \blue{1{,}00~\si{s}}}$$

We kunnen de race van Maria eigenlijk ook zien als een **functie** waarbij $x$
de **tijd** is die de chronometer aangeeft en $y$ de **positie** van Maria op
het tijdstip $x$. Op de luchtfoto's kunnen we inderdaad zien dat ze een mooie
functie vormen:

(illustratie)

## Gemiddeld vs. ogenblikkelijk

De **gemiddelde verandering** van een functie is zoals de gemiddelde snelheid. Je wilt te weten komen hoeveel een functie veranderd is over een interval. Dit kan je zelf kiezen: bijvoorbeeld $a = 2$ tot $b = 5$. De gemiddelde verandering vind je dan door ook de functie waarden op deze positie te gebruiken

$$ \frac{\Delta f(x)}{\Delta x} = \frac {f(b) - f(a)}{b - a} $$

De **ogenblikkelijke verandering** van een functie is zoals de ogenblikkelijke snelheid. Het geeft weer hoe snel een functie op die plaats veranderd. Die vind je door het tijdsinterval in de vorige formule heel klein te maken. In wiskunde termen: de limiet van $\Delta x$ naar $0$. Dit is ook de definitie van **de afgeleide**, aangegeven met het symbool $f'(x)$.

$$ f'(x) = \lim_{\Delta x \rightarrow 0} \frac{\Delta f(x)}{\Delta x} $$


## Samengevat

{{% attention "Wat is een afgeleide?" %}}
Dit is een afgeleide!
{{% /attention %}}
