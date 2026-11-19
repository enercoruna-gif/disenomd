"""Package the static demo and create its self-contained iPhone companion."""

import argparse
import base64
import mimetypes
import shutil
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent


def data_uri(path):
    portable_types = {".webp": "image/webp", ".md": "text/markdown"}
    mime = portable_types.get(path.suffix.lower()) or mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def build(output):
    output = Path(output).resolve()
    if output == ROOT:
        raise ValueError("La salida debe estar fuera de la carpeta fuente de la demo.")
    output.mkdir(parents=True, exist_ok=True)
    html = (ROOT / "index.html").read_text()
    css = (ROOT / "styles.css").read_text()
    js = (ROOT / "app.js").read_text()
    for asset in (ROOT / "assets").iterdir():
        if asset.is_file():
            uri = data_uri(asset)
            css = css.replace(f"assets/{asset.name}", uri)
            html = html.replace(f"assets/{asset.name}", uri)
    html = html.replace('<link rel="stylesheet" href="styles.css">', f"<style>\n{css}\n</style>")
    html = html.replace('<script src="app.js"></script>', f"<script>\n{js}\n</script>")
    html = html.replace('href="DESIGN.md"', f'href="{data_uri(ROOT / "DESIGN.md")}"')
    (output / "Crix-autonomo.html").write_text(html)
    shutil.copy2(ROOT / "DESIGN.md", output / "DESIGN.md")
    with ZipFile(output / "Crix-completo.zip", "w", ZIP_DEFLATED) as archive:
        for name in ("index.html", "styles.css", "app.js", "DESIGN.md", "README.md"):
            archive.write(ROOT / name, name)
        for asset in sorted((ROOT / "assets").iterdir()):
            if asset.is_file():
                archive.write(asset, f"assets/{asset.name}")
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    print(build(args.output))
