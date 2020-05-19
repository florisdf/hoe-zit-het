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

Stel dat we Maria's gemiddelde snelheid willen berekenen
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
**breuk** met in de teller {{< mute "(boven)" >}} het verschil van posities en in de noemer {{< mute "(onder)" >}} het
verschil van tijden. We kunnen de formule voor gemiddelde snelheid dus ook als
volgt schrijven:

$$\text{gem. snelheid} = \frac{\green{\text{positie}\_2} - \green{\text{positie}\_1}}{\orange{\text{tijd}\_2} - \orange{\text{tijd}\_1}}$$
 
## Gemiddelde snelheid veralgemenen naar het differentiequotiënt

Stel nu dat we de $\orange{\text{tijd}}$ op de chronometer "$\orange{x}$"
noemen. Maria kan op een bepaald tijdstip $\orange{x}$ natuurlijk maar op één
plaats tegelijk zijn. Met elke tijd $\orange{x}$ op de chronometer komt dus
*hooguit één* $\green{\text{positie}}$ overeen. Daarom mogen we zeggen dat
Maria's **positie een functie is van de tijd**.

> Als je niet meer goed weet vanaf wanneer een verband tussen twee variabelen
{{< mute "(zoals positie en tijd)" >}} een functie is, kan je altijd onze
[les over functies](../../functies/intro) eens nalezen. 

We kunnen de **positie** die overeenkomt met tijdstip $\orange{x}$ dus **de
functiewaarde van $\orange{x}$** noemen en afkorten als $\green{f(x)}$. Wanneer
we op de luchtfoto's de racewagens met elkaar verbinden, zien we inderdaad dat
de posities mooi de [grafiek van een functie](../../functies/grafiek) volgen
waarbij de **tijd op de x-as** {{< mute "(horizontale as)" >}} staat en de
**positie op de y-as** {{< mute "(verticale as)" >}}:

{{< svg "img/maria_race_function.svg" "De positie van Maria als functie van de tijd" >}}

We kunnen nu onze formule voor gemiddelde snelheid korter schrijven waarbij we

* $\green{\text{positie}\_2}$ en $\green{\text{positie}\_1}$ vervangen door
  $\green{f(x\_2)}$ en $\green{f(x\_1)}$
* $\orange{\text{tijd}\_2}$ en $\orange{\text{tijd}\_1}$ vervangen door
  $\orange{x\_2}$ en $\orange{x\_1}$ 

Zo krijgen we:

$$\frac{\green{f(x\_2)} - \green{f(x\_1)}}{\orange{x\_2} - \orange{x\_1}}$$

* In de teller {{< mute "(boven)" >}} staat $\green{f(x\_2)} -
  \green{f(x\_1)}$. Daarmee berekenen we het verschil van de functiewaarden van
  $x\_2$ en $x\_1$. **De teller zegt zo hoeveel de functiewaarde is veranderd**
  tussen $x\_1$ en $x\_2$.
* In de noemer {{< mute "(onder)" >}} staat dan weer het verschil van die
  $x\_2$ en $x\_1$ zélf. Door te delen door $\orange{x\_2} - \orange{x\_1}$
  berekenen we de "**gemiddelde** verandering van  de functiewaarde **per
  $x-$eenheid** {{< mute "(bv. per seconde)" >}} tussen $x\_1$ en $x\_2$" in
  plaats van gewoon de "verandering van  de functiewaarde tussen $x\_1$ en
  $x\_2$".

{{< expand "Waarom zorgt die deling door $\orange{x_2} - \orange{x_1}$ voor een gemiddelde?" >}}
Stel dat je de **gemiddelde** score wilt berekenen die de leerlingen van een bepaalde klas haalden op een test. Dan ga je alle punten optellen en **delen door het totaal aantal testen**. Door te delen door het totaal aantal testen, krijg je de gemiddelde score **per test**.

Op dezelfde manier krijgen we de **gemiddelde** verandering van  de functiewaarde **per $x-$eenheid** door te delen door $\orange{x_2} - \orange{x_1}$.
{{< /expand >}}

We zeggen dat deze formule de **gemiddelde verandering van de functiewaarde** berekent per $x-$eenheid tussen $\orange{x\_1}$ en $\orange{x\_2}$.

{{< svg "img/diff_quot_intuitie.svg" >}}

Het is belangrijk om te weten dat we die formule niet enkel kunnen gebruiken om gemiddelde snelheid te berekenen, maar voor nog veel andere soorten van *gemiddelde verandering*.
De formule wordt zelfs zo vaak gebruikt, dat ze een eigen naam heeft gekregen: het **differentiequotiënt**.

