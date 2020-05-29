---
title: "Formules invullen en omvormen"
date: 2019-01-28T08:07:58+01:00
weight: 8
draft: false
tags: ["grootheden_eenheden", "formules", "vergelijkingen"]
categories: ["grootheden_eenheden", "formules"]
level: "3M"
course: "Fysica"
topic: "grootheden_eenheden"
images: []
---

In een oefening fysica zijn er altijd een of meerdere dingen **gegeven** en
zijn er een of meerdere dingen **gevraagd**. We lossen de oefening op door een
**verband te vinden tussen de gegevens en het gevraagde**.

Maar hoe kunnen we dat **verband** vinden? Wel, natuurkundigen voeren al
honderden jaren **experimenten** uit en hebben bij die experimenten al heel veel
van zulke verbanden ontdekt. Die verbanden zijn neergeschreven in **formules**.

Een eenvoudig voorbeeld van zo'n formule is het verband tussen de invalshoek
{{< mute "(korten we af met $\hat{i}$)" >}} en de terugkaatsingshoek
{{< mute "(korten we af met $\hat{t}$)" >}} bij een vlakke spiegel:

$$\orange{\hat{i}} = \green{\hat{t}}$$

{{< svg "img/terugkaatsingswet.svg" "Illustratie van de terugkaatsingswet" >}}

We gaan eens kijken hoe we deze formule kunnen gebruiken bij het oplossen van
een oefening. Stel dat we de volgende opgave hebben:

> *Een lichstraal valt in op een vlakke spiegel en kaatst met een
> terugkaatsingshoek van $30\deg$ terug. Met welke hoek viel de lichtstraal
> in?*

Dan is

- **Gegeven**: de **terugkaatsingshoek** is $30\deg$
- **Gevraagd**: met welke hoek viel de lichtstraal in? Of met andere woorden,
wat was de **invalshoek**?

De formule $\orange{\hat{i}} = \green{\hat{t}}$ zegt ons dat de invalshoek
altijd gelijk is aan de terugkaatsingshoek. Deze oefening is dus heel snel
opgelost:

{{< svg "img/oplossing_terugkaatsing.svg" "Oplossing vraag invalshoek" >}}

De formule $\orange{\hat{i}} = \green{\hat{t}}$ gaf ons het verband tussen wat
gegeven was in de opgave {{< mute "(de terugkaatsingshoek $\hat{t}$)" >}} en
wat gevraagd was {{< mute "(de invalshoek $\hat{i}$)" >}}. Door in de formule
het gegeven in te vullen, vonden we de gevraagde invalshoek.

## Een gelijkheid omdraaien

Bij het vorige voorbeeld hadden we geluk dat $\orange{\hat{i}}$ gevraagd was en
er in onze formule letterlijk "$\orange{\hat{i}} = " stond. Wat als

## Een formule met een berekening


## Een formule met een vermenigvuldiging omvormen

## Een formule met een breuk omvormen

## Een formule met een kwadraat omvormen

$E\_{kin} = \frac{1}{2} m \cdot v^2$

Kunnen we een formule ook
De formule $\orange{\hat{i}} = \green{\hat{t}}$ is zeer eenvo

De fysica zit tjokvol formules. Ondanks die formules er soms op het eerste
zicht behoorlijk angstaanjagend kunnen uitzien, helpen de formules ons om
de uitkomst van ontelbare **situaties te voorspellen**.

Een formule bevat altijd meerdere **[grootheden](../intro)**.

Een eenvoudige formule is bijvoorbeeld hoe we
massadichtheid kunnen berekenen:

$$\rho = \frac{\si{m}}{\si{V}}$$

Dit lees je als:

$$\text{massadichtheid} = \frac{\text{massa}}{\text{volume}}$$

