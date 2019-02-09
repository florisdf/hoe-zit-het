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
Vaak wordt er gevraagd om een eindresultaat te noteren in [SI-eenheden](../intro#si-eenheden-maken-duidelijke-afspraken), terwijl de opgave niet in SI-eenheden gegeven is. Dan is het belangrijk om die eenheden te kunnen *omzetten naar* SI-eenheden.

## Van en naar prefixen
In de les over prefixen zagen we al hoe we eenheden konden omzetten waarvan enkel de prefix verschilde. Hierin zijn drie gevallen te onderscheiden:

1. Het [wegwerken van een prefix](../prefixen#prefixen-wegwerken), zoals van $\si{km}$ naar $\si{m}$;
2. Het [toevoegen van een prefix](../prefixen#prefixen-toevoegen), zoals van $\si{g}$ naar $\si{kg}$;
3. Het [omzetten van een prefix](../prefixen#prefixen-omzetten), zoals van $\si{mg}$ naar $\si{kg}$.

## Tijden omzetten
Het omzetten van tijden is iets lastiger.
Bijvoorbeeld: dagen ($\si{d}$) naar seconden ($\si{s}$), uren ($\si{h}$) naar seconden, minuten ($\si{min}$) naar dagen...
Het belangrijkste om te onthouden, weet je waarschijnlijk al:

$$1 \si{ d} = 24 \si{ h}$$
$$1 \si{ h} = 60 \si{ min}$$
$$1 \si{ min} = 60 \si{ s}$$


Bovenstaande gelijkheden kan je [omvormen](../../../wiskunde/vergelijkingen/factoren_omvormen#omvormen-van-a-cdot-x-b) naar:

$$1 \si{ h} = \frac{1}{24} \si{ d}$$
$$1 \si{ min} = \frac{1}{60} \si{ h}$$
$$1 \si{ s} = \frac{1}{60} \si{ min}$$

### Van dag naar...
|    Van    |    Naar    |    Voorbeeld    | Samengevat |
|-----------|------------|-----------------|------------|
| $\si{d}$  | $\si{h}$   | \begin{split}7 \orange{\si{ d}} &= 7 \cdot \orange{24 \si{ h}}\\\\\ &= 168 \orange{\si{ h}}\end{split} | $1 \si{ d} = 24 \si{ h}$ |
| $\si{d}$  | $\si{min}$ | \begin{split}7 \orange{\si{ d}} &= 7 \cdot \orange{24 \si{ h}}\\\\\ &= 168 \orange{\si{ h}}\\\\\ &= 168 \cdot \orange{60\si{ min}}\\\\\ &= 10\ 080 \orange{\si{ min}}\end{split} | $1 \si{ d} = 1440 \si{ min}$ |
| $\si{d}$  | $\si{s}$   | \begin{split}7 \orange{\si{ d}} &= 7 \cdot \orange{24 \si{ h}}\\\\\ &= 168 \orange{\si{ h}}\\\\\ &= 168 \cdot \orange{60\si{ min}}\\\\\ &= 10\ 080 \orange{\si{ min}}\\\\\ &= 10\ 080 \cdot \orange{60\si{ s}}\\\\\ &= 604\ 800 \orange{\si{ s}}\end{split} | $1 \si{ d} = 86\ 400 \si{ s}$ |

### Van uur naar...
|    Van    |    Naar    |    Voorbeeld    | Samengevat |
|-----------|------------|-----------------|------------|
| $\si{h}$  | $\si{d}$   | \begin{split}8 \orange{\si{ h}} &= 8 \cdot \orange{\frac{1}{24} \si{ d}}\\\\\ &= \frac{8}{24} \orange{\si{ d}}\\\\\ &\approx 0{,}33 \orange{\si{ d}} \end{split} | $1 \si{ h} = \frac{1}{24} \si{ d}$ |
| $\si{h}$  | $\si{min}$ | \begin{split}8 \orange{\si{ h}} &= 8 \cdot \orange{60 \si{ min}}\\\\\ &= 480 \orange{\si{ min}}\end{split} | $1 \si{ h} = 60 \si{ min}$ |
| $\si{h}$  | $\si{s}$   | \begin{split}8 \orange{\si{ h}} &= 8 \cdot \orange{60 \si{ min}}\\\\\ &= 480 \orange{\si{ min}}\\\\\ &= 480 \cdot \orange{60 \si{ s}}\\\\\ &= 28\ 800\orange{\si{ s}}\end{split} | $1 \si{ h} = 3600 \si{ s}$ |

### Van minuut naar...
|    Van    |    Naar    |    Voorbeeld    | Samengevat |
|-----------|------------|-----------------|------------|
| $\si{min}$| $\si{h}$   | \begin{split}90 \orange{\si{ min}} &= 90 \cdot \orange{\frac{1}{60} \si{ h}}\\\\\ &= \frac{90}{60} \orange{\si{ h}}\\\\\ &= 1{,}5 \orange{\si{ h}} \end{split}  | $1 \si{ min} = \frac{1}{60} \si{ h}$ |
| $\si{min}$| $\si{d}$   | \begin{split}90 \orange{\si{ min}} &= 90 \cdot \orange{\frac{1}{60} \si{ h}}\\\\\ &= \frac{90}{60} \orange{\si{ h}}\\\\\ &= \frac{90}{60} \cdot \orange{\frac{1}{24} \si{ d}}\\\\\ &= \frac{90}{1440} \orange{\si{ d}}\\\\\&= 0{,}0625 \orange{\si{ d}}\end{split} | $1 \si{ min} = \frac{1}{1440} \si{ d}$  |
| $\si{min}$| $\si{s}$   | \begin{split}90 \orange{\si{ min}} &= 90 \cdot \orange{60 \si{ s}}\\\\\ &= 5400 \orange{\si{ s}}\end{split} | $1 \si{ min} = 60 \si{ s}$  |

### Van seconde naar...
|    Van    |    Naar    |    Voorbeeld    | Samengevat |
|-----------|------------|-----------------|------------|
| $\si{s}$  | $\si{min}$ | \begin{split}30 \orange{\si{ s}} &= 30 \cdot \orange{\frac{1}{60} \si{ min}}\\\\\ &= \frac{30}{60} \orange{\si{ min}}\\\\\ &= 0{,}5 \orange{\si{ min}} \end{split} | $1 \si{ s} = \frac{1}{60} \si{ min}$  |
| $\si{s}$  | $\si{h}$   | \begin{split}30 \orange{\si{ s}} &= 30 \cdot \orange{\frac{1}{60} \si{ min}}\\\\\ &= \frac{30}{60} \orange{\si{ min}}\\\\\ &= \frac{30}{60} \cdot \orange{\frac{1}{60} \si{ h}}\\\\\ &= \frac{30}{3600} \orange{\si{ h}}\\\\\ &\approx 0{,}00833 \orange{\si{ h}} \end{split} | $1 \si{ s} = \frac{1}{3600} \si{ h}$  |
| $\si{s}$  | $\si{d}$   | \begin{split}30 \orange{\si{ s}} &= 30 \cdot \orange{\frac{1}{60} \si{ min}}\\\\\ &= \frac{30}{60} \orange{\si{ min}}\\\\\ &= \frac{30}{60} \cdot \orange{\frac{1}{60} \si{ h}}\\\\\ &= \frac{30}{3600} \orange{\si{ h}}\\\\\ &= \frac{30}{3600} \cdot \orange{\frac{1}{24} \si{ d}}\\\\\ &= \frac{30}{86\ 400} \orange{\si{ d}}\\\\\ &\approx 0{,}000347 \orange{\si{ d}} \end{split} | $1 \si{ s} = \frac{1}{86\ 400} \si{ d}$  |

## Snelheden omzetten

## Massadichtheid omzetten