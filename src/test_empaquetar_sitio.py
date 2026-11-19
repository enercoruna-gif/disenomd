from html import unescape
import json
from pathlib import Path
from PIL import Image
import re
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import URLError
import xml.etree.ElementTree as ET
import zipfile

import empaquetar_sitio as sitio


class EmpaquetarSitioTest(unittest.TestCase):
    def test_preparar(self):
        parametros = "?subject=Quiero%20un%20kit&body=Hola%2C%20quiero%20informacion"
        html = ('<head></head><a class="gh" href="https://github.com/org/repo">Estrellas</a>'
                '<a href="https://github.com/org/repo">Formato abierto</a>'
                '<a href="' + sitio.ORIGEN + 'kits/#web">Kits</a>'
                '<a href="/disenomd/webs/">Webs</a>'
                f'<a href="mailto:enercoruna@gmail.com{parametros}">Correo</a>'
                '<a href="https://payhip.com/b/abc">Comprar</a>'
                '<p class="tenue" id="aviso-cuadrantia">Aviso</p><footer></footer>')
        resultado = sitio.preparar(html, "analisis/ejemplo/")
        self.assertNotIn("github.com", resultado)
        self.assertNotIn("Estrellas", resultado)
        self.assertNotIn("aviso-cuadrantia", resultado)
        self.assertIn("Formato abierto", resultado)
        self.assertIn('href="/kits/#web"', resultado)
        self.assertIn('href="/webs/"', resultado)
        self.assertIn(f'href="mailto:{sitio.CORREO}{parametros}"', unescape(resultado))
        self.assertIn('href="https://payhip.com/b/abc"', resultado)
        self.assertIn(sitio.CORREO, re.sub(r"<[^>]*>", "", resultado))
        self.assertIn(f'rel="canonical" href="{sitio.DOMINIO}analisis/ejemplo/"', resultado)
        self.assertIn(f'property="og:url" content="{sitio.DOMINIO}analisis/ejemplo/"', resultado)
        self.assertEqual(sitio.preparar("", ""), "")

    def test_imagenes_sociales_absolutas(self):
        for url in (sitio.ORIGEN + 'assets/og.png', '/assets/og.png', 'assets/og.png'):
            html = '<head><meta property="og:image" content="' + url + '"><meta name="twitter:image" content="' + url + '"></head>'
            resultado = sitio.preparar(html, '')
            self.assertEqual(resultado.count('content="' + sitio.DOMINIO + 'assets/og.png"'), 2)
            self.assertNotRegex(resultado, r'github\.(io|com)|/disenomd/')

    def test_rutas_y_js(self):
        for url, pagina, esperado in (("../../assets/app.js", "analisis/apple/", "/assets/app.js"),
                                     ("#web", "kits/", "/kits/#web"),
                                     ("", "", "/"),
                                     ("../#catalogo", "webs/", "/#catalogo")):
            self.assertEqual(sitio.ruta_local(url, pagina), esperado)
        js = (sitio.DOCS / "assets/app.js").read_text()
        limpio = sitio.limpiar_js(js)
        self.assertNotIn("fetch(", limpio)
        self.assertNotIn("data-estrellas", limpio)
        self.assertIn("data-copiar", limpio)
        self.assertIn("function filtrar()", limpio)
        self.assertEqual(sitio.limpiar_js(""), "")
        self.assertEqual(sitio.limpiar_texto("[GitHub](https://github.com)"), "GitHub")

    def test_falta_build(self):
        with tempfile.TemporaryDirectory() as carpeta, patch.object(sitio, "DOCS", Path(carpeta)):
            with self.assertRaisesRegex(SystemExit, "Ejecuta primero"):
                sitio.main()

    def test_exportacion_completa_y_offline(self):
        originales = {p: p.read_bytes() for p in sitio.DOCS.rglob("*") if p.is_file()}
        def descargar(url):
            if "googleapis" in url:
                return b"@font-face{src:url(https://fonts.example/fuente.woff2)}", "text/css"
            if "fuente.woff2" in url:
                return b"fuente", "font/woff2"
            return b'<svg xmlns="http://www.w3.org/2000/svg"/>', "image/svg+xml"
        with tempfile.TemporaryDirectory() as carpeta, patch.object(sitio, "DESTINO", Path(carpeta)), patch.object(sitio, "descargar", side_effect=descargar):
            sitio.main()
            destino = Path(carpeta)
            copia = destino / "sitio"
            for origen, datos in originales.items():
                relativo = origen.relative_to(sitio.DOCS)
                if not origen.name.startswith("README") and ".git" not in relativo.parts:
                    self.assertTrue((copia / relativo).is_file(), relativo)
                    if origen.suffix in (".png", ".webp"):
                        self.assertEqual((copia / relativo).read_bytes(), datos)
            urls = {e.text for e in ET.parse(copia / "sitemap.xml").iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
            self.assertNotIn(sitio.DOMINIO + "404.html", urls)
            self.assertEqual(len(urls), len(list(copia.rglob("*.html"))) - 1)
            self.assertIn('<meta name="robots" content="noindex">', (copia / "404.html").read_text())
            for html in copia.rglob("*.html"):
                texto = html.read_text()
                canon = sitio.DOMINIO + sitio.ruta_pagina(html.relative_to(copia))
                if html != copia / "404.html":
                    self.assertIn(canon, urls)
                self.assertEqual(texto.count('rel="canonical"'), 1)
                self.assertIn(f'href="{canon}"', texto)
                self.assertEqual(set(sitio.EMAIL.findall(texto)), {sitio.CORREO})
                self.assertNotRegex(texto, r'github\.(io|com)|/disenomd/')
                meta = dict(re.findall(r'<meta (?:property|name)="([^"]*)" content="([^"]*)"', texto))
                self.assertEqual(meta['twitter:card'], 'summary_large_image')
                self.assertEqual(meta['og:image:width'], '1200')
                self.assertEqual(meta['og:image:height'], '630')
                self.assertEqual(meta['twitter:image'], meta['og:image'])
                for clave in ('og:title', 'og:description', 'og:type', 'og:site_name', 'og:image:alt', 'twitter:title', 'twitter:description'):
                    self.assertTrue(meta[clave], (html, clave))
                self.assertTrue(meta['og:image'].startswith(sitio.DOMINIO))
                imagen = copia / meta['og:image'].removeprefix(sitio.DOMINIO)
                self.assertIn(imagen.suffix, ('.jpg', '.png'))
                self.assertLess(imagen.stat().st_size, 1_000_000)
                with Image.open(imagen) as recurso:
                    self.assertEqual(recurso.size, (1200, 630))
                    self.assertIn(recurso.format, ('PNG', 'JPEG'))
            for _, url in sitio.ATRIBUTO.findall((copia / "404.html").read_text()):
                self.assertTrue(url.startswith(("/", "https:", "mailto:")), url)
            self.assertIn("Empieza con el 80", (copia / "kits/index.html").read_text())
            self.assertNotIn("Empieza con el 80", (copia / "index.html").read_text())
            html = (destino / "cuadrantia-ia-autonomo.html").read_text()
            self.assertIn('<meta name="twitter:card" content="summary_large_image">', html.split('</head>')[0])
            self.assertIn('<meta property="og:image" content="' + sitio.DOMINIO + 'assets/og.png">', html.split('</head>')[0])
            datos = json.loads(re.search(r'<script id="contenido" type="application/json">(.*?)</script>', html, re.S)[1])
            self.assertEqual(len(datos["paginas"]), len(list(copia.rglob("*.html"))))
            self.assertIn("/", datos["paginas"])
            self.assertIn("/webs/", datos["paginas"])
            self.assertIn("/analisis/apple/", datos["paginas"])
            self.assertIn("/descargas/disenomd-webs.zip", datos["recursos"])
            self.assertIn("function copiar", datos["recursos"]["js:/assets/app.js"])
            self.assertIn("data:font/woff2;base64,", "".join(datos["recursos"].values()))
            for pagina in datos["paginas"].values():
                for recurso in re.findall(r'@@recurso:(.*?)@@', pagina):
                    self.assertIn(recurso, datos["recursos"])
            self.assertLess(len(html.encode()), 15_000_000)
            self.assertNotRegex(html, r'github\.(io|com)|/disenomd/')
            with zipfile.ZipFile(destino / "cuadrantia-ia.zip") as paquete:
                self.assertIn("index.html", paquete.namelist())
                self.assertIn("analisis/apple/index.html", paquete.namelist())
                for nombre in paquete.namelist():
                    if Path(nombre).suffix in sitio.TEXTO:
                        self.assertNotRegex(paquete.read(nombre).decode(), r'github\.(io|com)|/disenomd/')
            with zipfile.ZipFile(copia / "descargas/disenomd-webs.zip") as descarga:
                self.assertNotIn(b"github.com", b"".join(descarga.read(n) for n in descarga.namelist()))
            with patch.object(sitio, "descargar", side_effect=URLError("sin conexión")):
                self.assertIn("data:image/svg+xml;base64,", sitio.autonomo(copia))
        self.assertTrue(all(p.read_bytes() == datos for p, datos in originales.items()))


if __name__ == "__main__":
    unittest.main()
