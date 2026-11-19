import re
"""Genera el sitio estático (docs/) y los DESIGN.md del catálogo."""
import html, json, shutil, zipfile
from pathlib import Path
from urllib.parse import quote_plus
from maquetas import M
import analisis_web as AW
from catalogo import DISENOS, TIPOS

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "docs"
MARCA = "diseño.md"
CONTACTO = "enercoruna@gmail.com"
TIENDA = "https://payhip.com/Cuadrantia"

PESOS = {
  "Press Start 2P": [400], "DM Serif Display": [400], "Space Mono": [400, 700],
  "Atkinson Hyperlegible": [400, 700], "Cormorant Garamond": [400, 500, 600, 700],
}
PESO_TITULAR = {"Press Start 2P": 400, "DM Serif Display": 400, "Cormorant Garamond": 500,
  "Fraunces": 600, "Source Serif 4": 600, "Archivo": 800, "Nunito": 800}
NOMBRE_COLOR = dict(primary="Primario", **{"on-primary": "Sobre primario"}, secondary="Secundario",
  accent="Acento", background="Fondo", surface="Superficie", text="Texto", muted="Atenuado", border="Borde")

esc = html.escape


def familias(d):
  return list(dict.fromkeys([d["fuentes"][0], d["fuentes"][1], d["mono"]]))


def url_fuentes(fams):
  partes = []
  for f in dict.fromkeys(fams):
    w = PESOS.get(f, [400, 500, 600, 700, 800] if f in ("Archivo", "Nunito", "Inter") else [400, 500, 600, 700])
    partes.append("family=" + quote_plus(f) + ":wght@" + ";".join(map(str, w)))
  return "https://fonts.googleapis.com/css2?" + "&".join(partes) + "&display=swap"


def peso(fuente, nominal):
  disp = PESOS.get(fuente)
  if disp:
    return min(disp, key=lambda w: abs(w - nominal))
  return nominal


def luminancia(hexa):
  r, g, b = (int(hexa[i:i + 2], 16) / 255 for i in (1, 3, 5))
  f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
  return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contraste(a, b):
  la, lb = sorted((luminancia(a), luminancia(b)), reverse=True)
  return (la + 0.05) / (lb + 0.05)


def texto_sobre(c, fondo):
  return max(("text", "background", "on-primary"), key=lambda k: contraste(c[k], c[fondo]))


