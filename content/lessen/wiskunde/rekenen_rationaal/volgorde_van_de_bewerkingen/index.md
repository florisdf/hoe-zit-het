---
title: "Volgorde van de bewerkingen"
date: 2018-10-19T22:00:00+02:00
weight: 7
draft: false
wiski: "http://wiski.be/oefenen/volgorde-van-bewerkingen-0/take"
tags: ["Rekenregels", "Volgorde van de bewerkingen"]
categories: ["wiskunde", "getallen", "1e middelbaar"]
images: []
tags: ["Volgorde van bewerkingen", "Rekenen", "Bewerkingen"]
description: "In deze les leren we over de verkeersregels in de wiskunde. We leren
de volgorde van bewerkingen en bekijken wat we eerst moeten uitrekenen."
---
Over rekenregels gaan we vaak nogal snel over. De volledige wiskunde is echter
uit die rekenregels ontstaan en bouwt erop verder. Als we de rekenregels dus
niet grondig begrijpen, staat onze wiskunde op losse schroeven. Misschien
daarom toch nog eens best alles proper opsommen (ba dum tss 🥁).

## De verkeersregels van het rekenen
Hoe moet je een wiskundige uitdrukking als
$\def\vba{4 - 5 \cdot 8 ^ 2}$
$\vba$
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
        &= 4 - 5 \cdot \pos{64} \\\\\
        &= 4 - \pos{320} \\\\\
        &= \pos{- 316}
    \end{split}
    \label{eq:expfirst}
\end{equation}

Welke van die manieren is juist: methode \ref{eq:sumfirst}, \ref{eq:multfirst} of
\ref{eq:expfirst}? De **volgorde van de bewerkingen** geeft ons enkele
voorrangsregels voor berekeningen zoals $\vba$.

{{< attention "Afspraak" >}}
Bij bewerkingen spreken we de volgende **voorrangsregels** af (A.K.A. *de
volgorde van de bewerkingen*):

1. **Haakjes** hebben voorrang op **alles**;
2. **Machten** {{< mute "(en wortels)" >}} hebben voorrang op
**vermenigvuldigingen** {{< mute "(en delingen)" >}};
3. **Vermenigvuldingen** {{< mute "(en delingen)" >}} hebben voorrang op
   **optellingen** {{< mute "(en aftrekkingen)">}};
4. **Optellingen** {{< mute "(en aftrekkingen)">}} hebben voorrang op **niets**.
{{< /attention >}}

De {{< mute "lichtgrijze" >}} bewerkingen hebben dezelfde voorrang als de
bewerking waar ze bij staan. Een vermenigvuldiging en een deling hebben dus
allebei voorrang op een som en een aftrekking. Wanneer twee zulke bewerkingen
na elkaar geschreven staan (dus bv. een deling en dan een vermenigvuldiging),
spreken we af om gewoon **van links naar rechts** te werken.
De uitdrukking $8 \div 4 \cdot 3$ rekenen we dus uit als
\begin{split}
    \pos{8 \div 4} \cdot 3
    &= \pos{2} \cdot 3 \\\\\
    &= \pos{6}
\end{split}
omdat we de deling eerst tegenkomen wanneer we van links naar rechts lezen.

We zullen die volgorde van de bewerkingen eens toepassen op $\vba$.

Er staan $3$ verschillende bewerkingen: min, maal en een macht. Moeten we eerst
$\clra{4 - 5}$ doen of eerst $\clra{5 \cdot 8}$ of eerst $\clra{8 ^ 2}$? De
regels zeggen: *"Machten hebben
voorrang op vermenigvuldigingen"*, de eerste stap is dus om de macht uit te rekenen:

$$ 4 - 5 \cdot \clra{8 ^ 2} = 4 - 5 \cdot \clra{64}$$

Nu hebben we de uitdrukking $4 - 5 \cdot 64$ met nog twee bewerkingen:
min en maal. Eerst $\clra{4 - 5}$ of eerst $\clra{5 \cdot 64}$?
*"Vermenigvuldingen hebben voorrang op optellingen {{< mute "(en aftrekkingen)" >}}"*, dus:

$$ 4 - \clra{5 \cdot 64} = 4 - \clra{320} $$

Tenslotte hebben we de uitdrukking $4 - 320$ en blijft er maar één
bewerking over; een aftrekking:

$$ \clra{4 - 320} = \clra{-316} $$

De juiste manier om $\vba$ uit te rekenen, is dus zoals in methode
$\ref{eq:expfirst}$.

