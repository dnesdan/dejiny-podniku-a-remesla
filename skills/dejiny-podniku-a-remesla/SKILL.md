---
name: dejiny-podniku-a-remesla
description: "Zkoumej dějiny podniku, továrny, dílny, obchodu, hostince, mlýna, pivovaru, řemesla nebo výrobku kdekoliv v České republice. Použij při otázkách kdo zde podnikal, co vyráběl, jak se měnili provozovatelé, kam sahá rodinná živnost, co dokládá reklama, značka nebo starý výrobek a zda dva podniky historicky souvisejí. Propoj archivní rejstříky, adresáře, noviny, mapy, muzejní sbírky, patenty a současné registry; vytvoř citovanou časovou osu a odděl fakta, hypotézy a rozpory."
---

# Dějiny podniku a řemesla

Pomoz i člověku bez archivní praxe. Vysvětli, co skutečně dokládají nalezené prameny; pátrej v celých českých zemích včetně dobových německých a dalších názvů. Lokalita v příkladu není výchozí lokalitou nového výzkumu.

## 1. Vymez otázku a založ výzkum

Zjisti místo, přibližné období a alespoň jeden záchytný údaj: jméno, název, adresu, obor, fotografii nebo výrobek. Použij údaje z konverzace; nevyžaduj znovu to, co již uživatel sdělil. Při chybějícím datu začni širším rozmezím. Při více možných obcích sestav kandidáty a rozhodni podle dalších dokladů; nikdy automaticky neber první výsledek geokódování.

Otevři [metodiku](references/metodika.md). Podle úlohy přidej [prameny](references/prameny.md), [regiony](references/regiony.md) a [řemesla a dotazy](references/remesla-a-dotazy.md). Při přenosu výzkumu nebo zveřejnění čti [výstupy a kontrolu](references/vystupy-a-kontrola.md).

Spusť z kořene repozitáře; při instalaci samotné složky nahraď prefix její skutečnou cestou:

```bash
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py init --title "Historie zvoleného podniku" --theme enterprise --place "Vybraná obec" --out vyzkum.json
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py plan --place "Plzeň" --region "Plzeňský kraj" --topic "strojírenství" --theme enterprise --name "Škoda" --from-year 1850 --to-year 1910
```

Ulož do JSON pouze zjištěné údaje. Prázdná kolonka je přípustná; domyšlený majitel nebo signatura ne.

## 2. Odděl identity a role

Udržuj samostatná ID pro člověka, podnik či právnickou osobu, provozovnu/budovu, značku, výrobek a řemeslo. Člověk mohl být vlastník domu, nájemce, provozovatel, zaměstnanec, vynálezce či obchodní zástupce; každá role vyžaduje doklad a dobu platnosti.

Nepřeváděj stejné jméno, logo, adresu či přetrvávající výrobu automaticky na právní nástupnictví. ARES identifikuje subjekt zdrojových registrů; rok zápisu dnešní společnosti nemusí být rokem vzniku výroby. Současné IČO nepřiděluj historickému živnostníkovi. Pro tvrzení o právní kontinuitě vyhledej konkrétní rejstříkový zápis nebo listinu; jinak označ pouze výrobní, místní nebo značkovou návaznost.

Přepisuj povolání nejprve v původním znění. Normalizaci a překlad uveď zvlášť s mírou jistoty. Brašnáře automaticky nepřejmenuj na sedláře; blízké obory lze použít pro rozšíření dotazu, ne pro změnu důkazu.

## 3. Vyber prameny a projdi je ve vrstvách

1. Zorientuj se v odborné bibliografii, místním muzeu a existujících inventářích. Firemní jubilejní text označ jako vlastní retrospektivu podniku.
2. Vyhledej dobové adresáře, inzerci, katalogy a ročenky v relevantních instalacích Krameria, případně ANNO. Kombinuj jméno, místo, obor a čas; ověř obraz stránky, datum, číslo a stránku. OCR je vodítko, ne věrný přepis.
3. Podle období zkoumej cechovní knihy, živnostenské a obchodní rejstříky, spisy firmy, okresní či městské fondy, komory a podnikové archivy. Zvol příslušný archiv podle původce, území a doby; katalog fondu není digitalizovaný obsah.
4. Propoj provozovnu s mapami, stavebními spisy, adresami a parcelami. Změna čísla domu ani vlastnictví budovy sama nedokládá změnu podniku.
5. Doplň výrobky, ochranné známky a vynálezy z muzejních katalogů a ÚPV. Rozliš autora, přihlašovatele, držitele práva, výrobce a prodejce. Záznam patentu nedokládá skutečnou sériovou výrobu.
6. U novějších subjektů kontroluj ARES, příslušný veřejný rejstřík a sbírku listin. Cituj datovaný stav a konkrétní dokument, ne dnešní vyhledávací výsledek jako důkaz staršího období.