def design_md(d):
  c = d["colores"]
  disp, cuerpo = d["fuentes"]
  ptit = PESO_TITULAR.get(disp, TIPOS["display"][3])
  y = ["---", 'version: "alpha"', f"name: {d['nombre']}", f'description: "{d["lema"]}"', "colors:"]
  y += [f'  {k}: "{v}"' for k, v in c.items()]
  y.append("typography:")
  tok = [("display-lg", disp, TIPOS["display"], ptit), ("headline-md", disp, TIPOS["headline"], peso(disp, max(ptit - 100, 400) if disp != cuerpo else 600)),
         ("body-md", cuerpo, d.get("cuerpo_tam", TIPOS["body"]), 400), ("label-sm", cuerpo, TIPOS["label"], peso(cuerpo, 500)),
         ("code-sm", d["mono"], ("0.875rem", "1.5", "0em", 400), 400)]
  for nombre, fam, (tam, lh, ls, _), w in tok:
    y += [f"  {nombre}:", f"    fontFamily: {fam}", f"    fontSize: {tam}", f"    fontWeight: {w}",
          f"    lineHeight: {lh}", f"    letterSpacing: {ls}"]
  y.append("rounded:")
  y += [f"  {k}: {v}" for k, v in d["radio"].items()]
  b = d["espacio_base"]
  y.append("spacing:")
  for k, m in [("xs", 1), ("sm", 2), ("md", 4), ("lg", 6), ("xl", 10), ("2xl", 16)]:
    y.append(f"  {k}: {b * m}px")
  y += ["components:",
        "  button-primary:", '    backgroundColor: "{colors.primary}"', '    textColor: "{colors.on-primary}"',
        '    typography: "{typography.label-sm}"', '    rounded: "{rounded.md}"', "    padding: 12px 20px", "    height: 44px",
        "  button-secondary:", '    backgroundColor: "{colors.surface}"', '    textColor: "{colors.text}"',
        '    rounded: "{rounded.md}"', "    padding: 12px 20px",
        "  card:", '    backgroundColor: "{colors.surface}"', '    textColor: "{colors.text}"',
        '    rounded: "{rounded.lg}"', "    padding: 24px",
        "  input:", '    backgroundColor: "{colors.surface}"', '    textColor: "{colors.text}"',
        '    typography: "{typography.body-md}"', '    rounded: "{rounded.sm}"', "    padding: 12px", "    height: 44px",
        "  chip:", '    backgroundColor: "{colors.background}"', '    textColor: "{colors.text}"',
        '    typography: "{typography.label-sm}"', '    rounded: "{rounded.full}"', "    padding: 4px 12px",
        "  badge:", '    backgroundColor: "{colors.accent}"', f'    textColor: "{{colors.{texto_sobre(c, "accent")}}}"',
        '    typography: "{typography.label-sm}"', '    rounded: "{rounded.full}"', "    padding: 2px 10px",
        "  caption:", '    backgroundColor: "{colors.background}"', '    textColor: "{colors.muted}"', '    typography: "{typography.label-sm}"',
        "  divider:", '    backgroundColor: "{colors.border}"', "    height: 1px",
        *[l for nom, props, _ in M[d["slug"]]["comps"] for l in [f"  {nom}:"] + [f'    {k}: "{v}"' if "{" in v else f"    {k}: {v}" for k, v in props.items()]],
        "---", ""]
  m = [f"# {d['nombre']} — DESIGN.md", "",
       f"> {d['lema']} Ideal para: {d['ideal']}", "",
       f"Sistema de diseño original de {MARCA}. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). "
       "Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.", "",
       "## Resumen", "", d["resumen"], "",
       "## Colores", ""]
  for k, v in c.items():
    nota = d["notas_color"].get(k)
    if nota:
      m.append(f"- **{NOMBRE_COLOR[k]} `{k}` ({v}):** {nota}")
  m += [f"- **Texto sobre primario `on-primary` ({c['on-primary']}):** color de texto e iconos dentro de botones primarios.",
        f"- **Superficie, atenuado y borde ({c['surface']}, {c['muted']}, {c['border']}):** tarjetas, texto secundario y divisores.", "",
        "## Tipografía", "", d["tipografia"], "",
        f"Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, "
        f"`body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` ({d['mono']}) para código y datos copiables.", "",
        "## Disposición", "", d["layout"], "",
        f"Espaciado en múltiplos de {b}px (tokens `spacing`), con un ritmo {M[d['slug']]['densidad']}. Objetivos táctiles de al menos 44px.", "",
        "## Elevación y profundidad", "", d["elevacion"], "",
        "## Formas", "", d["formas"], "",
        "## Movimiento", "", d["movimiento"] + " Respeta siempre `prefers-reduced-motion`.", "",
        "## Voz y contenido", "", d["voz"], "",
        "## Componentes", "",
        *[f"- **`{nom}`**: {txt}" for nom, _, txt in M[d["slug"]]["comps"]],
        f"- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios {d['radio']['sm']} / {d['radio']['md']} / {d['radio']['lg']}, etiquetas en {d['fuentes'][1]} y una sola acción primaria por vista.", "",
        "## Qué hacer y qué no", ""]
  m += [f"- Sí: {s}" for s in d["si"]]
  m += [f"- No: {s}" for s in d["no"]]
  m += ["", "---", "", f"Hecho por {MARCA} · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.", ""]
  return "\n".join(y + m)


def legible(color, fondo, tinta, minimo=4.5):
  mezcla = lambda a, b, t: "#" + "".join(f"{round(int(a[i:i + 2], 16) * (1 - t) + int(b[i:i + 2], 16) * t):02X}" for i in (1, 3, 5))
  t = 0.0
  while contraste(mezcla(color, tinta, t), fondo) < minimo and t < 1:
    t += 0.05
  return mezcla(color, tinta, min(t, 1))


def vars_css(d):
  c = d["colores"]
  disp, cuerpo = d["fuentes"]
  return (f"--bg:{c['background']};--fg:{c['text']};--pri:{c['primary']};--on:{c['on-primary']};--sec:{c['secondary']};"
          f"--acc:{c['accent']};--onacc:{c[texto_sobre(c, 'accent')]};--sur:{c['surface']};--mut:{legible(c['muted'], c['surface'], c['text'])};--bd:{c['border']};"
          f"--secT:{legible(c['secondary'], c['surface'], c['text'])};--accT:{legible(c['accent'], c['surface'], c['text'])};--priT:{legible(c['primary'], c['surface'], c['text'])};"
          f"--fd:'{disp}';--fb:'{cuerpo}';--fm:'{d['mono']}';--wd:{PESO_TITULAR.get(disp, 700)};"
          f"--r:{d['radio']['md']};--rl:{d['radio']['lg']};--rf:{d['radio']['full']}")


GRUPOS = {"terracota": "Negocio local", "azulejo": "Negocio local", "clinico": "Negocio local", "bosque": "Negocio local",
  "fintech-sobrio": "SaaS y apps", "panel-saas": "SaaS y apps", "pastel-suave": "SaaS y apps",
  "editorial": "Editorial y premium", "lujo-noir": "Editorial y premium",
  "neon-nocturno": "Oscuro y tech", "retro-pixel": "Oscuro y tech",
  "papel-suizo": "Creativo", "brutalista": "Creativo"}

