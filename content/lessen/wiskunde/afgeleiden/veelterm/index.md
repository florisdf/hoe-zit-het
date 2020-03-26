---
title: "De afgeleide van een veeltermfunctie"
date: 2020-03-18T19:42:11+02:00
weight: 2
draft: true
images: []
---

In de vorige les zagen we [wat afgeleiden zijn](../intro) en wat hun nut is.
Maar hoe berekenen we nu zo'n afgeleide? In deze les leren we hoe je de
afgeleide van een **veeltermfunctie** kan berekenen.

We leerden al de definitie van de afgeleide van een functie:

$$ f'(x) = \lim\_{\Delta x \rightarrow 0} \frac{ f(x + \Delta x) - f(x) }{\Delta x} $$

Lees zeker de [vorige les](../intro) eens na als je die formule niet zo goed begrijpt.

## De afgeleide van een tweedegraadsfunctie

Stel dat we de afgeleide willen berekening van de volgende functie:

$$ f(x) = -3x^2 + 4x - 1 $$

Als we naar de definitie van een afgeleide kijken, zien we dat er op twee
plaatsen iets met "$f(x)$" staat:

{{< svg "img/fx_in_afgeleide.svg" >}}

Om de definitie van een afgeleide hierop toe te passen, moeten we op twee
plaatsen de $f(x)$ in de formule vervangen door ons
[functievoorschrift](../../functies/voorschrift):


Voor de 

\begin{split}
    f'(x) &= \lim\_{\Delta x \rightarrow 0} \frac{ \orange{f(x + \Delta x)} - \orange{f(x)} }{\Delta x} \\\\\
          &= \lim\_{\Delta x \rightarrow 0} \frac{ \orange{f(x + \Delta x)} - \orange{f(x)} }{\Delta x} \\\\\
      &=  \lim\_{\Delta x \rightarrow 0} \frac { x^2 + 2x \Delta x + \Delta x^2 - x^2 } {\Delta x} \\\\\ 
      &=  \lim\_{\Delta x \rightarrow 0} \frac { 2x \Delta x  + \Delta x^2} {\Delta x} \\\\\ 
      &=  2x
\end{split}

In de tweede lijn wordt een **[merkwaardig product](../../veeltermen/merkwaardige_producten)** gebruikt om het kwadraat uit te werken. In de laatste twee lijnen wordt een limiet uitgereknd. Als je geïntereseerd bent hoe dit werkt kan je dat in onderstaand blokje lezen, maar dat is niet noodzakelijk om afgeleiden te begrijpen.

{{< expand "Hoe wordt de limiet berekend?" >}}
Om de limiet te bereken is het belangrijk eerst stil te staan naar waar onze limiet gaat. In dit geval bereken we limiet van $\Delta x$ naar $0$. Dit betekent dat de lagere graadstermen van een limiet belangrijker zijn dan de hogere. De hogere graadstermen zullen immers sneller nul worden. We kunnen daarom onze limiet versimpelen tot de volgende limiet:

$$ \lim\_{\Delta x \rightarrow 0} \frac { 2x \Delta x } {\Delta x} $$

Nu krijgen we in zowel teller als noemer een term met $\Delta x$ en mogen we deze dus schrappen. Wat overblijft is nu:

$$ \lim\_{\Delta x \rightarrow 0} 2x $$

In deze limiet staat geen $\Delta x$ meer, dus wanneer we dan $\Delta x$ naar $0$ laten gaan, blijft de limiet gelijk aan $2x$, de oplossing!
{{< /expand >}}

## Afgeleide van een eenterm

We kunnen nu een afgeleide berekenen met behulp van de definitie. Dit is natuurlijk nogal veel werk om elke keer opnieuw te doen. Gelukkig bestaan er handige trucjes om snel afgeleiden van veeltermen te berekenen. Laten we beginnen met een **[eenterm](../../veeltermen/eenterm/)**. Heel algemeen ziet die er zo uit:

$$ f(x) = x^b $$

$x$ is de veranderlijke en $b$ de exponent. In het voorbeeld eerder was $b$ gelijk aan $2$. De afgeleide van deze eenterm is nu heel simpel:

$$ f'(x) = bx^{b-1} $$ 

We vermenigvuldigen de oorspronkelijke functie dus met $b$, de exponent. Daarnaast wordt de exponent in de afgeleide met $1$ verminderd. 

We geven snel een voorbeeld. In de functie $f(x) = x^7$ is $b$ gelijk aan  $7$. De afgeleide wordt dan $f'(x) = 7x^6$. Kijk voor je verder gaat nog eens naar de algemene formule en dit voorbeeld, en overtuig jezelf ervan dat je weet waar de $7$ en $6$ in het voorbeeld vandaan komt.

## Afgeleide van een veelterm

Als je eentermen bij elkaar optelt, dan krijg je een veelterm. De volgende functie is een voorbeeld van zo'n veelterm:

$$ f(x) = x^4 + x^2 + x $$

Je moet eigenlijk maar een ding weten om een veelterm af te leiden. Als je weet hoe je een eenterm kan afleiden, dan kan je ook een veelterm afleiden (en als je dit niet meer weet, ben je de vorige alinea overgeslagen! :wink:). En dan rest er ons nog 1 zinnetje: **De afgeleide van een som, is de som van de afgeleiden**. De afgeleide van de veelterm is dus de som van de afgeleiden van zijn eentermen. Passen we dit nu toe op de vorige veelterm $f$, dan krijgen we:

$$ f(x) = 4x^3 + 2x + 1 $$

-> (tabel met afgeleiden van de eentermen afzonderlijk? )

## Een opmerking

Je kan je nu misschien afvragen: wat als er nog een constante voor mijn eenterm staat? Hoe moet ik bijvoorbeeld $4x^3$ afleiden? Eingelijk is het poepsimpel. Als een functie ($f$) gelijk is aan een constante ($c$) maal een andere functie ($g$) dan is de afgeleide van $f$ gelijk aan de constante $c$ maal de afgeleide van $g$. Uit die woorden alleen word je natuurlijk niet veel wijzer. Uit dit voorbeeld hopelijk wel!

\begin{split}
 f(x) &= 4x^3 \\\\\
 f(x) &= cg(x) \\\\\
 f'(x) &= c*g'(x) \\\\\
 g'(x) &= 3x^2  \\\\\
f'(x) = & 4 * 3x^2 = 12x^2 \\\\\
\end{split}

(vervangen door duidelijkere illustratie)


## Samengevat
{{< attention "Afgeleide van een eenterm" >}}
De afgeleide van een éénterm $f(x) = x^b$ is gelijk aan $f(x) = bx^{b-1}$s
{{< /attention >}}

{{< attention "Afgeleide van een veelterm" >}}
Om een veelterm af te leiden moet je twee dingen weten:
* Hoe je een eenterm afleidt
* De afgeleide van een som, is de som van de afgeleiden
{{< /attention >}}