{{< expand "Waar komt de naam differentiequotiënt vandaan?" >}}
Nu denk je misschien: "Een differ-**watte**?! 🤨" Waar komt die 
naam vandaan? Het woord bestaat uit twee stukken:

1. **differentie-**: moeilijk woord voor een *aftrekking* of *verschil*, denk 
   maar aan het Engelse woord *difference*. Dit wijst erop dat er een 
   **verschil wordt berekend** in de teller en noemer.
2. **-quotiënt**: moeilijk woord voor een *deling* of een *breuk*. Dit wijst
   op het feit dat **het ene verschil wordt gedeeld door het andere**.
   
{{< /expand >}}

## Voorbeelden met het differentiequotiënt

Wanneer kan het berekenen van de *gemiddelde verandering* van een functie en
dus het **differentiequotiënt** nu van pas komen? In deze paragraaf geven we
enkele concrete voorbeelden.

### Gemiddelde winst per dag

Ronny baat een online snoepwinkel uit.

(illustratie)

Voor de maand april heeft hij een overzicht van het saldo dat op het einde van
elke dag op de rekening van zijn webwinkel stond. Op onderstaand overzicht zie
je dat er op het einde van de eerste dag $€10~000$ op de rekening stond, de dag
nadien $€10~300$ enzovoort.

(illustratie)

Op het einde van een bepaalde dag $\orange{x}$ kan er natuurlijk maar één saldo
op de rekening van de webwinkel staan. Met elke $\orange{x}$ komt dus **hooguit
één** $\green{\text{saldo}}$ overeen. Daarom mogen we zeggen dat **het saldo
een functie is van de dag $\orange{x}$** die we kiezen. We kunnen het
$\green{\text{saldo}}$ dat overeenkomt met dag $\orange{x}$ **de functiewaarde
van $\orange{x}$** noemen en afkorten als $\green{f(x)}$.

(illustratie van overzicht met x en f(x) aangeduid)

We weten dat het differentiequotiënt gedefinieerd is als:

$$\frac{\green{f(x\_2)} - \green{f(x\_1)}}{\orange{x\_2} - \orange{x\_1}}$$

Maar wat betekent dat differentiequotiënt voor het saldo van Ronny's
snoepwinkel?

* In de teller {{< mute "(boven)" >}} berekenen we het **verschil tussen de
saldo's** op dag $x\_2$ en dag $x\_1$. De teller zegt dus **hoeveel het saldo is
veranderd** van dag $x\_1$ naar dag $x\_2$.
* In de noemer {{< mute "(onder)" >}} berekenen we het **verschil tussen dag
$x\_2$ en dag $x\_1$**. De noemer zegt dus **hoeveel dagen er tussen dag $x\_1$
en dag $x\_2$ zitten**.

(illustratie met difquot en vertaling naast elkaar)

Positief differentiequotiënt: winst. Negatief differentiequotiënt: verlies.

### Gemiddelde helling
van een berg wanneer de hoogte in functie van de positie is gegeven

Positief differentiequotiënt: winst. Negatief differentiequotiënt: verlies.

### Gemiddelde snelheid

Met dit voorbeeld zijn we de les begonnen. We gaan het hier even herhalen, maar
nu vertrekkend van een functievoorschrift. Stel dat Maria's positie in functie
van de tijd het volgende voorschrift volgt:

$$\green{f(x)} = \green{20\cdot x^2}$$

Wanneer $\green{f(x)}$ de positie in functie van de tijd is, berekenen we met
het differentiequotiënt de **gemiddelde snelheid** tussen tijdstippen
$\orange{x\_1}$ en $\orange{x\_2}$.

Samengevat zegt onze formule:

* Hoeveel verandert de $\green{\text{functiewaarde}}$ gemiddeld
  $\orange{\text{per x-eenheid}}$ tussen $\orange{x\_1}$ en $\orange{x\_2}$?


Als je die formulering nogal ingewikkeld vindt, kan je altijd terugdenken aan 
de analogie met de dragrace van Maria:

* Hoeveel verandert de $\green{\text{positie van Maria}}$ gemiddeld
  $\orange{\text{per seconde}}$ tussen tijd $\orange{x\_1}$ en tijd
  $\orange{x\_2}$?

* Wat betekent de functiewaarde?
* Wat betekent de verandering van de functiewaarde?
* Wat betekent de x-eenheid?
* Wat betekent de verandering van de functiewaarde per x-eenheid?