SECTORES = dict(
  terracota="bar cafetería cafeteria café panadería pastelería pizzería catering vinos comida food tapas obrador",
  azulejo="hotel hostal camping agencia de viajes alquiler vacacional airbnb tours rutas ayuntamiento",
  **{"fintech-sobrio": "gestoría asesoría contabilidad seguros banco inversiones abogado finanzas app"},
  **{"neon-nocturno": "discoteca dj música videojuegos esports tecnología software startup oscuro"},
  **{"papel-suizo": "arquitecto interiorismo fotógrafo diseñador freelance reformas construcción minimalista estudio"},
  bosque="eco ecológico jardinería huerto herbolario yoga spa masajes veterinaria granja natural",
  brutalista="evento festival podcast creador tienda online moda urbana tatuajes barbería atrevido",
  **{"pastel-suave": "colegio academia profesor clases guardería psicólogo nutricionista infantil escuela"},
  editorial="blog revista periódico escritor abogado despacho notaría librería newsletter",
  clinico="clínica médico dentista fisioterapeuta óptica farmacia veterinario salud psicología centro",
  **{"lujo-noir": "joyería peluquería estética hotel boutique inmobiliaria bodega vino moda lujo elegante oscuro dark"},
  **{"panel-saas": "app panel crm erp reservas gestión inventario dashboard herramienta"},
  **{"retro-pixel": "videojuegos tienda de cómics juegos de mesa escape room ludoteca arcade streamer oscuro dark"},
)


def tarjeta(d, prefijo):
  c = d["colores"]
  sw = "".join(f'<i style="background:{c[k]}"></i>' for k in ("primary", "secondary", "accent", "text", "background"))
  return f'''<a class="tarjeta" href="{prefijo}disenos/{d["slug"]}/" data-cat="{esc(GRUPOS[d["slug"]])}" data-texto="{esc((d["nombre"] + " " + d["categoria"] + " " + d["ideal"] + " " + d["lema"] + " web " + SECTORES.get(d["slug"], "")).lower())}">
  <div class="mini" style="{vars_css(d)}">
    <div class="mini-nav"><b></b><span></span><span></span></div>
    <div class="mini-tit">{esc(d["nombre"])}</div>
    <div class="mini-txt">{esc(d["lema"])}</div>
    <div class="mini-btns"><span class="mb1">Ver diseño</span></div>
  </div>
  <div class="tarjeta-pie"><div><strong>{esc(d["categoria"])}</strong><small>{esc(d["ideal"].split(",")[0])} y más</small></div><div class="sw">{sw}</div></div>
</a>'''


def pagina(titulo, desc, cuerpo, prefijo="", fuentes_extra=None, canon=""):
  fams = ["Inter", "JetBrains Mono"] + (fuentes_extra or [])
  return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(titulo)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<link rel="icon" href="{prefijo}assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{prefijo}assets/icono-180.png">
<link rel="manifest" href="{prefijo}manifest.webmanifest" crossorigin="use-credentials">
<meta name="theme-color" content="#161616">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{url_fuentes(fams)}">
<link rel="stylesheet" href="{prefijo}assets/estilo.css">
</head>
<body>
<a class="aviso" href="{prefijo}#catalogo"><span class="pill">NUEVO</span> {len(DISENOS) + len(AW.SITIOS)} diseños listos para copiar en ChatGPT <span aria-hidden="true">→</span></a>
<header class="cab">
  <a class="logo" href="{prefijo}"><span>diseño</span>.md</a>
  <button class="menu-btn" aria-label="Abrir menú" aria-expanded="false" onclick="document.body.classList.toggle('menu-abierto');this.setAttribute('aria-expanded',document.body.classList.contains('menu-abierto'))">☰</button>
  <nav class="nav" aria-label="Menú principal">
    <a class="nav-dest" href="{prefijo}kits/#a-medida"><span aria-hidden="true">➤</span> Pedir un DESIGN.md a medida</a>
    <a href="{prefijo}#catalogo">Catálogo DESIGN.md</a>
    <a href="{prefijo}webs/">Webs populares</a>
    <a href="{prefijo}kits/#pase">Pase del catálogo</a>
    <a href="{prefijo}kits/#web">Kit web inicial <span class="nav-ext" aria-hidden="true">↗</span></a>
    <a href="{prefijo}kits/#app">Kit app móvil</a>
    <a href="{prefijo}kits/#prompts">Pack de prompts</a>
    <a href="{prefijo}kits/#fondos">Fondos</a>
    <a href="{prefijo}kits/#videos">Plantillas de vídeo</a>
    <a href="{prefijo}descargas/disenomd-catalogo.zip" download>DESIGN.md gratis</a>
    <hr>
    <a href="{prefijo}como-usar/">Qué es el formato DESIGN.md</a>
    <a href="{prefijo}aviso-legal/">Aviso legal</a>
  </nav>
</header>
<main>
{cuerpo}
</main>
<footer class="pie">
  <div><a class="logo" href="{prefijo}"><span>diseño</span>.md</a><p>Sistemas de diseño en español para que la IA haga webs con buen gusto. Un proyecto de Cuadrantia, hecho en España.</p></div>
  <div class="pie-links"><a href="{prefijo}#catalogo">Catálogo</a><a href="{prefijo}kits/">Kits</a><a href="{prefijo}como-usar/">Cómo usarlo</a><a href="{prefijo}aviso-legal/">Aviso legal y privacidad</a></div>
  <p class="badge-cp"><a target="_blank" rel="noopener" href="https://cazaproducto.com/productos/diseno-md"><img alt="diseño.md — CazaProducto" width="290" height="54" style="width:290px;height:54px;" src="https://cazaproducto.com/productos/diseno-md/badge?theme=light" /></a></p>
  <p class="legal">DESIGN.md es un formato abierto. Los diseños de este catálogo son originales de {MARCA}. Claude Code, Cursor, Codex, Gemini y ChatGPT son marcas de sus respectivos dueños; no hay afiliación.</p>
