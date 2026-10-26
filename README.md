# Unser Zuhause – Automationen (Blueprints)

Automationen zum Dashboard **„Unser Zuhause“** als Home-Assistant-Blueprints. Mit einem Klick importieren,
Personen auswählen, fertig.

| Blueprint | Was er macht | Import |
| --- | --- | --- |
| **Systemwarnungen** | Push an die Home-Assistant-App, wenn der Global Health Score fällt, der Speicher fast voll ist oder das letzte Backup zu alt ist. Antippen öffnet die System-Seite. | [![Blueprint importieren](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FSebastianInTheWild%2Fha-unser-zuhause-blueprints%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Funser_zuhause%2Fsystemwarnungen.yaml) |
| **Abwesenheits-Check** | Wechselt der Hausmodus auf „Abwesend“: Push mit allem, was noch offen ist oder läuft (Fenster & Türen, Lichter, Musik, Geräte) – mit Knopf „Lichter & Musik aus“. | [![Blueprint importieren](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FSebastianInTheWild%2Fha-unser-zuhause-blueprints%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Funser_zuhause%2Fabwesenheits_check.yaml) |
| **Kamera-Modus** | Stellt Kameras/Alarmanlagen nach Hausmodus und Uhrzeit auf Abwesend, Zuhause oder Nacht – einzelne erst, wenn z. B. der Fernseher aus ist. Optional Push, wenn sich ein Modus geändert hat. | [![Blueprint importieren](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FSebastianInTheWild%2Fha-unser-zuhause-blueprints%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Funser_zuhause%2Fkamera_modus.yaml) |

## Voraussetzungen

- **Home-Assistant-App** auf dem Handy, angemeldet mit dem eigenen Benutzer – dorthin gehen die Nachrichten.
- Integration [Unser Zuhause](https://github.com/SebastianInTheWild/ha-unser-zuhause-integration): Du wählst
  im Blueprint Personen statt Handys, die Aktion „Benachrichtigen“ findet deren Handys selbst. Die Person muss
  mit ihrem Benutzer verknüpft sein (Einstellungen → Personen).
- **Systemwarnungen:** Integration *System Monitor* (Sensor „Speicherplatz belegt“ in %), die eingebaute
  *Backup*-Integration und optional *Home Assistant Global Health Score* (HAGHS, über HACS).
- **Abwesenheits-Check:** am einfachsten die Sensoren der Integration Unser Zuhause (Hausmodus,
  „Fenster & Türen“, „Lichter an“). Eigene Sensoren gehen auch, wenn sie im Attribut `entity_id` die Liste
  der offenen bzw. eingeschalteten Entitäten führen (wie Gruppen).
- **Kamera-Modus:** eine Alarm-Zentrale (`alarm_control_panel`), z. B. Eufy (Entität „Security mode“), Alarmo
  oder Ring. Die Integration Unser Zuhause braucht es nur für die Nachricht und den Hausmodus.

## Einrichten

1. Oben auf **Blueprint importieren** klicken (oder in HA: *Einstellungen → Automationen & Szenen →
   Blueprints → Blueprint importieren* und den Link zur YAML-Datei einfügen).
2. *Automation erstellen* aus dem Blueprint, **Personen** auswählen (eine oder mehrere), Werte bei Bedarf anpassen, speichern.

### Systemwarnungen – Einstellungen

| Feld | Standard |
| --- | --- |
| Global Health Score / Warnen unter | `sensor.system_ha_global_health_score` / 80 (30 Minuten lang) |
| Speicherplatz / Warnen über | `sensor.disk_use_percent_config` / 85 % (10 Minuten lang) |
| Letztes Backup / älter als | `sensor.backup_letztes_erfolgreiches_automatisches_backup` / 2 Tage, geprüft um 09:00 |
| Seite beim Antippen | `/unser-zuhause/system` |

### Abwesenheits-Check – Einstellungen

| Feld | Standard |
| --- | --- |
| Hausmodus / Zustand „abwesend“ | `select.unser_zuhause_hausmodus` / `abwesend` |
| Fenster & Türen | `binary_sensor.unser_zuhause_fenster_turen` |
| Lichter an | `sensor.unser_zuhause_lichter_an` |
| Weitere Geräte | leer – z. B. „Läuft“-Sensor des Trockners (gemeldet bei `on`, `run`, `running`) |
| Musik/Medien melden | an (alle `media_player` im Zustand „playing“) |

Beispiel-Nachricht:

```
🏠 Noch offen oder an
🪟 Offen: Büro Fenster
💡 An: Deko Lampe, Pisskott
🔊 Spielt: Wohnzimmer
[ Lichter & Musik aus ]
```

### Kamera-Modus – Einstellungen

| Feld | Standard |
| --- | --- |
| Alarm-Zentralen | – (Pflicht) |
| Hausmodus / Zustand „abwesend“ | `select.unser_zuhause_hausmodus` / `abwesend` (jeder andere Wert gilt als zuhause) |
| Zuhause-Modus ab / Nacht-Modus ab | 07:00 / 21:00 |
| Später in den Nacht-Modus | leer – z. B. die Zentrale im Wohnzimmer, erst wenn der Fernseher 5 Minuten aus ist; bis dahin Zuhause-Modus |
| Personen | leer = keine Nachricht |
| Status prüfen nach | 30 Sekunden (Eufy meldet den neuen Modus verzögert) |

Beispiel-Nachricht (nur, wenn sich ein Modus geändert hat):

```
📷 Kameras
Hamm: 😴 Nacht
Speicher: 😴 Nacht
```

## Dazugehörige Repos

- [ha-unser-zuhause](https://github.com/SebastianInTheWild/ha-unser-zuhause) – Dashboard-Strategy
- [ha-unser-zuhause-cards](https://github.com/SebastianInTheWild/ha-unser-zuhause-cards) – Karten
- [ha-unser-zuhause-integration](https://github.com/SebastianInTheWild/ha-unser-zuhause-integration) – Integration

## Lizenz

MIT · Autor: SebastianInTheWild
