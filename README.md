![Hoe Zit Het? - Wetenschap verlicht](/static/images/fb/banner.png)

Deze repository bevat de programmacode achter [_Hoe Zit Het?_](https://hoezithet.nu/).

Inhoud
======

   * [Algemeen overzicht](#algemeen-overzicht)
   * [Lessen schrijven](#lessen-schrijven)
      * [Front matter van een les](#front-matter-van-een-les)
      * [Front matter van een lesblok](#front-matter-van-een-lesblok)
      * [Illustraties in lessen](#illustraties-in-lessen)
      * [Wiskunde noteren](#wiskunde-noteren)
      * [Kleur gebruiken](#kleur-gebruiken)
      * [Kaders met uitleg of samenvattingen](#kaders-met-uitleg-of-samenvattingen)
      * [Uitbreidingen op de leerstof](#uitbreidingen-op-de-leerstof)
      * [Grafieken](#grafieken)
   * [Contributing](#contributing)

# Algemeen overzicht

De HTML-pagina's van de website worden gegenereerd door het 
[Hugo](https://github.com/gohugoio/hugo) framework. Door Hugo te gebruiken 
zorgen we dat de *inhoud* van de site en de *weergave* ervan duidelijk van 
elkaar gescheiden zijn. De twee belangrijkste folders bevatten dan ook 
bestanden die instaan voor de *inhoud* (`content`) en de *weergave* 
(`layouts`). Hieronder een overzicht van de directories:

| Directory | Beschrijving |
|-----------|--------------|
| `archetypes` | Het commando `hugo new` ([doc](https://gohugo.io/commands/hugo_new/)) gebruikt deze bestanden als basis voor nieuwe content files. ([docs: archetype](https://gohugo.io/content-management/archetypes/)) |
| `content` | Bevat markdown-bestanden met de tekstuele inhoud van elke pagina. |
| `layouts` | Op basis van deze bestanden zullen de markdown-bestanden omgezet worden naar HTML-pagina's. |
| `public` | Hierin komen de gegenereerde HTML-pagina's terecht na het uitvoeren van het commando `hugo`. |
| `src` | Deze directory staat los van Hugo en bevat enkele handige Python scripts. |
| `static` | Elk bestand dat in deze directory staat, zal op dezelfde locatie terechtkomen op de site. ([docs: static files](https://gohugo.io/content-management/static-files/)) |

# Lessen schrijven

De lessen worden geschreven in markdown-bestanden in de `content/lessen` 
directory. Eender welk `index.md`-bestand in 
`content/lessen/<vak>/<lesblok>/<les>/`, zal omgezet worden naar de HTML-pagina 
van een les.

Het bestand `content/lessen/wiskunde/functies/domein_beeld/index.md`, 
bijvoorbeeld, zal als basis dienen voor de webpagina 
<https://hoezithet.nu/lessen/wiskunde/functies/domein_beeld>.

## Front matter van een les

Elk `index.md`-bestand in de `content` directory heeft een *front matter*. Dat 
is een soort header die meta-informatie bevat over die les. De front matter van 
een les moet minstens de key `title` bevatten. De waarde hiervan wordt de titel 
van de les. Meestal bevat de front matter echter nog meer informatie.  
Bijvoorbeeld:

```yaml
---
title: "Wat zijn lichtstralen?"
date: 2019-01-28T18:38:31+01:00
weight: 1
draft: false
images: ['/lessen/fysica/lichtstralen/intro/img/mosaic.png', ...]
---
```

Een belangrijke key hierbij is **weight**. De waarde hiervan bepaalt de 
**positie van de les in de bijhorende lesblok**. Voor het bestand 
`content/lessen/fysica/lichtstralen/intro/index.md` is `lichtstralen` de 
bijhorende lesblok. Een `weight` van 1 zorgt dat deze les als eerste zal staan 
in de lijst van lessen in de lesblok over lichtstralen.

## Front matter van een lesblok

Een **lesblok** is een verzameling van lessen die in zekere zin bij elkaar 
horen. In de directory tree zit een lesblok een niveau hoger dan een les. De 
lesblok-directory bevat ook een markdown bestand: `_index.md`. Hierin staat 
eveneens een front matter. Deze moet minstens de keys `title`, `section_color`,
`level` en `topic` bevatten.

| Key   | Beschrijving |
|-------|--------------|
| `title` | De titel van de lesblok. |
| `section_color` | De primaire kleur van deze sectie. Dit bepaalt bv. de kleur van de titel van iedere les in dit lesblok. |
| `level` | Voor welk niveau de leerstof is bedoeld. |
| `topic` | Bij welk vakonderdeel de leerstof hoort. |

Een voorbeeld van een front matter voor een lesblok over lichtstralen voor 
leerlingen van het 3e middelbaar:

```yaml
---
title: "Lichtstralen"
section_color: "#ff6300"
level: "3e middelbaar"
topic: "optica"
---
```

Ook lesblokken kunnen de key `weight` bevatten in hun front matter. De waarde 
hiervan zal bepalen in welke volgorde meerdere lesblokken getoond worden.

## Illustraties in lessen

Illustraties zet je best in een subdirectory `img` van de les waarin je de
illustratie nodig hebt. Vervolgens gebruik je de
[shortcode](https://gohugo.io/content-management/shortcodes/)
[`svg`](layouts/shortcodes/svg.html) om de
illustratie in te voegen in de les.

Bijvoorbeeld:
```md
Zoals je ziet, wordt het beeld omgekeerd gevormd op het netvlies, maar daar
hoef je je momenteel geen zorgen over te maken.

{{% svg "img/oog.svg" %}}

De lens van een fototoestel doet hetzelfde, behalve dat die de lichtstralen
samenbrengt op een lichtgevoelige sensor. Ook hier krijgen we een omgekeerd
beeld.

{{% svg "img/sony_a7ii.svg" %}}
```

## Wiskunde noteren

Wiskunde noteer je met behulp van LaTeX-syntax. Wanneer je de wiskunde tussen
enkelvoudige dollartkens ($) plaatst, zal ze in de zin zelf verschijnen. Tussen
dubbele dollartekens ($$) zal de wiskunde in een aparte lijn gezet worden.

LaTeX environments als `split` kunnen handig zijn om vergelijkingen proper uit
te lijnen. Merk wel op dat je *5* (!) backslashes nodig hebt om een nieuwe lijn
te beginnen.

```md
Hieronder lossen we een vergelijking op:

\begin{split}
    x + 1 &= 2 \\\\\
    \Leftrightarrow x &= 2 - 1 \\\\\
    \Leftrightarrow x &= 1 \\\\\
\end{split}
```

## Kleur gebruiken

Je kan zowel in de tekst als in formules kleur gebruiken. In de tekst gebruik
je hiervoor de [`class`](layouts/shortcodes/class.html) shortcode:

```md
Toon de volgende tekst in een {{% class "blauwe kleur" "blue" %}},
{{% class "rode kleur" "red" %}} en {{% class "groene kleur" "green" %}}.
```

Tekst die als snelle uitleg dient zonder al te veel de *flow* van de tekst
te doorbreken, kun je lichtgrijs maken met de shortcode
[`mute`](/layouts/shortcodes/mute.html):

```md
Als je wilt weten wat er met een slee gebeurt als iemand eraan trekt, moet je
niet alleen weten **hoe hard** {{% mute "(= grootte)" %}}, maar ook
**waarheen** {{% mute "(= richting en zin)" %}} de slee getrokken wordt.
```

In formules kan je dezelfde kleuren gebruiken als voor de
[`class`](layouts/shortcodes/class.html) shortcode. De naam van de kleur is
eenvoudigweg het LaTeX commando om die kleur te gebruiken:

```md
We zijn op zoek naar een rode $\red{x}$. Gevonden!
```

## Kaders met uitleg of samenvattingen

Op het einde van de les maak je best een korte samenvatting in een kadertje. In
de les zelf is het dan weer soms handig om dingen die leerlingen moeten
onthouden even in te kaderen. Voor zulke kaders kan je de
[shortcode](https://gohugo.io/content-management/shortcodes/)
[`attention`](layouts/shortcodes/attention.html)
gebruiken:

```md
{{% attention "Titel van de kader" "Kleur van de kader (optioneel)" %}}

Het is belangrijk om af en toe een kader toe te voegen.

{{% /attention %}}
```

## Uitbreidingen op de leerstof

Soms wil je als auteur van een les een kleine nuance of wat extra
informatie toevoegen. Het is echter belangrijk dat je hiermee de focus van de
les niet verliest. Daarom kan het interessanter zijn om dit soort uitbreidingen
op de leerstof in een uitklapbare blok te plaatsen. Hiervoor gebruiken we de
[shortcode](https://gohugo.io/content-management/shortcodes/)
[`expand`](layouts/shortcodes/expand.html).

Bijvoorbeeld:

```md
Een resulterende kracht $\vec{F}$ op een massa $m$ zal altijd leiden tot een
versnelling $d\vec{v}/dt$ van die massa volgens het verband

$\vec{F} = m \cdot \frac{d\vec{v}}{dt}$

Dit verband is beter bekend als de **derde wet van Newton**.

{{% expand "UITBREIDING: Relativiteit" %}}

De derde wet van Newton geldt enkel voor massa's die - ten opzicht van het
gekozen inertiaalstelsel - met een snelheid bewegen die *veel* kleiner is
dan de snelheid van het licht.

Een juister verband is:

$\vec{F} = \frac{d}{dt} \frac{m\vec{v}}{\sqrt{1 - v^2/c^2}}$

{{% /expand %}}
```

## Grafieken

De interactieve grafieken in de lessen over
[functies](https://hoezithet.nu/lessen/wiskunde/functies/) zijn gemaakt met de
library [Bokeh](https://docs.bokeh.org/en/latest/). Met Bokeh kan je heel
eenvoudig grafieken maken in Python en ze vervolgens exporteren naar een
JSON-bestand.

Het Python-script [`graphs.py`](src/graphs.py) helpt je om een grafiek te maken
die past in de *Hoe Zit Het?*-stijl. De methode `get_plot()` maakt een lege
Bokeh plot waar je meteen mee aan de slag kan.

Bijvoorbeeld:

```python
from pathlib import Path

from hoezithet.src import graphs
from bokeh.embed import json_item

def f(x): return x**2
xs = [x/10 for x in range(-100, 100)]
ys = [f(x) for x in xs]

p = graphs.get_plot()
p.line(xs, ys, color=graphs.BLUE, line_cap='round')

item = json.dumps(json_item(p))
Path('plt/quad_fx.json').write_text(item)
```

De output van bovenstaand script is een JSON-bestand `plt/quad_fx.json`. Dit
kan je met de shortcode [`bokeh`](layouts/shortcodes/bokeh.html) gebruiken in
een les.

Bijvoorbeeld:

```md
De kwadratische functie $f(x) = x^2$ heeft de volgende grafiek:

{{% bokeh "plt/quad_fx.json" %}}
```

# Contributing

Bij het schrijven van nieuwe lessen, maak je een nieuwe branch vanuit de `develop` branch. De naam van de branch begint met `cont-` (van **cont**ent), bijvoorbeeld `cont-lichtstralen`. Nadat je alle lessen geschreven hebt, merge je de branch terug in de `develop` branch.

We maken gebruik van [commitizen](http://commitizen.github.io/cz-cli/) opdat de commit messages op een uniforme wijze geschreven zouden worden. Het benodigde node package zit in de `package.json`, dus een eenvoudige `npm install` in de directory moet volstaan om commitizen zelf te kunnen gaan gebruiken. Lees gerust een door [de documentatie](http://commitizen.github.io/cz-cli/) voor meer info.
