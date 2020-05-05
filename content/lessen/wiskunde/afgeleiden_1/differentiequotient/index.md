---
title: "Wat is een differentiequotiënt?"
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

Vooraleer we aan afgeleiden kunnen beginnen, moeten we het
**differentiequotiënt** begrijpen. Wat een monster van een woord! 🦕 Maar geen
paniek. We gaan het stap voor stap uitleggen aan de hand van iets waar je wel
al ervaring mee zal hebben: het berekenen van de gemiddelde snelheid.

## Gemiddelde snelheid als een breuk van twee verschillen

Maria houdt van dragracen. Bij een dragrace vertrekken twee wagens vanuit
stilstand en racen ze $300~\si{m}$ in een rechte lijn. De eerste aan de finish
wint.

{{< svg "img/drag_racing.svg" "Maria racet en is bijna aan de finish." >}}

De wagens halen enorme snelheden tot meer dan $500~\si{km/h}$. Hieronder zie je
enkele luchtfoto's van Maria in haar *Top Fuel dragster* tijdens het dragracen.

{{< svg "img/maria_race_top.svg" "Luchtfoto's van Maria tijdens haar race." >}}

Stel dat we Maria haar gemiddelde snelheid willen berekenen
tussen $\orange{1{,}00~\si{s}}$ en $\orange{3{,}00~\si{s}}$.

{{< svg "img/maria_avg_speed_1s_3s.svg" "Gemiddelde snelheid van Maria tussen 1 s en 3 s berekenen" >}}

Daarvoor moeten we de **afgelegde afstand**
{{< mute "(hoeveel (kilo)meter?)" >}} delen door de **tijd die nodig was**
{{< mute "(hoeveel uur of seconden?)" >}} om die afstand af te leggen:

\begin{split}
    \text{gem. snelheid} &= \frac{\green{\text{afgelegde afstand} }}{\orange{\text{tijd die nodig was}}}\\\\\
\end{split}
 
Wanneer de chronometer op $\orange{1{,}00~\si{s}}$ stond, was Maria
$\green{20~\si{m}}$ ver. Bij $\orange{3{,}00~\si{s}}$, was ze
$\green{180~\si{m}}$ ver. De gemiddelde snelheid tussen
$\orange{1{,}00~\si{s}}$ en $\orange{3{,}00~\si{s}}$ is dus:

\begin{split}
    \text{gem. snelheid} &= \frac{\green{\text{afgelegde afstand} }}{\orange{\text{tijd die nodig was}}}\\\\\
                         &= \frac{\green{180~\si{m}} - \green{20~\si{m}}}{\orange{3{,}00~\si{s}} - \orange{1{,}00~\si{s}}}\\\\\
                         &= \frac{\green{160~\si{m}}}{\orange{2{,}00~\si{s}}}\\\\\
                         &= 80{,}0~\si{m/s}\\\\\
                         &= 288~\si{km/h}
\end{split}

Lekker snel! 🚀

Je ziet dat we voor de afgelegde afstand en de tijd die nodig was telkens een
**verschil** berekenen. Voor de afstand is dat het **verschil tussen de tweede
positie** ($\green{180~\si{m}}$) **en de eerste positie**
($\green{20~\si{m}}$). Voor de tijd is dat het **verschil tussen de tweede
tijd** ($\orange{3{,}00~\si{s}}$) **en de eerste tijd**
($\orange{1{,}00~\si{s}}$). Die twee verschillen zetten we vervolgens in een
**breuk** met in de teller het verschil van posities en in de noemer het
verschil van tijden. We kunnen de formule voor gemiddelde snelheid dus ook als
volgt schrijven:

$$\text{gem. snelheid} = \frac{\green{\text{positie}\_2} - \green{\text{positie}\_1}}{\orange{\text{tijd}\_2} - \orange{\text{tijd}\_1}}$$
 
## Gemiddelde snelheid veralgemenen naar gemiddelde verandering

Stel nu dat we de $\orange{\text{tijd}}$ op de chronometer "$\orange{x}$"
noemen. Maria kan op een bepaald tijdstip $\orange{x}$ natuurlijk maar op één
plaats tegelijk zijn. Met elke tijd $\orange{x}$ op de chronometer komt dus
*hooguit één* $\green{\text{positie}}$ overeen. Daarom mogen we zeggen dat
Maria haar **positie een functie is van de tijd**. We kunnen de positie die
overeenkomt met tijdstip $\orange{x}$ dus $\green{f(x)}$ noemen. Op de
luchtfoto's zien we inderdaad dat de posities een mooie [grafiek van een
functie](../../functies/grafiek) vormen:

