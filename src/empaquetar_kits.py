"""Ejecutar después de build.py: exporta los kits a ~/kits-cuadrantia/."""

import base64
import json
import mimetypes
from pathlib import Path
import re
import shutil
from urllib.error import URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen
import zipfile


DOCS = Path(__file__).resolve().parents[1] / "docs"
DESTINO = Path.home() / "kits-cuadrantia"
ORIGEN = "https://enercoruna-gif.github.io/disenomd/"
DOMINIO = "https://kits.cuadrantia.store/"
ATRIBUTO = re.compile(r'\b(href|src)="([^"]*)"')
CORREO = "hola@cuadrantia.store"
EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}', re.I)


def ruta_raiz(url, pagina):
    if not url or url.startswith(("#", "mailto:", "data:", "https:", "http:", "//")):
        return url
    absoluta = urljoin(ORIGEN + pagina + "/", url)
    relativa = absoluta.removeprefix(ORIGEN)
    prefijo = "/" if pagina == "aviso-legal" else ""
    if relativa.startswith("kits/#"):
        return ("/" if prefijo else "") + relativa[5:]
    if relativa == "kits/":
        return "/"
    if relativa.startswith("aviso-legal/"):
        return prefijo + relativa
    if relativa.startswith("assets/") or relativa == "manifest.webmanifest":
        return prefijo + relativa
    return absoluta


def preparar(html, pagina, canon):
    html = re.sub(r'<p class="tenue" id="aviso-cuadrantia">.*?</p>\n?', "", html)
    html = ATRIBUTO.sub(lambda m: f'{m[1]}="{ruta_raiz(m[2], pagina)}"', html)
    html = EMAIL.sub(CORREO, html)
    if CORREO not in re.sub(r"<[^>]*>", "", html):
        html = html.replace("</footer>", f'<p class="legal">Contacto: <a href="mailto:{CORREO}">{CORREO}</a></p>\n</footer>')
    return html.replace("</head>", f'<link rel="canonical" href="{canon}">\n<meta property="og:url" content="{canon}">\n</head>')


def data_uri(datos, tipo):
    return f"data:{tipo};base64," + base64.b64encode(datos).decode("ascii")


def enlaces_404(html):
    return ATRIBUTO.sub(lambda m: f'{m[1]}="{urljoin("/", m[2])}"', html)


def autonomo(html, sitio):
    html = html.replace('<link rel="stylesheet" href="assets/estilo.css">',
                        "<style>" + (sitio / "assets/estilo.css").read_text() + "</style>")
    html = html.replace('<script src="assets/app.js"></script>',
                        "<script>" + (sitio / "assets/app.js").read_text() + "</script>")
    manifest = json.loads((sitio / "manifest.webmanifest").read_text())
    manifest.update(start_url=DOMINIO, scope=DOMINIO)
    for icono in manifest["icons"]:
        archivo = sitio / icono["src"].lstrip("/")
        icono["src"] = data_uri(archivo.read_bytes(), icono["type"])
    html = html.replace('href="manifest.webmanifest"',
                        'href="' + data_uri(json.dumps(manifest).encode(), "application/manifest+json") + '"')

    def incrustar(m):
        atributo, url = m[1], m[2]
        if url.startswith("assets/"):
            archivo = sitio / url
            url = data_uri(archivo.read_bytes(), mimetypes.guess_type(archivo)[0] or "application/octet-stream")
        elif url.startswith("aviso-legal/") or url == "/":
            url = urljoin(DOMINIO, url)
        elif atributo == "src" and urlsplit(url).hostname == "cazaproducto.com":
            try:
                with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=20) as respuesta:
                    tipo = respuesta.headers.get_content_type()
                    if tipo.startswith("image/"):
                        url = data_uri(respuesta.read(), tipo)
                    else:
                        print("Aviso: el badge no devolvió una imagen; se conserva su URL.")
            except (URLError, TimeoutError, OSError) as error:
                print(f"Aviso: no se pudo descargar el badge ({error}); se conserva su URL.")
        return f'{atributo}="{url}"'

    return ATRIBUTO.sub(incrustar, html)


def main():
    for ruta in ("kits/index.html", "aviso-legal/index.html", "manifest.webmanifest"):
        if not (DOCS / ruta).is_file():
            raise SystemExit(f"Falta docs/{ruta}. Ejecuta primero python3 src/build.py")
    sitio = DESTINO / "sitio"
    if sitio.exists():
        shutil.rmtree(sitio)
    (sitio / "assets").mkdir(parents=True)
    (sitio / "aviso-legal").mkdir()
    indice = preparar((DOCS / "kits/index.html").read_text(), "kits", DOMINIO)
    legal = preparar((DOCS / "aviso-legal/index.html").read_text(), "aviso-legal", DOMINIO + "aviso-legal/")
    error = re.sub(r"<main>.*?</main>", '<main><section class="det-cab"><p class="eti">Error 404</p><h1>Página no encontrada</h1><p class="intro">Esta página no existe. <a href="/">Volver al inicio →</a></p></section></main>', indice, flags=re.S)
    error = error.replace("Kits de inicio para crear webs y apps con IA | diseño.md", "Página no encontrada | diseño.md")
    error = error.replace(f'<link rel="canonical" href="{DOMINIO}">', "")
    error = re.sub(r'<meta property="og:url"[^>]*>', "", error)
    error = enlaces_404(error)
    for nombre, contenido in (("index.html", indice), ("aviso-legal/index.html", legal), ("404.html", error)):
        (sitio / nombre).write_text(contenido, encoding="utf-8")
    manifest = json.loads((DOCS / "manifest.webmanifest").read_text())
    manifest.update(start_url="/", scope="/")
    for icono in manifest["icons"]:
        icono["src"] = "/" + icono["src"].lstrip("/")
    (sitio / "manifest.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
    recursos = {"estilo.css", "app.js", "favicon.svg", "icono-180.png"}
    recursos.update(Path(icono["src"]).name for icono in manifest["icons"])
    for nombre in sorted(recursos):
        shutil.copyfile(DOCS / "assets" / nombre, sitio / "assets" / nombre)
    (sitio / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMINIO}sitemap.xml\n")
    urls = (DOMINIO, DOMINIO + "aviso-legal/")
    (sitio / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{url}</loc></url>" for url in urls) + "</urlset>\n")
    for archivo in sitio.rglob("*"):
        if archivo.is_file() and archivo.suffix not in (".png",):
            contenido = EMAIL.sub(CORREO, archivo.read_text(encoding="utf-8"))
            archivo.write_text(contenido, encoding="utf-8")
            if "../" in contenido:
                raise ValueError(f"Ruta sin resolver: {archivo}")
    (DESTINO / "cuadrantia-kits-autonomo.html").write_text(autonomo(indice, sitio), encoding="utf-8")
    with zipfile.ZipFile(DESTINO / "cuadrantia-kits.zip", "w", zipfile.ZIP_DEFLATED) as paquete:
        for archivo in sorted(sitio.rglob("*")):
            if archivo.is_file():
                paquete.write(archivo, archivo.relative_to(sitio))
    print(f"Sitio, ZIP y HTML autónomo generados en {DESTINO}")


if __name__ == "__main__":
    main()
