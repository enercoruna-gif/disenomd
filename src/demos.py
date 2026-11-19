"""Publica las demos locales conservando sus archivos y licencias."""

from html import escape, unescape
from pathlib import Path
import re
import shutil


ORIGEN = "https://enercoruna-gif.github.io/disenomd/"
FUENTES = Path(__file__).resolve().parent / "demos"


def preparar(html, slug):
    titulo = unescape(re.search(r"<title>(.*?)</title>", html, re.S)[1])
    desc = unescape(re.search(r'<meta name="description" content="([^"]*)"', html)[1])
    html = re.sub(r'<meta\b[^>]*(?:property="og:[^"]*"|name="twitter:[^"]*")[^>]*>\s*', '', html)
    imagen = ORIGEN + f"analisis/{slug}/og.jpg"
    meta = {
        "og:title": titulo, "og:description": desc, "og:type": "website", "og:site_name": "diseño.md",
        "og:image": imagen, "og:image:width": "1200", "og:image:height": "630",
        "og:image:alt": f"{slug.title()} — demo en español de diseño.md",
        "twitter:card": "summary_large_image", "twitter:title": titulo,
        "twitter:description": desc, "twitter:image": imagen,
    }
    etiquetas = '\n'.join(f'<meta {"property" if k.startswith("og:") else "name"}="{k}" content="{escape(v, quote=True)}">' for k, v in meta.items())
    return html.replace('</head>', etiquetas + '\n</head>')


def publicar(salida, sitios):
    originales = [s for s in sitios if s.get("original")]
    if not originales:
        return
    for s in originales:
        slug = s["slug"]
        destino = salida / "demos" / slug
        shutil.copytree(FUENTES / slug, destino)
        (destino / "index.html").write_text(preparar((destino / "index.html").read_text(), slug))
        carpeta = salida / "analisis" / slug
        carpeta.mkdir(parents=True, exist_ok=True)
        for nombre in ("captura.webp", "icono.png"):
            shutil.copyfile(FUENTES.parent / "analisis" / slug / nombre, carpeta / nombre)