{{< svg "img/maria_race_function.svg" "De positie van Maria als functie van de tijd" >}}

> Als je niet meer goed weet vanaf wanneer een verband tussen twee variabelen
{{< mute "(zoals positie en tijd)" >}} een functie is, kan je altijd onze
[intro over functies](../../functies/intro) eens nalezen.

We kunnen nu onze formule voor gemiddelde snelheid korter schrijven waarbij we

* $\orange{\text{tijd}\_1}$ en $\orange{\text{tijd}\_2}$ vervangen door
  $\orange{x\_1}$ en $\orange{x\_2}$
* $\green{\text{positie}\_1}$ en $\green{\text{positie}\_2}$ vervangen door
  $\green{f(x\_1)}$ en $\green{f(x\_2)}$

Zo krijgen we:

$$\frac{\green{f(x\_2)} - \green{f(x\_1)}}{\orange{x\_2} - \orange{x\_1}}$$

Merk op dat in de teller telkens de *functiewaarde* staat van de $x-$waarden in
de noemer. Stel dat $\orange{x\_1} = \orange{2{,}00~\si{s}}$ en $\orange{x\_2}
= \orange{2{,}50~\si{s}}$, dan zal $\green{f(x\_1)} = \green{80~\si{m}}$ en
$\green{f(x\_2)} = \green{125~\si{m}}$, zoals je kan zien in onderstaande
figuur:

{{< svg "img/race_positie_fx_waarde.svg" "De posities zijn functiewaarden van de tijd." >}}

De formule $\frac{\green{f(x\_2)} - \green{f(x\_1)}}{\orange{x\_2} -
\orange{x\_1}}$ noemen we het **differentiequotiënt**. Hier gaan we in de
volgende paragraaf verder op in.

## Het differentiequotiënt

In de vorige paragraaf leerden we dat we de formule voor het berekenen van
gemiddelde snelheid konden schrijven als het **differentiequotiënt**:

{{< svg "img/diff_quot_intuitie.svg" "Intuïtie achter formule van differentiequotiënt" >}}

Het is belangrijk dat we niet uit het oog verliezen wat deze formule **in
mensentaal wilt zeggen**. Wiskundig gezien zegt deze formule het volgende:

* Hoeveel verandert de $\green{\text{functiewaarde}}$ gemiddeld
  $\orange{\text{per x-eenheid}}$ tussen $\orange{x\_1}$ en $\orange{x\_2}$?

Het kan echter helpen om de analogie met de dragrace van Maria in ons
achterhoofd te houden. In dat geval kunnen we de formule lezen als:

* Hoeveel verandert de $\green{\text{positie van Maria}}$ gemiddeld
  $\orange{\text{per seconde}}$ tussen tijd $\orange{x\_1}$ en tijd
  $\orange{x\_2}$?

Wanneer een **differentiequotiënt groot** is, betekent het dat de functie veel
verandert per x-eenheid tussen $\orange{x\_1}$ en $\orange{x\_2}$. Bij de
dragrace gebeurt dit wanneer Maria heel **snel rijdt**. Je ziet dat de
functiewaarde {{< mute "(de positie dus)" >}} dan inderdaad veel verandert per
x-eenheid {{< mute "(per seconde dus)" >}}:

{{< svg "img/race_groot_difquot.svg" "x-waarden die een groot differentiequotiënt geven" >}}

Nadat ze over de finish is, **remt Maria haar wagen af** met behulp van een
parachute. We zien dat de functiewaarde {{< mute "(de positie dus)" >}} dan
veel minder verandert per x-eenheid {{< mute "(per seconde dus)" >}}. Het
**differentiequotiënt is in dit geval klein**:

{{< svg "img/race_klein_difquot.svg" "x-waarden die een klein differentiequotiënt geven" >}}

{{< expand "Waar komt de naam differentiequotiënt vandaan?" >}}
Nu denk je misschien: "Een differ-**watte**?! 🤨" Waar komt die 
naam vandaan? Het woord bestaat uit twee stukken:

1. **differentie-**: moeilijk woord voor een *aftrekking* of *verschil*, denk 
   maar aan het Engelse woord *difference*. Dit wijst erop dat er een 
   **verschil wordt berekend** in de teller en noemer.
