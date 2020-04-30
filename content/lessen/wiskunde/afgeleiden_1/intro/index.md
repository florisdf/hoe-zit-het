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

In deze paragraaf gaan we deze formule op een iets wiskundigere manier leren 
schrijven zodat de formule niet enkel toepasbaar is voor het berekenen van 
*gemiddelde snelheid*, maar ook voor het berekenen van **gemiddelde 
verandering** in het algemeen. Gemiddelde snelheid is namelijk een soort van
gemiddelde verandering. Die formule voor gemiddelde verandering ziet er zo 
uit:

$$\text{gem. verandering} = \frac{\orange{\Delta y}}{\blue{\Delta x}}$$

We zullen de formule ook wel als volgt schrijven:

$$\text{gem. verandering} = \frac{\orange{\Delta f(x)}}{\blue{\Delta x}}$$

Eens we die formule goed begrijpen, zullen we een naadloze overgang kunnen 
maken naar afgeleiden! 🏄‍♀️

### Gemiddelde snelheid berekenen van start tot finish

Om de gemiddelde snelheid van Maria te berekenen, moeten we weten **hoeveel
afstand** ze heeft afgelegd in **welke tijd**. We weten dat een dragrace altijd
over een afstand van $300~\si{m}$ gaat. Op de luchtfoto net voor Maria over de
finish ging, kunnen we zien wat haar tijd tot de finish was:

{{< svg "img/maria_avg_speed.svg" "Gemiddelde snelheid van Maria voor de volledige race berekenen." >}}

Wanneer Maria over de finish rijdt ($\orange{300~\si{m}}$), zien we dat de
chronometer $\blue{3{,}87~\si{s}}$ aangeeft. Haar 
**gemiddelde snelheid voor de volledige race** is dus:

\begin{split}
    \text{gem. snelheid} &= \frac{\orange{afstand}}{\blue{tijd}}\\\\\
                         &= \frac{\orange{300~\si{m}}}{\blue{3{,}87~\si{s}}}\\\\\
                         &= 77{,}5~\si{m/s}
\end{split}

Uit onze [les fysica over het omzetten van
eenheden](../../../fysica/grootheden_eenheden/eenheden_omzetten) weten we dat
$1~\si{m/s} = 3{,}6~\si{km/h}$. Maria had dus een gemiddelde snelheid van

$$77{,}5\cdot3{,}6~\si{km/h} = 279~\si{km/h}$$

Lekker snel! :rocket:

Kunnen we ook haar gemiddelde snelheid berekenen
voor de **laatste $100~\si{m}$**? Daarvoor moeten we ook weer haar **afgelegde
afstand delen door de tijd** die ze nodig had om die afstand af te leggen.

{{< svg "img/maria_avg_speed_last_100.svg" "Gemiddelde snelheid van Maria voor de laatste 100 m berekenen" >}}

Ze rijdt van $\orange{200~\si{m}}$ naar $\orange{300~\si{m}}$. Dat betekent dat
ze inderdaad $\orange{100~\si{m}}$ heeft afgelegd:

\begin{split}
    \orange{\text{afstand}} &= \orange{300~\si{m}} - \orange{200~\si{m}}\\\\\
                            &= \orange{100~\si{m}}
\end{split}

Je ziet dat we de afgelegde afstand berekenen door het **verschil te nemen
tussen de eind- en beginpositie**. Haar eindpositie was $\orange{300~\si{m}}$ 
en haar beginpositie was $\orange{200~\si{m}}$.


Bij $\orange{200~\si{m}}$ stond de chronometer op $\blue{3{,}16~\si{s}}$ en bij
$\orange{300~\si{m}}$ stond de chronometer op $\blue{3{,}87~\si{s}}$. Ze had
dus $\blue{0{,}71~\si{s}}$ nodig:

\begin{split}
    \blue{\text{tijd}} &= \blue{3{,}87~\si{s}} - \blue{3{,}16~\si{s}}\\\\\
                       &= \blue{0{,}71~\si{s}}
\end{split}

Haar **gemiddelde snelheid voor de laatste $100~\si{m}$** is dus:

\begin{split}
    \text{gem. snelheid}  &= \frac{\orange{afstand}}{\blue{tijd}}\\\\\
                          &= \frac{\orange{300~\si{m}} - \orange{200~\si{m}}}{\blue{3{,}87~\si{s}} - \blue{3{,}16~\si{s}}}\\\\\
                         &= \frac{\orange{100~\si{m}}}{\blue{0{,}71~\si{s}}}\\\\\
                         &= 141~\si{m/s}\\\\\
                         &= 507~\si{km/h}
\end{split}

In onderstaande applet kan je de gemiddelde snelheden laten berekenen voor 
andere begin- en eindposities. 

(applet)

## Differentiequotiënt

## Gemiddeld vs. ogenblikkelijk

De **gemiddelde verandering** van een functie is zoals de gemiddelde snelheid. Je wilt te weten komen hoeveel een functie veranderd is over een interval. Dit kan je zelf kiezen: bijvoorbeeld $a = 2$ tot $b = 5$. De gemiddelde verandering vind je dan door ook de functie waarden op deze positie te gebruiken:

$$ \frac{\Delta f(x)}{\Delta x} = \frac {f(b) - f(a)}{b - a} $$

De **ogenblikkelijke verandering** van een functie is zoals de ogenblikkelijke snelheid. Het geeft weer hoe snel een functie op die plaats veranderd. Die vind je door het tijdsinterval in de vorige formule heel klein te maken. In wiskunde termen: de limiet van $\Delta x$ naar $0$. Dit is ook de definitie van **de afgeleide**, aangegeven met het symbool $f'(x)$.

$$ f'(x) = \lim_{\Delta x \rightarrow 0} \frac{\Delta f(x)}{\Delta x} $$


## Samengevat

{{% attention "Wat is een afgeleide?" %}}
Dit is een afgeleide!
{{% /attention %}}