</footer>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="{prefijo}assets/app.js"></script>
</body>
</html>'''


HERRAMIENTAS = '<div class="herr"><span>Claude Code</span><span>Cursor</span><span>Codex</span><span>Gemini CLI</span><span>ChatGPT</span><span>Lovable</span><span>v0</span><span class="tenue">y cualquier asistente de código</span></div>'

KITS = [
  dict(slug="web", icono="▭", nombre="Kit Web Inicial", sub="Tu web casi terminada: cambia textos y fotos",
       llano="5 webs completas (página de presentación, tienda, blog, portfolio y web de servicio) que le pasas a tu IA para que las adapte a tu negocio en una tarde.",
       precio="79 €", detalle="5 plantillas (presentación, servicio, tienda, blog, portfolio) en Next.js + Tailwind, cada una con su DESIGN.md, AGENTS.md y prompts listos para Claude Code, Cursor o Codex.",
       incluye=["5 webs completas: presentación, servicio, tienda, blog y portfolio", "DESIGN.md + AGENTS.md en cada plantilla", "Biblioteca de 60 prompts en español por pantalla", "Guía paso a paso para publicar gratis", "Pago único y actualizaciones de por vida"]),
  dict(slug="app", icono="▯", nombre="Kit App Móvil", sub="Tu app para iPhone y Android, ya empezada",
       llano="Una app base con registro, pagos y avisos ya montados: solo falta conectarlos a tus cuentas. Le pides a la IA los cambios en español y te guía hasta publicarla en App Store y Google Play.",
       precio="79 €", detalle="Base de app en Expo / React Native con inicio de sesión, pagos, notificaciones y navegación ya montados: solo falta conectarlos a tus cuentas. Guiada por DESIGN.md.",
       incluye=["Plantilla Expo con 12 pantallas tipo", "Registro, pagos y avisos montados, listos para conectar a tus cuentas", "DESIGN.md móvil + AGENTS.md", "Prompts para añadir pantallas sin romper el estilo", "Guía para subir a App Store y Google Play"]),
  dict(slug="prompts", icono="✦", nombre="Pack Prompts e Instrucciones", sub="Instrucciones listas para tu IA",
       llano="Más de 100 instrucciones probadas para pedirle a la IA textos, diseños y webs que salgan bien a la primera.",
       precio="19 €", detalle="Colección de prompts, habilidades para tu IA (archivos SKILL.md) y reglas (.cursorrules, CLAUDE.md, AGENTS.md) en español para diseñar, programar, escribir textos y revisar webs.",
       incluye=["40 habilidades (archivos SKILL.md) listas para Claude y Codex", "Plantillas CLAUDE.md, AGENTS.md y .cursorrules", "120 prompts de diseño, código y marketing", "Ejemplos antes/después", "Actualizaciones mensuales"]),
]




COLOR_LOGO = dict(claude="#D97757", stackblitz="#1269D3", framer="#0055FF", webflow="#146EF5", wordpress="#21759B", wix="#0C6EFC",
                  replit="#F26207", googlegemini="url(#grad-gemini)")
DEGRADADOS = {"grad-gemini": ("#4285F4", "#9B72CB", "#D96570")}


def _logo(slug, nombre, color=None):
  if not slug:
    estilo = f' style="color:{color}"' if color and not color.startswith("grad") else ""
    clase = " logo-grad" if color == "grad" else ""
    return f'<span class="logo logo-txt{clase}" title="{nombre}"{estilo}>{nombre}</span>'
  d = re.search(r' d="([^"]+)"', (Path(__file__).parent / "logos" / f"{slug}.svg").read_text()).group(1)
  relleno = COLOR_LOGO.get(slug, "currentColor")
  return f'<span class="logo" title="{nombre}"><svg viewBox="0 0 24 24" role="img" aria-label="{nombre}"><path fill="{relleno}" d="{d}"/></svg></span>'


CREADORES = [(None, "Lovable", "grad"), ("v0", "v0"), ("stackblitz", "Bolt"), ("framer", "Framer"), ("webflow", "Webflow"),
             ("wordpress", "WordPress"), ("wix", "Wix"), ("squarespace", "Squarespace"), ("replit", "Replit")]
AGENTES = [("claude", "Claude"), ("cursor", "Cursor"), ("googlegemini", "Gemini"), (None, "ChatGPT", "#10A37F"), ("githubcopilot", "GitHub Copilot"),
           ("windsurf", "Windsurf"), (None, "Codex")]


def logos():
  fila = lambda xs: "".join(_logo(*x) for x in xs)
  defs = "".join(f'<linearGradient id="{k}" x1="0" y1="0" x2="1" y2="1">' + "".join(f'<stop offset="{n / (len(v) - 1):.2f}" stop-color="{c}"/>' for n, c in enumerate(v)) + "</linearGradient>" for k, v in DEGRADADOS.items())
  svgdefs = f'<svg width="0" height="0" aria-hidden="true" style="position:absolute"><defs>{defs}</defs></svg>'
  return (f'<div class="logos">{svgdefs}<p class="eti">▸ Úsalo en cualquier creador web con IA</p><div class="fila-logos">{fila(CREADORES)}</div>'
          f'<p class="eti">▸ O en cualquier agente de código</p><div class="fila-logos">{fila(AGENTES)}</div>'
          '<p class="tenue peq">Pega el DESIGN.md donde construyas y úsalo como referencia de diseño con una sola instrucción. '
          'Logotipos de <a href="https://simpleicons.org" rel="noopener">Simple Icons</a> (CC0); las marcas son de sus dueños y no hay afiliación.</p></div>')


def portada():
  tarjetas = "\n".join(tarjeta(d, "") for d in DISENOS)
  cats = list(dict.fromkeys(GRUPOS[d["slug"]] for d in DISENOS))
  chips = '<button class="chip activo" data-filtro="">Todos</button>' + "".join(f'<button class="chip" data-filtro="{esc(c)}">{esc(c)}</button>' for c in cats)
  _kits = "".join(f'''<a class="kit-btn{' kit-dest' if i == 0 else ''}" href="kits/#{k["slug"]}"><span class="kit-ico">{k["icono"]}</span><span><strong>{k["nombre"]}</strong><small>{k["sub"]}</small></span></a>''' for i, k in enumerate(KITS[:2]))
  usos = [("01", "Dar estilo sin saber diseñar", "Elige un DESIGN.md, ponlo en tu proyecto y tu agente aplica colores, tipografía y componentes coherentes."),
          ("02", "Partir de una referencia que te guste", "Usa un sistema del catálogo como base y pide a la IA que lo adapte a tu marca."),
          ("03", "Mantener todo igual en cada pantalla", "El agente consulta el archivo antes de cada pantalla, así la décima se parece a la primera."),
          ("04", "Ahorrar horas de retoques", "Menos «hazlo más bonito» y más tiempo para tu producto.")]
  usos_html = "".join(f'<a class="uso" href="como-usar/"><span class="num">{n}</span><span><strong>{t}</strong><small>{s}</small></span><span aria-hidden="true">→</span></a>' for n, t, s in usos)
  faq = [("¿Qué es un DESIGN.md?", "Un archivo de texto que explica a la IA cómo debe verse tu web: colores, tipos de letra, espacios y botones. Lo pegas junto a tu petición y la IA lo sigue. Usa el formato abierto publicado por Google."),
         ("¿Es gratis?", "Sí. Todos los DESIGN.md del catálogo son gratuitos para proyectos personales y comerciales. Los kits de inicio, cuando salgan, serán de pago."),
         ("¿Funciona desde el móvil?", "Sí. Copia el DESIGN.md o el prompt con un toque y pégalo en ChatGPT, Claude, Gemini o tu herramienta favorita."),
         ("¿Necesito saber programar?", "No para empezar: basta con pegar el prompt. Para publicar tu web, los kits incluyen una guía paso a paso.")]
  faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
  cuerpo = f'''
