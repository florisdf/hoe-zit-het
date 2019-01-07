---
title: "Tekenschema"
date: 2019-01-04T18:56:13+01:00
weight: 7
draft: false
tags: ["Functies", "Analyse"]
categories: ["wiskunde", "analyse", "3e middelbaar"]
level: "3M"
course: "wiskunde"
topic: "analyse"
---
Een functie kunnen we [voorstellen als een machientje](../intro) waar we een
waarde voor $x$ in stoppen en waar [hoogstens één](../intro#samengevat) waarde
voor $y$ uit komt.

{{% img "img/conveyor_plain.svg" "" %}}

De [nulwaarden](../nulpunten#nulwaarden-van-een-functie) van de functie zeggen
welke x-waarden we in de functie moeten stoppen om als functiewaarde
{{% mute "(of y-waarde)" %}} nul te krijgen. We kunnen nu ook op zoek gaan naar
de x-waarden die een *positieve* functiewaarde opleveren en de x-waarden die
een *negatieve* functiewaarde opleveren.

## Tekenschema vanuit een grafiek
Welke x-waarden welk teken {{% mute "(positief/negatief/nul)" %}} opleveren
voor de y-waarden, vatten we samen in een **tekenschema**
{{% mute "(ook wel \"tekentabel\" of \"tekenverloop\" genoemd)" %}}.
Als de [grafiek van een functie](../grafiek) is gegeven, kunnen we zien waar de
functiewaarden {{% mute "(of de y-waarden)" %}} *positief*, *negatief* of *nul*
zijn.

{{% bokeh "plt/tekenschema.json" %}}

We zien op de grafiek:

* Voor x-waarden kleiner dan $-3$ zijn alle y-waarden **{{% class "negatief" "red" %}}**;
* Voor x gelijk aan $-3$ is de y-waarde **{{% class "nul" "blue" %}}**;
* Voor x-waarden tussen $-3$ en $3$ zijn alle y-waarden **{{% class "positief" "green" %}}**;
* Voor x gelijk aan $3$ is de y-waarde **{{% class "nul" "blue" %}}**;
* Voor x-waarden groter dan $3$ zijn alle y-waarden **{{% class "negatief" "red" %}}**.

Dit vatten we als volgt samen in een **tekenschema**:

Ingang $x$               | $-\infty$    |           | $-3$       |             | $3$        |           | $+\infty$
-------------------------|--------------|-----------|------------|-------------|------------|-----------|----------------
**Uitgang** $y = f(x)$   |              | $\red{-}$ | $\blue{0}$ | $\green{+}$ | $\blue{0}$ | $\red{-}$ |

Het schema toont:

* Als de ingang ($x$) iets tussen $-\infty$ en $-3$ is, is de uitgang ($y$) *{{% class "negatief" "red" %}}*;
* Als $x=-3$, is $y$ *{{% class "nul" "blue" %}}*;
* Als $x$ iets tussen $-3$ en $3$ is, is $y$ *{{% class "positief" "green" %}}*;
* Als $x=3$ is, is $y$ *{{% class "nul" "blue" %}}*;
* Als $x$ iets tussen $3$ en $+\infty$ is, is $y$ *{{% class "negatief" "red" %}}*.

## Tekenschema zonder grafiek
We kunnen een tekenschema ook maken *zonder* een grafiek. Dit doen we in drie
stappen.

1. Zet de grenzen van het [domein](../domein_beeld#domein-van-een-functie) in de bovenste rij van het tekenschema;
2. Zoek alle [nulpunten](../nulpunten) en zet ze van klein naar groot {{% mute "(volgens x-waarde)" %}} tussen de grenzen van het domein;
3. Vind de tekens van $y$ tussen alle x-waarden in het schema {{% mute "(tenzij die x-waarden buiten het domein liggen)" %}}.

We werken deze stappen uit voor de ([reële](../../reele_fies)) functie
met [voorschrift](../voorschrift)
$$f(x) = -x^2 + 9$$
Dit is de functie die hoort bij de grafiek van daarnet. We hopen dus ook hetzelfde tekenschema te krijgen.

### Grenzen van het domein
We kunnen van eender welk reëel getal het kwadraat berekenen, dus we kunnen
$f(x) = -x^2 + 9$ voor elk reëel getal $x$ berekenen. Dit betekent dat het
domein van $f$ alle reële getallen is:
$$dom f = \mathbb{R}$$
Als [interval](../../verzamelingen/intervallen) geschreven is dit
$$dom f = \left] -\infty, +\infty \right[%]$$
De grenzen van het domein zijn dus $-\infty$
en $+\infty$. Die zetten we op de bovenste rij van het tekenschema:

Ingang $x$               | $-\infty$    |           |            |             |            |           | $+\infty$
-------------------------|--------------|-----------|------------|-------------|------------|-----------|----------------
**Uitgang** $y = f(x)$   |              |           |            |             |            |           |

### Nulpunten zoeken
We vinden de nulwaarden van de functie $f(x) = -x^2 + 9$ door de
[vergelijking](../../vergelijkingen)
$$-x^2 + 9 = 0$$
op te lossen naar $x$.
Als je dat zou doen, vind je dat $x=-3$ en $x=3$ de nulwaarden zijn van deze functie $f$. De
[nulpunten](../nulpunten#nulpunten-van-een-functie) zijn dus $(-3, \blue{0})$ en
$(3, \blue{0})$. We zetten deze nulpunten gerangschikt in het tekenschema:

Ingang $x$               | $-\infty$    |           | $-3$       |             | $3$        |           | $+\infty$
-------------------------|--------------|-----------|------------|-------------|------------|-----------|----------------
**Uitgang** $y = f(x)$   |              |           | $\blue{0}$ |             | $\blue{0}$ |           |

### Tekens van $y$ tussen alle x-waarden
Om het tekenschema te vervolledigen, moeten we op zoek naar welk teken er moet
staan bij $y$ tussen alle x-waarden die in het schema staan. Dus tussen
$-\infty$ en $-3$, tussen $-3$ en $3$, en tussen $3$ en $+\infty$. Een trucje
dat *altijd* werkt is:

1. Kies een eenvoudige x-waarde die ligt tussen de twee x-waarden;
2. Vul de gekozen x-waarde [in in de functie](../voorschrift#x-invullen-in-een-voorschrift);
3. Zet het teken van de uitkomst in het tekenschema.

Bijvoorbeeld het teken van
$y$ voor $x$ tussen $-3$ en $3$. Een eenvoudig getal dat ligt tussen $-3$ en $3$ is
$0$. Die vullen we in in $f(x) = -x^2 + 9$:
$$f(\orange{0}) = -(\orange{0})^2 + 9 = \green{9}$$
We komen een **{{% class "positief" "green" %}}** getal uit, dus we zetten een $\green{+}$ tussen $-3$ en $3$:

Ingang $x$               | $-\infty$    |           | $-3$       |             | $3$        |           | $+\infty$
-------------------------|--------------|-----------|------------|-------------|------------|-----------|----------------
**Uitgang** $y = f(x)$   |              |           | $\blue{0}$ | $\green{+}$ | $\blue{0}$ |           |

Voor een x-waarde tussen $-\infty$ en $-3$, kunnen we $-5$ nemen.
$$f(\orange{-5}) = -(\orange{-5})^2 + 9 = -25 + 9 = \red{-16}$$
Invullen geeft een **{{% class "negatief" "red" %}}** getal, dus we zetten een $\red{-}$ tussen $-\infty$ en $-3$:

Ingang $x$               | $-\infty$    |           | $-3$       |             | $3$        |           | $+\infty$
-------------------------|--------------|-----------|------------|-------------|------------|-----------|----------------
**Uitgang** $y = f(x)$   |              | $\red{-}$ | $\blue{0}$ | $\green{+}$ | $\blue{0}$ |           |

Voor een x-waarde tussen $3$ en $+\infty$, ten slotte, kunnen we
$5$ nemen.  $$f(\orange{5}) = -(\orange{5})^2 + 9 = -25 + 9 =
\red{-16}$$ Invullen geeft een **{{% class "negatief" "red" %}}** getal, dus we zetten een $\red{-}$ tussen $3$ en
$+\infty$:

Ingang $x$               | $-\infty$    |           | $-3$       |             | $3$        |           | $+\infty$
-------------------------|--------------|-----------|------------|-------------|------------|-----------|----------------
**Uitgang** $y = f(x)$   |              | $\red{-}$ | $\blue{0}$ | $\green{+}$ | $\blue{0}$ | $\red{-}$ |

Et voilà! :muscle: We krijgen hetzelfde tekenschema als daarnet.

## Enkel nulpunten en grenzen van domein
De x-waarden die in een tekenschema staan {{% mute "(de bovenste rij)" %}}, zijn *ofwel nulwaarden* {{% mute
"($-3$ en $3$ in het vorige voorbeeld)" %}} *ofwel grenzen van het domein* {{%
mute "($-\infty$ en $+\infty$ in het voorbeeld)" %}} . Er zijn geen andere
x-waarden nodig. Dat is omdat **het teken van $y$ enkel kan veranderen na een
nulpunt of na een grens van het domein**.

Voor echt heel speciale functies kan het teken ook na andere x-waarden
veranderen, namelijk na een *discontinuïteit*. Zulke functies zullen we niet zo
vaak tegenkomen, dus is het niet de moeite om er nu verder op in te gaan.
Zorgen voor later! :wave:

## Samengevat
{{% attention "Tekenschema" %}}
Het **tekenschema van een functie $f$** toont schematisch **het teken van $y$
voor alle x-waarden** die in het domein van $f$ zitten.
{{% /attention %}}

{{% attention "Tekenschema opstellen" %}}
1. Zet de **grenzen van het domein** in het tekenschema;
2. Zoek alle **nulpunten** en zet ze tussen de grenzen van het domein;
3. Vind de **tekens van $y$** tussen alle x-waarden in het schema.
{{% /attention %}}
