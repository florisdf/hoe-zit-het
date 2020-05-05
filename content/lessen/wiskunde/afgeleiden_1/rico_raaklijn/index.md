---
title: "De afgeleide als rico van een raaklijn"
date: 2020-03-29T15:58:07+02:00
weight: 3
draft: true
tags: ["afgeleide", "richtingscoëfficiënt", "rico", "raaklijn"]
images: []
description: "Door eens goed naar de definitie van een afgeleide te kijken,
kunnen we inzien dat deze eigenlijk gelijk is aan een richtingscoëfficiënt.
Meer bepaald is de afgeleide in een punt a de rico van de raaklijn aan de
grafiek van de functie in a. Dat is een hele mond vol. Maar gelukkig bouwen we
in deze les stap per stap en met behulp van veel illustraties op naar deze
interpretatie van een afgeleide."
---

In deze les tonen we intuïtief hoe de definitie van $f'(a)$ de
rico van de raaklijn aan de functie in $x=a$ beschrijft.

$$ f'(a) = \lim\_{\Delta x \rightarrow 0} \frac{ f(a + \Delta x) - f(a) }{\Delta x} $$

Grafiek met twee punten op een grafiek waarvan tweede punt naar eerste punt kan
getrokken worden. Concept: lijn die door twee punten gaat op curve wordt de raaklijn
aan de curve wanneer de punten dichter bij elkaar komen.
Uitklapbaar blokje met "Wat is een raaklijn weer?"

## Wat was de rico weer?

De rico is het getal dat weergeeft hoe hard een rechte stijgt of daalt wanneer je 1 bij x optelt of aftrekt. Een rechte met rico 4, die op $x=2$ waarde 7 heeft, zal op $x=3$ waarde 11 hebben en op $x=2$ waarde 3. Dit is ook makkelijk te zien op een grafiek.

(illustratie)

Een rico kan natuurlijk ook kleiner dan nul zijn, dan daalt de rechte als x groter wordt. De absolute waarde (dat is het getal zonder teken) van de rico geeft aan hoe stijl een rechte is. Op de grafiek hieronder kan je zien dat een grotere absolute waarde inderdaad een stijlere rechte geeft.

(illustratie)

De rico berekenen is helemaal niet moeilijk. Je neemt gewoon twee x-waarden en berekend hun bijbehorende y-waarden. Als je die hebt, gooi je ze in onderstaand formuletje en klaar is kees!

$$\text{rico} = \frac{y\_2 - y\_1}{x\_2 - x\_1}$$

Dit is natuurlijk geen magische formule die uit het niets werkt. Als je twee x'en kiest die maar '1' (*beter formuleren*) uit elkaar liggen, zie je dat de noemer 1 wordt en de rico dus gewoon het verschil is van de twee y-waarden. De formule zorgt er gewoon voor dat het niet uitmaakt welke x'en je juist gebruikt.

## Rico = afgeleide? :astonished:

Nee, maar ook ja, soms. Bv. voor een rechte. Zetten we de formule voor de afgeleide en de rico van een rechte naast elkaar dan wordt het snel duidelijk.


$$ \text{rico} = \frac{y\_2 - y\_1}{x\_2 - x\_1}  \qquad  f'(a) = \lim\_{\Delta x \rightarrow 0} \frac{ f(a + \Delta x) - f(a) }{\Delta x} $$

Op het eerste zicht is het misschien niet heel gelijkaardig. Maar als we het punt $a + \Delta x$ herschrijven als $b$, dan wordt het snel duidelijk.

$$ \text{rico} = \frac{y\_2 - y\_1}{x\_2 - x\_1}  \qquad  f'(a) = \lim\_{(b-a) \rightarrow 0} \frac{ f(b) - f(a) }{b - a} $$

Denk voorlopig even die limiet weg, noem $x_2 \rightarrow b$ en $x_1 \rightarrow a$ en je hebt twee keer dezelfde formule! Maar, het zou wiskunde natuurlijk niet zijn mochten we limieten en andere dingen die niet leuk zijn mogen weglaten... Nu komt het: voor een rechte, mag je die limiet wel zomaar weglaten. De formule van de rico geeft dezelfde waarde voor alle x'en, dus ook voor x'en die dicht tegen elkaar liggen. En dat is het enige dat de limiet doet: er voor zorgen dat die twee punten (heel, heel, heel) dicht tegen elkaar liggen.

(interactieve? illustratie -> tonen dat rico niet veranderd als punten heel dicht tegen elkaar liggen)

*Nog korter schrijven, of opsplitsen*
Nu, die rechten zijn natuurlijk een speciaal geval waar de afgeleide altijd gelijk is aan de rico. Een rico betekent eigenlijk ook niet veel voor functies die geen rechte zijn. Maar, er is een speciaal geval wanneer de rico toch iets betekent. We hebben al gzien dat de formule van de rico heel hard lijkt op die van de afgeleide, maar bij de afgeleide nog een limiet in de formule staat. Voor een rechte konden we de limiet weglaten, omdat die niets veranderd. In het algemeen kan dat niet, maar we kunnen er toch voor zorgen dat de formule van de rico gelijk wordt aan die van de afgeleide. Als we $a$ en $b$ heel dicht tegen elkaar plaatsen, zo dicht, dat er zelfs geen haar meer tussen past (*mogelijkheid voor beter mopje*) dan zijn de twee formules gelijk. Allemaal mooi en wel, maar betekend die rico dan nog iets? We leggen het onder de illustratie uit!

(illustratie, twee punten dichterbij elkaar, raaklijn)

Zie je wat er gebeurd als $a$ en $b$ heel dicht tegen elkaar liggen? De rechte die dan door $a$ en $b$ loopt (en waarvan we de rico berekenen) wordt dan een raaklijn aan de rechte in $a$. 


Herinneren aan formule van rico die ze geleerd hebben bij eerstegraadsfuncties: verschil van y-waarden van twee punten gedeeld door verschil van x-waarden van twee punten.
Vervolgens: link met formule van afgeleiden. Bij afgeleiden liggen onze twee punten gewoon heel dicht bij elkaar door limiet. Afgeleide is dus rico (want zelfde formule als rico) van raaklijn (want twee punten liggen dicht bij elkaar).

Op het einde: zeggen dat je dus een idee van de snelheid kan krijgen door te kijken naar hoe steil de plaatsgrafiek is. Vraag: waar rijdt Maria het snelst?