<section class="hero">
  <h1>Haz que la web que te crea la IA parezca <em>hecha por un diseñador</em>.</h1>
  <p class="intro">Elige un estilo, cópialo con un toque y pégalo en ChatGPT, Lovable o la IA que uses junto a tu petición. Colores, letras y botones salen coherentes desde el primer intento. Gratis.</p>
  <div class="acciones"><a class="btn btn-grande" href="#catalogo">Elige un diseño gratis</a><a class="btn btn-claro" href="como-usar/">Cómo funciona</a></div>
  {logos()}
  <div class="antes-despues">
    <div><p class="eti">Sin DESIGN.md</p><p>«Hazme una web para mi peluquería» → colores al azar, letras distintas en cada sección, botones que no pegan.</p></div>
    <div><p class="eti eti-acc">Con DESIGN.md</p><p>«Hazme una web para mi peluquería siguiendo este DESIGN.md» → una paleta, dos tipografías y el mismo estilo en todas las páginas.</p></div>
  </div>
  <p class="spec">Sigue el formato abierto <a href="https://github.com/google-labs-code/design.md" rel="noopener">DESIGN.md de Google</a></p>
</section>
<section class="bloque lista-webs" aria-labelledby="t-webs">
  <p class="eti" id="t-webs"># Análisis de webs populares</p>
  <ul class="lista-iconos">{"".join(f'<li><a href="analisis/{x["slug"]}/"><img src="analisis/{x["slug"]}/icono.png" alt="" width="28" height="28"><span>{esc(x["nombre"])}</span><small>{esc(x["sector"])}</small></a></li>' for x in AW.SITIOS[:12])}</ul>
  <p><a class="btn btn-claro btn-peq" href="webs/">Ver las {len(AW.SITIOS)} webs →</a></p>
