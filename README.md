# Unser Zuhause – Automationen (Blueprints)

[![Validate](https://github.com/SebastianInTheWild/ha-unser-zuhause-blueprints/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/SebastianInTheWild/ha-unser-zuhause-blueprints/actions/workflows/validate.yml)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2024.10%2B-41BDF5?logo=homeassistant&logoColor=white)](https://www.home-assistant.io/)
[![Blueprints](https://img.shields.io/github/directory-file-count/SebastianInTheWild/ha-unser-zuhause-blueprints/blueprints/automation/unser_zuhause?type=file&label=Blueprints&color=41BDF5)](blueprints/automation/unser_zuhause)
[![Benötigt: Unser Zuhause](https://img.shields.io/badge/ben%C3%B6tigt-Unser%20Zuhause-blue)](https://github.com/SebastianInTheWild/ha-unser-zuhause-integration)
[![Lizenz](https://img.shields.io/github/license/SebastianInTheWild/ha-unser-zuhause-blueprints)](LICENSE)
[![Letzter Commit](https://img.shields.io/github/last-commit/SebastianInTheWild/ha-unser-zuhause-blueprints)](https://github.com/SebastianInTheWild/ha-unser-zuhause-blueprints/commits/main)

Automationen zum Dashboard **„Unser Zuhause“** als Home-Assistant-Blueprints. Mit einem Klick importieren,
Personen auswählen, fertig.

| Blueprint | Was er macht | Import |
| --- | --- | --- |
| **Systemwarnungen** | Push an die Home-Assistant-App, wenn der Global Health Score fällt, der Speicher fast voll ist oder das letzte Backup zu alt ist. Antippen öffnet die System-Seite. | [![Blueprint importieren](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FSebastianInTheWild%2Fha-unser-zuhause-blueprints%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Funser_zuhause%2Fsystemwarnungen.yaml) |
| **Abwesenheits-Check** | Wechselt der Hausmodus auf „Abwesend“: Push mit allem, was noch offen ist oder läuft (Fenster & Türen, Lichter, Musik, Geräte) – mit Knopf „Lichter & Musik aus“. | [![Blueprint importieren](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FSebastianInTheWild%2Fha-unser-zuhause-blueprints%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Funser_zuhause%2Fabwesenheits_check.yaml) |
| **Kamera-Modus** | Stellt Kameras/Alarmanlagen nach Hausmodus und Uhrzeit auf Abwesend, Zuhause oder Nacht – einzelne erst, wenn z. B. der Fernseher aus ist. Optional Push, wenn sich ein Modus geändert hat. | [![Blueprint importieren](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FSebastianInTheWild%2Fha-unser-zuhause-blueprints%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Funser_zuhause%2Fkamera_modus.yaml) |
| **Hausmodus** | Setzt den Hausmodus auf „anwesend“, sobald jemand heimkommt, und auf „abwesend“, wenn alle weg sind. Optional mit Pause-Schalter, der sich selbst wieder abschaltet. | [![Blueprint importieren](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FSebastianInTheWild%2Fha-unser-zuhause-blueprints%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Funser_zuhause%2Fhausmodus.yaml) |
| **Rollläden** | Schließt die Rollläden, wenn der Hausmodus auf „abwesend“ geht, und öffnet sie beim Heimkommen – tagsüber alle gewählten, abends nur ausgewählte. | [![Blueprint importieren](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FSebastianInTheWild%2Fha-unser-zuhause-blueprints%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Funser_zuhause%2Frolllaeden.yaml) |
| **Licht nach Zeitplan** | Lichter an bei Sonnenuntergang und/oder zur Uhrzeit, aus zur Uhrzeit und/oder bei Sonnenaufgang – mit Helligkeit, Farbtemperatur, Einblenden und Bedingung. | [![Blueprint importieren](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FSebastianInTheWild%2Fha-unser-zuhause-blueprints%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Funser_zuhause%2Flicht_zeitplan.yaml) |
| **Person kommt/geht** | Push, wenn jemand nach Hause kommt oder geht (mit Zone, z. B. „📍 Arbeit“). | [![Blueprint importieren](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FSebastianInTheWild%2Fha-unser-zuhause-blueprints%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Funser_zuhause%2Fkommt_geht.yaml) |
| **Wake on LAN** | Push nach dem Wake-on-LAN-Knopf: war schon an, ist jetzt online oder nach der Wartezeit noch nicht erreichbar. | [![Blueprint importieren](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FSebastianInTheWild%2Fha-unser-zuhause-blueprints%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Funser_zuhause%2Fwake_on_lan.yaml) |

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
- **Hausmodus, Rollläden:** der Hausmodus der Integration Unser Zuhause (oder ein eigenes `input_select`).
  Der Rollläden-Blueprint braucht Home Assistant 2025.4 oder neuer.
- **Wake on LAN:** ein Wake-on-LAN-Knopf (Integration *Wake on LAN*) und ein Online-Status – Geräte-Tracker
  (z. B. UniFi, FRITZ!Box) oder Binärsensor (z. B. *Ping*).

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
💡 An: LED Streifen
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

### Hausmodus – Einstellungen

| Feld | Standard |
| --- | --- |
| Personen | – (Pflicht) |
| Alle weg seit mindestens | 30 Sekunden |
| Hausmodus / Zustände | `select.unser_zuhause_hausmodus` / `anwesend` / `abwesend` |
| Pause-Schalter / endet nach | leer / 1 Stunde – solange an, bleibt der Hausmodus, wie er ist |
| Personen benachrichtigen | leer – sonst Nachricht, wenn die Pause beginnt oder endet |

Wer in einer anderen Zone ist (z. B. Arbeit), zählt als weg. Beim Start von Home Assistant und am Ende einer
Pause wird der Hausmodus neu berechnet.

### Rollläden – Einstellungen

| Feld | Standard |
| --- | --- |
| Bei Abwesenheit schließen | – (Pflicht; Rollläden, Bereiche oder Etagen) |
| Beim Heimkommen öffnen (tagsüber) | – (Pflicht) |
| Beim Heimkommen öffnen (abends) | leer |
| Tagsüber bis | 20:00 (und zwischen Sonnenaufgang und Sonnenuntergang) |
| Personen benachrichtigen | leer = keine Nachricht |
| Zusätzlich beim Schließen / Öffnen | leer – z. B. einen Status-Helfer setzen |

### Licht nach Zeitplan – Einstellungen

| Feld | Standard |
| --- | --- |
| Lichter | – (Pflicht; auch Bereich oder Label) |
| Einschalten bei Sonnenuntergang / zur Uhrzeit | an / aus (05:00) |
| Nur einschalten, wenn | leer – z. B. Hausmodus ist „anwesend“ |
| Ausschalten zur Uhrzeit / bei Sonnenaufgang | an (23:00) / an |
| Helligkeit / Farbtemperatur | 0 = so lassen |
| Sanft einblenden | 0 s – sonst ab 1 % in dieser Zeit hoch |

Für mehrere Lampen mit unterschiedlichen Zeiten einfach mehrere Automationen aus dem Blueprint anlegen.

### Person kommt/geht – Einstellungen

| Feld | Standard |
| --- | --- |
| Personen / Empfänger | – (Pflicht) |
| Titel | `Anwesenheit` |

### Wake on LAN – Einstellungen

| Feld | Standard |
| --- | --- |
| Wake-on-LAN-Knopf / Online-Status | – (Pflicht) |
| Name des Rechners | leer = Name des Online-Status |
| Warten bis zu | 5 Minuten |
| Personen | – (Pflicht) |

## Dazugehörige Repos

- [ha-unser-zuhause](https://github.com/SebastianInTheWild/ha-unser-zuhause) – Dashboard-Strategy
- [ha-unser-zuhause-cards](https://github.com/SebastianInTheWild/ha-unser-zuhause-cards) – Karten
- [ha-unser-zuhause-integration](https://github.com/SebastianInTheWild/ha-unser-zuhause-integration) – Integration

## Lizenz

MIT · Autor: SebastianInTheWild