## Het verschil afkorten met $\Delta$

Tot slot gaan we het differentiequotiënt nog een tikkeltje korter leren
schrijven. Verschillen als "$\green{f(x\_2)} - \green{f(x\_1)}$" en
"$\orange{x\_2} - \orange{x\_1}$" komen namelijk vaak voor en het is lastig om
die telkens voluit te moeten schrijven. Daarom gaan we zulke verschillen
afkorten. Hiervoor gebruiken we de Griekse hoofdletter $\Delta$ (de delta):

\begin{split}
    \green{f(x\_2)} - \green{f(x\_1)} &= \green{\Delta f(x)}\\\\\
    \orange{x\_2} - \orange{x\_1} &= \orange{\Delta x}
\end{split}

Die "$\Delta$" lijkt wat overweldigend, maar is eigenlijk niets meer dan een
verkorte schrijfwijze. Met behulp van deze $\Delta$, kunnen we het
differentiequotiënt als volgt afkorten:

$$\frac{\green{f(x\_2)} - \green{f(x\_1)}}{\orange{x\_2} - \orange{x\_1}} = \frac{\green{\Delta f(x)}}{\orange{\Delta x}}$$

Op een grafiek kan je $\green{\Delta f(x)}$ en $\orange{\Delta x}$ ook aanduiden:

{{< svg "img/graph_delta_fx_delta_x.svg" "Delta f(x) en Delta x aangeduid op een grafiek." >}}

Je zult het waarschijnlijk niet graag horen, maar er is nog een derde en laatste manier om het differentiequotiënt te schrijven. Daarbij gaan we drie dingen veranderen aan de oorspronkelijke formule van het differentiequotiënt:

1. Vervang $\orange{x\_2} - \orange{x\_1}$ door $\orange{\Delta x}$: $$\frac{\green{f(x\_2)} - \green{f(x\_1)}}{\orange{\Delta x}}$$
2. Vervang $x\_2$ door $x\_1 + \Delta x$: $$\frac{\green{f(x\_1 + \Delta x)} - \green{f(x\_1)}}{\orange{\Delta x}}$$
3. Vervang $x\_1$ overal door $a$: $$\frac{\green{f(a + \Delta x)} - \green{f(a)}}{\orange{\Delta x}}$$

Dat ziet er grafisch zo uit:

{{< svg "img/graph_delta_fa+delta_x_delta_x.svg" "Delta f(a + Delta x) en Delta x aangeduid op een grafiek." >}}

We hebben nu drie verschillende manieren gezien om het differentiequotiënt te schrijven:

1. $$\frac{\green{f(x\_2)} - \green{f(x\_1)}}{\orange{x\_2} - \orange{x\_1}}$$
2. $$\frac{\green{\Delta f(x)}}{\orange{\Delta x}}$$
3. $$\frac{\green{f(a + \Delta x)} - \green{f(a)}}{\orange{\Delta x}}$$


Het is belangrijk om in te zien dat deze alle drie **identiek dezelfde berekening** maken. De berekening wordt enkel anders *verwoord*. Kijk dus nog eens extra naar de drie formules voor het differentiequotiënt, bekijk de bijhorende grafieken nogmaals en zorg dat je de gelijkenis begrijpt.

## Samengevat

{{< attention "Wat is een differentiequotiënt?" >}}
Een differentiequotiënt zegt hoeveel de $\green{\text{functiewaarde}}$
gemiddeld $\orange{\text{per x-eenheid}}$ verandert tussen een gekozen
$\orange{x\_1}$ en $\orange{x\_2}$.

Het differentiequotiënt is gedefinieerd als:

$$\frac{\green{f(x\_2)} - \green{f(x\_1)}}{\orange{x\_2} - \orange{x\_1}}$$

Door $\green{f(x\_2) - f(x\_1)}$ te vervangen door $\green{\Delta f(x)}$ en $\orange{x\_2 - x\_1}$ door $\orange{\Delta x}$, kunnen we het differentiequotiënt ook schrijven als:

$$\frac{\green{\Delta f(x)}}{\orange{\Delta x}}$$

Een andere schrijfwijze vervangt $\orange{x\_2} - \orange{x\_1}$ door $\orange{\Delta x}$, $\green{f(x\_2)}$ door $\green{f(x\_1 + \Delta x)}$ en vervangt ten slotte $\green{x\_1}$ overal door $\green{a}$:

$$\frac{\green{f(a + \Delta x)} - \green{f(a)}}{\orange{\Delta x}}$$
{{< /attention >}}
