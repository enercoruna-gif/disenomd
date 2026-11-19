from pathlib import Path
import tempfile
import unittest

from PIL import Image

import build
import imagenes_og


class ImagenesOgTest(unittest.TestCase):
    def test_generar_y_captura_ausente(self):
        with tempfile.TemporaryDirectory() as temporal:
            salida = Path(temporal)
            (salida / "assets").mkdir()
            carpeta = salida / "analisis/ejemplo"
            carpeta.mkdir(parents=True)
            Image.new("RGB", (960, 600), "white").save(carpeta / "captura.webp")
            imagenes_og.generar(salida, [dict(slug="ejemplo", nombre="Ejemplo"), dict(slug="ausente", nombre="Ausente")])
            for ruta in (salida / "assets/og.png", carpeta / "og.jpg"):
                with Image.open(ruta) as imagen:
                    self.assertEqual(imagen.size, (1200, 630))
                    self.assertIn(imagen.format, ("PNG", "JPEG"))
                self.assertLess(ruta.stat().st_size, 1_000_000)
            self.assertFalse((salida / "analisis/ausente/og.jpg").exists())

    def test_lista_vacia(self):
        with tempfile.TemporaryDirectory() as temporal:
            salida = Path(temporal)
            (salida / "assets").mkdir()
            imagenes_og.generar(salida, [])
            self.assertTrue((salida / "assets/og.png").is_file())

    def test_captura_corrupta(self):
        with tempfile.TemporaryDirectory() as temporal:
            salida = Path(temporal)
            (salida / "assets").mkdir()
            carpeta = salida / "analisis/ejemplo"
            carpeta.mkdir(parents=True)
            (carpeta / "captura.webp").write_bytes(b"imagen no valida")
            with self.assertRaises(OSError):
                imagenes_og.generar(salida, [dict(slug="ejemplo", nombre="Ejemplo")])

    def test_metadatos_y_escape(self):
        html = build.pagina('Web <ejemplo>', 'Texto & fotos', '', imagen='analisis/ejemplo/og.jpg', imagen_alt='Ejemplo "visual"')
        self.assertIn('property="og:image" content="' + build.ORIGEN + 'analisis/ejemplo/og.jpg"', html)
        self.assertIn('name="twitter:image" content="' + build.ORIGEN + 'analisis/ejemplo/og.jpg"', html)
        self.assertIn('name="twitter:title" content="Web &lt;ejemplo&gt;"', html)
        self.assertIn('name="twitter:description" content="Texto &amp; fotos"', html)
        self.assertIn('property="og:image:alt" content="Ejemplo &quot;visual&quot;"', html)


if __name__ == "__main__":
    unittest.main()
