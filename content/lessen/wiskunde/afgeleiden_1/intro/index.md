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
    \text{gem. snelheid} &= \frac{\green{\text{afgelegde afstand} }}{\orange{\text{tijd die nodig was}}}\\\\\
\end{split}

In de volgende paragrafen gaan we deze formule op een iets wiskundigere 
manier leren 
schrijven zodat de formule niet enkel toepasbaar is voor het berekenen van 
*gemiddelde snelheid*, maar ook voor het berekenen van **gemiddelde 
verandering van een functie**. We zullen leren dat die formule voor 
gemiddelde verandering van een functie er zo uitziet:

$$\text{gem. verandering v.e. functie} = \frac{\green{\Delta f(x)}}{\orange{\Delta x}}$$

Die breuk zullen we het **differentiequotiënt** noemen. Moeilijk woord, maar 
geen paniek! We gaan het je stap voor stap uitleggen. Eens we dat 
differentiequotiënt goed begrijpen, zullen we een naadloze overgang kunnen 
maken naar afgeleiden! 🏄‍♀️

## Gemiddelde snelheid als een breuk van twee verschillen

Stel dat we Maria haar gemiddelde snelheid willen berekenen
tussen $\orange{1{,}00~\si{s}}$ en $\orange{3{,}00~\si{s}}$.

{{< svg "img/maria_avg_speed_1s_3s.svg" "Gemiddelde snelheid van Maria tussen 1 s en 3 s berekenen" >}}

Wanneer de chronometer op $\orange{1{,}00~\si{s}}$ stond, was Maria
$\green{20~\si{m}}$ ver. Bij $\orange{3{,}00~\si{s}}$, was ze
$\green{180~\si{m}}$ ver. De gemiddelde snelheid tussen $\orange{1{,}00~\si{s}}$ en
$\orange{3{,}00~\si{s}}$ is dus:

\begin{split}
    \text{gem. snelheid} &= \frac{\green{\text{afgelegde afstand} }}{\orange{\text{tijd die nodig was}}}\\\\\
                         &= \frac{\green{180~\si{m}} - \green{20~\si{m}}}{\orange{3{,}00~\si{s}} - \orange{1{,}00~\si{s}}}\\\\\
                         &= \frac{\green{160~\si{m}}}{\orange{2{,}00~\si{s}}}\\\\\
                         &= 80{,}0~\si{m/s}\\\\\
                         &= 288~\si{km/h}
\end{split}

Lekker snel! 🚀

Je ziet dat we voor de afgelegde afstand en de tijd die nodig was telkens
een **verschil** berekenen. Voor de afstand is dat het **verschil
tussen de tweede positie** ($\green{180~\si{m}}$) **en de eerste positie**
($\green{20~\si{m}}$). Voor de tijd is dat het **verschil tussen de 
tweede tijd** ($\orange{3{,}00~\si{s}}$) **en de eerste tijd**
($\orange{1{,}00~\si{s}}$). Die twee verschillen zetten we vervolgens in een 
**breuk** met in de teller het verschil van posities en in de noemer het 
verschil van tijden.


## Gemiddelde snelheid veralgemenen naar gemiddelde verandering

We kunnen de race van Maria zien als een **functie** waarbij
$\orange{x}$ de **tijd** is die de chronometer aangeeft en $\green{f(x)}$ de 
**positie** van Maria op het tijdstip $\orange{x}$. Op de luchtfoto's kunnen we 
inderdaad zien dat de foto's een mooie [grafiek van een functie](../../functies/grafiek) vormen:

{{< svg "img/maria_race_function.svg" "De positie van Maria als functie van de tijd" >}}

In onze berekening voor gemiddelde snelheid zijn $\orange{1{,}00~\si{s}}$ en 
$\orange{3{,}00~\si{s}}$ dus allebei $x-$waarden. We zullen ze $\orange{x\_1}$ en $\orange{x\_2}$ noemen waarbij

\begin{split}
    \orange{x\_1} &= \orange{1{,}00~\si{s}}\\\\\
    \orange{x\_2} &= \orange{3{,}00~\si{s}}
\end{split}

In de teller van onze berekening voor gemiddelde snelheid staan de posities 
$\green{20~\si{m}}$ en $\green{180~\si{m}}$. Dat zijn de posities waar
Maria was toen de chronometer op $\orange{x\_1} = \orange{1{,}00~\si{s}}$ en
$\orange{x\_2} = \orange{3{,}00~\si{s}}$ stond. Op de grafiek van de functie, 
zien we inderdaad dat de **posities de functiewaarden zijn van de tijden op 
de chronometer**:

