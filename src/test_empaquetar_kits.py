import json
from pathlib import Path
import tempfile
import unittest
import zipfile
from unittest.mock import patch
from urllib.error import URLError
from urllib.parse import urljoin

import empaquetar_kits as kits


class EmpaquetarKitsTest(unittest.TestCase):
    def test_rutas(self):
        casos = {
            "../assets/estilo.css": "assets/estilo.css",
            "../kits/#web": "#web",
            "../kits/": "/",
            "../": kits.ORIGEN,
            "../#catalogo": kits.ORIGEN + "#catalogo",
            "../webs/": kits.ORIGEN + "webs/",
            "../como-usar/": kits.ORIGEN + "como-usar/",
            "../descargas/disenomd-webs.zip": kits.ORIGEN + "descargas/disenomd-webs.zip",
            "../aviso-legal/": "aviso-legal/",
            "https://payhip.com/b/abc": "https://payhip.com/b/abc",
            "": "",
        }
        for original, esperado in casos.items():
            with self.subTest(original=original):
                self.assertEqual(kits.ruta_raiz(original, "kits"), esperado)
        self.assertEqual(kits.ruta_raiz("../assets/app.js", "aviso-legal"), "/assets/app.js")
        self.assertEqual(kits.ruta_raiz("../kits/#web", "aviso-legal"), "/#web")

    def test_preparar(self):
        html = '<head></head><p class="tenue" id="aviso-cuadrantia">Aviso</p>\n<a href="../kits/">Kits</a>'
        resultado = kits.preparar(html, "kits", kits.DOMINIO)
        self.assertNotIn("aviso-cuadrantia", resultado)
        self.assertIn(f'rel="canonical" href="{kits.DOMINIO}"', resultado)
        self.assertIn('property="og:url"', resultado)
        self.assertIn('href="/"', resultado)
        self.assertEqual(kits.preparar("", "kits", kits.DOMINIO), "")

    def test_autonomo_badge_y_error(self):
        with tempfile.TemporaryDirectory() as carpeta:
            sitio = Path(carpeta)
            (sitio / "assets").mkdir()
            (sitio / "assets/estilo.css").write_text("body{}")
            (sitio / "assets/app.js").write_text("void 0;")
            (sitio / "manifest.webmanifest").write_text(json.dumps({"icons": []}))
            html = '<link rel="stylesheet" href="assets/estilo.css"><script src="assets/app.js"></script><img src="https://cazaproducto.com/badge">'
            with patch.object(kits, "urlopen", side_effect=URLError("sin conexión")):
                resultado = kits.autonomo(html, sitio)
            self.assertIn("<style>body{}</style>", resultado)
            self.assertIn("<script>void 0;</script>", resultado)
            self.assertIn('src="https://cazaproducto.com/badge"', resultado)
            with patch.object(kits, "urlopen") as descargar:
                respuesta = descargar.return_value.__enter__.return_value
                respuesta.headers.get_content_type.return_value = "image/svg+xml"
                respuesta.read.return_value = b"<svg/>"
                self.assertIn("data:image/svg+xml;base64,", kits.autonomo(html, sitio))
            self.assertEqual(kits.autonomo("", sitio), "")

    def test_enlaces_404_desde_cualquier_profundidad(self):
        casos = {
            "#web": "/#web",
            "#app": "/#app",
            "assets/estilo.css": "/assets/estilo.css",
            "assets/app.js": "/assets/app.js",
            "manifest.webmanifest": "/manifest.webmanifest",
            "aviso-legal/": "/aviso-legal/",
            "./otra/": "/otra/",
            "/": "/",
            "": "/",
            kits.ORIGEN + "#catalogo": kits.ORIGEN + "#catalogo",
            "mailto:info@example.com": "mailto:info@example.com",
            "data:image/png;base64,AA==": "data:image/png;base64,AA==",
        }
        for original, esperado in casos.items():
            for atributo in ("href", "src"):
                with self.subTest(original=original, atributo=atributo):
                    html = f'<a {atributo}="{original}">'
                    self.assertEqual(kits.enlaces_404(html), f'<a {atributo}="{esperado}">')
                    for ruta in ("404.html", "no/existe/", "a/b/c.html"):
                        self.assertEqual(urljoin(kits.DOMINIO + ruta, esperado), urljoin(kits.DOMINIO, esperado))
        self.assertEqual(kits.enlaces_404(""), "")

    def test_falta_build(self):
        with tempfile.TemporaryDirectory() as carpeta, patch.object(kits, "DOCS", Path(carpeta)):
            with self.assertRaisesRegex(SystemExit, "Ejecuta primero"):
                kits.main()

    def test_correo_solo_en_paquete(self):
        parametros = "?subject=Quiero%20un%20kit&body=Hola%2C%20quiero%20informacion"
        for contenido in ("", "<p>Contacto: otro@example.com</p>"):
            html = f'<a href="mailto:enercoruna@gmail.com{parametros}">Correo</a>{contenido}<footer></footer>'
            resultado = kits.preparar(html, "kits", kits.DOMINIO)
            self.assertIn(f'href="mailto:{kits.CORREO}{parametros}"', resultado)
            self.assertIn(kits.CORREO, kits.re.sub(r"<[^>]*>", "", resultado))
            self.assertEqual(set(kits.EMAIL.findall(resultado)), {kits.CORREO})
        originales = {p: p.read_bytes() for p in kits.DOCS.rglob("*") if p.is_file()}
        with tempfile.TemporaryDirectory() as carpeta, patch.object(kits, "DESTINO", Path(carpeta)), patch.object(kits, "urlopen", side_effect=URLError("sin conexión")):
            kits.main()
            destino = Path(carpeta)
            for nombre in ("index.html", "aviso-legal/index.html", "404.html"):
                html = (destino / "sitio" / nombre).read_text()
                self.assertEqual(set(kits.EMAIL.findall(html)), {kits.CORREO})
                self.assertIn(kits.CORREO, kits.re.sub(r"<[^>]*>", "", html))
            html = (destino / "cuadrantia-ia-autonomo.html").read_text()
            self.assertEqual(set(kits.EMAIL.findall(html)), {kits.CORREO})
            with zipfile.ZipFile(destino / "cuadrantia-ia.zip") as paquete:
                for nombre in paquete.namelist():
                    if not nombre.endswith(".png"):
                        self.assertLessEqual(set(kits.EMAIL.findall(paquete.read(nombre).decode())), {kits.CORREO})
        self.assertTrue(all(p.read_bytes() == datos for p, datos in originales.items()))


if __name__ == "__main__":
    unittest.main()
