import hashlib
from html import unescape
import json
from pathlib import Path
import re
import tempfile
import unittest
import zipfile

from PIL import Image

import analisis_web as analisis
import build
import demos
import empaquetar_sitio as sitio


class DemosTest(unittest.TestCase):
    def test_entradas_y_design_sin_reinterpretar(self):
        originales = [s for s in analisis.SITIOS if s.get('original')]
        self.assertEqual({s['slug'] for s in originales}, {'crix', 'launchkit', 'cauce'})
        self.assertEqual(len(analisis.SITIOS), 71)
        self.assertEqual(sum(not s.get('original', False) for s in analisis.SITIOS), 68)
        for s in originales:
            slug = s['slug']
            datos = json.loads((analisis.RAIZ / 'src/analisis' / (slug + '.json')).read_text())
            md, colores = analisis.design_md(s, datos)
            fuente = demos.FUENTES / slug / 'DESIGN.md'
            self.assertEqual(md.encode(), fuente.read_bytes())
            self.assertTrue(all(valor in md for valor in colores.values()))
            carpeta = build.SALIDA / 'analisis' / slug
            self.assertEqual((carpeta / 'DESIGN.md').read_bytes(), fuente.read_bytes())
            html = (carpeta / 'index.html').read_text()
            self.assertIn('data-copiar-de="md"', html)
            self.assertIn('data-copiar-de="prompt"', html)
            self.assertIn(f'href="../../demos/{slug}/">Ver demo', html)
            self.assertNotIn('Análisis de web real', html)
            self.assertIn('Diseño de muestra de diseño.md', html)
            self.assertIn(md, unescape(re.search(r'<pre class="codigo" id="md"[^>]*>(.*?)</pre>', html, re.S)[1]))
            for nombre, dimensiones in (('captura.webp', (960, 600)), ('icono.png', (64, 64)), ('og.jpg', (1200, 630))):
                with Image.open(carpeta / nombre) as im:
                    self.assertEqual(im.size, dimensiones)
            with zipfile.ZipFile(build.SALIDA / 'descargas/disenomd-webs.zip') as z:
                self.assertEqual(len(z.namelist()), 71)
                self.assertEqual(z.read(slug + '/DESIGN.md'), fuente.read_bytes())
        self.assertIn('inspirada en Payer', (build.SALIDA / 'analisis/cauce/index.html').read_text())
        self.assertEqual(hashlib.sha256((demos.FUENTES / 'crix/DESIGN.md').read_bytes()).hexdigest(),
                         '820fd6892a686cc26ace60de05da92505cc783e16998cb8060d9e688716412fb')

    def test_catalogo_y_demos(self):
        html = (build.SALIDA / 'webs/index.html').read_text()
        self.assertIn('71 diseños gratuitos', html)
        self.assertIn('68 análisis independientes', html)
        self.assertIn('3 demos propias', html)
        for slug in ('crix', 'launchkit', 'cauce'):
            self.assertIn(f'href="../analisis/{slug}/" data-cat="Diseños propios"', html)
            demo = build.SALIDA / 'demos' / slug
            self.assertTrue((demo / 'index.html').is_file())
            self.assertEqual((demo / 'DESIGN.md').read_bytes(), (demos.FUENTES / slug / 'DESIGN.md').read_bytes())
            self.assertIn(build.ORIGEN + f'analisis/{slug}/og.jpg', (demo / 'index.html').read_text())
        for licencia in ('LICENSE.txt', 'Manrope-OFL.txt'):
            self.assertEqual((build.SALIDA / 'demos/cauce' / licencia).read_bytes(), (demos.FUENTES / 'cauce' / licencia).read_bytes())

    def test_publicar_vacio(self):
        with tempfile.TemporaryDirectory() as temporal:
            demos.publicar(Path(temporal), [])
            self.assertEqual(list(Path(temporal).iterdir()), [])

    def test_recurso_ausente(self):
        with tempfile.TemporaryDirectory() as temporal:
            with self.assertRaises(FileNotFoundError):
                demos.publicar(Path(temporal), [dict(slug='no-existe', original=True)])

    def test_svg_con_referencias_locales(self):
        html = '<svg><use href="#mark"/></svg><a href="#contenido">Contenido</a>'
        preparado = sitio.preparar(html, 'demos/cauce/')
        self.assertIn('<use href="#mark"/>', preparado)
        self.assertIn('href="/demos/cauce/#contenido"', preparado)


if __name__ == '__main__':
    unittest.main()