De massadichtheid van een stof zegt hoeveel $\si{kg}$ een bepaald volume van
die stof is. Eén liter water, bijvoorbeeld, heeft een massa van ongeveer $1
\si{ kg}$. Water heeft dus een massadichtheid van $1 \si{ kg/l}$, [wat gelijk
is aan](../eenheden_omzetten#volumes-omzetten) $10^3 \si{ kg/m}^3$.


## Grootheden invullen
Als we de massadichtheid willen berekenen wanneer we van een stof de massa $\orange{\si{m}}$ voor een bepaald volume $\orange{\si{V}}$ kennen, kunnen we de formule $\rho = \frac{\orange{\si{m}}}{\orange{\si{V}}}$ rechtstreeks gebruiken.

Bijvoorbeeld: we leggen een kubusvormig blokje kurk met een zijde van $5 \si{ cm}$ op een weegschaal en lezen af dat het blokje een massa heeft van $26 \si{ g}$. Dan is de massadichtheid van kurk:
\begin{split}
\rho &= \frac{\si{m}}{\si{V}} \\\\\
&= \frac{26 \si{ g}}{5 \si{ cm} \cdot 5 \si{ cm} \cdot 5 \si{ cm}}\\\\\
&= \frac{26 \si{ g}}{125 \si{ cm}^3}\\\\\
&= 0{,}208 \frac{\si{g}}{\si{cm}^3}\\\\\
&\approx 0{,}21 \frac{\si{g}}{\si{cm}^3}
\end{split}

## Omvormen zoals vergelijkingen
De technieken die we gebruiken om [vergelijkingen om te vormen](../../../wiskunde/1g_vgl/omvormen), kunnen we ook gebruiken om formules om te vormen. Zo kunnen we de formule voor massadichtheid omvormen zodat $m$ alleen overblijft aan één kant:
\begin{split}
\rho &= \frac{m}{V}\\\\\
\Leftrightarrow \rho \cdot \orange{V} &= \frac{m}{V} \cdot \orange{V}\\\\\
\Leftrightarrow \rho \cdot \orange{V} &= m \cdot \frac{\orange{V}}{V} \\\\\
\Leftrightarrow \rho \cdot \orange{V} &= m \cdot 1 \\\\\
\Leftrightarrow \rho \cdot \orange{V} &= m \\\\\
\Leftrightarrow m &= \rho \cdot V \\\\\
\end{split}

Zo kunnen we $m$ berekenen wanneer we $\rho$ en $V$ kennen. We kunnen deze formule dan weer verder omvormen zodat $V$ alleen overblijft aan één kant:

\begin{split}
m &= \rho \cdot V \\\\\
\Leftrightarrow \frac{m}{\orange{\rho}} &= \frac{\rho \cdot V}{\orange{\rho}} \\\\\
\Leftrightarrow \frac{m}{\orange{\rho}} &= \frac{\rho}{\orange{\rho}} \cdot V \\\\\
\Leftrightarrow \frac{m}{\orange{\rho}} &= 1 \cdot V \\\\\
\Leftrightarrow \frac{m}{\orange{\rho}} &= V \\\\\
\Leftrightarrow V &= \frac{m}{\rho}
\end{split}

Met die formule kunnen we dan $V$ berekenen wanneer $m$ en $\rho$ gegeven zijn.


## Formules optica omvormen

$\frac{\sin{\hat{i}}}{\sin{\hat{r}}} = \frac{v\_a}{v\_b}$

$\frac{v\_a}{v\_b} = n\_{a \to b}$

$f = \frac{r}{2}$

$\hat{i} = \hat{t}$

$\frac{1}{f} = \frac{1}{v} + \frac{1}{b}$

$G = \frac{-b}{v}$

## Formules snelheid omvormen

$v_x = \frac{\Delta x}{\Delta t}$

## Formules kracht omvormen

$F_{z} = m \cdot g$

$F_{v} = k \cdot \Delta l$

## Formules materie omvormen

$\rho = \frac{m}{V}$

## Formules arbeid en energie omvormen

$W = F \cdot \Delta x$

$W = - F \cdot \Delta x$

$W = F \cdot \Delta x \cdot \cos{\theta}$

$E\_{kin} = \frac{1}{2} m \cdot v^2$

$E\_{pot, g} = m \cdot g \cdot h$

$E\_{pot, v} = \frac{1}{2} k \cdot (\Delta l)^2$

$E\_{mech} = E\_{pot} +  E\_{kin}$

$E\_{mech, 1} = E\_{mech, 2}$

## Formules rendement en vermogen omvormen

$P = \frac{W}{\Delta t}$

$\eta = \frac{E\_{nuttig}}{E\_{verbruikt}}$

## Formules druk omvormen

$p = \frac{F}{A}$

$p\_{hydr} = \rho\_{vl} \cdot g \cdot h$

$F\_a = \rho\_{vl} \cdot V_{onder} \cdot g$

## Formules gas omvormen

$p\_1 \cdot V\_1 = p\_2 \cdot V\_2$