</section>
<section class="bloque" id="catalogo">
  <div class="tit-sec"><h2>Catálogo gratuito</h2><span class="tenue">{len(DISENOS)} estilos originales · <a href="webs/">{len(AW.SITIOS)} webs populares en su propia sección →</a></span></div>
  <p><a class="btn btn-claro btn-peq" href="descargas/disenomd-catalogo.zip" download>Descargar los {len(DISENOS)} DESIGN.md (zip)</a></p>
  <input class="buscar" id="buscar" type="search" placeholder="Busca tu negocio: peluquería, bar, clínica…" aria-label="Buscar diseños">
  <div class="chips" id="chips">{chips}</div>
  <p class="vacio" id="vacio" hidden>Ningún diseño menciona «<span id="vacio-q"></span>», pero todos sirven para cualquier negocio: elige el que más te guste por sus colores.</p>
  <div class="rejilla" id="rejilla">{tarjetas}</div>
</section>
<section class="bloque">
  <p class="eti">Usa DESIGN.md para</p>
  <div class="usos">{usos_html}</div>
</section>
<section class="bloque banda">
  <p class="eti eti-acc">Kits de inicio</p>
  <h2>Próximamente: webs y apps casi terminadas.</h2>
  <p>Plantillas completas con las pantallas, el diseño y las instrucciones para la IA ya preparadas. Tú solo cambias textos y fotos.</p>
  <a class="btn" href="kits/">Ver qué incluirán</a>
</section>
<section class="bloque"><h2>Preguntas frecuentes</h2><div class="faq">{faq_html}</div></section>
'''
  fams = [f for d in DISENOS for f in familias(d)]
  return pagina(f"{MARCA} — Sistemas de diseño DESIGN.md en español para agentes de IA",
                "Catálogo gratuito de archivos DESIGN.md en español para Claude Code, Cursor, Codex, Gemini y ChatGPT. Dale a tu web un diseño coherente en minutos.",
                cuerpo, "", fams)


def detalle(d, i):
  c = d["colores"]
  md = design_md(d)
  prompt = (f"Crea [describe aquí tu web: p. ej. la página de mi peluquería en Lugo con servicios, precios y botón de WhatsApp]. Usa el DESIGN.md que te he pasado (estilo «{d['nombre']}») como única referencia visual. "
            "Aplica sus colores, tipografías, espaciados, radios y componentes en todas las pantallas, respeta su apartado «Qué hacer y qué no» "
            "y no inventes estilos nuevos. Si falta algo, deriva la decisión de los tokens existentes.")
  sw = "".join(f'<button class="muestra" data-copiar="{v}"><i style="background:{v}"></i><span><strong>{NOMBRE_COLOR[k]}</strong><code>{v}</code></span></button>' for k, v in c.items())
  ant, sig = DISENOS[i - 1], DISENOS[(i + 1) % len(DISENOS)]
  disp, cuerpo_f = d["fuentes"]
  cuerpo = f'''
<nav class="migas"><a href="../../#catalogo">Catálogo</a> / {esc(d["nombre"])}</nav>
<section class="det-cab">
  <p class="eti">{esc(d["categoria"])}</p>
  <h1>{esc(d["nombre"])}</h1>
  <div class="demo maqueta" style="{vars_css(d)}" aria-label="Vista previa de {esc(d["nombre"])}">{M[d["slug"]]["html"]}</div>
  <p class="intro">{esc(d["lema"])} <span class="tenue">Ideal para: {esc(d["ideal"])}</span></p>
  <div class="acciones">
    <button class="btn" data-copiar-de="md">Copiar DESIGN.md</button>
    <button class="btn btn-claro" data-copiar-de="prompt">Copiar instrucción</button>
  </div>
  <p class="tenue peq">Pega primero el DESIGN.md en ChatGPT o Lovable y después la instrucción con lo que quieres. <a href="../../como-usar/">Paso a paso</a></p>
</section>

<section class="bloque">
  <h2>Colores</h2><p class="tenue peq">Toca un color para copiar su código.</p>
  <div class="muestras">{sw}</div>
</section>
<section class="bloque">
  <h2>Tipografía</h2>
  <div class="tipos" style="{vars_css(d)}">
    <div><small>Titulares · {esc(disp)}</small><p class="t-disp">Aa Bb Cc Ññ 123</p></div>
    <div><small>Texto · {esc(cuerpo_f)}</small><p class="t-cuerpo">El veloz murciélago hindú comía feliz cardillo y kiwi.</p></div>
    <div><small>Código · {esc(d["mono"])}</small><p class="t-mono">npx @google/design.md lint DESIGN.md</p></div>
  </div>
