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

## De volgorde van bewerkingen
Hoe moet je
$ \clra{ 4 - 5 \cdot 8 ^ 2} $
uitrekenen?

Zo?
\begin{equation}
    \begin{split}
        \clrneg{4 - 5} \cdot 8 ^ 2
        &= \clrneg{-1} \cdot 8 ^ 2 \\\\\
        &= -8 ^ 2 \\\\\
        &= \clrneg{-64}
    \end{split}
    \label{eq:sumfirst}
\end{equation}

Of zo?
\begin{equation}
    \begin{split}
        4 - \clrneg{5 \cdot 8} ^ 2
        &= 4 - \clrneg{40}^2 \\\\\
        &= 4 - \clrneg{1600} \\\\\
        &= \clrneg{- 1596}
    \end{split}
    \label{eq:multfirst}
\end{equation}

 Of misschien zo?
\begin{equation}
    \begin{split}
        4 - 5 \cdot \clrpos{8 ^ 2}
        &= 4 - 5 \cdot 64 \\\\\
        &= 4 - \clrpos{5 \cdot 64} \\\\\
        &= 4 - 320 \\\\\
        &= \clrpos{- 316}
    \end{split}
    \label{eq:expfirst}
\end{equation}

Welke van die manieren is juist: \ref{eq:sumfirst}, \ref{eq:multfirst} of
\ref{eq:expfirst}? De **volgorde van de bewerkingen** geeft ons enkele
voorrangsregels voor berekeningen zoals $ 4 - 5 \cdot 8 ^ 2$.

{{% attention "Afspraak" %}}
Bij bewerkingen spreken we de volgende **voorrangsregels** af:

1. Haakjes hebben voorrang op de macht;\\
2. De macht heeft voorrang op het product;\\
3. Het product heeft voorrang op de som.
{{% /attention %}}

Merk op dat we niets over wortels, delingen en aftrekkingen hebben gezegd. Dat
is omdat die drie eigenlijk speciale gevallen zijn van machten, producten en
sommen:

1. Een wortel is een macht: $\sqrt[b]{a} = a\clrneut{^{1/b}}$
1. Een deling is een product: $\frac{a}{b} = a \clrneut{\cdot} b^{-1}$
1. Een aftrekking is een som: $a - b = a \clrneut{+} (-b)$

We zullen die voorrangsregels eens toepassen op $ \clra{4 - 5 \cdot 8 ^ 2} $.

Er staan $3$ verschillende bewerkingen: min, maal en een macht. Moeten we eerst
$\clra{4 - 5}$ doen of eerst $\clra{5 \cdot 8}$ of eerst $\clra{8 ^ 2}$? De regels zeggen: *"De macht heeft
voorrang op het product"*, de eerste stap is dus om de macht uit te rekenen:
$$ 4 - 5 \cdot \clrpos{8 ^ 2} = 4 - 5 \cdot \clrpos{64}$$

Nu zijn er nog $2$ bewerkingen: min en maal. Eerst $\clra{4 - 5}$ of eerst
$\clra{5 \cdot 64}$ doen? *"Het product heeft voorrang op de som"*, dus:
$$ 4 - \clrpos{5 \cdot 64} = 4 - \clrpos{320} $$

Tenslotte blijft er maar $1$ bewerking over; een aftrekking:
$$ \clrpos{4 - 320} = \clrpos{-316} $$

### Kijk enkel naar de rechtstreekse buren

## Optellen (en aftrekken)
**Zie een minteken als een toestandsteken, niet als een bewerking**

## Vermenigvuldigen (en delen)

## Machten (en wortels)

## Extra: merkwaardige producten
Niets meer en niets minder dan *shortcuts*
