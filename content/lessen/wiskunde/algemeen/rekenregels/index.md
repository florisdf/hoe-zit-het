---
title: "Rekenregels"
date: 2018-10-19T22:00:00+02:00
draft: true
tags: ["Rekenregels", "Volgorde van de bewerkingen"]
categories: ["wiskunde", "getallen", "1e middelbaar"]
---
Over rekenregels gaan we vaak nogal snel over. De volledige wiskunde is echter
uit die rekenregels ontstaan en bouwt erop verder. Als we de rekenregels dus
niet grondig begrijpen, staat onze wiskunde op losse schroeven. Misschien
daarom toch nog eens best alles proper opsommen (ba dum tss :drum: :trollface:).

## De verkeersregels van het rekenen
Hoe moet je een wiskundige uitdrukking als
$\def\vb{\clra{ 4 - 5 \cdot 8 ^ 2} }$
$\vb$
uitrekenen?

Zo?
\begin{equation}
    \begin{split}
        \neg{4 - 5} \cdot 8 ^ 2
        &= \neg{-1} \cdot 8 ^ 2 \\\\\
        &= -8 ^ 2 \\\\\
        &= \neg{-64}
    \end{split}
    \label{eq:sumfirst}
\end{equation}

Of zo?
\begin{equation}
    \begin{split}
        4 - \neg{5 \cdot 8} ^ 2
        &= 4 - \neg{40}^2 \\\\\
        &= 4 - \neg{1600} \\\\\
        &= \neg{- 1596}
    \end{split}
    \label{eq:multfirst}
\end{equation}

 Of misschien zo?
\begin{equation}
    \begin{split}
        4 - 5 \cdot \pos{8 ^ 2}
        &= 4 - 5 \cdot 64 \\\\\
        &= 4 - \pos{5 \cdot 64} \\\\\
        &= 4 - 320 \\\\\
        &= \pos{- 316}
    \end{split}
    \label{eq:expfirst}
\end{equation}

Welke van die manieren is juist: methode \ref{eq:sumfirst}, \ref{eq:multfirst} of
\ref{eq:expfirst}? De **volgorde van de bewerkingen** geeft ons enkele
voorrangsregels voor berekeningen zoals $\vb$.

{{% attention "Afspraak" %}}
Bij bewerkingen spreken we de volgende **voorrangsregels** af (A.K.A. *de
volgorde van de bewerkingen*):

1. **Haakjes** hebben voorrang op **alles**;\\
2. **Machten** {{% mute "(en wortels)" %}} hebben voorrang op
**vermenigvuldigingen** {{% mute "(en delingen)" %}};\\
3. **Vermenigvuldingen** {{% mute "(en delingen)" %}} hebben voorrang op
    **sommen** {{% mute "(en aftrekkingen)" %}}.
{{% /attention %}}

We zullen die voorrangsregels eens toepassen op $ \clra{4 - 5 \cdot 8 ^ 2} $.

Er staan $3$ verschillende bewerkingen: min, maal en een macht. Moeten we eerst
$\clra{4 - 5}$ doen of eerst $\clra{5 \cdot 8}$ of eerst $\clra{8 ^ 2}$? De
regels zeggen: *"Machten hebben
voorrang op vermenigvuldigingen"*, de eerste stap is dus om de macht uit te rekenen:
$$ 4 - 5 \cdot \pos{8 ^ 2} = 4 - 5 \cdot \pos{64}$$

Nu zijn er nog $2$ bewerkingen: min en maal. Eerst $\clra{4 - 5}$ of eerst
$\clra{5 \cdot 64}$? *"Vermenigvuldingen hebben voorrang op sommen {{%
        mute "(en aftrekkingen)" %}}"*, dus:
$$ 4 - \pos{5 \cdot 64} = 4 - \pos{320} $$

Tenslotte blijft er maar $1$ bewerking over; een aftrekking:
$$ \pos{4 - 320} = \pos{-316} $$

De juiste manier om $\vb$ uit te rekenen, is dus zoals in methode
$\ref{eq:expfirst}$.

### De lagen van een uitdrukking
Ik vind het het eenvoudigst om in een wiskundige uitdrukking als $\vb$
verschillende *laagjes* te onderscheiden. De onderste laagjes moeten eerst
uitgerekend worden, dan de laagjes erboven. De uiteindelijke uitkomst krijg je
als de bovenste laag is uitgerekend.

#### Termen
$\def\vbba{\clra{ -6 + 9 - 75 }}$
De bovenste laag is de laag met de *termen*. **Termen** zijn de stukken van een
**optelling**. Bv. $\vbba$ bevat *drie* termen: $\clra{-6}$ en $\clra{9}$ en
$\clra{-75}$. Merk op hoe het minnetje van $\clra{-6}$ en $\clra{-75}$ bij de
term horen. De bovenste laag van $\vbba$ bevat dus *drie* stukken:
$(\clra{-6}) + (\clra{9}) + (\clra{-75})$.

$\def\vbbb{\clrb{ -3 \cdot 2 + 9 - 25 \cdot 3 }}$
Ander voorbeeld: de termen van $\vbbb$ zijn $\clrb{-3 \cdot 2}$ en $\clrb{9}$ en
$\clrb{-25 \cdot 3}$. Die uitdrukking bevat weer drie stukken in die bovenste
laag van termen:
$(\clrb{ -3 \cdot 2 }) + (\clrb{9}) + ( \clrb{- 25 \cdot 3} )$.

