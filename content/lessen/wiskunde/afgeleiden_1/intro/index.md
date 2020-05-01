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
in de **snelheid op een bepaald tijdstip**. In deze les leren we voor het eerst
over **afgeleiden**. Een afgeleide is eigenlijk een veralgemening van die
**ogenblikkelijke snelheid**.  Met behulp van een afgeleide zullen we vragen
als "Met welke snelheid reed de wagen voorbij de flitspaal?" wél kunnen
beantwoorden.


## Dragracen met Maria

Als voorbeeld voor deze les, gaan we een van de favoriete hobby's van Maria 
gebruiken: dragracen.  Bij dragracen vertrekken twee wagens vanuit stilstand 
en racen ze $300~\si{m}$ in een rechte lijn. De eerste aan de finish wint.

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
verandering van een functie**. We zullen leren dat die formule voor 
gemiddelde verandering van een functie er zo uitziet:

$$\text{gem. verandering v.e. functie} = \frac{\orange{\Delta f(x)}}{\blue{\Delta x}}$$

Die breuk zullen we het **differentiequotiënt** noemen. Moeilijk woord, maar 
geen paniek! We gaan het je stap voor stap uitleggen. Eens we dat 
differentiequotiënt goed begrijpen, zullen we een naadloze overgang kunnen 
maken naar afgeleiden! 🏄‍♀️

## Gemiddelde snelheid als een breuk van twee verschillen

Stel dat we Maria haar gemiddelde snelheid willen berekenen
tussen $\blue{1{,}00~\si{s}}$ en $\blue{3{,}00~\si{s}}$.

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
($\blue{1{,}00~\si{s}}$). Die twee verschillen zetten we vervolgens in een 
**breuk** met in de teller het verschil van posities en in de noemer het 
verschil van tijden.


## Gemiddelde snelheid veralgemenen naar gemiddelde verandering

We kunnen de race van Maria zien als een **functie** waarbij
$\blue{x}$ de **tijd** is die de chronometer aangeeft en $\orange{f(x)}$ de 
**positie** van Maria op het tijdstip $\blue{x}$. Op de luchtfoto's kunnen we 
inderdaad zien dat de foto's een mooie [grafiek van een functie](../../functies/grafiek) vormen:

(illustratie)

In onze berekening voor gemiddelde snelheid zijn $\blue{1{,}00~\si{s}}$ en 
$\blue{3{,}00~\si{s}}$ dus allebei $x-$waarden. We zullen ze $\blue{x\_1}$ en $\blue{x\_2}$ noemen waarbij

\begin{split}
    \blue{x\_1} &= \blue{1{,}00~\si{s}}\\\\\
    \blue{x\_2} &= \blue{3{,}00~\si{s}}
\end{split}

In de teller van onze berekening voor gemiddelde snelheid staan de posities 
$\orange{20~\si{m}}$ en $\orange{180~\si{m}}$. Dat zijn de posities waar
Maria was toen de chronometer op $\blue{x\_1} = \blue{1{,}00~\si{s}}$ en
$\blue{x\_2} = \blue{3{,}00~\si{s}}$ stond. Op de grafiek van de functie, 
zien we inderdaad dat de **posities de functiewaarden zijn van de tijden op 
de chronometer**:

(illustratie)

We kunnen dus zeggen dat:

\begin{split}
    \orange{f(x\_1)} &= \orange{20~\si{m}}\\\\\
    \orange{f(x\_2)}  &= \orange{180~\si{m}}
\end{split}

Als we onze berekening voor gemiddelde snelheid met deze 
$\blue{x\_1}$, $\blue{x\_2}$, $\orange{f(x\_1)}$ en $\orange{f(x\_2)}$  
schrijven, krijgen we:

$$\text{gem. snelheid} = \frac{\orange{f(x\_2)} - \orange{f(x\_1)}}{\blue{x\_2} - \blue{x\_1}}$$

Met deze formule kunnen we nog steeds de gemiddelde snelheid berekenen, maar
**nog veel meer dan enkel dat**! Deze breuk geeft ons de 
**gemiddelde verandering van een functie**. Het zegt hoeveel 
[de functiewaarde](../../functies/functiewaarde) gemiddeld verandert wanneer 
de $x-$waarde verandert van $\blue{x\_1}$ naar $\blue{x\_2}$.

(illustratie met enkel grafiek van functie, zonder racewagen)

## Het differentiequotiënt

We zagen in de vorige paragraaf dat we de gemiddelde verandering van een functie tussen twee $x-$waarden kunnen berekenen met de volgende breuk:

$$\text{gem. verandering v.e. functie} = \frac{\orange{f(x\_2)} - \orange{f(x\_1)}}{\blue{x\_2} - \blue{x\_1}}$$

Zo'n breuk noemen we een **differentiequotiënt**. In de noemer van het 
differentiequotiënt staat het verschil van twee $x-$waarden en in de teller 
het verschil van de bijhorende functiewaarden.

Nu denk je misschien: "Een differ-**watte**?! 🤨" Waar komt die 
naam vandaan? Het woord bestaat uit twee stukken:

1. **differentie-**: moeilijk woord voor een *aftrekking* of *verschil*, denk 
   maar aan het Engelse woord *difference*. Dit wijst erop dat er een 
   **verschil wordt berekend** in de teller en noemer.
2. **-quotiënt**: moeilijk woord voor een *deling* of een *breuk*. Dit wijst
   op het feit dat **het ene verschil wordt gedeeld door het andere**.

## Het verschil afkorten met $\Delta$

Om niet elke keer "$\orange{f(x\_2)} - \orange{f(x\_1)}$" en "$\blue{x\_2} - 
\blue{x\_1}$" languit te moeten schrijven in het differentiequotiënt, 
gebruiken we een afkorting met de Griekse hoofdletter $\Delta$ (de delta):

\begin{split}
    \blue{\Delta x} &= \blue{x\_2} - \blue{x\_1}\\\\\
    \orange{\Delta f(x)} &= \orange{f(x\_2)} - \orange{f(x\_1)}
\end{split}

Die "$\Delta$" is niets meer dan een afkorting om niet telkens die aftrekking
voluit te moeten schrijven. Met behulp van deze $\Delta$, kunnen we het 
differentiequotiënt veel korter schrijven:

$$\text{gem. verandering v.e. functie} = \frac{\orange{\Delta f(x)}}{\blue{\Delta x}}$$

## Gemiddeld vs. ogenblikkelijk

De **gemiddelde verandering** van een functie is zoals de gemiddelde snelheid. Je wilt te weten komen hoeveel een functie veranderd is over een interval. Dit kan je zelf kiezen: bijvoorbeeld $a = 2$ tot $b = 5$. De gemiddelde verandering vind je dan door ook de functie waarden op deze positie te gebruiken

$$ \frac{\Delta f(x)}{\Delta x} = \frac {f(b) - f(a)}{b - a} $$

De **ogenblikkelijke verandering** van een functie is zoals de ogenblikkelijke snelheid. Het geeft weer hoe snel een functie op die plaats veranderd. Die vind je door het tijdsinterval in de vorige formule heel klein te maken. In wiskunde termen: de limiet van $\Delta x$ naar $0$. Dit is ook de definitie van **de afgeleide**, aangegeven met het symbool $f'(x)$.

$$ f'(x) = \lim_{\Delta x \rightarrow 0} \frac{\Delta f(x)}{\Delta x} $$


## Samengevat

{{% attention "Wat is een afgeleide?" %}}
Dit is een afgeleide!
{{% /attention %}}