2. **-quotiënt**: moeilijk woord voor een *deling* of een *breuk*. Dit wijst
   op het feit dat **het ene verschil wordt gedeeld door het andere**.
   
{{< /expand >}}

## Het verschil afkorten met $\Delta$

Tot slot gaan we het differentiequotiënt nog een tikkeltje korter leren
schrijven. Verschillen als "$\green{f(x\_2)} - \green{f(x\_1)}$" en
"$\orange{x\_2} - \orange{x\_1}$" komen namelijk vaak voor en het is lastig om
die telkens voluit te moeten schrijven. Daarom gaan we zulke verschillen
afkorten. Hiervoor gebruiken we de Griekse hoofdletter $\Delta$ (de delta):

\begin{split}
    \orange{\Delta x} &= \orange{x\_2} - \orange{x\_1}\\\\\
    \green{\Delta f(x)} &= \green{f(x\_2)} - \green{f(x\_1)}
\end{split}

Die "$\Delta$" lijkt wat overweldigend, maar is eigenlijk niets meer dan een
verkorte schrijfwijze. Met behulp van deze $\Delta$, kunnen we het
differentiequotiënt als volgt afkorten:

$$\frac{\green{f(x\_2)} - \green{f(x\_1)}}{\orange{x\_2} - \orange{x\_1}} = \frac{\green{\Delta f(x)}}{\orange{\Delta x}}$$

Op een grafiek kan je $\green{\Delta f(x)}$ en $\orange{\Delta x}$ ook aanduiden:

{{< svg "img/graph_delta_fx_delta_x.svg" "Delta f(x) en Delta x aangeduid op een grafiek." >}}

Een andere vaakgebruikte manier om het differentiequotiënt verkort te schrijven gaat zo:

$$\frac{\green{f(x\_2)} - \green{f(x\_1)}}{\orange{x\_2} - \orange{x\_1}} = \frac{\green{f(x\_1 + \Delta x)} - \green{f(x\_1)}}{\orange{\Delta x}}$$

Grafisch zie je dat de formule inderdaad hetzelfde zegt als voordien:

{{< svg "img/graph_delta_fx1+delta_x_delta_x.svg" "Delta f(x1 + Delta x) en Delta x aangeduid op een grafiek." >}}

In de noemer doen we hetzelfde als voordien, namelijk $\orange{x\_2} -
\orange{x\_1}$ vervangen door $\orange{\Delta x}$. In de teller doen we iets
anders nu. We vervangen $\green{f(x\_2)}$ door $\green{f(x\_1 + \Delta x)}$.
Dat mag omdat $x\_2 = x\_1 + \Delta x$:

\begin{split}
    \Delta x &= x\_2 - x\_1\\\\\
    \Leftrightarrow \Delta x + x\_1 &= x\_2\\\\\
    \Leftrightarrow x\_2 &= x\_1 + \Delta x
\end{split}

Meestal gaat $\frac{\green{f(x\_1 + \Delta x)} -
\green{f(x\_1)}}{\orange{\Delta x}}$ echter nog korter geschreven worden door
in plaats van $x\_1$ gewoon $a$ te schrijven:

$$\frac{\green{f(a + \Delta x)} - \green{f(a)}}{\orange{\Delta x}}$$

Dat ziet er grafisch zo uit:

{{< svg "img/graph_delta_fa+delta_x_delta_x.svg" "Delta f(a + Delta x) en Delta x aangeduid op een grafiek." >}}

## Samengevat

{{< attention "Wat is een differentiequotiënt?" >}}
Het differentiequotiënt is gedefinieerd als

$$\frac{\green{f(x\_2)} - \green{f(x\_1)}}{\orange{x\_2} - \orange{x\_1}}$$

Dit kunnen we korter schrijven als:

$$\frac{\green{f(a + \Delta x)} - \green{f(a)}}{\orange{\Delta x}}$$

Waarbij $a=x\_1$. Je kan het differentiequotiënt nog korter schrijven als:

$$\frac{\green{\Delta f(x)}}{\orange{\Delta x}}$$

Een differentiequotiënt zegt hoeveel de $\green{\text{functiewaarde}}$
gemiddeld $\orange{\text{per x-eenheid}}$ verandert tussen de gekozen
$\orange{x\_1}$ en $\orange{x\_2}$.
{{< /attention >}}