</section>
<section class="bloque">
  <h2>Instrucción para tu IA</h2>
  <pre class="codigo corto" id="prompt" tabindex="0" aria-label="Instrucción para tu IA">{esc(prompt)}</pre>
  <details class="archivo"><summary>Ver el archivo DESIGN.md completo (para técnicos)</summary>
  <div class="tit-sec"><span class="tenue peq">{len(md.splitlines())} líneas</span><span><button class="btn btn-peq" data-copiar-de="md">Copiar</button> <a class="btn btn-peq btn-claro" href="DESIGN.md" download="DESIGN.md">Descargar</a></span></div>
  <pre class="codigo" id="md" tabindex="0" aria-label="Archivo DESIGN.md completo">{esc(md)}</pre></details>
</section>
<nav class="pasos"><a href="../{ant["slug"]}/">← {esc(ant["nombre"])}</a><a href="../{sig["slug"]}/">{esc(sig["nombre"])} →</a></nav>
'''
  return md, pagina(f"{d['nombre']} — DESIGN.md gratis en español | {MARCA}",
                    f"{d['lema']} DESIGN.md gratuito para {d['ideal'].lower()} Cópialo y úsalo con Claude Code, Cursor o ChatGPT.",
                    cuerpo, "../../", familias(d))


def como_usar():
  pasos = [
    ("ChatGPT, Claude o Gemini (web o app del móvil)", "Elige un diseño y toca «Copiar DESIGN.md». Pégalo en el chat y, en el mismo mensaje o justo después, escribe lo que quieres: <em>«Crea una web para mi peluquería siguiendo este DESIGN.md, en un único archivo HTML»</em>. Si quieres retocar algo, pídelo con palabras normales: «botones más grandes», «añade un mapa»."),
    ("Lovable, Bolt, v0 y similares", "Pega el DESIGN.md en el primer mensaje o en el apartado de conocimiento o instrucciones del proyecto, y pide que lo respete en cada pantalla."),
    ("Claude Code / Codex / Gemini CLI (si programas)", "Guarda el archivo como <code>DESIGN.md</code> en la raíz del proyecto y escribe: <em>«Lee DESIGN.md y rediseña la página de inicio siguiéndolo»</em>. Para que lo tenga siempre presente, añade a tu CLAUDE.md o AGENTS.md la línea: <code>Sigue siempre DESIGN.md para cualquier decisión visual.</code>"),
    ("Cursor / Windsurf (si programas)", "Añade DESIGN.md al proyecto y menciónalo en el chat con <code>@DESIGN.md</code>. Si usas reglas, crea una en <code>.cursor/rules</code> que diga que toda la interfaz debe seguir DESIGN.md."),
  ]
  bloques = "".join(f'<div class="paso"><span class="num">{i:02d}</span><div><h3>{t}</h3><p>{p}</p></div></div>' for i, (t, p) in enumerate(pasos, 1))
  cuerpo = f'''
<section class="det-cab"><p class="eti">Guía</p><h1>Cómo usar un DESIGN.md</h1>
<p class="intro">Elige un diseño del catálogo, pégalo donde tu IA pueda leerlo y pídele que lo siga. Funciona igual desde el móvil que desde el ordenador. Busca abajo la herramienta que usas.</p></section>
<section class="bloque">{bloques}</section>
<section class="bloque"><h2>Consejos</h2><ul class="lista">
<li>Un DESIGN.md por proyecto. Si cambias de estilo, sustituye el archivo entero.</li>
<li>Personalízalo: cambia el color <code>primary</code> por el de tu marca y pide a la IA que ajuste el resto para mantener el contraste.</li>
<li>Si programas, valídalo con <code>npx @google/design.md lint DESIGN.md</code>.</li>
<li>Pide cambios en lenguaje normal: «haz los botones más grandes», «usa el acento solo en ofertas».</li>
</ul><a class="btn" href="../#catalogo">Elegir un diseño</a></section>
'''
  return pagina(f"Cómo usar un DESIGN.md con Claude Code, Cursor o ChatGPT | {MARCA}",
                "Guía en español para usar archivos DESIGN.md con Claude Code, Cursor, Codex, Gemini, ChatGPT, Lovable o v0.", cuerpo, "../")


def kits():
  bloques = ""
  for k in KITS:
    inc = "".join(f"<li>{x}</li>" for x in k["incluye"])
    bloques += f'''<article class="kit" id="{k["slug"]}">
  <p class="eti eti-acc">{k["nombre"]}</p>
  <h2>{k["sub"]}.</h2>
  <p>{k["llano"]}</p>
  <details class="tecnico"><summary>Detalles técnicos</summary><p>{k["detalle"]}</p><ul class="lista">{inc}</ul></details>
  <div class="precio"><strong>{k["precio"]}</strong><span class="tenue">precio previsto · pago único</span></div>
  <div class="acciones"><span class="btn btn-off" aria-disabled="true">Todavía no está a la venta</span></div>
</article>'''
  cuerpo = f'''
