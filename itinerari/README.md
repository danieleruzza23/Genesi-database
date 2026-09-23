# Itinerari, una zona e una disciplina alla volta

Elenchi pronti da importare dalla schermata **Database** del Profilo: formato
`4monkeys-itinerari` v1, lo stesso che l'app esporta
(`apps/mobile/lib/domain/catalog_file.dart`).

- `<ZONA>-<disciplina>.json`, una regione **e una disciplina** per file
- Le zone sono quelle di Profilo → Database
  (`apps/mobile/lib/domain/territory.dart`): codice ISO dello stato e della
  regione, `IT-25-lombardia`, come in `strutture/`.
- Le discipline sono `climbing`, `ice_mixed`, `skialp`, `mountaineering`.

**Una disciplina per file, non quattro insieme**: la schermata Database chiede
una zona **e** una disciplina alla volta, e un file con dentro tutto darebbe a
chi ha scelto l'arrampicata anche le gite con gli sci.

Dentro, la gerarchia che l'import si aspetta: **luogo → parete → itinerari**.
Ogni itinerario ha i campi della tabella `Routes` — `nome`, `gradoMassimo`,
`gradoObbligatorio`, `tiri`, `sviluppo`, `quotaMassima`, `link`.

**Ogni campo sta dove la sua disciplina lo dichiara** (`route_fields.dart`), o
sarebbe un dato che la schermata non mostra e non lascia correggere:

- su **scialpinismo** la difficoltà sciistica è il *grado obbligatorio*
  ("Difficoltà sciistica" nel modulo), perché un grado massimo lì non esiste;
- su **ghiaccio** l'impegno è il grado obbligatorio, e si chiama "Impegno";
- la **spittatura** è solo roccia, i **tiri** solo dove si sale a tiri;
- su **scialpinismo e alpinismo** il nome dell'itinerario è il **versante**
  ("Nord-est"), scritto per esteso come lo scrive la tendina dell'app: la
  montagna è la parete, il versante è la via.

## Da dove arrivano

[gulliver.it](https://www.gulliver.it) e
[camptocamp.org](https://www.camptocamp.org). **Si tiene il dato di fatto e si
rimanda alla relazione: il testo non si copia.** Grado, esposizione, quota,
sviluppo, tiri — più il **link alla scheda originale**, che è la forma
dell'attribuzione e viaggia dentro ogni voce. Descrizioni, relazioni tiro per
tiro e storico restano fuori: sono testi dei singoli utenti che li hanno
scritti, e nessun accordo col sito potrebbe coprirli.

**16.650 itinerari** in 37 zone, quattro discipline: arrampicata, scialpinismo,
alpinismo, ghiaccio e misto.

Chi trova un proprio testo qui dentro apra una issue: si toglie.

## Cosa non c'è

**1.888 voci non sono entrate**, e non è una perdita da recuperare
indovinando: su scialpinismo e alpinismo l'itinerario si chiama col versante, e
dove la fonte non lo dichiara dedurlo dal nome della montagna inventerebbe
proprio il dato che distingue due itinerari sulla stessa cima.

Si rifanno con `python tools/converti-itinerari.py` dal repository dell'app.

⚠️ **Non è la piattaforma ufficiale dei cataloghi** (D206): sono file da
importare a mano, una zona alla volta, non un pacchetto che l'app va a
prendere. L'import salta quel che c'è già e non sovrascrive le proprie
annotazioni.
