from html import escape
import re
import unittest
from unittest.mock import patch

import build


class PortadaTest(unittest.TestCase):
    def test_todos_los_kits_antes_de_los_botones(self):
        html = build.portada()
        tarjetas = re.search(r'<div class="kits-hero"[^>]*>(.*?)</div>', html, re.S)
        self.assertIsNotNone(tarjetas)
        self.assertLess(html.index('<p class="intro">'), tarjetas.start())
        self.assertLess(tarjetas.end(), html.index('class="btn btn-grande"'))
        self.assertIn('grid-template-columns:1fr;max-width:none', tarjetas[0])
        self.assertEqual(tarjetas[1].count('class="kit-btn'), len(build.KITS))
        self.assertEqual(tarjetas[1].count('kit-dest'), 1)
        for kit in build.KITS:
            self.assertIn(f'href="kits/#{kit["slug"]}"', tarjetas[1])
            self.assertIn(escape(kit["nombre"]), tarjetas[1])
            self.assertIn(escape(kit["sub"]), tarjetas[1])
            self.assertIn(escape(kit["precio"]), tarjetas[1])
        self.assertIn('Kit Web Inicial · <span style="white-space:nowrap">79 €</span>', tarjetas[1])
        self.assertIn('149 €</span> orientativos', tarjetas[1])

    def test_resto_de_portada_sin_cambios(self):
        html = build.portada()
        for contenido in ('Elige un diseño gratis', 'Cómo funciona', 'class="logos"',
                          'class="antes-despues"', 'class="lista-iconos"', 'id="catalogo"',
                          'Usa DESIGN.md para', 'Kits de inicio', 'Preguntas frecuentes'):
            self.assertIn(contenido, html)

    def test_lista_vacia_y_texto_escapado(self):
        with patch.object(build, 'KITS', []):
            self.assertNotIn('class="kit-btn', build.portada())
        kit = dict(slug='ejemplo', icono='<', nombre='Kit <web>', sub='Texto & fotos', precio='19 €')
        with patch.object(build, 'KITS', [kit]):
            html = build.portada()
        self.assertIn('Kit &lt;web&gt;', html)
        self.assertIn('Texto &amp; fotos', html)


if __name__ == '__main__':
    unittest.main()