{{< svg "img/race_positie_fx_waarde.svg" "De posities zijn functiewaarden van de tijd." >}}

We kunnen dus zeggen dat:

\begin{split}
    \green{f(x\_1)} &= \green{20~\si{m}}\\\\\
    \green{f(x\_2)}  &= \green{180~\si{m}}
\end{split}

Als we onze berekening voor gemiddelde snelheid met deze 
$\orange{x\_1}$, $\orange{x\_2}$, $\green{f(x\_1)}$ en $\green{f(x\_2)}$
schrijven, krijgen we:

$$\frac{\green{f(x\_2)} - \green{f(x\_1)}}{\orange{x\_2} - \orange{x\_1}}$$

Dit is de formule van het **differentiequotiënt**. Hier gaan we in de volgende
paragraaf verder op in.

## Het differentiequotiënt

In de vorige paragraaf schreven we onze berekening voor de gemiddelde snelheid
als het **differentiequotiënt**:

{{< svg "img/diff_quot_intuitie.svg" "Intuïtie achter formule van differentiequotiënt" >}}

Vertaald naar woorden zegt deze formule:

* Hoeveel verandert de $\green{\text{functiewaarde}}$ gemiddeld
  $\orange{\text{per x-eenheid}}$ tussen $\orange{x\_1}$ en $\orange{x\_2}$?
* Of: Wat is de **gemiddelde functieverandering** tussen $\orange{x\_1}$ en
  $\orange{x\_2}$?

Voor de race van Maria kunnen we dat vertalen als:

* Hoeveel verandert de $\green{\text{positie van Maria}}$ gemiddeld
  $\orange{\text{per seconde}}$ tussen tijd $\orange{x\_1}$ en tijd
  $\orange{x\_2}$?
* Of: Wat is de **gemiddelde snelheid** tussen tijd $\orange{x\_1}$ en tijd
  $\orange{x\_2}$?

Nu denk je misschien: "Een differ-**watte**?! 🤨" Waar komt die 
naam vandaan? Het woord bestaat uit twee stukken:

1. **differentie-**: moeilijk woord voor een *aftrekking* of *verschil*, denk 
   maar aan het Engelse woord *difference*. Dit wijst erop dat er een 
   **verschil wordt berekend** in de teller en noemer.
2. **-quotiënt**: moeilijk woord voor een *deling* of een *breuk*. Dit wijst
   op het feit dat **het ene verschil wordt gedeeld door het andere**.

## Het verschil afkorten met $\Delta$

Om niet elke keer "$\green{f(x\_2)} - \green{f(x\_1)}$" en "$\orange{x\_2} - 
\orange{x\_1}$" languit te moeten schrijven in het differentiequotiënt, 
gebruiken we een afkorting met de Griekse hoofdletter $\Delta$ (de delta):

\begin{split}
    \orange{\Delta x} &= \orange{x\_2} - \orange{x\_1}\\\\\
    \green{\Delta f(x)} &= \green{f(x\_2)} - \green{f(x\_1)}
\end{split}

Die "$\Delta$" is niets meer dan een afkorting om niet telkens die aftrekking
voluit te moeten schrijven. Met behulp van deze $\Delta$, kunnen we het 
differentiequotiënt veel korter schrijven:

$$\text{gem. verandering v.e. functie} = \frac{\green{\Delta f(x)}}{\orange{\Delta x}}$$

## Gemiddeld vs. ogenblikkelijk

De **gemiddelde verandering** van een functie is zoals de gemiddelde snelheid. Je wilt te weten komen hoeveel een functie veranderd is over een interval. Dit kan je zelf kiezen: bijvoorbeeld $a = 2$ tot $b = 5$. De gemiddelde verandering vind je dan door ook de functie waarden op deze positie te gebruiken

$$ \frac{\Delta f(x)}{\Delta x} = \frac {f(b) - f(a)}{b - a} $$

De **ogenblikkelijke verandering** van een functie is zoals de ogenblikkelijke snelheid. Het geeft weer hoe snel een functie op die plaats veranderd. Die vind je door het tijdsinterval in de vorige formule heel klein te maken. In wiskunde termen: de limiet van $\Delta x$ naar $0$. Dit is ook de definitie van **de afgeleide**, aangegeven met het symbool $f'(x)$.

$$ f'(x) = \lim_{\Delta x \rightarrow 0} \frac{\Delta f(x)}{\Delta x} $$


## Samengevat

{{% attention "Wat is een afgeleide?" %}}
Dit is een afgeleide!
{{% /attention %}}
