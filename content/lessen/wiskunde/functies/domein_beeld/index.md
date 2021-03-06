---
title: "Domein en beeld"
date: 2018-07-01T22:13:11+02:00
weight: 5
draft: false
tags: ["beeld van een functie", "bereik van een functie", "domein van een
functie", "domein en beeld", "domein en bereik"]
description: "Wat zijn domein en beeld of bereik van een functie? In deze les
leggen we het domein en beeld of bereik van een functie uit. Dat doen we met
behulp van verschillende illustraties zodat je een goede intuïtie krijgt voor
deze begrippen."
images: ['/lessen/wiskunde/functies/domein_beeld/plt/fx.png', '/lessen/wiskunde/functies/domein_beeld/plt/dom.png', '/lessen/wiskunde/functies/domein_beeld/plt/bld.png']
---
We kunnen niet altijd eender welk getal als $x$ kiezen om in ons
[functievoorschrift](../voorschrift) te stoppen. Omgekeerd is het mogelijk dat
niet eender welk getal als $y$ uit de functie komt. Deze twee eigenschappen van
een functie worden beschreven door het **domein** en het **beeld** van de
functie.

## Domein van een functie
Het *domein* van een functie is de verzameling
van x-waarden waarvoor er een functiewaarde {{<mute "(een y-waarde)" >}} bestaat.

* Voor elke x-waarde die **niet in het domein** zit, bestaat er **géén
y-waarde**.
* Voor elke x-waarde die **wel in het domein** zit, bestaat er **juist één
y-waarde**.

Een typisch voorbeeld is het domein van de functie die als
[functievoorschrift](../voorschrift) heeft

$$f(x) = \sqrt{x}$$

Omdat de wortel van een negatief
getal niet bestaat, kan $f(x)$ niet bestaan 
wanner x negatief is. Er bestaan met andere woorden géén y-waarden voor
negatieve x-waarden. 
Het domein van deze functie $f$ is dus alle *positieve* reële getallen, want
enkel voor positieve x-waarden bestaat er een functiewaarde. We schrijven:

$$dom f = \mathbb{R}^+$$

Dit kunnen we ook schrijven als een interval:

$$dom f = [0; +\infty[%]$$

## Beeld van een functie
Het *beeld* of het *bereik* van een functie is de verzameling
van alle y-waarden die ooit uit de functie kunnen komen.

Een typisch voorbeeld is het beeld van de functie die als
[functievoorschrift](../voorschrift) heeft

$$f(x) = x^2$$

Omdat het kwadraat van elk reëel getal positief is, kunnen er uit deze functie
$f$ enkel *positieve* getallen komen. Met andere woorden is het beeld van deze
functie alle *positieve* reële getallen. We schrijven:

$$bld f = \mathbb{R}^+$$

Dit kunnen we natuurlijk ook schrijven als een interval:

$$bld f = [0; +\infty[%]$$

## Domein en beeld op een grafiek
Het domein en beeld van een functie kan je ook aflezen van de [grafiek van die
functie](../grafiek). Neem bijvoorbeeld de grafiek van de functie 
$$f(x) = 3\cdot \sqrt{x + 5} - 6$$
Die grafiek ziet er zo uit:

{{< bokeh "plt/fx.json" >}}

Om op deze grafiek het **domein** af te lezen, moet je de grafiek **projecteren
op de x-as**.  Het resultaat van de projectie
is aangeduid **{{< class "in het groen op de x-as" "green" >}}**.
{{< mute "We gaan ervan uit dat de grafiek oneindig blijft verder stijgen aan de rechterkant." >}}
We zien dan dat $\green{dom f = [-5; +\infty[}$.

{{< bokeh "plt/dom.json" >}}


Het **beeld** {{< mute "(of het bereik)" >}} van diezelfde functie kunnen we
vinden door de grafiek nu te **projecteren op de y-as**. Op de onderstaande
grafiek zie je het resultaat van deze projectie
**{{< class "in het groen op de y-as" "green" >}}**.
{{< bokeh "plt/bld.json" >}}
{{< mute "We gaan ervan uit dat de grafiek oneindig blijft verder stijgen aan de rechterkant." >}}
Je vindt dat $\green{bld f = [-6; +\infty[}$.

## Samengevat
{{< attention "Definitie domein" >}}
Het **domein van een functie** is de verzameling van alle mogelijke **x-waarden
waarvoor er een functiewaarde bestaat**.
{{< /attention >}}

{{< attention "Definitie beeld" >}}
Het **beeld van een functie** is de verzameling van **alle mogelijke functiewaarden**.
{{< /attention >}}
   
{{< attention "Domein aflezen op een grafiek" >}}
Het **domein van een functie** lees je af op een grafiek door de grafiek te **projecteren op de x-as**.
{{< /attention >}}

{{< attention "Beeld aflezen op een grafiek" >}}
Het **beeld van een functie** lees je af op een grafiek door de grafiek te **projecteren op de y-as**.
{{< /attention >}}
