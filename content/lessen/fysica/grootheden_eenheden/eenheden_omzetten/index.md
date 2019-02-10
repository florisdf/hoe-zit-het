---
title: "Eenheden omzetten"
date: 2019-02-08T07:53:47+01:00
weight: 4
draft: true
tags: []
categories: []
level: ""
course: ""
topic: ""
---
Vaak wordt er gevraagd om een eindresultaat te noteren in [SI-eenheden](../intro#si-eenheden-maken-duidelijke-afspraken), terwijl de opgave niet in SI-eenheden gegeven is. Dan is het belangrijk om die eenheden te kunnen omzetten naar de SI-eenheden.

Soms zullen we een eenheid ook omzetten om beter te begrijpen wat ze betekent. Zo kunnen we ons beter voorstellen hoe lang 2 uren duren, eerder dan hoe lang 7200 seconden duren, ondanks dat de seconde de SI-eenheid van tijd is.

Er zijn dus verschillende situaties waarbij we eenheden zullen moeten omzetten. In deze les bespreken we hoe je zulke omzettingen kan doen.


## Van en naar prefixen
In de les over [prefixen](../prefixen) zagen we al hoe we eenheden konden omzetten waarvan enkel de prefix verschilde. Hierin zijn drie gevallen te onderscheiden:

1. Het [wegwerken van een prefix](../prefixen#prefixen-wegwerken), zoals van $\si{km}$ naar $\si{m}$;
2. Het [toevoegen van een prefix](../prefixen#prefixen-toevoegen), zoals van $\si{g}$ naar $\si{kg}$;
3. Het [omzetten van een prefix](../prefixen#prefixen-omzetten), zoals van $\si{mg}$ naar $\si{kg}$.


## Tijden omzetten
Het omzetten van tijden is iets lastiger.
Bijvoorbeeld: uren ($\si{h}$) naar seconden ($\si{s}$), minuten ($\si{min}$) naar seconden, seconden naar uren...
Het belangrijkste om te onthouden, weet je waarschijnlijk al:

$$1 \si{ h} = 60 \si{ min}$$
$$1 \si{ min} = 60 \si{ s}$$


Met de voorgaande 2 gelijkheden, kunnen we alle omzettingen tussen uren,
minuten en seconden doen. Hieronder een samenvatting van alle mogelijke
omzettingen. Leer deze omzettingen alsjeblieft **niet uit je hoofd**. Je
vergeet ze vroeg of laat toch. Probeer in de plaats daarvan telkens de **afleiding te
begrijpen** zodat je deze tijdens een toets snel op een kladblad kan hermaken.
Het enige wat je van buiten moet kennen zijn de bovenstaande 2 gelijkheden.

Merk op: we maken gebruik van de [benaderingsregels](../benaderingsregels) in de kolom met voorbeelden.

### Van uur naar...
| Van           | Naar           | Afleiding                                                                                                                                                                                                                                                                         | Kort gezegd                          | Voorbeeld                                                                                                                                                        |
|---------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $\si{h}$      | $\si{min}$     | /                                                                                                                                                                                                                                                                                 | $1 \si{ h} = 60 \si{ min}$           | \begin{split}8{,}00 \orange{\si{ h}} &= 8{,}00 \cdot \orange{60 \si{ min}}\\\\\ &= 480 \orange{\si{ min}} \end{split} |
| $\si{h}$      | $\si{s}$       | \begin{split}1 \si{ h} &= 60 \orange{\si{ min}}\\\\\ &= 60 \cdot \orange{60 \si{ s}}\\\\\ &= 3600 \orange{\si{ s}}\end{split}                                                                                                                                                     | $1 \si{ h} = 3600 \si{ s}$           | \begin{split}8{,}00 \orange{\si{ h}} &= 8{,}00 \cdot \orange{3600 \si{ s}} \\\\\ &= 28{,}8 \cdot 10^{3} \orange{\si{ s}} \end{split} |

### Van minuut naar...
| Van          | Naar       | Afleiding                                                                                                                                                                                                                                                                                   | Kort gezegd                              | Voorbeeld                                                                                                                                                               |
| ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $\si{min}$   | $\si{h}$   | \begin{split}1 \si{ h} &= 60 \si{ min}\\\\\ &\Updownarrow\\\\\  \frac{1 \si{ h}}{\orange{60}} &= \frac{60 \si{ min}}{\orange{60}}\\\\\ &\Updownarrow\\\\\  \frac{1}{\orange{60}} \si{ h} &= 1 \si{ min} \\\\\ &\Updownarrow\\\\\  1 \si{ min} &= \frac{1}{\orange{60}} \si{ h}\end{split}   | $1 \si{ min} = \frac{1}{60} \si{ h}$     | \begin{split}90{,}0 \orange{\si{ min}} &= 90{,}0 \cdot \orange{\frac{1}{60} \si{ h}}\\\\\ &= \frac{90{,}0}{60} \orange{\si{ h}}\\\\\ &= 1{,}50 \orange{\si{ h}} \end{split}          |
| $\si{min}$   | $\si{s}$   | /                                                                                                                                                                                                                                                                                           | $1 \si{ min} = 60 \si{ s}$             | \begin{split}90{,}0 \orange{\si{ min}} &= 90{,}0 \cdot \orange{60 \si{ s}} \\\\\ &= 5{,}40 \cdot 10^{3} \orange{\si{ s}} \end{split}                                                        |

### Van seconde naar...
| Van        | Naar       | Afleiding                                                                                                                                                                                                                                                                                   | Kort gezegd                              | Voorbeeld                                                                                                                                                                                        |
| ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------------------                          |
| $\si{s}$   | $\si{min}$ | \begin{split}1 \si{ min} &= 60 \si{ s}\\\\\ &\Updownarrow\\\\\  \frac{1 \si{ min}}{\orange{60}} &= \frac{60 \si{ s}}{\orange{60}}\\\\\ &\Updownarrow\\\\\  \frac{1}{\orange{60}} \si{ min} &= 1 \si{ s} \\\\\ &\Updownarrow\\\\\  1 \si{ s} &= \frac{1}{\orange{60}} \si{ min}\end{split}   | $1 \si{ s} = \frac{1}{60} \si{ min}$     | \begin{split}30{,}0 \orange{\si{ s}} &= 30{,}0 \cdot \orange{\frac{1}{60} \si{ min}}\\\\\ &= \frac{30{,}0}{60} \orange{\si{ min}}\\\\\ &= 0{,}500 \orange{\si{ min}} \end{split}                 |
| $\si{s}$   | $\si{h}$   | \begin{split}1 \si{ s} &= \frac{1}{60}\orange{\si{ min}} \\\\\ &=\frac{1}{60}\cdot \orange{\frac{1}{60}\si{ h}}\\\\\ &=\frac{1}{\orange{3600}}\si{ h} \end{split}                                                                                                                           | $1 \si{ s} = \frac{1}{3600} \si{ h}$     | \begin{split}30{,}0 \orange{\si{ s}} &= 30{,}0 \cdot \orange{\frac{1}{3600} \si{ h}}\\\\\ &= \frac{30{,}0}{3600} \orange{\si{ h}}\\\\\ &= 8{,}33\cdot 10^{-3} \orange{\si{ h}} \end{split}       |

## Snelheden omzetten
Door het omzetten van [prefixen](#van-en-naar-prefixen) te combineren met het omzetten van [tijden](#tijden-omzetten), kunnen we $\si{km}/\si{h}$ omzetten naar $\si{m}/\si{s}$ en omgekeerd.

Om $\si{km}/\si{h}$ om te zetten naar $\si{m}/\si{s}$, vervangen we de $\blue{\si{k}}$ door $\blue{10^{3}}$ en de $\orange{\si{h}}$ door $\orange{3600 \si{ s}}$:

\begin{split}
1 \frac{\blue{\si{k}}\si{m}}{\orange{\si{h}}}
&= 1 \cdot \frac{\blue{10^3}\si{ m}}{\orange{3600\si{ s}}}\\\\\
&= \frac{1\cdot \blue{10^3}} {\orange{3600}} \frac{\si{ m}}{\si{s}}\\\\\
&= \frac{1}{3{,}6} \frac{\si{ m}}{\si{s}}
\end{split}

Of kort gezegd:
$$1 \si{ km}/\si{h} = \frac{1}{3{,}6} \si{ m}/\si{s}$$

We kunnen deze vergelijking gebruiken om $\si{km}/\si{h}$ naar $\si{m}/\si{s}$ om te zetten. We kunnen deze vergelijkingen ook [omvormen](../../../wiskunde/vergelijkingen/factoren_omvormen#omvormen-van-frac-x-a-b) naar:

$$1 \si{ m}/\si{s} = 3{,}6 \si{ km}/\si{h}$$

Die gelijkheid kunnen we dan gebruiken om $\si{m}/\si{s}$ om te zetten naar $\si{km}/\si{h}$.

## Volumes omzetten
In het dagelijkse leven drukt men volumes meestal uit in liter ($\si{l}$) of een afgeleide hiervan (vnl. $\si{ml}$, $\si{cl}$ of $\si{dl}$). De SI-eenheid voor volume is echter de kubieke meter ($\si{m}^3$). Een omzetting tussen beiden is niet zo voor de hand liggend. Het belangrijkste dat je moet onthouden is:

$$1 \si{ l} = 1 \si{ dm}^3$$

Hiermee kan je dan aan de slag om de omzetting te doen tussen de liter en de kubieke meter:

\begin{split}
1 \si{ l}
&= 1 \blue{\si{ d}} \si{m}^3\\\\\
&= 1 \cdot (\blue{10^{-1}}\si{ m})^3\\\\\
&= 1 \cdot (\blue{10^{-1}})^3 \si{ m}^3\\\\\
&= 10^{-3} \si{ m}^3
\end{split}

Of kort gezegd:
$$1 \si{ l} = 10^{-3} \si{ m}^3$$

Dit kunnen we ook [omvormen](../../../wiskunde/vergelijkingen/factoren_omvormen#omvormen-van-a-cdot-x-b) naar:
$$1 \si{ m}^3 = 10^{3} \si{ l}$$

Nu kunnen we ook $\si{dl}$ omzetten naar $\si{m}^3$:

\begin{split}
1 \blue{\si{ d}} \orange{\si{l}}
&= 1 \cdot \blue{10^{-1}} \orange{\si{l}}\\\\\
&= 1 \cdot \blue{10^{-1}} \cdot \orange{10^{-3} \si{ m}^3}\\\\\
&= 10^{-4} \si{ m}^3
\end{split}

Of kort gezegd:
$$1 \si{ dl} = 10^{-4} \si{ m}^3$$

Op een gelijkaardige manier kan je vinden dat:
$$1 \si{cl} = 10^{-5} \si{ m}^3$$
$$1 \si{ml} = 10^{-6} \si{ m}^3$$

## Massadichtheid omzetten
Ten slotte tonen we hoe je de omzetting van $\si{g}/\si{ml}$ naar $\si{kg}/\si{m}^3$ kan doen en omgekeerd.

\begin{split}
1 \frac{\si{g}}{\blue{\si{m}}\si{l}}
&= 1 \frac{\si{g}}{\blue{\si{dm}^3}}\\\\\
&= 1 \frac{\si{g}}{\blue{\si{dm}^3}}\\\\\
&= 1 \frac{\si{g}}{\blue{(10^{-1})^3\si{ m}^3}}\\\\\
&= 1 \cdot \frac{1}{10^{-3}}\frac{\si{g}}{\si{m}^3}\\\\\
&= 10^{3}\frac{\si{g}}{\si{m}^3}\\\\\
\end{split}
