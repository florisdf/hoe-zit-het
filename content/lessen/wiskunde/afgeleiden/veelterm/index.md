---
title: "De afgeleide van een veelterm"
date: 2020-03-18T19:42:11+02:00
weight: 2
draft: true
images: []
---

Nu we weten wat een afgeleide is en waarvoor een afgeleide kan dienen, moeten we de afgeleide nog kunnen berekenen. 
Een van de makkelijkste families van functies om afgeleiden te berekenen zijn de **[veeltermen](../../veeltermen)**.

Stel nu dat we de veelterm van de functie $f(x) = x^2$ willen berekenen. Wat we zouden kunnen doen is 
met de definitie van de [vorige les](../intro) de afgeleiden proberen te vinden. De definitie werd gegeven door:

$$ f'(x) = \lim\_{\Delta x \rightarrow 0} \frac{\Delta f(x)}{\Delta x} $$

Herinner je dat $\Delta$ de verandering van iets betekend. We kunnen de definitie dus ook anners schrjven

$$ f'(x) = \lim\_{\Delta x \rightarrow 0} \frac{ f(x + \Delta x) - f(x) }{\Delta x} $$

In de teller staat nu het verschil tussen de functie waarde in $x$ en de functie waarde een klein beetje verder, in $x + \Delta x$. Dit verschil wordt gedeeld door het verschil in deze $x-$waarden: $x - (x + \Delta x) = \Delta x$. 

\begin{split}
f'(x) &=  \lim\_{\Delta x \rightarrow 0} \frac { (x + \Delta x)^2 - x^2 } {\Delta x} \\\\\ 
      &=  \lim\_{\Delta x \rightarrow 0} \frac { x^2 + 2x \Delta x + \Delta x^2 - x^2 } {\Delta x} \\\\\ 
      &=  \lim\_{\Delta x \rightarrow 0} \frac { 2x \Delta x  + \Delta x^2} {\Delta x} \\\\\ 
      &=  2x
\end{split}

In de tweede lijn wordt een **[merkwaardig product](../../veeltermen/merkwaardige_producten)** gebruikt om het kwadraat uittewerken. In de laatste twee lijnen wordt een limiet uitgewerkt, als je geïntereseerd bent hoe dit werkt kan je dat in onderstaand blokje lezen, maar dat is niet noodzakelijk om afgeleiden te begrijpen.

{{< expand "Hoe wordt de limiet berekend?" >}}
Om de limiet te bereken is het belangrijk eerst stil te staan naar waar onze limiet gaat. In dit geval bereken we limiet van $\Delta x$ naar $0$. Dit betekent dat de lagere graadstermen van een limiet belangrijker zijn dan de hogere. De hogere graadstermen zullen immers sneller nul worden. We kunnen daarom onze limiet versimpelen tot de volgende limiet:

$$ \lim\_{\Delta x \rightarrow 0} \frac { 2x \Delta x } {\Delta x} $$

Nu krijgen we in zowel teller als noemer een term met $\Delta x$ en mogen we deze dus schrappen. Wat overblijft is nu:

$$ \lim\_{\Delta x \rightarrow 0} 2x $$

In deze limiet staat geen $\Delta x$ meer, dus wanneer we dan $\Delta x$ naar $0$ laten gaan, blijft de limiet gelijk aan $2x$, de oplossing!
{{< /expand >}}