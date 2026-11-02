# Návaznost na existující české badatelské skilly

Jde o spolupráci samostatných projektů. Existence nástroje v cizím repozitáři neznamená, že je přibalen zde nebo že každý jeho síťový endpoint právě funguje. Otevřený PR neposuzuj jako vydanou verzi. Přesný auditovaný stav a licenční původ je uveden v dokumentaci tohoto repozitáře.

## Kdy přepnout téma

| Projekt | Předej mu | Vrať do tohoto výzkumu |
|---|---|---|
| [Rodokmen](https://github.com/sarsonj/rodokmen-skill) | Identifikaci člověka v matrice, sčítání či pobytové evidenci | Přepis, identifikátory osoby, citaci snímku a míru jistoty |
| [Paměť rodu](https://github.com/thejanhromek/pamet-rodu) | Rozhovor s pamětníkem, rodinné doklady, osobní příběh | Jednotlivá tvrzení a jejich původ; vzpomínku nezaměň za úřední záznam |
| [Dějiny domu](https://github.com/vzoha/dejiny-domu-skill) | Vlastnictví a stavební historii konkrétní provozovny | Časově doložené držitele/vlastníky, historická čísla a mapové doklady |
| [Paměť krajiny](https://github.com/dnesdan/pamet-krajiny) | Náhon, důl, vlečku, cestu, proměny širšího areálu | Místa a intervaly změn se zdroji a nejistotou lokalizace |

Pro přenos použij stabilní ID a citace, ne automatické spuštění datového Pythonu z cizího projektu. Pokud se dvě osoby nebo objekty pouze podobají, zachovej dva kandidáty. Neimportuj celý soukromý rodokmen jen kvůli ověření jednoho historického živnostníka.

## Užitečné podněty z PR Rodokmenu

- [#29](https://github.com/sarsonj/rodokmen-skill/pull/29): rozšíření archivních klientů a Krameria; jednotlivé adaptéry ověř před použitím, sjednoť je se společnými limity.
- [#46](https://github.com/sarsonj/rodokmen-skill/pull/46): předání rozpracovaného bádání; pro podniky zachovej zejména nenalezené a nerozhodnuté varianty názvů.
- [#53](https://github.com/sarsonj/rodokmen-skill/pull/53) a [#60](https://github.com/sarsonj/rodokmen-skill/pull/60): přenositelnost omezování rychlosti a sdílená cache; více agentů nesmí násobit zatížení stejného archivu.
- [#62](https://github.com/sarsonj/rodokmen-skill/pull/62): vodní mlýny a vrchnostenské prameny; jde o metodické doplnění, ne kompletní nový stahovač mlýnských databází.
- [#19](https://github.com/sarsonj/rodokmen-skill/pull/19): propojení domů a mapových výstupů; nepřebírej heuristiku výběru první nebo nejčastější obce jako důkaz identity.

Při použití cizího klienta přečti jeho aktuální návod a licenci. Nepřebírej výslovně vyňaté playbooky. Zdejší instrukce jsou nově sepsané; tematické principy se uplatňují obecně na Čechy, Moravu i Slezsko.
