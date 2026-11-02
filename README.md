# Dějiny podniku a řemesla

[![Tests](https://github.com/dnesdan/dejiny-podniku-a-remesla/actions/workflows/tests.yml/badge.svg)](https://github.com/dnesdan/dejiny-podniku-a-remesla/actions/workflows/tests.yml)

**Obecný badatelský skill pro historii podnikání v celé České republice.** Pomáhá zkoumat továrny, dílny, obchody, hostince, mlýny, pivovary, značky, výrobky i jednotlivá řemesla. Výsledkem je citovaná časová osa a přehled toho, co víme, co si zatím jen myslíme a co má smysl hledat dál.

Podnik, jeho právní forma, majitel, značka a budova mají vlastní identitu. Stejné logo nebo adresa nejsou automatickým důkazem právního nástupnictví. To je hlavní zásada tohoto skillu.

## Co umí

- Vést výzkum od jednoho jména, fotografie, adresy či oboru až k doloženým tvrzením.
- Vybrat celostátní i regionální prameny pro všech 14 krajů; pracovat také s dobovými názvy a přeshraničními zdroji.
- Spojit archivní rejstříky, adresáře, novinovou inzerci, mapy, muzejní sbírky, ochranné známky a aktuální registry.
- Uchovat zdroje a tvrzení v přenositelném JSON; kontrolovat odkazy, datace a důkazy.
- Vytvořit samostatné HTML, Markdown nebo GeoJSON z doložených dat. GeoJSON obsahuje pouze entity, kterým byla skutečně přiřazena geometrie.
- Připravit další konkrétní archivní postup tam, kde skeny nebo oprávnění nejsou dostupné.

Internetové zdroje mají různé režimy: některé lze číst přes API, jiné pouze přes portál a část až v badatelně. Katalog tyto možnosti rozlišuje. Skill není univerzální stahovač všech českých archivů.

## Začni s AI

Použij složku [`skills/dejiny-podniku-a-remesla`](skills/dejiny-podniku-a-remesla) jako standardní balíček skillu v klientovi, který podporuje `SKILL.md`. Obsahuje instrukce, reference, skripty, datové schéma a šablonu. Celý repozitář navíc obsahuje příklady a testy.

Pokud klient neumí instalovat skill, dej mu přečíst [`SKILL.md`](skills/dejiny-podniku-a-remesla/SKILL.md) a zpřístupni ostatní soubory ze stejné složky. K práci s webem je potřeba vyhledávací nebo prohlížecí nástroj daného klienta; deterministické příkazy níže fungují i bez AI.

Příklady zadání:

> „Zjisti, kdo provozoval tento mlýn u Pelhřimova v letech 1850–1930. Odděl vlastníky budovy od mlynářů a u každého tvrzení připoj pramen.“

> „Mám starou reklamu na krejčovství v Liberci. Přečti název, zkus najít adresu a vysvětli, které údaje ještě nejsou jisté.“

> „Prozkoumej počátky strojírny v Plzni. Nezaměň ji s mladoboleslavskou automobilkou ani dnešní společností stejné značky.“

> „Porovnej zmínky o brašnáři a sedláři stejného příjmení v Uherském Brodě. Zatím předpokládej dvě osoby, dokud nebude doklad identity.“

Další regionální a chybové scénáře jsou v [`examples/prompts.md`](examples/prompts.md).

## Rychlé vyzkoušení

Potřebuješ **Python 3.10 nebo novější**. Běžné příkazy používají standardní knihovnu Pythonu.

```bash
git clone https://github.com/dnesdan/dejiny-podniku-a-remesla.git
cd dejiny-podniku-a-remesla
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py validate examples/plzen-skoda.json
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py render examples/plzen-skoda.json --format html --out plzen-skoda.html
```

Otevři vytvořený `plzen-skoda.html` v prohlížeči. Není potřeba webový server. Pokud se `python3` ve tvém prostředí jmenuje `python`, použij toto jméno.

Nový projekt a plán:

```bash
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py init --title "Historie dílny" --theme enterprise --place "Vybraná obec" --out vyzkum.json
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py plan --place "Liberec" --region "Liberecký kraj" --topic "textil" --theme enterprise --from-year 1850 --to-year 1930 --out plan.json
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py sources --theme enterprise
python3 skills/dejiny-podniku-a-remesla/scripts/zdroje.py --help
```

Plán je seznam další práce, nikoli hotová rešerše. Síťové výstupy nejprve posuď a až potom z nich vytvoř tvrzení. Schéma ani validátor neposuzují pravdivost historického závěru.

## Doložené příklady

| Příklad | Co ukazuje | Rozsah důkazů |
|---|---|---|
| [Uherský Brod – Česká zbrojovka](examples/uhersky-brod-cz.md) · [JSON](examples/uhersky-brod-cz.json) | Rozlišení areálu, podniku, pobočky a značky | Firemní ročenka 2019 a jubilejní text 2021; retrospektivní zdroje stejného původu |
| [Plzeň – Waldstein / Škoda](examples/plzen-skoda.md) · [JSON](examples/plzen-skoda.json) | Rozdíl mezi založením strojírny, příchodem inženýra a koupí podniku | Přehled města Plzně a podniková historie; původní smlouva zatím neprohlédnuta |
| [Příbram – fotografická živnost](examples/pribram-drtikol.md) · [JSON](examples/pribram-drtikol.json) | Přechod od známého jména k identifikovatelnému živnostenskému prameni | Výstava SOA Praha s konkrétní archivní citací a reprodukcí; bez úplného přepisu originálu |
| [Liberec – Liebiegové](examples/liberec-liebieg.md) · [JSON](examples/liberec-liebieg.json) | Rozlišení obchodu, výroby v nájmu a koupě existujícího areálu; zachování neověřených archivních tipů | Tři tvrzení podpořená otevřeným městským přehledem; dvě hypotézy pouze z vyhledávacího indexu, bez prohlédnutí archivních průvodců a inventářů |

Čtyři malé skutečné rešeršní ukázky vznikly z veřejných podkladů 2. listopadu 2026. Liberecký příklad výslovně odlišuje přečtený městský text od dvou neověřených archivních stop. Příklady neobsahují soukromou rodinnou historii zadavatele. Dodané přehledy jsou exportované bez `--public`, aby zachovaly rozsah rešerše, deník a další kroky. Podrobnosti, meze a reprodukovatelné příkazy: [`examples/README.md`](examples/README.md).

## Testování

```bash
python3 -m unittest discover -s tests -v
```

Automatické testy ověřují datový model, exporty, chování síťových klientů nad řízenými odpověďmi a průchod dodaných příkladů. Živé síťové ověření je oddělené, aby výpadek cizího archivu neznamenal chybu lokálního testu. Úspěšný test modelu nedokazuje úplnost pramenů nebo správnost všech historických interpretací. Konkrétní provedená ověření zachycuje dokumentace testování v repozitáři.

## Na čem navazuje

Projekt využívá zkušenosti z [Rodokmenu](https://github.com/sarsonj/rodokmen-skill), [Paměti rodu](https://github.com/thejanhromek/pamet-rodu) a [Dějin domu](https://github.com/vzoha/dejiny-domu-skill), včetně posouzených otevřených PR. Převádí jejich podněty do obecného modelu tvrzení, institucí, provozoven a časových vztahů. Rozsah převzetí a licence jsou popsány v dokumentaci původu v repozitáři; otevřený PR není automaticky součástí upstream vydání.

Pro širší okolí továrny, náhony, dopravní spojení či proměny průmyslové krajiny použij sourozenecký skill [Paměť krajiny](https://github.com/dnesdan/pamet-krajiny).

## Práva a soukromí

Licence kódu a vlastních textů neuděluje práva k cizím skenům, fotografiím nebo logům. U každého zdroje se uchovává jeho dostupnost a licence; při neznámém oprávnění se sdílí citace a vlastní shrnutí. Veřejný export s `--public` respektuje označené citlivé záznamy, ale vyžaduje následné přečtení člověkem. Historické zápisy o zaměstnancích ani současné osobní údaje automaticky nepatří na veřejný web.

## Implementované klienty a ověření

Součástí balíku je **62 popsaných zdrojů** a **7 síťových příkazů**: registr Krameriů, kandidáti RÚIAN, vyhledávání Kramerius v5/v7, seznam WMS vrstev, jednotlivý mapový výřez, inspekce IIIF manifestu a ARES. Kompletní příklady příkazů, limity a zacházení s chybami jsou v [referenci nástrojů](skills/dejiny-podniku-a-remesla/references/nastroje.md).

Původ návrhu a vyhodnocení **všech 25 upstream PR** najdeš v [UPSTREAM.md](UPSTREAM.md). Konkrétní lokální, nezávislé a živé ověření zaznamenává [TESTING.md](TESTING.md). Externí podklady mají [vlastní licenční podmínky](THIRD_PARTY_NOTICES.md).

Čtvrtý příklad z nezávislého průchodu: [Liebiegové v Liberci](examples/liberec-liebieg.md). Rozlišuje tři závěry z otevřeného městského přehledu a dvě výslovně neověřené archivní stopy z vyhledávacího indexu. K dispozici je JSON, Markdown a samostatné HTML.
