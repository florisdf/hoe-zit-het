---
title: "Lagen van een uitdrukking"
date: 2018-11-19T22:00:00+02:00
draft: true
tags: ["Rekenregels", "Volgorde van de bewerkingen", "Lagen van een uitdrukking"]
categories: ["wiskunde", "getallen", "algemeen", "1e middelbaar"]
---
## De lagen van een uitdrukking
Ik vind het het eenvoudigst om in een wiskundige uitdrukking als $\vba$
verschillende *laagjes* te onderscheiden. Er zijn 5 lagen:

1. Een *uitdrukking* bestaat uit een of meerdere *termen*;
2. Een *term* bestaat uit een of meerdere *factoren*;
3. Een *factor* kan een *grondtal* en een *exponent* hebben;
4. Een *macht* bestaat uit een of meerdere *deel-uitdrukkingen*.

Iedere laag bestaat dus uit een of meerdere delen. Je kan een laag pas uitrekenen
als je elk van die delen hebt uitgerekend.

### Termen
$\def\vbba{\clra{ -6 + 9 - 75 }}$
$\def\vbbac{\clra{-75}}$
De eerste laag is de laag met termen. We zeggen dat iedere uitdrukking altijd
een of meerdere *termen* bevat. **Termen** zijn de stukken van een
**optelling**. Bijvoorbeeld de uitdrukking $$\vbba$$ bevat *drie* termen:
$\clra{-6}$ en $\clra{9}$ en $\vbbac$. Merk op hoe het minnetje van $\clra{-6}$
en $\vbbac$ bij de term horen. De eerste laag van $\vbba$ bevat dus *drie*
stukken:
$$\big(\clra{-6}\big)\quad
+\quad \big(\clra{9}\big)\quad
+\quad \big( \vbbac \big)$$.

$\def\vbbb{\clrb{ -3 \cdot 2 + 9 - \frac{25 \cdot 6}{2} }}$
$\def\vbbbc{\clrb{- \frac{25 \cdot 6}{2}}}$
Ander voorbeeld: de termen van de uitdrukking  $$\vbbb$$ zijn $\clrb{-3 \cdot
2}$ en $\clrb{9}$ en $\vbbbc$. Die uitdrukking bevat weer drie stukken in die
eerste laag van termen:
$$\big(\clrb{ -3 \cdot 2 }\big)\quad
+\quad \big(\clrb{9}\big)\quad
+\quad \big( \vbbbc \big)$$.

$\def\vbbc{\clrc{ -3 \cdot 2 + 3^2 - \frac{5^2 \cdot \sqrt{36}}{2} }}$
$\def\vbbcc{\clrc{- \frac{5^2 \cdot \sqrt{36}}{2}}}$
We zullen het nog iets ingewikkelder maken. De uitdrukking
$$\vbbc$$
heeft ook weer drie stukken in de eerste laag:
$$\big(\clrc{ -3 \cdot 2 }\big)\quad
+\quad \big(\clrc{3^2}\big)\quad
+\quad \big( \vbbcc \big)$$

$\def\vbbdc{\clrd{-\frac{(9 - 4)^2 \cdot \sqrt{36}}{-5 + 7}}}$
Tenslotte heeft de uitdrukking $$\vbbd$$ ook maar *drie* termen:
$$\big(\clrd{ -(7 - 4) \cdot 2}\big)\quad
+\quad \big(\clrd{(1 + 2)^2}\big)\quad
+\quad \big( \vbbdc \big)$$

Je ziet dat de stukken in die eerste laag (de *termen*) heel ingewikkeld
kunnen worden. $\vbbdc$ is bijvoorbeeld één grote term, maar
$\vbbac$ is evenzeer één term. Om de eerste laag te kunnen uitrekenen,
moeten alle termen gewoon getallen zijn zoals bij $\vbba$. Pas dan kunnen we de
volledige uitkomst vinden door gewoon die getallen op te tellen:
$$\vbba = \clra{-72}$$

### Factoren
De laag *onder* de termen is de laag met de *factoren*. Daarmee bedoelen we dat
een *term bestaat uit een of meerdere factoren*. **Factoren** zijn de stukken
van een **vermenigvuldiging**.

Hierboven zagen we dat $$\vbbbc$$ één term was. Deze *term*
bevat vier *factoren*:
$$\big(\clrb{-1}\big)\quad
\cdot\quad \big(\clrb{25}\big)\quad
\cdot\quad \big(\clrb{6}\big)
\cdot\quad \big(\clrb{ \frac{1}{2} }\big)$$
Merk op hoe we het minteken als een factor $\clrb{-1}$ zien en hoe we de noemer
van de breuk helemaal naar rechts schuiven en schrijven als een aparte factor
$\clrb{ \frac{1}{2}}$.

De term $$\vbbcc$$ bevat
ook vier factoren:
$$\big(\clrc{-1}\big)\quad
\cdot\quad \big(\clrc{5^2}\big)\quad
\cdot\quad \big(\clrc{\sqrt{36}}\big)\quad
\cdot\quad \big(\clrc{ \frac{1}{2} }\big)$$