$\def\vbbc{\clrc{ -3 \cdot 2 + 3^2 - 5^2 \cdot 3 }}$
En $\vbbc$ heeft ook weer drie stukken in de bovenste laag:
$(\clrc{ -3 \cdot 2 }) + (\clrc{3^2}) + ( \clrc{- 5^2 \cdot 3} )$.

Je ziet dat de stukken in die bovenste laag (de *termen*) heel ingewikkeld
kunnen worden. $\clrc{- 5^2 \cdot 3}$ is bijvoorbeeld één grote term, maar
$\clra{-75}$ is evenzeer één term. Om de bovenste laag te kunnen uitrekenen,
moeten alle termen gewoon getallen zijn zoals bij $\vbba$. Pas dan kunnen we de
volledige uitkomst vinden, hier $\clra{-72}$.

#### Factoren
De laag *onder* de termen is de laag met de *factoren*. **Factoren** zijn de stukken
van een **vermenigvuldiging**. $\clrb{-3 \cdot 2}$ bevat drie factoren:
$\clrb{-1}$ en $\clrb{3}$ en $\clrb{2}$. Maar $\clrc{- 5^2 \cdot 3}$ bevat er
ook drie: $\clrc{-1}$ en $\clrc{5^2}$ en $\clrc{3}$. Merk op hoe we het
minteken als een factor $-1$ zien. We zien $\clrb{-3 \cdot 2}$ dus als
$\clrb{-1 \cdot 3 \cdot 2}$ waardoor het inderdaad *drie* factoren heeft.

Termen bevatten altijd één of meerdere factoren. De uitdrukking
$\vbbb$ bevatte drie *termen*. Elk van die termen bevat ook een aantal
*factoren*:

* De eerste term $\clrb{-3 \cdot 2}$ bevat *drie* factoren: $\clrb{-1}$ en $\clrb{3}$ en
$\clrb{2}$;
* De tweede term $\clrb{9}$ bevat *één* factor: $\clrb{9}$;
* De derde term $\clrb{- 25 \cdot 3}$ bevat drie factoren: $\clrb{-1}$ en $\clrb{25}$
en $\clrb{3}$.

Om de laag met de factoren te
kunnen uitrekenen, moeten alle factoren gewoon getallen zijn. Dat is bij de
drie termen hierboven het geval. We kunnen de drie termen dus elk berekenen.

* De eerste term is $\clrb{-3 \cdot 2} = \clrb{-1} \cdot \clrb{3} \cdot \clrb{2} =
\clra{-6}$;
* De tweede term is $\clra{9}$;
* De derde term is $\clrb{-25 \cdot 3} = \clrb{-1} \cdot \clrb{25} \cdot \clrb{3} =
\clra{-75}$;

We hebben de laag met de *factoren* uitgerekend en we krijgen zo voor iedere
term een gewoon getal. We kunnen dus nu ook de bovenste laag met de *termen*
uitrekenen:
$(\clra{-6}) + (\clra{9}) + (\clra{-75}) = \clra{-72}$.

#### Machten
Een **macht** is de combinatie van een **grondtal** en een **exponent**.
Bijvoorbeeld de macht $\clrc{5^2}$ bevat het grondtal $\clrc{5}$ en de exponent
$\clrc{2}$.
De *machten* zitten nog een laagje dieper dan de factoren. We hebben namelijk
gezien dat een factor gewoon $\clrb{3}$ kan zijn (zoals in $\clrb{-3 \cdot
2}$), maar dat een factor ook $\clrc{5^2}$ kan zijn (zoals in $\clrc{-5^2 \cdot
3}$). Voor we de laag van de factoren kunnen uitrekenen, moeten we dus zorgen
dat alle machten zijn uitgerekend.

We hadden al gezien dat $\vbbc$ drie *termen* bevat. Elk van die termen bevat een
aantal *factoren*. En elk van die factoren bevat op zijn beurt een aantal
*machten*.

* De eerste term $\clrc{-3 \cdot 2}$ bevat drie factoren
    - De eerste factor is $\clrb{-1}$
    - De tweede factor is $\clrb{3}$
    - De derde factor is $\clrb{2}$
* De tweede term $\clrc{3^2}$ bevat één factor
    - De factor is $\clrc{3^2}$ en is een macht: $\clrc{3^2} = \clrb{9}$
* De derde term $\clrc{-5^2 \cdot 3}$ bevat drie factoren
    - De eerste factor is $\clrb{-1}$ 
    - De tweede factor is $\clrc{5^2}$ en is een macht: $\clrc{5^2} = \clrb{25}$
    - De derde factor is $\clrb{3}$

We hebben nu de onderste laag van machten uitgerekend en de resultaten staan in
het $\clrb{blauw}$. Wanneer we die opnieuw in een uitdrukking gieten, krijgen
we $\vbbb$. Deze bevat enkel nog *termen* en *factoren*. Voor we alle termen
kunnen combineren, moeten we eerst alle factoren uitgerekend hebben.

* De eerste term is $\clrb{-3 \cdot 2} = \clrb{-1} \cdot \clrb{3} \cdot \clrb{2} =
\clra{-6}$;
* De tweede term is $\clra{9}$;
* De derde term is $\clrb{-25 \cdot 3} = \clrb{-1} \cdot \clrb{25} \cdot \clrb{3} =
\clra{-75}$;

Nu is ook de laag van de *factoren* uitgerekend en kunnen we alle termen
combineren.

De uitdrukking is gelijk aan $\vbba = \clra{-72}$.
