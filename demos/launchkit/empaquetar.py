"""Sincroniza DESIGN.md y crea el ZIP autónomo, sin red ni dependencias."""

import argparse
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parent
FILES = ("index.html", "DESIGN.md", "og.png", "README.md")
DESIGN_BLOCK = re.compile(r'(<script id="design-source" type="text/plain">).*?(</script>)', re.S)


def package(destination):
    design = (ROOT / "DESIGN.md").read_text(encoding="utf-8")
    if "</script" in design.lower():
        raise ValueError("DESIGN.md no puede contener un cierre de script HTML.")
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    html, count = DESIGN_BLOCK.subn(lambda match: match[1] + "\n" + design + match[2], html)
    if count != 1:
        raise ValueError("El HTML debe contener un único bloque design-source.")
    if "@@BACKGROUND@@" in html or "@@DESIGN@@" in html:
        raise ValueError("Quedan recursos pendientes de integrar.")
    for name in FILES:
        if not (ROOT / name).is_file():
            raise FileNotFoundError(ROOT / name)
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    destination = Path(destination).expanduser().resolve()
    if destination in [ROOT / name for name in FILES]:
        raise ValueError("El ZIP no puede sobrescribir un archivo de la demo.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(destination, "w", compression=ZIP_DEFLATED) as archive:
        for name in FILES:
            archive.write(ROOT / name, arcname=name)
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path.home() / "kits-cuadrantia/LaunchKit-gratis.zip")
    args = parser.parse_args()
    print(package(args.output))