Tenslotte, de term
$$\vbbdc$$
bevat ook weer *vier* factoren:
$$\big(\clrd{-1}\big)\quad
\cdot\quad \big(\clrd{(9 - 4)^2}\big)\quad
\cdot\quad \big(\clrd{\sqrt{36}}\big)\quad
\cdot\quad \big(\clrd{ \frac{1}{-5 + 7} }\big)\quad
$$

Als we een volledige uitdrukking met **meerdere termen** bekijken, zoals
$\vbbb$, kunnen we nu voor iedere *term* zeggen welke *factoren* er zijn:

* De eerste term $\clrb{-3 \cdot 2}$ bevat *drie* factoren: $\clrb{-1}$ en $\clrb{3}$ en
$\clrb{2}$;
* De tweede term $\clrb{9}$ bevat *één* factor: $\clrb{9}$;
* De derde term $\clrb{- 25 \cdot 3}$ bevat drie factoren: $\clrb{-1}$ en $\clrb{25}$
en $\clrb{3}$.

Om de laag met de factoren te
kunnen uitrekenen, moeten alle factoren gewoon getallen zijn. Dat is bij de
drie termen hierboven het geval. We kunnen de drie termen dus elk berekenen
door alle factoren per term te vermenigvuldigen.

* De eerste term is $\clrb{-3 \cdot 2} = \clrb{-1} \cdot \clrb{3} \cdot \clrb{2} =
\clra{-6}$;
* De tweede term is $\clra{9}$;
* De derde term is $\clrb{-25 \cdot 3} = \clrb{-1} \cdot \clrb{25} \cdot \clrb{3} =
\clra{-75}$;

We hebben de laag met de *factoren* uitgerekend en we krijgen zo voor iedere
term een gewoon getal. We kunnen dus nu ook de eerste laag met de *termen*
uitrekenen:
$(\clra{-6}) + (\clra{9}) + (\clra{-75}) = \clra{-72}$.

### Machten
De derde laag is de laag met *machten*. Deze laag zit net onder de laag met de
factoren. In principe bevat iedere *factor* een **grondtal** en een
**exponent**, maar als de exponent gelijk is aan $1$, heeft het niet veel zin
om echt van een *exponent* te spreken.

Bij de factor $\clrc{5^2}$ is het grondtal duidelijk $\clrc{5}$
en de exponent $\clrc{2}$. Als de factor gewoon een getal is zoals $\clrc{-1}$
is het grondtal $\clrc{-1}$ en de exponent eigenlijk $1$ omdat je kan zeggen
dat $\clrc{-1} = (\clrc{-1})^\clrc{1}$. Maar in dat geval spreken we meestal
niet van een exponent.

Een speciaal geval van machten zijn de *wortels*. Een *vierkantswortel* komt
eigenlijk overeen met een exponent van $\frac{1}{2}$, dus $\clrc{\sqrt{36}} =
(\clrc{36})^\clrc{\frac{1}{2}}$. Waarom dit zo is, leggen we in een latere les
uit. Voorlopig mag je er gewoon van uitgaan dat een *wortel* een speciaal soort
*exponent* is.

We hadden al gezien dat $\vbbc$ drie *termen* bevat. Elk van die termen bevat een
aantal *factoren*. En elk van die factoren bevat op zijn beurt een aantal
*machten*.

* De eerste term $\clrc{-3 \cdot 2}$ bevat drie factoren
    - De eerste factor is $\clrb{-1}$
    - De tweede factor is $\clrb{3}$
    - De derde factor is $\clrb{2}$
* De tweede term $\clrc{3^2}$ bevat één factor
    - De factor is $\clrc{3^2}$ en is een macht: $\clrc{3^2} = \clrb{9}$
* De derde term $\vbbcc$ bevat vier factoren
    - De eerste factor is $\clrb{-1}$ 
    - De tweede factor is $\clrc{5^2}$ en is een macht: $\clrc{5^2} = \clrb{25}$
    - De derde factor is $\clrb{\sqrt{36}}$ en een wortel:
    $\clrc{\sqrt{36}} = \clrb{6}$
    - De vierde factor is $\clrb{\frac{1}{2}}$

We hebben nu de onderste laag van machten uitgerekend en de resultaten staan in
het $\clrb{blauw}$. Wanneer we die opnieuw in een uitdrukking gieten, krijgen
we $\vbbb$. Deze bevat enkel nog *termen* en *factoren*. Voor we alle termen
kunnen combineren, moeten we eerst de laag van de factoren uitgerekend hebben.

* De eerste term is $\clrb{-3 \cdot 2} = \clrb{-1} \cdot \clrb{3} \cdot \clrb{2} =
\clra{-6}$;
* De tweede term is $\clra{9}$;
* De derde term is $\clrb{-25 \cdot 3} = \clrb{-1} \cdot \clrb{25} \cdot \clrb{3} =
\clra{-75}$;

Nu is ook de laag van de *factoren* uitgerekend en kunnen we alle termen
combineren.

De uitdrukking is gelijk aan $\vbba = \clra{-72}$.

### Haakjes
Buiten termen, factoren en machten kunnen er ook haakjes voorkomen in de
uitdrukking. De regel hiervoor is heel eenvoudig: behandel wat in de haakjes
staat als een aparte uitdrukking en reken die **volledig** uit tot je **één
getal** hebt. Vervang de haakjes dan door dat éne getal.
