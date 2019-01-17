---
title: "Mix van bewerkingen"
date: 2019-01-17T18:50:35+01:00
weight: 7
draft: true
tags: ["vergelijkingen", "algebra"]
categories: ["wiskunde", "algebra"]
level: "2M"
course: "wiskunde"
topic: "algebra"
---
Een [vergelijking](../intro) oplossen betekent dat we de waarden van de
onbekende(n) vinden waarvoor de gelijkheid klopt. Vaak is er maar één
onbekende, namelijk $x$.

We kunnen een vergelijking oplossen door de vergelijking [om te
vormen](../omvormen) naar de vorm $x = \text{(een getal)}$. We hebben in vorige
lessen gezien hoe we bepaalde vergelijkingen kunnen omvormen. De
oplossingsmethodes kunnen als volgt worden samengevat:

| Vergelijking        | Tussenstap                                                                | Oplossing                              | {{% mute "Voorwaarden" %}}                                  |                                                        |
|---------------------|---------------------------------------------------------------------------|----------------------------------------|-------------------------------------------------------------|--------------------------------------------------------|
| $x + a = b$         | $x + a \orange{- a} = b \orange{- a}$                                     | $x = b \orange{- a}$                   | {{% mute "$a, b \in \mathbb{R}$" %}}                        | [uitleg](../termen_omvormen#omvormen-van-x-a-b)        |
| $x - a = b$         | $x - a \orange{+ a} = b \orange{+ a}$                                     | $x = b \orange{+ a}$                   | {{% mute "$a, b \in \mathbb{R}$" %}}                        | [uitleg](../termen_omvormen#en-wat-met-x-a-b)          |
| $a \cdot x = b$     | $\orange{\frac{\normal{a \cdot x}}{a}} = \orange{\frac{\normal{b}}{a}}$   | $x = \orange{\frac{\normal{b}}{a}}$    | {{% mute "$a \in \mathbb{R}_0$ en $b \in \mathbb{R}$" %}}   | [uitleg](../factoren_omvormen#omvormen-van-a-cdot-x-b) |
| $\frac{x}{a} = b$   | $\frac{x}{a} \orange{\cdot a} = b \orange{\cdot a}$                       | $x = b \orange{\cdot a}$               | {{% mute "$a \in \mathbb{R}_0$ en $b \in \mathbb{R}$" %}}   | [uitleg](../factoren_omvormen#omvormen-van-frac-x-a-b) |
| $x^2 = a$           | $\orange{\sqrt{\normal{x^2}}} = \orange{\sqrt{\normal{a}}}$               | $x = \pm \orange{\sqrt{\normal{a}}}$   | {{% mute "$a \in \mathbb{R}^+$" %}}                         | [uitleg](../machten_omvormen#omvormen-van-x-2-a)       |
| $\sqrt{x} = a$      | $\orange{(\normal{\sqrt{x}})^2} = a^\orange{2}$                           | $x = a^\orange{2}$                     | {{% mute "$a \in \mathbb{R}^+$" %}}                         | [uitleg](../machten_omvormen#omvormen-van-x-3-a)       |
| $x^3 = a$           | $\orange{\sqrt[3]{\normal{x^3}}} = \orange{\sqrt[3]{\normal{a}}}$         | $x = \orange{\sqrt[3]{\normal{a}}}$    | {{% mute "$a \in \mathbb{R}$" %}}                           | [uitleg](../machten_omvormen#omvormen-van-sqrt-x-a)    |
| $\sqrt[3]{x} = a$   | $\orange{(\normal{\sqrt[3]{x}})^3} = a^\orange{3}$                        | $x = a^\orange{3}$                     | {{% mute "$a \in \mathbb{R}$" %}}                           | [uitleg](../machten_omvormen#omvormen-van-sqrt-3-x-a)  |


In deze les zullen we zien wat er gebeurt als we een combinatie hebben van
de bovenstaande vormen.
