---
title: "Afgeleide functie"
date: 2020-04-02T16:13:59+02:00
weight: 4
draft: true
tags: []
images: ['/lessen/wiskunde/afgeleiden/afgeleide_functie/img/zonder_met_afgeleide_fx.png', '/lessen/wiskunde/afgeleiden/afgeleide_functie/img/fx_ingevuld_in_afgeleide.png', '/lessen/wiskunde/afgeleiden/afgeleide_functie/img/f_delta_x_ingevuld.png', '/lessen/wiskunde/afgeleiden/afgeleide_functie/img/f_delta_x_uitwerking.png', '/lessen/wiskunde/afgeleiden/afgeleide_functie/img/afgeleide_teller_uitwerking.png']
description: ""
---

In de vorige les zagen we hoe je de [afgeleide voor een bepaalde
x-waarde](../in_een_punt) van een functie $f(x)$ kan berekenen. Lees die les
zeker eens na als je nog niet goed begrijpt wat we daar juist mee bedoelen.  Je
kan in die les zien dat het eigenlijk nogal **veel werk** is om zo'n afgeleide
te berekenen. Zeker als we voor meerdere x-waarden die afgeleide zouden willen
berekenen.

Gelukkig kunnen we ook de **afgeleide van een volledige functie** berekenen.
Dat betekent dat we van **alle x-waarden tegelijk** de afgeleide berekenen!
:open_mouth: Dat noemen we een **afgeleide functie**.

{{< svg "img/zonder_met_afgeleide_fx.svg" "Met de afgeleide functie kunnen we sneller afgeleiden berekenen" >}}

## De afgeleide functie $f'(x)$

Met de **afgeleide functie** kunnen we heel snel de afgeleide vinden voor
eender welke x-waarde in het domein van een functie. De afgeleide functie
duiden we aan door een accent naast de $f$ van onze functie te zetten: 

| Je schrijft | Je leest het als               |
|-------------|--------------------------------|
| $f'(x)$     | De afgeleide functie van $f$   |

De afgeleide functie geeft ons een **nieuw functievoorschrift $f'(x)$**. In
dat voorschrift kunnen we dan weer x-waarden invullen, net zoals we in $f(x)$
x-waarden kunnen invullen. Als we in $f'(x)$ een x-waarde invullen, berekenen
we meteen de **afgeleide voor die x-waarde**. Zo moeten we niet telkens al het
werk herhalen van de [vorige les](../in_een_punt).

## De afgeleide van een tweedegraadsfunctie

We hebben al geleerd dat een afgeleide functie $f'(x)$ ons veel werk kan
besparen. Eens we $f'(x)$ gevonden hebben, kunnen we er namelijk eender welke
x-waarde in invullen en vinden we meteen de afgeleide voor die x-waarde. Maar
**hoe vinden we die afgeleide functie**? Als voorbeeld zoeken we in deze
paragraaf de afgeleide functie van de volgende tweedegraadsfunctie:

$$f(x) = -3x^2 + 4x - 1$$

We leerden in de vorige les hoe je voor een [bepaalde x-waarde de
afgeleide](../in_een_punt) kan berekenen. Daarvoor vulden we de x-waarde in in
de definitie van een afgeleide. Nu doen we hetzelfde, maar in plaats van een
bepaald getal in te vullen, laten we **alle symbolen in de definitie staan**.

Herinner je dat de definitie van een afgeleide als volgt ging:

$$ f'(x) = \lim\_{\Delta x \rightarrow 0} \frac{ f(x + \Delta x) - f(x) }{\Delta x} $$

Lees zeker [onze introductie tot afgeleiden](../intro) eens na als je die
formule niet zo goed begrijpt. Als we naar die definitie kijken, zien we dat er
twee keer iets met $f(\ldots)$ staat. De eerste keer staat er $f(x + \Delta x)$
en de tweede keer staat er $f(x)$:

{{< svg "img/fx_in_afgeleide.svg"  "Definitie van een afgeleide" >}}

Die $f(x + \Delta x)$ en $f(x)$ moeten we bepalen voor de functie waar
we de afgeleide van willen vinden. Wij zoeken de afgeleide van
$f(x) = -3x^2 + 4x - 1$, dus de $f(x)$ kunnen we al meteen vervangen in de
definitie:

{{< svg "img/fx_ingevuld_in_afgeleide.svg" "Functievoorschrift ingevuld in de definitie van een afgeleide." >}}

Maar hoe vinden we die vreemde $f(x + \Delta x)$? Daarvoor moeten we
eigenlijk gewoon alle $x-$en in het functievoorschrift $f(x) = -3x^2 + 4x - 1$
vervangen door $(x + \Delta x)$:

{{< svg "img/f_delta_x_ingevuld.svg" "$(x + \Delta x)$ ingevuld in de definitie van een afgeleide." >}}

We hebben nu $f(x + \Delta x)$ en $f(x)$ gevonden voor de functie die we willen
afleiden. Nu moeten we alles uitwerken en de limiet uitrekenen. Om alles een
beetje verteerbaar te houden, gaan we die harige $f(\blue{x + \Delta x})$ eerst
apart uitwerken:

{{< svg "img/f_delta_x_uitwerking.svg" "Uitwerking van $f(x + \Delta x)$" >}}

Die $f(x + \Delta x)$ blijft een serieus harige uitdrukking... :rolling_eyes:
Als je terug even naar boven gaat, zie je in de definitie van $f'(x)$ in de
teller van de breuk "$f(x + \Delta x) - f(x)$" staan. We moeten van onze $f(x +
\Delta x)$ dus nog $f(x)$ aftrekken. Gelukkig vallen er dan een hele hoop
dingen weg:

{{< svg "img/afgeleide_teller_uitwerking.svg" "Uitwerking van de teller van de breuk voor onze $f(x)$ in de definitie van de afgeleide." >}}

