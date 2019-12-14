![Hoe Zit Het? - Wetenschap verlicht](/static/images/fb/banner.png)

Deze repository bevat de programmacode achter [_Hoe Zit Het?_](https://hoezithet.nu/).

# Algemeen overzicht

De HTML-pagina's van de website worden gegenereerd door het 
[Hugo](https://github.com/gohugoio/hugo) framework. Door Hugo te gebruiken 
zorgen we dat de *inhoud* van de site en de *weergave* ervan duidelijk van 
elkaar gescheiden zijn. De twee belangrijkste folders bevatten dan ook 
bestanden die instaan voor de *inhoud* (`content`) en de *weergave* 
(`layouts`). Hieronder een overzicht van de andere directories:

| Directory | Beschrijving |
+-----------+--------------+
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
van een les.  Het bestand 
`content/lessen/wiskunde/functies/domein_beeld/index.md`, bijvoorbeeld, zal als 
basis dienen voor de webpagina 
<https://hoezithet.nu/lessen/wiskunde/functies/domein_beeld>.

## Front matter van een les

Elk markdown-bestand in de `content` directory heeft een *front matter*. Dat is 
een soort header die meta-informatie bevat over die les. De front matter van 
een les moet minstens de key `title` bevatten. De waarde hiervan wordt de titel 
van de les. Meestal bevat de front matter echter nog meer informatie.  
Bijvoorbeeld:

```toml
title: "Wat zijn lichtstralen?"
date: 2019-01-28T18:38:31+01:00
weight: 1
draft: false
images: ['/lessen/fysica/lichtstralen/intro/img/mosaic.png', ...]
```

Een belangrijke key hierbij is **weight**. De waarde hiervan bepaalt de 
**positie van de les in de bijhorende lesblok**. Voor het bestand 
`content/lessen/fysica/lichtstralen/intro/index.md` is `lichtstralen` de 
bijhorende lesblok. Een `weight` van 1 zorgt dat deze les als eerste zal staan 
in de lijst van lessen in de lesblok over lichtstralen.

## Front matter van een lesblok

TODO

## Markdown cheat sheet

TODO

## Illustraties

TODO

## Wiskunde noteren

TODO

## Kleur gebruiken

TODO

## Kaders met uitleg of samenvattingen

TODO

## Uitbreidingen op de leerstof

TODO

## Grafieken

TODO

## Schrijfstijl

TODO
