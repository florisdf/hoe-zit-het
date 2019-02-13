---
title: "Benaderingsregels"
date: 2019-01-28T08:07:39+01:00
weight: 7
draft: true
tags: []
categories: []
level: ""
course: ""
topic: ""
---
Als we berekeningen doen met metingen, moeten we altijd in ons achterhoofd
houden dat **metingen nooit exact** zijn. Stel dat we bijvoorbeeld een meetlat
naast een LEGO-blokje leggen, en we meten dat de zijde
$1{,}6 \si{ cm}$ is.

{{% img "img/lego_meetlat.svg" %}}

Als we 100 zulke blokjes naast elkaar leggen,
hoe lang zal die rij blokjes dan zijn?

{{% img "img/lego_100_bricks.svg" %}}

Dat lijkt heel eenvoudig, gewoon $100 \cdot 1{,}6 \si{ cm} = 160 \si{ cm}$. We
hebben het blokje echter gemeten met een meetlat die maar tot op $0{,}1 \si{
cm}$ nauwkeurig kan meten. Stel dat we het blokje nu meten met een schuifmaat
die tot op $0{,}01 \si{ cm}$ nauwkeurig kan meten. Nu vinden we dat het blokje
$1{,}58 \si{ cm}$ is.

{{% img "img/lego_schuifmaat.svg" %}}

Als we 100 blokjes naast elkaar zouden leggen, zullen we dus een rij van $158
\si{ cm}$ krijgen, niet $160 \si{ cm}$.

{{% img "img/lego_100_measured.svg" %}}

Met **benaderingsregels** kunnen we de onzekerheid van een berekening
uitdrukken. Als we de benaderingsregels toepassen die we straks zullen leren,
krijgen we $1{,}6 \si{ m}$ voor de eerste berekening en $1{,}58 \si{ m}$ voor
de tweede berekening. Het belangrijke hierbij is dat er $1{,}6$ staat en
**{{% class "niet" "red" %}}**
$1{,}6\red{0}$. 

Met $1{,}6 \si{ m}$ bedoelen we namelijk: "Iets tussen $1{,}55 \si{ m}$ en
$1{,}65 \si{ m}$," en inderdaad, $1{,}58 \si{ m}$
**{{% class "ligt binnen die foutenmarge." "green" %}}**

{{% img "img/lego_100_correct_margin.svg" %}}

Als we bij de eerste berekening $1{,}6\red{0}$ hadden geschreven, zou dat
betekenen: "Iets tussen $1{,}5\red{95} \si{ m}$ en $1{,}6\red{05} \si{ m}$,"
maar
**{{% class "dat is fout" "red" %}}**,
want $1{,}58 \si{ m}$
**{{% class "ligt buiten die foutenmarge." "red" %}}**

{{% img "img/lego_100_wrong_margin.svg" %}}

Door na onze berekeningen benaderingsregels toe te passen, zorgen we dat de
uitkomst de juiste **foutenmarge** heeft.

## Afronden na de komma
Voor we de benaderingsregels uit de doeken doen,
frissen we nog snel even op hoe je getallen moet afronden.

* Rond af naar **boven** als het **volgende cijfer 5 of meer** is;
* Rond of naar **beneden** als het **volgende cijfer 4 of minder** is.

In de volgende voorbeelden ronden we telkens af tot op het **eerste cijfer na
de komma**.  $$3{,}\orange{5}61 \approx 3{,}\orange{6}$$ $$12{,}\orange{9}5
\approx 13{,}\orange{0}$$ $$0{,}\orange{0}12 \approx 0{,}\orange{0}$$

## Afronden vóór de komma
Maar wat als we bijvoorbeeld $5810$ moeten afronden
tot op het **derde cijfer vóór de komma**? Dan zullen we het getal moeten
[omzetten naar een macht van
10](../machten_van_10#getallen-omzetten-naar-een-macht-van-10):

$$5\orange{8}10 \approx 5\orange{8} \cdot 10^2$$


## Optellingen en aftrekkingen
Aantal **cijfers na de komma** is van belang.

## Vermenigvuldigingen en delingen
Aantal **beduidende cijfers** is van belang.
