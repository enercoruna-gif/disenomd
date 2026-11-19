"""Exporta todo docs/ a ~/kits-cuadrantia/ sin modificar el sitio original."""

import base64
from html import escape, unescape
import io
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
DOMINIO = "https://ia.cuadrantia.store/"
CORREO = "hola@cuadrantia.store"
EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}', re.I)
ATRIBUTO = re.compile(r'\b(href|src)="([^"]*)"')
GITHUB = re.compile(r'https?://(?:[\w-]+\.)?github\.(?:com|io)[^\s<>"\'()&]*', re.I)
TEXTO = {".html", ".css", ".js", ".json", ".webmanifest", ".svg", ".md", ".txt", ".xml"}


def limpiar_texto(texto):
    texto = texto.replace(ORIGEN.rstrip("/"), DOMINIO.rstrip("/"))
    texto = texto.replace("/disenomd/", "/")
    texto = re.sub(r'\[([^\]]+)\]\(' + GITHUB.pattern + r'\)', r'\1', texto, flags=re.I)
    texto = GITHUB.sub("", texto)
    return EMAIL.sub(CORREO, texto)


def ruta_local(url, pagina):
    url = unescape(url)
    absoluta = urljoin(DOMINIO + pagina, url)
    if urlsplit(absoluta).netloc == urlsplit(DOMINIO).netloc:
        partes = urlsplit(absoluta)
        return partes.path + ("?" + partes.query if partes.query else "") + ("#" + partes.fragment if partes.fragment else "")
    return url


def ruta_pagina(archivo):
    ruta = archivo.as_posix()
    return ruta.removesuffix("index.html") if archivo.name == "index.html" else ruta


def preparar(html, pagina):
    html = re.sub(r'<p class="tenue" id="aviso-cuadrantia">.*?</p>\n?', "", html)
    html = re.sub(r'<a\b([^>]*)>(.*?)</a>',
                  lambda m: "" if re.search(r'\bclass="gh"', m[1]) else (m[2] if GITHUB.search(m[1]) and ORIGEN.rstrip("/") not in m[1] else m[0]), html, flags=re.S)
    html = limpiar_texto(html)
    html = re.sub(r'<link\b[^>]*rel="canonical"[^>]*>\s*|<meta\b[^>]*property="og:url"[^>]*>\s*', "", html)
    html = ATRIBUTO.sub(lambda m: f'{m[1]}="{escape(ruta_local(m[2], pagina), quote=True)}"', html)
    if CORREO not in re.sub(r"<[^>]*>", "", html):
        html = html.replace("</footer>", f'<p class="legal">Contacto: <a href="mailto:{CORREO}">{CORREO}</a></p>\n</footer>')
    canon = DOMINIO + pagina
    return html.replace("</head>", f'<link rel="canonical" href="{canon}">\n<meta property="og:url" content="{canon}">\n</head>')


def limpiar_js(texto):
    texto = re.sub(r'\(function \(\) \{\s*var els = document.querySelectorAll\(\x27\[data-estrellas\].*?\}\)\(\);', "", texto, flags=re.S)
    return limpiar_texto(texto)


def limpiar_zip(datos):
    salida = io.BytesIO()
    with zipfile.ZipFile(io.BytesIO(datos)) as original, zipfile.ZipFile(salida, "w") as nuevo:
        for info in original.infolist():
            contenido = original.read(info)
            if Path(info.filename).suffix in TEXTO:
                contenido = limpiar_texto(contenido.decode("utf-8")).encode("utf-8")
            nuevo.writestr(info, contenido)
    return salida.getvalue()


def data_uri(datos, tipo):
    return f"data:{tipo};base64," + base64.b64encode(datos).decode("ascii")


def descargar(url):
    with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as respuesta:
        return respuesta.read(), respuesta.headers.get_content_type()