<section class="det-cab"><p class="eti">Kits de inicio · próximamente</p><h1>Empieza con el 80 % hecho.</h1>
<p class="intro">Webs y apps casi terminadas, preparadas para que tu IA las entienda a la primera. Tú le pides en español lo que quieres cambiar y el resultado es tuyo. Aún no están a la venta; mientras tanto, el <a href="../#catalogo">catálogo de diseños</a> es gratis.</p>
{HERRAMIENTAS}</section>
<section class="bloque kits">{bloques}</section>
<section class="bloque banda"><h2>¿Todo junto?</h2><p>Kit Web + Kit App + Pack de instrucciones: <strong>129 €</strong> previstos en el lanzamiento.</p><a class="btn" href="../#catalogo">Mientras, elige un diseño gratis</a></section>
'''
  return pagina(f"Kits de inicio para crear webs y apps con IA | {MARCA}",
                "Kits de inicio en español para crear webs y apps móviles con Claude Code, Cursor o Codex: plantillas, DESIGN.md, AGENTS.md y prompts.", cuerpo, "../")


def aviso_legal():
  cuerpo = f'''
<section class="det-cab"><p class="eti">Información</p><h1>Aviso legal y privacidad</h1></section>
<section class="bloque"><ul class="lista">
<li><strong>Titular:</strong> Jorge, creador de Cuadrantia (España), persona física responsable de esta web. Los datos fiscales completos se publicarán aquí antes de vender ningún kit.</li>
<li><strong>Contacto:</strong> a través de la tienda de Cuadrantia en <a href="https://payhip.com/Cuadrantia" rel="noopener">payhip.com/Cuadrantia</a>.</li>
<li><strong>Quién está detrás:</strong> {MARCA} es un proyecto de Cuadrantia, una marca española de plantillas digitales.</li>
<li><strong>Datos personales:</strong> esta web no tiene formularios, no usa cookies propias ni analítica y no guarda ningún dato tuyo. Las tipografías se cargan desde Google Fonts.</li>
<li><strong>Licencia de los diseños:</strong> puedes usar los DESIGN.md gratis en proyectos personales y comerciales. No está permitido revenderlos como producto propio.</li>
<li><strong>Kits:</strong> todavía no están a la venta; los precios mostrados son orientativos. Las condiciones de compra, devolución y licencia se publicarán con ellos.</li>
<li><strong>Marcas:</strong> Claude Code, Cursor, Codex, Gemini, ChatGPT, Lovable y v0 son marcas de sus respectivos dueños; no hay afiliación.</li>
</ul></section>
'''
  return pagina(f"Aviso legal y privacidad | {MARCA}", f"Quién está detrás de {MARCA} y cómo tratamos tus datos.", cuerpo, "../")


def main():
  if SALIDA.exists():
    for p in SALIDA.iterdir():
      if p.name not in ("assets", "analisis"):
        shutil.rmtree(p) if p.is_dir() else p.unlink()
  SALIDA.mkdir(exist_ok=True)
  (SALIDA / "index.html").write_text(portada())
  for ruta, f in [("como-usar", como_usar), ("kits", kits), ("aviso-legal", aviso_legal)]:
    (SALIDA / ruta).mkdir(parents=True, exist_ok=True)
    (SALIDA / ruta / "index.html").write_text(f())
  (SALIDA / "descargas").mkdir(exist_ok=True)
  catalogo = []
  with zipfile.ZipFile(SALIDA / "descargas" / "disenomd-catalogo.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for i, d in enumerate(DISENOS):
      md, pag = detalle(d, i)
      carpeta = SALIDA / "disenos" / d["slug"]
      carpeta.mkdir(parents=True, exist_ok=True)
      (carpeta / "DESIGN.md").write_text(md)
      (carpeta / "index.html").write_text(pag)
      z.writestr(f"{d['slug']}/DESIGN.md", md)
      catalogo.append(dict(slug=d["slug"], nombre=d["nombre"], categoria=d["categoria"], lema=d["lema"], colores=d["colores"]))
  with zipfile.ZipFile(SALIDA / "descargas" / "disenomd-webs.zip", "w", zipfile.ZIP_DEFLATED) as z:
    reales = AW.generar(SALIDA, pagina, z)
  (SALIDA / "webs").mkdir(exist_ok=True)
  (SALIDA / "webs" / "index.html").write_text(AW.zona(reales, pagina))
  catalogo += [dict(slug=x["slug"], nombre=x["nombre"], categoria="Webs populares", url=x["url"], colores=c) for x, c in reales]
  (SALIDA / "catalogo.json").write_text(json.dumps(catalogo, ensure_ascii=False, indent=1))
  (SALIDA / "manifest.webmanifest").write_text(json.dumps(dict(name=MARCA, short_name=MARCA, start_url="./", display="standalone",
    background_color="#0D0D0F", theme_color="#141414", lang="es",
    icons=[dict(src=f"assets/icono-{n}.png", sizes=f"{n}x{n}", type="image/png") for n in (192, 512)]), ensure_ascii=False))
  (SALIDA / ".nojekyll").write_text("")
  (SALIDA / "robots.txt").write_text("User-agent: *\nAllow: /\n")
  print(f"{len(DISENOS)} diseños y {len(AW.SITIOS)} análisis generados en {SALIDA}")


if __name__ == "__main__":
  main()
