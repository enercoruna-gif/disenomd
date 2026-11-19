# diseño.md

Catálogo gratuito de archivos DESIGN.md en español (formato abierto de Google) para agentes de código con IA, más fichas de kits de pago.

- `src/catalogo.py`: datos de los 13 sistemas de diseño originales.
- `src/sitios.json` + `src/rastreo.py`: lista de webs públicas analizadas; el rastreo hace capturas propias (`docs/analisis/<slug>/captura.webp`) y extrae colores y tipografías a `src/analisis/<slug>.json`. Requiere Playwright y Chrome; solo hace falta volver a lanzarlo para añadir o refrescar webs.
- `src/notas_analisis.py` y `src/analisis_web.py`: análisis redactados por nosotros y generación de sus DESIGN.md.
- `src/logos/`: logotipos de [Simple Icons](https://simpleicons.org) (CC0).
- `src/build.py`: genera la web estática en `docs/` (`python3 src/build.py`).
- Comprobar formato: `npx @google/design.md lint docs/disenos/*/DESIGN.md docs/analisis/*/DESIGN.md`.
- Publicación gratis: GitHub Pages desde la carpeta `docs/` de la rama principal.
