# Čtyři skutečné malé rešerše

Příklady vznikly z veřejných podkladů 2. listopadu 2026. Závěry opírají o konkrétní citované části přečtených pramenů; dva liberecké archivní tipy známé pouze z vyhledávacího indexu zůstávají výslovně označené jako hypotézy. Nejsou kompletní historií čtyř zkoumaných témat ani ukázkami plošného automatického čtení všech archivů.

| Soubor | Charakter | Co bylo skutečně přečteno |
|---|---|---|
| [uhersky-brod-cz.json](uhersky-brod-cz.json) | Založení závodu, vazba na historický podnik | Firemní ročenka 2019, s. 94–95, a jubilejní článek 2021 |
| [plzen-skoda.json](plzen-skoda.json) | Rozlišení vzniku podniku, pracovní role a koupě | Městská chronologie a podniková historie |
| [pribram-drtikol.json](pribram-drtikol.json) | Živnost, ateliér, konkrétní archivní citace | Kurátorský popisek SOA Praha; odkaz na reprodukci otevřen, zápis nebyl celý přepsán |
| [liberec-liebieg.json](liberec-liebieg.json) | Počátky obchodu a výroby, nájem a koupě areálu; tři podpořená tvrzení a dvě hypotézy | Relevantní odstavce městského přehledu Visit Liberec; u dvou archivních tipů pouze vyhledávací úryvky, stránky průvodců ani inventáře nebyly prohlédnuty |

## Uherský Brod

Základní otázkou je vztah nového závodu k historické České zbrojovce a čas výstavby. Dva firemní zdroje nelze počítat jako dva nezávislé archivní důkazy. Ukázka proto uchovává stav `supported`, odděluje historickou pobočku, areál a značku a neodvozuje dnešní právní kontinuitu.

Příští krok: dohledat dobovou dokumentaci stavby a rozlišit výstavbu od zahájení výroby. Přesná archivní signatura zatím známa není a není doplněna odhadem.

## Plzeň

Příklad zachovává tři události, které zjednodušené příběhy mohou sloučit: vznik strojírny, nástup Emila Škody jako inženýra a koupě podniku. Značka je samostatná entita; žádná moderní společnost nedostává automaticky celý tento životopis.

Příští krok: najít originální doklad převodu a ověřit, jaké podklady používají oba retrospektivní přehledy. Dvě instituce nemusí znamenat dva nezávislé historické prameny.

## Příbram

Ukázka přechází od veřejné archivní výstavy ke konkrétně citované archiválii: SOkA Příbram, Okresní úřad Příbram, inv. č. 135. Rozlišuje údaj z kurátorského popisku od neprovedeného úplného čtení originálu. Nevyplňuje neověřenou adresu nebo přesné datum ohlášení.

Příští krok: studium obrazu nebo originálu, přepis zápisu a spojení s dobovým adresářem. Samotný interval provozu ateliéru neurčuje datum registrace živnosti.

## Liberec

Příklad vznikl při nezávislém průchodu skillu. Odděluje obchodní oprávnění, začátek výroby v pronajatých prostorách a koupi již existujícího areálu. Tři tvrzení mají stav `supported` a opírají se o přečtený městský přehled. Dvě archivní stopy mají stav `hypothesis`: přesné názvy, rozsahy a uložení fondů byly nalezeny pouze ve vyhledávacím indexu a vyžadují kontrolu v otevřeném archivním průvodci či inventáři.

Příští krok: nejprve ověřit kandidátní fondy a inventáře, potom hledat původní obchodní oprávnění, nájemní doklady a kupní smlouvu. Datum koupě areálu nenahrazuje datum výstavby budov ani samo neprokazuje právní nástupnictví.

## Přečti hotový výstup

- [Uherský Brod](uhersky-brod-cz.md) · [HTML](uhersky-brod-cz.html)
- [Plzeň](plzen-skoda.md) · [HTML](plzen-skoda.html)
- [Příbram](pribram-drtikol.md) · [HTML](pribram-drtikol.html)
- [Liberec](liberec-liebieg.md) · [HTML](liberec-liebieg.html)

Tyto Markdown a HTML soubory jsou vygenerovány stejným nástrojem ze sousedních JSON dat bez `--public`. Veřejné příklady tak zachovávají rozsah rešerše, badatelský deník a další kroky. Po změně dat je znovu vygeneruj.

## Spusť příklady

Z kořene repozitáře:

```bash
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py validate examples/uhersky-brod-cz.json
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py validate examples/plzen-skoda.json
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py validate examples/pribram-drtikol.json
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py validate examples/liberec-liebieg.json
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py render examples/uhersky-brod-cz.json --format html --out uhersky-brod-cz.html
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py render examples/uhersky-brod-cz.json --format markdown --out uhersky-brod-cz.md
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py render examples/plzen-skoda.json --format html --out plzen-skoda.html
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py render examples/plzen-skoda.json --format markdown --out plzen-skoda.md
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py render examples/pribram-drtikol.json --format html --out pribram-drtikol.html
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py render examples/pribram-drtikol.json --format markdown --out pribram-drtikol.md
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py render examples/liberec-liebieg.json --format html --out liberec-liebieg.html
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py render examples/liberec-liebieg.json --format markdown --out liberec-liebieg.md
```

Příklady úmyslně nemají geometrii: v této rešerši nebyly přesné hranice ani body areálů nezávisle určeny. Prázdná `FeatureCollection` z jejich GeoJSON exportu je poctivější než vymyšlený bod. K mapovému výstupu nejprve dolož místo a jeho přesnost.

Dossier obsahuje `research_log` a `open_questions`. Není v něm stažený archivní korpus, celé texty článků ani fotografie bez ověřených práv. Licence aplikace se na cizí reprodukce nepřenáší.

Další zadání pro všech 14 krajů a situace pro ověření chování jsou v [prompts.md](prompts.md).
