---
title: "Domein en beeld"
date: 2018-07-01T22:13:11+02:00
weight: 5
draft: false
tags: ["Functies", "Analyse"]
categories: ["wiskunde", "analyse", "3e middelbaar"]
level: 3M
course: wiskunde
topic: analyse
---
Een functie kunnen we [voorstellen als een machientje](../intro) waar we een
waarde voor $x$ in stoppen en waar [hoogstens één](../intro#samengevat) waarde
voor $y$ uit komt.

{{% img "img/conveyor_plain.svg" "" %}}

Voor een bepaalde x-waarde kan er dus **één of géén** y-waarde uit de
functie komen.

## Domein van een functie
Het *domein* van een functie is de [verzameling](../../verzamelingen/verzamelingen)
van x-waarden waarvoor er een functiewaarde {{%mute "(een y-waarde)" %}} bestaat.

* Voor elke x-waarde die **niet in het domein** zit, bestaat er **géén
y-waarde**.
* Voor elke x-waarde die **wel in het domein** zit, bestaat er **juist één
y-waarde**.

Een typisch voorbeeld is het domein van de [reële functie](../reele_functies) die als
[functievoorschrift](../voorschrift) heeft

$$f(x) = \sqrt{x}$$

Omdat de [wortel van een negatief
getal](../../rekenen/vierkantswortel#vierkantswortel-van-een-negatief-getal)
geen [reëel getal](../../verzamelingen/reele_getallen) is, kan $f(x)$ niet reëel zijn 
voor negatieve x-waarden. Er bestaan met andere woorden géén y-waarden
 voor negatieve x-waarden. 
Het domein
van deze functie $f$ is dus alle *positieve* reële getallen, want enkel voor
positieve x-waarden bestaat er een functiewaarde. We schrijven:
$$dom f = \mathbb{R}^+$$

Dit kunnen we ook schrijven als een [interval](../../verzamelingen/intervallen):
$$dom f = [0, +\infty[%]$$

## Beeld van een functie
Het *beeld* of het *bereik* van een functie is de [verzameling](../../verzamelingen/verzamelingen) 
van alle y-waarden die ooit uit de functie kunnen komen.

Een typisch voorbeeld is het beeld van de [reële functie](../reele_functies) die als
[functievoorschrift](../voorschrift) heeft

$$f(x) = x^2$$

Omdat het kwadraat van elk [reëel getal](../../verzamelingen/reele_getallen) positief is, kunnen er uit deze functie $f$ enkel *positieve* getallen komen. Met andere woorden is het beeld van deze functie alle *positieve* reële getallen. We schrijven:
$$bld f = \mathbb{R}^+$$

Dit kunnen we natuurlijk ook schrijven als een [interval](../../verzamelingen/intervallen):
$$bld f = [0, +\infty[%]$$

## Domein en beeld op een grafiek
Het domein en beeld van een functie kan je ook aflezen van de [grafiek van die
functie](../grafiek). Neem bijvoorbeeld de grafiek van de functie 
$$f(x) = 3\cdot \sqrt{x + 5} - 6$$
Die grafiek ziet er zo uit:

{{% bokeh "plt/fx.json" %}}

Om op deze grafiek het **domein** af te lezen, moet je de grafiek **projecteren
op de x-as**.  Het resultaat van de projectie
is aangeduid **{{% class "in het groen op de x-as" "green" %}}**.
{{% mute "We gaan ervan uit dat de grafiek oneindig blijft verder stijgen aan de rechterkant." %}}
We zien dan dat $\green{dom f = [-5, +\infty[}$.

{{% bokeh "plt/dom.json" %}}


Het **beeld** {{% mute "(of het bereik)" %}} van diezelfde functie kunnen we
vinden door de grafiek nu te **projecteren op de y-as**. Op de onderstaande
grafiek zie je het resultaat van deze projectie
**{{% class "in het groen op de y-as" "green" %}}**.
{{% bokeh "plt/bld.json" %}}
{{% mute "We gaan ervan uit dat de grafiek oneindig blijft verder stijgen aan de rechterkant." %}}
Je vindt dat $\green{bld f = [-6, +\infty[}$.

## Samengevat
{{% attention "Definitie domein" %}}
Het **domein van een functie** is de verzameling van alle mogelijke **x-waarden
waarvoor er een functiewaarde bestaat**.
{{% /attention %}}

{{% attention "Definitie beeld" %}}
Het **beeld van een functie** is de verzameling van **alle mogelijke functiewaarden**.
{{% /attention %}}
   
{{% attention "Domein aflezen op een grafiek" %}}
Het **domein van een functie** lees je af op een grafiek door de grafiek te **projecteren op de x-as**.
{{% /attention %}}

{{% attention "Beeld aflezen op een grafiek" %}}
Het **beeld van een functie** lees je af op een grafiek door de grafiek te **projecteren op de y-as**.
{{% /attention %}}
