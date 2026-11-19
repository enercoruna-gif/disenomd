"""Comprobaciones del HTML autónomo y del ZIP de entrega."""

from html.parser import HTMLParser
import json
from pathlib import Path
import re
import struct
import tempfile
import unittest
from zipfile import ZipFile

from empaquetar import FILES, ROOT, package


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class LaunchKitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.doc = Document(cls.html)

    def test_spanish_document_and_single_h1(self):
        self.assertIn(("html", {"lang": "es", "data-type": "software"}), self.doc.tags)
        self.assertEqual(sum(tag == "h1" for tag, _ in self.doc.tags), 1)

    def test_unique_ids_and_valid_local_anchors(self):
        ids = [attrs["id"] for _, attrs in self.doc.tags if "id" in attrs]
        self.assertEqual(len(ids), len(set(ids)))
        for tag, attrs in self.doc.tags:
            target = attrs.get("href", "")
            if target.startswith("#"):
                self.assertIn(target[1:], ids, (tag, target))
        self.assertNotIn('href="#"', self.html)

    def test_no_external_runtime_dependencies(self):
        for tag, attrs in self.doc.tags:
            if tag in {"script", "img", "iframe", "video", "audio", "source"}:
                self.assertFalse(attrs.get("src", "").startswith(("http", "//")))
            if tag == "link":
                self.assertNotIn(attrs.get("rel"), {"stylesheet", "preload"})
        for css_url in re.findall(r"url\(['\"]?([^)'\"]+)", self.html):
            self.assertTrue(css_url.startswith("data:"), css_url[:80])
        self.assertNotRegex(self.html, r"\b(?:fetch|XMLHttpRequest|WebSocket|localStorage|sessionStorage|sendBeacon)\s*[.(]")
        self.assertNotIn("document.cookie", self.html)

    def test_no_unresolved_placeholders(self):
        self.assertNotRegex(self.html, r"@@[A-Z]+@@")

    def test_design_matches_embedded_download(self):
        embedded = re.search(r'<script id="design-source" type="text/plain">(.*?)</script>', self.html, re.S)
        self.assertIsNotNone(embedded)
        self.assertEqual(embedded[1].strip(), (ROOT / "DESIGN.md").read_text(encoding="utf-8").strip())

    def test_safety_and_accessibility_basics(self):
        self.assertIn('href="#contenido"', self.html)
        self.assertIn(":focus-visible", self.html)
        self.assertIn("prefers-reduced-motion:reduce", self.html)
        self.assertNotIn("user-scalable=no", self.html)
        for tag, attrs in self.doc.tags:
            if tag in {"input", "textarea", "select"}:
                self.assertIn("name", attrs)
                self.assertTrue(any(t == "label" and a.get("for") == attrs.get("id") for t, a in self.doc.tags))
            if tag == "button":
                self.assertIn(attrs.get("type"), {"button", "submit"})
        self.assertIn("Sin conexión bancaria", self.html)
        self.assertIn("no se ha enviado ni guardado", self.html)

    def test_metadata_is_demo_not_financial_service(self):
        schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', self.html, re.S)
        self.assertEqual(len(schemas), 1)
        schema = json.loads(schemas[0])
        self.assertEqual(schema["@type"], "WebPage")
        self.assertEqual(schema["inLanguage"], "es")
        self.assertTrue(schema["isAccessibleForFree"])
        metas = {attrs.get("property", attrs.get("name")): attrs.get("content") for tag, attrs in self.doc.tags if tag == "meta"}
        self.assertEqual(metas["og:image:width"], "1200")
        self.assertEqual(metas["og:image:height"], "630")
        self.assertEqual(metas["robots"], "noindex,follow")

    def test_og_dimensions(self):
        png = (ROOT / "og.png").read_bytes()
        self.assertEqual(png[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(struct.unpack(">II", png[16:24]), (1200, 630))

    def test_zip_has_root_index_and_only_delivery_files(self):
        with tempfile.TemporaryDirectory() as temp:
            output = package(Path(temp) / "LaunchKit-gratis.zip")
            with ZipFile(output) as archive:
                self.assertEqual(set(archive.namelist()), set(FILES))
                self.assertIsNone(archive.testzip())
                for name in FILES:
                    self.assertEqual(archive.read(name), (ROOT / name).read_bytes())

    def test_package_rejects_overwriting_source(self):
        with self.assertRaises(ValueError):
            package(ROOT / "index.html")


if __name__ == "__main__":
    unittest.main()
