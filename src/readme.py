import json
from urllib.parse import quote

import analisis_web as AW
from notas_analisis import N

WEB = "https://enercoruna-gif.github.io/disenomd/"
REPO = "enercoruna-gif/disenomd"


def insignia(izq, der, color, fondo="161616"):
  e = lambda t: quote(t.replace("-", "--").replace("_", "__"))
  return f"https://img.shields.io/badge/{e(izq)}-{e(der)}-{color}?style=for-the-badge&labelColor={fondo}"


def muestra(hexa):
  return f'<img src="https://img.shields.io/badge/-%20-{hexa.lstrip("#")}?style=flat-square" alt="{hexa}" height="14">'


def corta(t, n=95):
  return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"


def fila(s, c):
  slug = s["slug"]
  paleta = "".join(muestra(c[k]) for k in ("primary", "accent", "background") if k in c)
  return (f'| <img src="docs/analisis/{slug}/icono.png" width="20" height="20" alt=""> | **[{s["nombre"]}]({WEB}analisis/{slug}/)** | {s["sector"]} | '
          f'{corta(N[slug][0])} | {paleta} | [DESIGN.md](docs/analisis/{slug}/DESIGN.md) |')


def tabla(items):
  return "| | Web | Sector | Estilo | Paleta | Archivo |\n|:-:|---|---|---|---|---|\n" + "\n".join(fila(s, c) for s, c in items)


def generar(raiz):
  items = [(s, AW.design_md(s, json.loads((AW.RAIZ / "src/analisis" / f"{s['slug']}.json").read_text()))[1]) for s in AW.SITIOS]
  dest = [x for x in items if x[0].get("portada")]
  grupos = ""
  for g in AW.GRUPOS:
    del_grupo = [x for x in items if AW.GRUPO[x[0]["sector"]] == g]
    if del_grupo:
      grupos += f"\n<details>\n<summary><b>{g}</b> · {len(del_grupo)} webs</summary>\n\n{tabla(del_grupo)}\n\n</details>\n"
  from build import KITS, COMPRA, COMPRA_TODO
  comprar = lambda k: f"[Comprar]({COMPRA[k['slug']]})" if k['slug'] in COMPRA else 'Pronto'
  colores = ["FF7A45", "7B6CFF", "2EA043", "F5A9D6", "4285F4", "F5B83D", "C60B1E"]
  packs = ("## 🎁 Packs de pago\n\nPago único en Payhip. Detalles de cada uno en la [página de kits](" + WEB + "kits/).\n\n"
           "| Pack | Qué es | Precio | |\n|---|---|:-:|:-:|\n"
           + "\n".join(f'| **[{k["nombre"]}]({WEB}kits/#{k["slug"]})** | {k["sub"]} | <img src="{insignia("precio", k["precio"].replace(" ", ""), colores[i % len(colores)])}" alt="{k["precio"]}"> | {comprar(k)} |' for i, k in enumerate(KITS))
           + f'\n| **[Pack completo]({WEB}kits/#todo)** | Los 7 packs digitales juntos | <img src="{insignia("precio", "199€", "C60B1E")}" alt="199 €"> | [Comprar]({COMPRA_TODO}) |')
  badges = " ".join(f'<img src="{u}" alt="{a}">' for a, u in [
    ("DESIGN.md", insignia("DESIGN.md", str(len(items)), "F5A9D6")),
    ("idioma", insignia("idioma", "español", "C60B1E", "FFC400")),
    ("precio", insignia("precio", "gratis", "2EA043")),
    ("formato", insignia("formato", "Google DESIGN.md", "4285F4")),
  ])
  estrellas = f'<a href="https://github.com/{REPO}/stargazers"><img src="https://img.shields.io/github/stars/{REPO}?style=for-the-badge&color=F5B83D&labelColor=161616&label=estrellas" alt="estrellas"></a>'
  texto = f'''<p align="center"><a href="{WEB}"><img src="docs/assets/readme-banner.svg" alt="diseño.md — DESIGN.md gratis en español para tu IA" width="100%"></a></p>

<p align="center">{badges}<br>{estrellas} <a href="{WEB}"><img src="{insignia("web", "abrir catálogo", "7B6CFF")}" alt="web"></a></p>

<h3 align="center">Copia el estilo de las webs que te gustan y haz que tu IA lo respete en cada pantalla.</h3>

<p align="center"><a href="{WEB}"><b>🌐 Abrir la web</b></a> · <a href="{WEB}webs/"><b>📚 Ver las {len(items)} webs</b></a> · <a href="{WEB}kits/"><b>🎁 Kits</b></a> · <a href="{WEB}como-usar/"><b>❓ Cómo se usa</b></a></p>

{packs}

---

## ⚡ En 30 segundos

1. **Elige** una web cuyo estilo te guste en la [web del catálogo]({WEB}).
2. **Copia** su DESIGN.md con un toque, también desde el móvil.
3. **Pégalo** en tu IA junto a tu petición: *«Hazme la web de mi negocio siguiendo este DESIGN.md»*.

Saldrá con una paleta, dos tipografías y los mismos botones en todas las páginas, en lugar de colores al azar en cada sección.

## 🧩 ¿Qué es un DESIGN.md?

Es un archivo de texto con el sistema de diseño de una web: **colores, tipografías, radios, espaciados y componentes**, escrito para que un agente de IA lo lea y lo aplique. Sigue el [formato abierto de Google](https://github.com/google-labs-code/design.md), así que funciona igual en cualquier herramienta.

Cada análisis de este repositorio lo hemos hecho nosotros: visitamos la web, hacemos la captura, extraemos sus colores y letras y escribimos en español qué la hace reconocible.

## 🛠️ Dónde funciona

| Para crear webs con IA | Agentes de código | Chats |
|---|---|---|
| Lovable · v0 · Bolt · Framer · Webflow | Claude Code · Cursor · Codex · Copilot · Windsurf | ChatGPT · Claude · Gemini |

En los agentes de código basta con guardar el archivo como `DESIGN.md` en la raíz del proyecto y pedir *«sigue el DESIGN.md»*.

## ⭐ Destacados

{tabla(dest)}

## 📚 Catálogo completo por sector
{grupos}
## 🤝 ¿Echas en falta una web?

[Abre una petición](https://github.com/{REPO}/issues/new?title=Analizar%20la%20web%20de%20...) con la web que quieres ver analizada. Y si el catálogo te ahorra tiempo, **dale una ⭐ al repositorio**: así más gente lo encuentra.

## ⚖️ Aviso

Análisis independientes y sin afiliación. Los nombres, logotipos y marcas son de sus dueños y solo se citan para identificar la web analizada; las capturas son nuestras. Úsalos como referencia de estilo para tu propia web, con tus textos, tu logotipo y tus imágenes.

## 🧱 Cómo está hecho

- `src/sitios.json` + `src/rastreo.py`: lista de webs y rastreo con Playwright y Chrome, que hace las capturas (`docs/analisis/<slug>/captura.webp`) y extrae colores y tipografías a `src/analisis/<slug>.json`.
- `src/notas_analisis.py` y `src/analisis_web.py`: textos de cada análisis y generación de sus DESIGN.md.
- `src/build.py`: genera la web en `docs/` y este README (`python3 src/build.py`).
- `src/logos/`: logotipos de [Simple Icons](https://simpleicons.org) (CC0).
- Validación: `npx @google/design.md lint docs/analisis/*/DESIGN.md`.
- Publicación gratis con GitHub Pages desde `docs/` en `main`.
'''
  (raiz / "README.md").write_text(texto)