def autonomo(sitio):
    recursos, paginas, remotos = {}, {}, {}

    def recurso(url):
        if url in recursos:
            return "@@recurso:" + url + "@@"
        if url.startswith("/"):
            archivo = sitio / url.lstrip("/")
            recursos[url] = data_uri(archivo.read_bytes(), mimetypes.guess_type(archivo)[0] or "application/octet-stream")
        else:
            try:
                datos, tipo = descargar(url)
                if not tipo.startswith("image/"):
                    raise ValueError("La respuesta no es una imagen")
            except (URLError, TimeoutError, OSError, ValueError) as error:
                print(f"Aviso: imagen externa no disponible ({url}): {error}; se usa un marcador offline.")
                datos, tipo = b'<svg xmlns="http://www.w3.org/2000/svg" width="290" height="54"><text x="8" y="32">CazaProducto</text></svg>', "image/svg+xml"
            recursos[url] = data_uri(datos, tipo)
        return "@@recurso:" + url + "@@"

    def fuentes(url):
        if url not in remotos:
            try:
                css = descargar(url)[0].decode("utf-8")
                def fuente(m):
                    datos, tipo = descargar(m[1])
                    return "url(" + data_uri(datos, tipo) + ")"
                remotos[url] = re.sub(r'url\((https://[^)]+)\)', fuente, css)
            except (URLError, TimeoutError, OSError) as error:
                print(f"Aviso: fuentes externas no disponibles: {error}; se usan las fuentes de respaldo.")
                remotos[url] = ""
        clave = "fuentes:" + url
        recursos[clave] = remotos[url]
        return "@@recurso:" + clave + "@@"

    for archivo in sorted(sitio.rglob("*.json")):
        recurso("/" + archivo.relative_to(sitio).as_posix())
    for archivo in sorted(sitio.rglob("*.html")):
        pagina = "/" + ruta_pagina(archivo.relative_to(sitio))
        html = archivo.read_text(encoding="utf-8")
        html = re.sub(r'<link\b[^>]*rel="(?:manifest|preconnect)"[^>]*>', "", html)

        def estilo(m):
            url = unescape(m[1])
            if url.startswith("/"):
                clave = "css:" + url
                recursos[clave] = (sitio / url.lstrip("/")).read_text(encoding="utf-8")
                return "<style>@@recurso:" + clave + "@@</style>"
            return "<style>" + fuentes(url) + "</style>"

        html = re.sub(r'<link rel="stylesheet" href="([^"]*)">', estilo, html)
        def script(m):
            url = unescape(m[1])
            clave = "js:" + url
            recursos[clave] = (sitio / url.lstrip("/")).read_text(encoding="utf-8")
            return "<script>@@recurso:" + clave + "@@</script>"
        html = re.sub(r'<script src="([^"]*)"></script>', script, html)

        def incrustar(m):
            atributo, url = m[1], unescape(m[2])
            if url.startswith("data:"):
                return m[0]
            if atributo == "src" or (url.startswith("/") and Path(url).suffix and Path(url).suffix != ".html"):
                url = recurso(url)
            return f'{atributo}="{escape(url, quote=True)}"'

        paginas[pagina] = ATRIBUTO.sub(incrustar, html)
    datos = json.dumps({"paginas": paginas, "recursos": recursos, "dominio": DOMINIO}, ensure_ascii=False).replace("<", "\\u003c")
    navegador = Path(__file__).with_name("navegador_autonomo.js").read_text(encoding="utf-8")
    return '''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><title>diseño.md — sin conexión</title><style>html,body{margin:0;height:100%;background:#161616}iframe{border:0;width:100%;height:100%;display:block}</style></head><body><iframe id="sitio" title="diseño.md" allow="clipboard-write"></iframe><script id="contenido" type="application/json">''' + datos + "</script><script>" + navegador + "</script></body></html>"


def main():
    if not (DOCS / "index.html").is_file():
        raise SystemExit("Falta docs/index.html. Ejecuta primero python3 src/build.py")
    sitio = DESTINO / "sitio"
    if sitio.exists():
        shutil.rmtree(sitio)
    shutil.copytree(DOCS, sitio, ignore=shutil.ignore_patterns(".git", "README*"))
    for archivo in sorted(sitio.rglob("*")):
        if not archivo.is_file():
            continue
        if archivo.suffix == ".zip":
            archivo.write_bytes(limpiar_zip(archivo.read_bytes()))
        elif archivo.suffix in TEXTO:
            texto = archivo.read_text(encoding="utf-8")
            if archivo.suffix == ".html":
                texto = preparar(texto, ruta_pagina(archivo.relative_to(sitio)))
            elif archivo.suffix == ".js":
                texto = limpiar_js(texto)
            else:
                texto = limpiar_texto(texto)
            archivo.write_text(texto, encoding="utf-8")
    error = (sitio / "index.html").read_text(encoding="utf-8")
    error = re.sub(r"<main>.*?</main>", '<main><section class="det-cab"><p class="eti">Error 404</p><h1>Página no encontrada</h1><p class="intro">Esta página no existe. <a href="/">Volver al inicio →</a></p></section></main>', error, flags=re.S)
    error = re.sub(r"<title>.*?</title>", "<title>Página no encontrada | diseño.md</title>", error)
    error = error.replace("</head>", '<meta name="robots" content="noindex">\n</head>')
    (sitio / "404.html").write_text(preparar(error, "404.html"), encoding="utf-8")
    manifest = json.loads((sitio / "manifest.webmanifest").read_text())
    manifest.update(start_url="/", scope="/")
    for icono in manifest["icons"]:
        icono["src"] = "/" + icono["src"].lstrip("/")
    (sitio / "manifest.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
    (sitio / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMINIO}sitemap.xml\n")
    urls = [DOMINIO + ruta_pagina(p.relative_to(sitio)) for p in sorted(sitio.rglob("*.html")) if p != sitio / "404.html"]
    (sitio / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(f"<url><loc>{url}</loc></url>" for url in urls) + "\n</urlset>\n")
    (DESTINO / "cuadrantia-ia-autonomo.html").write_text(autonomo(sitio), encoding="utf-8")
    with zipfile.ZipFile(DESTINO / "cuadrantia-ia.zip", "w", zipfile.ZIP_DEFLATED) as paquete:
        for archivo in sorted(sitio.rglob("*")):
            if archivo.is_file():
                paquete.write(archivo, archivo.relative_to(sitio))
    print(f"{len(urls)} páginas en sitemap; sitio, ZIP y HTML autónomo generados en {DESTINO}")


if __name__ == "__main__":
    main()
