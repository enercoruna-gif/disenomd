"""Dependency-free integrity checks for the Crix handoff."""

import re
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile

from build import ROOT, build, data_uri


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids = []
        self.links = []
        self.files = []
        self.downloads = []
        self.h1 = 0
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if "download" in attrs:
            self.downloads.append(attrs["download"])
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "h1":
            self.h1 += 1
        for name in ("href", "src"):
            if name not in attrs:
                continue
            value = attrs[name]
            if value.startswith("#"):
                self.links.append(value[1:])
            elif not value.startswith(("https:", "data:")):
                self.files.append(value)


class DeliveryTest(unittest.TestCase):
    def test_portable_mime_types(self):
        with patch("build.mimetypes.guess_type", return_value=(None, None)):
            self.assertTrue(data_uri(ROOT / "assets/montanas.webp").startswith("data:image/webp;base64,"))
            self.assertTrue(data_uri(ROOT / "DESIGN.md").startswith("data:text/markdown;base64,"))

    def test_document_and_assets(self):
        source = (ROOT / "index.html").read_text()
        doc = Document(source)
        self.assertEqual(doc.downloads, ["DESIGN.md"] * 3)
        self.assertEqual(doc.h1, 1)
        self.assertEqual(len(doc.ids), len(set(doc.ids)))
        self.assertIn('lang="es"', source)
        self.assertIn('application/ld+json', source)
        for target in doc.links:
            self.assertIn(target, doc.ids)
        for name in doc.files:
            self.assertTrue((ROOT / name).is_file(), name)
        for asset in re.findall(r"url\(['\"]?([^)'\"]+)", (ROOT / "styles.css").read_text()):
            self.assertTrue((ROOT / asset).is_file(), asset)

    def test_packaging(self):
        with tempfile.TemporaryDirectory() as directory:
            output = build(directory)
            with ZipFile(output / "Crix-completo.zip") as archive:
                self.assertIsNone(archive.testzip())
                self.assertIn("index.html", archive.namelist())
                self.assertIn("DESIGN.md", archive.namelist())
                self.assertNotIn("crix/index.html", archive.namelist())
            standalone = (output / "Crix-autonomo.html").read_text()
            self.assertEqual(Document(standalone).files, [])
            self.assertNotIn('src="app.js"', standalone)
            self.assertNotIn("url('assets/", standalone)
            self.assertIn("data:image/webp;base64,", standalone)
            self.assertEqual(Document(standalone).downloads, ["DESIGN.md"] * 3)
            self.assertEqual((output / "DESIGN.md").read_bytes(), (ROOT / "DESIGN.md").read_bytes())

    def test_demo_honesty_and_safety(self):
        source = (ROOT / "index.html").read_text()
        script = (ROOT / "app.js").read_text()
        self.assertIn("Datos de ejemplo", source)
        self.assertIn("no es un testimonio", source)
        self.assertNotIn("fetch(", script)
        self.assertNotIn("innerHTML", script)
        self.assertNotIn("localStorage", script)
        self.assertEqual(source.count('name="billing"'), 2)
        self.assertEqual(source.count('data-plan='), 3)
        self.assertIn('prefers-reduced-motion:reduce', (ROOT / "styles.css").read_text())


if __name__ == "__main__":
    unittest.main()