## Een ingewikkelder voorbeeld
In plaats van langzaam op te bouwen naar een ingewikkeld voorbeeld, zullen we
meteen eens een monster van uitdrukking uitrekenen.
$$-(4 - 7)^2 \cdot 2 + \sqrt{9 \cdot 4} \div 3 - \frac{4 \cdot 3}{-5 + 7}$$

Hoe kan je zoiets uitrekenen? De volgorde van de bewerkingen leidt er ons
stapje per stapje door. Ze zegt dat de **haakjes** altijd eerst moeten worden
uitgerekend, zij hebben voorrang op **alles**. Hier staan **vier** dingen tussen haakjes:
$$-(\clra{4 - 7})^2 \cdot 2 + \sqrt{\clra{9 \cdot 4}} \div 3 - \frac{\clra{4 \cdot 3}}{\clra{-5 + 7}}$$

Merk op dat we de *teller* en *noemer* van een breuk ook als iets tussen haakjes zien. Dat
komt omdat we een breuk zoals bijvoorbeeld $\frac{1 - 4}{3 + 2}$ ook kunnen schrijven als
een deling $(1 - 4) \div (3 + 2)$. De teller en noemer staan dus eigenlijk tussen haakjes. Ook alles wat *onder een wortel* staat, staat eigenlijk tussen haakjes.
Al die haakjes uitrekenen is snel gebeurd:
$$-(\clra{-3})^2 \cdot 2 + \sqrt{\clra{36}}\div 3 - \frac{\clra{12}}{\clra{2}}$$

De uitdrukking wordt al meteen een pak eenvoudiger. Na de haakjes hebben de
**machten en wortels** voorrang. Er zijn **twee** machten en wortels:
$$-\clra{(-3)^2} \cdot 2 + \clra{\sqrt{36}}\div 3 - \frac{12}{2}$$

Deze macht en wortel uitrekenen geeft:
$$-\clra{9} \cdot 2 + \clra{6}\div 3 - \frac{12}{2}$$

Onthoud dat een negatief getal kwadrateren (zoals $\clra{(-3)^2}$), een
positief getal oplevert (hier $\clra{9}$). Het minnetje voor de $\clra{9}$ in
de bovenstaande uitdrukking komt van het zwarte minnetje dat helemaal vooraan stond
bij $-\clra{(-3)^2}$.

Na de machten en wortels, hebben de **vermenigvuldigingen en delingen**
voorrang. Zo zijn er **drie**:
$$\clra{-9 \cdot 2} + \clra{6\div 3} - \clra{\frac{12}{2}}$$

Herinner je dat een breuk gewoon een deling is van de *teller* gedeeld door de
*noemer*. De vermenigvuldigingen en delingen uitrekenen geeft:
$$\clra{-18} + \clra{2} - \clra{6}$$

Er schiet enkel nog een eenvoudig sommetje over met enkel optellingen en
aftrekkingen. Die werken we gewoon uit van links naar rechts:
$$\clra{-18 + 2 - 6} = \clra{-22}$$

## Volledige uitdrukkingen binnen haakjes
Het "leuke" aan haakjes is dat ze volledige uitdrukkingen kunnen bevatten. In
het voorgaande voorbeeld bevatten de haakjes nooit echt iets ingewikkelds.
Moest er wel een grote uitdrukking in de haakjes zitten, dan pas je op die
uitdrukking binnen de haakjes natuurlijk ook gewoon de volgorde van de
bewerkingen toe.

Bijvoorbeeld
$$-5^3 + \frac{\sqrt{-6 + 5^2 \cdot 2}}{2}$$

In de teller staat een uitdrukking op zich:
$$\sqrt{-6 + 5^2 \cdot 2}$$

Hier passen we apart de volgorde van de bewerkingen op toe. Het resultaat
stoppen we dan in de oorspronkelijke uitdrukking.
\begin{equation}
    \begin{split}
        \sqrt{-6 + \clra{5^2} \cdot 2}
        &= \sqrt{-6 + \clra{25} \cdot 2} \\\\\
        &= \sqrt{-6 + \clra{25 \cdot 2}} \\\\\
        &= \sqrt{-6 + \clra{50}} \\\\\
        &= \sqrt{\clra{-6 + 50}} \\\\\
        &= \sqrt{\clra{44}} \\\\\
        &= \clra{\sqrt{44}} \\\\\
        &\approx \clra{6{,}63\ldots}
    \end{split}
\end{equation}

De oorspronkelijke uitdrukking wordt dus:
$$-5^3 + \frac{\clra{6{,}63\ldots}}{2}$$

Hier kan je weer de volgorde van de bewerkingen op toepassen. Je zult vinden
dat de uitdrukking gelijk is aan $\clra{-121{,}6}$ (afgerond op 1 cijfer na de
komma).
