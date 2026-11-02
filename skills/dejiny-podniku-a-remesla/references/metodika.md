# Metodika podnikových a řemeslných dějin

## Obsah

1. Rozlišení subjektů a času
2. Postup podle vstupu
3. Závěry a rozpory
4. Dokončení jednoho pracovního kola

## Rozlišení subjektů a času

Před psaním příběhu sestav malé tabulky entit. Základní jednotkou není příjmení ani adresa. Používej stabilní ID, jejichž význam se nemění s aktuální podobou názvu.

| Entita | Typ v JSON | Co k ní patří | Co z ní neplyne |
|---|---|---|---|
| Člověk | `person` | Dobové jméno, doložená role, identifikační doklady | Že každý stejnojmenný živnostník je tatáž osoba |
| Historický podnik / právnická osoba | `organization` | Dobové označení, forma, registrace, provozní historie; zásadní meze identity vysvětli v textu příslušného tvrzení | Že dnešní firma je totožná se všemi předchozími nositeli názvu |
| Dílna / tovární budova | `building` | Adresy, parcely, stavební vývoj a skutečná lokalizace | Že vlastník budovy řídil podnik |
| Značka | `brand` | Nápis, logo, doložený držitel a období užívání | Že její uživatel je původní výrobce |
| Výrobek / výrobková řada | `product` | Model, katalogové označení, doklad výrobce, datace konkrétního kusu | Že obchodník uvedený v reklamě vše vyráběl |
| Řemeslo | `craft` | Přesně přepsaný název a kontext historického výrazu | Vlastnictví dílny, kvalifikace nebo členství v cechu |

Neznámé údaje nech neznámé. Samotná podobnost nestačí k připojení aliasu. Alias potřebuje zdroj a pokud je to možné čas platnosti; dva odlišné podniky stejného názvu mají dvě entity. Překlad názvu není nová právní identita.

### Události, které je nutné oddělit

- první známá zmínka;
- ohlášení živnosti nebo zápis společnosti;
- vznik dílny či stavební povolení;
- zahájení výroby nebo první dodávka;
- koupě aktiv, budov, podílu nebo celého podniku;
- změna firmy, ochranné známky nebo sídla;
- uzavření konkrétní provozovny, zastavení výroby, likvidace a výmaz subjektu.

Těmto událostem nepřiřazuj stejné datum bez dokladu. Přesný den uváděj v textu tvrzení jen tehdy, je-li opravdu doložen; časový model může uchovat rok nebo interval. Při pouhém intervalu vytvoř `precision: range` nebo `approximate`, ne uměle přesný okamžik.

### Druhy návaznosti

Právní nástupnictví vyžaduje odpovídající listinu či rejstříkový zápis. Technická návaznost může spočívat v převzetí strojů či výroby. Personální návaznost v přechodu zaměstnanců. Místní návaznost ve využití stejného areálu. Značková návaznost v užívání názvu či známky. Každý z těchto vztahů vyjádři zvlášť a připoj konkrétní důkaz. Vlastníkem podílu může být jiný subjekt než vlastník areálu nebo držitel známky.

## Postup podle vstupu

### Známé jméno nebo název

1. Zapiš původní podobu včetně právní formy, diakritiky, iniciál a dobového jazyka.
2. Vyhledej název s místem a oborem; postupně obměňuj varianty. Časté příjmení bez dalšího identifikátoru nepovažuj za shodu.
3. Porovnej datum, adresu, obor, osoby v orgánech nebo rodinné vazby jen tam, kde jsou relevantní a doložené.
4. Získej nejstarší a nejmladší dohledaný doklad. Pojmenuj je tak, nikoli jako založení a zánik.
5. Přejdi od novinového nálezu k archivnímu fondu podle původce: firma, rejstříkový soud, okresní úřad, město, komora či cech.

### Známý dům nebo areál

1. Rozliš popisné/orientační číslo, parcelu a dnešní adresu. Číslo v adresáři může patřit bydlišti, kanceláři či prodejně.
2. Dohledávej provozovatele, nájemce a vlastníka nezávisle. Stavební spis může popisovat zamýšlené, nikoli dokončené využití.
3. Porovnej plány s mapou a fotografiemi. Souřadnice centra obce nejsou souřadnicemi podniku.
4. Zachyť přesun provozu do jiné části města, rozdělení závodů či zánik budovy jako samostatné události.

