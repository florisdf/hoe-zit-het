---
title: "Nulpunten en nulwaarden"
date: 2018-07-01T22:13:11+02:00
draft: false
weight: 6
tags: ["nulpunt van een functie", "nulwaarde van een functie", "nulpunt", "nulwaarde", "nulpunt op een grafiek"]
description: "Wat is een nulpunt van een functie? Wat is een nulwaarde van een functie? In deze les leggen we deze begrippen uit. Naast een analytische uitleg, tonen we op een grafiek hoe je nulpunten kan herkennen."
images: ['/lessen/wiskunde/functies/nulpunten/plt/nulpunten.png']
---
In veel toepassingen van functies zijn we geïnteresseerd in de waarde die we
voor $x$ moeten kiezen zodat $f(x)$ gelijk wordt aan nul. Een $\orange{x}$ die zorgt dat
$f(\orange{x}) = 0$, noemen we een **nulwaarde**. Het bijhorend **nulpunt** is
dan $(\orange{x},~0)$.

## Nulwaarden van een functie
Stel dat we een $x$ in het machientje stoppen en dat er $0$ uit komt. Dan noemen
we $x$ een **nulwaarde** van de functie. Bijvoorbeeld voor de functie met als
[functievoorschrift](../voorschrift)
$$f(x) = x - 2$$
is $x=\orange{2}$ een nulwaarde want $f(\orange{2}) = \orange{2} - 2 = 0$.

Je vindt de nulwaarden van een functie door **het functievoorschrift gelijk te
stellen aan nul** en die [vergelijking op te lossen](../../1g_vgl/oplossen). We
stellen het functievoorschrift gelijk aan *nul* omdat we op zoek zijn naar de
x-waarden die het voorschrift {{< mute "en dus de y-waarde" >}} *nul* maken.
Voor het bovenstaande voorbeeld:

\begin{split}
    f(x) = 0 \\\\\
    \Leftrightarrow x - 2 = 0 \\\\\
    \Leftrightarrow x = 2
\end{split}

We vinden inderdaad de nulwaarde $x=2$.

## Nulpunten van een functie
De namen *nulpunten* en *nulwaarden* worden soms door elkaar gebruikt, maar
strikt gezien zijn ze niet hetzelfde. Nul*waarden* zijn x-*waarden*, maar
nul*punten* zijn *punten* met een x- én y-coördinaat. De x-coördinaat van een
nulpunt is de nul*waarde*. De y-coördinaat van een nulpunt is altijd *nul*
{{< mute "(uiteraard)" >}}. Als de nulwaarde bijvoorbeeld $\orange{-2}$ is, dan is het
nulpunt $(\orange{-2},~0)$.

## Nulpunten op een grafiek
We kunnen een functie voorstellen met een [grafiek](../grafiek) door de x- en
y-waarden als x- en y-coördinaten te interpreteren. De nulpunten van een
functie kan je snel op de grafiek vinden omdat je weet dat de **y-coördinaat van
een nulpunt altijd 0 is**. Nulpunten zijn met andere woorden de punten waar de
**grafiek de x-as snijdt**.

Hieronder staat de grafiek getekend van de functie $f(x) = -x^2 + 9$ die de
nul*waarden* $x=-3$ en $x=3$ heeft en dus de nul*punten* $(-3,~0)$ en $(3,~0)$.
De twee nulpunten zijn aangeduid in het **{{< class "oranje" "orange" >}}**.

{{< bokeh "plt/nulpunten.json" >}}

## Samengevat
{{< attention "Definitie nulwaarden" >}}
De **nulwaarden van een functie** zijn de **x-waarden waarvoor de
functiewaarde gelijk is aan 0**.
{{< /attention >}}

{{< attention "Definitie nulpunten" >}}
De **nulpunten van een functie** zijn de punten op de grafiek van die functie
die als **y-waarde 0 hebben**. Ze zijn de **snijpunten met de x-as**.
{{< /attention >}}
