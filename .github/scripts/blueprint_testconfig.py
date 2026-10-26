"""Baut eine Test-Konfiguration für Home Assistant: aus jedem Blueprint eine Automation.

Pflicht-Eingaben (ohne `default`) bekommen Platzhalter passend zum Selector, z. B. `cover.ci_test`.
Danach prüft `check_config` von Home Assistant, ob sich alle Automationen laden lassen.

Aufruf: python blueprint_testconfig.py <blueprints-ordner> <config-ordner>
"""

import pathlib
import shutil
import sys

import yaml


class Loader(yaml.SafeLoader):
    pass


Loader.add_constructor("!input", lambda loader, node: loader.construct_scalar(node))


def domains(selector_config):
    """Erste Domain aus `filter` bzw. aus der Entity-Liste eines target-Selectors."""
    filters = selector_config.get("filter") or selector_config.get("entity") or []
    if isinstance(filters, dict):
        filters = [filters]
    for f in filters:
        domain = f.get("domain")
        if domain:
            return domain if isinstance(domain, list) else [domain]
    return ["sensor"]


def placeholder(selector):
    kind, config = next(iter(selector.items()))
    config = config or {}
    if kind == "entity":
        entity = f"{domains(config)[0]}.ci_test"
        return [entity] if config.get("multiple") else entity
    if kind == "target":
        return {"entity_id": [f"{domains(config)[0]}.ci_test"]}
    if kind == "number":
        return config.get("min", 0)
    if kind == "boolean":
        return True
    if kind == "time":
        return "12:00:00"
    if kind == "duration":
        return {"seconds": 1}
    if kind in ("action", "condition"):
        return []
    return "ci"


def inputs(blueprint_inputs):
    """Eingaben flach, auch aus Abschnitten (sections)."""
    for key, value in blueprint_inputs.items():
        if "input" in (value or {}):
            yield from inputs(value["input"])
        else:
            yield key, value or {}


def main(source, config):
    source, config = pathlib.Path(source), pathlib.Path(config)
    shutil.rmtree(config, ignore_errors=True)
    automations = []
    for path in sorted(source.rglob("*.yaml")):
        data = yaml.load(path.read_text(encoding="utf-8"), Loader=Loader)
        bp = data["blueprint"]
        if bp.get("domain") != "automation":
            continue
        relative = path.relative_to(source / "automation")
        target = config / "blueprints" / "automation" / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(path, target)
        values = {
            key: placeholder(value.get("selector", {"text": {}}))
            for key, value in inputs(bp.get("input", {}))
            if "default" not in value
        }
        automations.append({
            "id": f"ci_{relative.stem}",
            "alias": f"CI {relative}",
            "use_blueprint": {"path": relative.as_posix(), "input": values},
        })
        print(f"{relative}: {len(values)} Pflicht-Eingaben mit Platzhaltern")
    (config / "automations.yaml").write_text(yaml.safe_dump(automations, allow_unicode=True), encoding="utf-8")
    (config / "configuration.yaml").write_text("automation: !include automations.yaml\n", encoding="utf-8")


if __name__ == "__main__":
    main(*sys.argv[1:3])