Použij [strojový katalog zdrojů](references/sources.json) a `badatel.py sources --theme enterprise`. Síťový nástroj `scripts/zdroje.py --help` uvádí skutečně implementované adaptéry. Odkaz na portál v katalogu není automatický stahovač. Při dostupnosti navazujících skillů postupuj podle [návaznosti](references/navazujici-skilly.md).

## 4. Zapiš důkaz a nejistotu

Ke každému tvrzení ulož `entity_ids`, `status` a `evidence` s `source_id`, přesným `locator` a druhem záznamu. Připoj URL, instituci, datum přístupu, dostupnost a práva zdroje. Pro archiv přidej fond, inventární číslo/signaturu, karton/knihu a folio či snímek; pro tisk titul, datum, číslo a stránku. Je-li k dispozici jen kurátorský popis, řekni to.

Používej `documented` pro tvrzení přímo doložené odpovídajícím záznamem, `supported` pro závěr podpořený např. retrospektivními přehledy, `hypothesis` pro neověřenou domněnku a `disputed` pro rozpor. Počet kopií téhož článku není počet nezávislých důkazů. Nepovyšuj stav tvrzení jen podle počtu nalezených webů.

Odliš první nalezenou zmínku, doložený interval provozu, zahájení výroby, registraci a přesné datum založení. „Nenalezeno“ zapiš včetně dotazu, rozsahu a limitů hledání; nepřepiš je na „neexistovalo“ nebo „zaniklo“.

## 5. Odevzdej výsledek, který lze ověřit a rozšířit

Vytvoř stručný závěr, časovou osu, oddělené karty subjektů/provozoven a výrobků, přehled pramenů a tři nejcennější další kroky. U zásadních rozporů ukaž obě verze. Nezaměň mapu areálu za důkaz právní identity.

```bash
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py validate vyzkum.json
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py render vyzkum.json --format html --out vyzkum.html
python3 skills/dejiny-podniku-a-remesla/scripts/badatel.py render vyzkum.json --format markdown --out vyzkum.md
```

Před veřejným vydáním označ citlivé entity a tvrzení, vytvoř export s `--public` a přečti skutečný výstup. Automatický filtr nemůže poznat citlivost neznačeného textu. Výroky o žijících lidech, zaměstnanecké spisy a ústní vzpomínky vyžadují zvláštní kontrolu. Skeny a fotografie přibaluj jen při doloženém oprávnění; režim DNNT neobcházej. Bez výslovného pokynu uživatele neodesílej dotazy archivům ani firmám.

Síťové klienty používej šetrně se sdílenou cache. Při 401/403/429/503 skonči, zapiš překážku a nabídni autorizované ruční pokračování či jiný druh pramene; nestřídej účty nebo proxy pro obcházení blokace. Při předání výzkumu zachovej nezpracované kandidáty a neúspěšné dotazy.

## Hotové příklady a ověření

Repozitář obsahuje malé doložené příklady **Uherský Brod – Česká zbrojovka**, **Plzeň – Waldsteinova strojírna a Emil Škoda** a **Příbram – fotografická živnost Františka Drtikola**. Jejich cílem je ukázat práci s důkazy a odlišnými typy podnikání, ne nahradit úplnou monografii. Pro novou obec vždy vytvoř nový výzkum. Dodané příklady neprohlašuj za nové živé hledání.

## Nástroje a hranice získání důkazu

Před síťovým dotazem čti [přehled přibalených nástrojů](references/nastroje.md). U zdrojů zapisuj, zda byl prohlédnut jejich obsah (`verification_status`), nebo je znám pouze úryvek z indexu. Samotný úryvek nesmí být jediným podkladem tvrzení `documented` či `supported`. U geometrie zachovej strukturovaný význam bodu v `geometry_role`; neukládej toto rozlišení jen do pracovních poznámek.