### Fotografie, reklama nebo výrobek

1. Zachovej nezměněný vstup; eviduj vlastníka a možnost zveřejnění.
2. Přepiš čitelné nápisy, označ nečitelnost. Vizuální odhad odliš od přepisu.
3. Hledej přesný text, značku, model, ulici nebo adresu v katalozích a tisku. Prověř, zda se název vztahuje k výrobci, prodejci, servisu či dovozci.
4. Ověř dataci vydání katalogu a případné pozdější přetisky. Starý model se mohl vyrábět dlouho a kus mohl být opraven.
5. Formuluj nejvýše doložený interval. Fotografie z publikace dokládá reprodukci v dané publikaci; datum knihy nemusí být datem snímku.

### Neznámý živnostník a známé řemeslo

Postupuj od místního adresáře či soupisu ke konkrétnímu člověku. Potom teprve připoj matriku nebo sčítání z Rodokmenu. Údaj „sedlář“ může být zaměstnání, nikoli samostatná živnost. Nepředpokládej, že existuje dochovaný personální spis nebo úplný seznam zaměstnanců.

Oblastní a okresní rejstříky, městské a cechovní fondy jsou hlavní cíle starší podnikové rešerše. Tento přechod vysvětluje [SOA Praha – Práce šlechtí](https://soapraha.gov.cz/vystavagenealogie/05_praceslechti/); skutečné uložení a dochování ověř v konkrétním inventáři.

## Závěry a rozpory

| Typ nálezu | Bezpečný závěr | Nepodložené rozšíření |
|---|---|---|
| Inzerát v datovaném čísle novin | V tomto vydání byla publikována tato nabídka a adresa | Živnost vznikla právě toho dne; inzerent opravdu poskytl všechny služby |
| Adresář označený rokem | Osoba/firma je uvedena v daném vydání | Vydání přesně odpovídá stavu k 1. lednu a obsahuje všechny subjekty |
| Patent nebo ochranná známka | Konkrétní záznam přihlášky, vlastníka či stavu k datu | Patent byl využit ve výrobě; známka byla nepřetržitě užívána |
| Prázdné hledání v OCR | Daný dotaz v daném rozsahu nic nevrátil | Firma neexistovala nebo ukončila činnost |
| Firemní jubileum | Podnik se prezentuje touto chronologií | Všechny údaje jsou nezávisle archivně ověřené |
| Podobné logo na předmětu | Kandidát na původ / značku | Jistá autenticita, výrobní rok či provenience tohoto kusu |

U rozporu nevybírej pohodlnější datum. Zapiš oba zdroje, možné vysvětlení (jiná událost, přetisk, změna kalendáře, OCR, reklamní tradice) a krok, který rozpor může rozhodnout. Reklamní prvenství „první“, „nejstarší“, „největší“ nepřebírej jako vlastní závěr bez nezávislého srovnání.

## Dokončení jednoho pracovního kola

Uzavři smysluplný rozsah: například identifikace provozovny a první tři doklady. Uveď co bylo čteno, co je jen katalogový tip a co bylo nepřístupné. Zaznamenej neúspěšné dotazy. Ponech jednu prioritní otázku ke každé větší mezeře; neslibuj výsledky z nedigitalizovaného fondu. Pokud lze smysluplně pokračovat online, pokračuj; otázku uživateli si nech jen pro rozlišení zásadních kandidátů nebo chybějící neveřejný podklad.

## Veřejně srozumitelné meze identity

Rozdíl mezi historickým podnikem, právnickou osobou, značkou a budovou vysvětli i v textu příslušného tvrzení. Nestačí pracovní `notes`, které veřejný export odstraňuje. U mapového bodu zapiš `geometry_role`; centroid obce se nesmí prezentovat jako poloha dílny. Stav přímého prohlédnutí zdroje uchovej v `verification_status`; vyhledávací index je pouze vodítko. Viz [příkazy a důkazní kontrola](nastroje.md).
