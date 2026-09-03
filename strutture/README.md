# Rifugi e bivacchi, una zona alla volta

Elenchi pronti da importare dalla schermata **Strutture** del Profilo: formato
`mountainers-strutture` v1, lo stesso che l'app esporta
(`apps/mobile/lib/domain/shelter_file.dart`).

- `rifugi/<ZONA>.json` · `bivacchi/<ZONA>.json`
- Le zone sono quelle di Profilo → Database (`apps/mobile/lib/domain/territory.dart`):
  codice ISO dello stato e della regione, `IT-25-lombardia`.

Ogni struttura ha i campi della tabella `Shelters`: `nome`, `tipo`
(`refuge`/`bivouac`), `userTag`, `luogo`, `telefono`, `lat`, `lon`. **`luogo` e
`telefono` stanno solo sui rifugi**, come nel database: un bivacco non ha un
comune dichiarato da nessuno e non risponde al telefono.

In testa al file ci sono `zona`, `fonte` e `licenza`, che il parser ignora:
l'attribuzione deve viaggiare col dato, non con questo README.

## Da dove arrivano

OpenStreetMap, via Overpass API — dati © contributori OpenStreetMap, licenza
**ODbL 1.0**. `tourism=alpine_hut` sono i rifugi, `tourism=wilderness_hut` e
`amenity=shelter` con `shelter_type` da ricovero sono i bivacchi; il nome
corregge il tag quando dice «Bivacco» o «Rifugio» esplicitamente. Le tettoie
restano fuori. Il comune si ricava dal punto con `is_in`.

Si rifanno con `python tools/scarica_strutture.py` (tutte) o
`python tools/scarica_strutture.py IT-25 CH-TI` (alcune).

⚠️ **Non e' la piattaforma ufficiale dei cataloghi** (D206): sono file da
importare a mano, non un pacchetto che l'app va a prendere.
