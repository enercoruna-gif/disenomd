"""Genera los DESIGN.md y fichas de los análisis de webs reales a partir de src/analisis/*.json."""
import json
from html import escape as esc
from pathlib import Path
from notas_analisis import N

RAIZ = Path(__file__).resolve().parent.parent
SITIOS = json.loads((RAIZ / "src/sitios.json").read_text())
SERIF = ("serif", "times", "georgia", "majrit", "tiempos", "garamond", "playfair", "charlie", "tally")


def _lum(h):
  r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
  f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
  return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def con(a, b):
  x, y = sorted((_lum(a), _lum(b)), reverse=True)
  return (x + 0.05) / (y + 0.05)


def sat(h):
  r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
  return max(r, g, b) - min(r, g, b)


def mezcla(a, b, t):
  return "#" + "".join(f"{round(int(a[i:i + 2], 16) * (1 - t) + int(b[i:i + 2], 16) * t):02X}" for i in (1, 3, 5))


def hasta(color, fondo, tinta, minimo):
  t = 0.0
  while con(mezcla(color, tinta, t), fondo) < minimo and t < 1:
    t += 0.05
  return mezcla(color, tinta, min(t, 1))


def fam(nombre, por_defecto):
  n = (nombre or "").strip()
  return por_defecto if not n or n.lower() in ("sans-serif", "system-ui", "-apple-system", "blinkmacsystemfont", "times new roman") else n


def tokens(j):
  bg = j["fondo"]
  oscuro = _lum(bg) < 0.25
  textos = [t for t in j["textos"] if con(t, bg) >= 3] or (["#F5F5F5"] if oscuro else ["#141414"])
  text = max(textos[:3], key=lambda t: con(t, bg))
  if con(text, bg) < 7:
    text = hasta(text, bg, "#FFFFFF" if oscuro else "#000000", 7)
  muted = next((t for t in textos if t != text and con(t, bg) >= 4.5), mezcla(text, bg, 0.35))
  if con(muted, bg) < 4.5:
    muted = hasta(muted, bg, text, 4.5)
  cand = [c for c in ([j["boton"]["fondo"]] if j.get("boton") else []) + j["fondos"] + ([j["enlace"]] if j.get("enlace") else []) if c and c != bg]
  vivos = sorted({c for c in cand if sat(c) > 40}, key=lambda c: -sat(c))
  primary = next((c for c in cand if sat(c) > 40), None) or next((c for c in cand if con(c, bg) > 3), text)
  on = max(("#FFFFFF", "#000000", text, bg), key=lambda c: con(c, primary))
  if con(on, primary) < 4.5:
    primary = hasta(primary, on, "#000000" if on == "#FFFFFF" else "#FFFFFF", 4.5)
  secondary = next((c for c in vivos if c != primary), mezcla(primary, text, 0.5))
  accent = j.get("enlace") if j.get("enlace") and j["enlace"] not in (text, bg, primary) else (vivos[2] if len(vivos) > 2 else mezcla(secondary, bg, 0.3))
  mejor = max((text, bg, on), key=lambda t: con(t, accent))
  if con(mejor, accent) < 4.5:
    accent = hasta(accent, mejor, "#000000" if _lum(mejor) > 0.5 else "#FFFFFF", 4.5)
  claros = [c for c in j["fondos"] if c != bg and con(c, bg) < 1.6]
  surface = claros[0] if claros else mezcla(bg, text, 0.04)
  border = mezcla(bg, text, 0.14)
  return dict(primary=primary, **{"on-primary": on}, secondary=secondary, accent=accent, background=bg,
              surface=surface, text=text, muted=muted, border=border), oscuro


def radio(j):
  vals = [float(r[:-2]) for r in j["radios"] if r.endswith("px") and float(r[:-2]) < 60]
  md = int(sorted(vals)[len(vals) // 2]) if vals else 8
  boton = j.get("boton", {}) or {}
  pildora = boton.get("radio", "").endswith("px") and float(boton["radio"][:-2]) >= 40
  return dict(sm=f"{max(md // 2, 2)}px", md=f"{md}px", lg=f"{md * 2}px", full="9999px"), pildora


def design_md(s, j):
  c, oscuro = tokens(j)
  r, pildora = radio(j)
  h1 = j.get("h1") or {}
  serif = any(k in (h1.get("familia") or "").lower() for k in SERIF)
  disp = fam(h1.get("familia"), "Inter")
  cuerpo = fam(j["cuerpo"]["familia"], "Inter")
  alt_disp = "Source Serif 4" if serif else "Inter"
  pt = int(float(h1.get("peso") or 700))
  resumen, claves = N[s["slug"]]
  forma_boton = "píldoras" if pildora else "rectángulos con radio " + r["md"]
  y = ["---", 'version: "alpha"', f"name: {s['nombre']} (análisis)",
       f'description: "Análisis independiente del estilo visual de {s["nombre"]} ({s["url"]})."', "colors:"]
  y += [f'  {k}: "{v}"' for k, v in c.items()]
  y += ["typography:"]
  for n, f_, tam, w, lh, ls in [("display-lg", disp, "3rem", pt, "1.1", "-0.02em"), ("headline-md", disp, "1.75rem", max(pt - 100, 400), "1.2", "-0.01em"),
                                ("body-md", cuerpo, "1rem", 400, "1.6", "0em"), ("label-sm", cuerpo, "0.8125rem", 500, "1.3", "0.01em")]:
    y += [f"  {n}:", f"    fontFamily: {f_}", f"    fontSize: {tam}", f"    fontWeight: {w}", f"    lineHeight: {lh}", f"    letterSpacing: {ls}"]
  y += ["rounded:"] + [f"  {k}: {v}" for k, v in r.items()]
  y += ["spacing:", "  xs: 4px", "  sm: 8px", "  md: 16px", "  lg: 32px", "  xl: 64px", "components:",
        "  button-primary:", '    backgroundColor: "{colors.primary}"', '    textColor: "{colors.on-primary}"', '    typography: "{typography.label-sm}"',
        f'    rounded: "{{rounded.{"full" if pildora else "md"}}}"', "    padding: 12px 20px",
        "  card:", '    backgroundColor: "{colors.surface}"', '    textColor: "{colors.text}"', '    rounded: "{rounded.lg}"', "    padding: 24px",
        "  link:", '    backgroundColor: "{colors.background}"', '    textColor: "{colors.secondary}"' if con(c["secondary"], c["background"]) >= 4.5 else '    textColor: "{colors.text}"',
        "  tag:", '    backgroundColor: "{colors.accent}"', f'    textColor: "{{colors.{max(("text", "background", "on-primary"), key=lambda k: con(c[k], c["accent"]))}}}"', '    rounded: "{rounded.full}"', "    padding: 2px 10px",
        "  caption:", '    backgroundColor: "{colors.background}"', '    textColor: "{colors.muted}"', '    typography: "{typography.label-sm}"',
        "  divider:", '    backgroundColor: "{colors.border}"', "    height: 1px", "---", "",
        f"# {s['nombre']}: análisis de su estilo visual", "",
        f"> Análisis independiente de la portada pública de [{s['nombre']}]({s['url']}), hecho por {'diseño.md'} el 19 de noviembre de 2026. "
        "No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.", "",
        "## Resumen", "", resumen, "", claves, "",
        "## Colores", "", f"Fondo {'oscuro' if oscuro else 'claro'} `{c['background']}` con texto `{c['text']}`. "
        f"El color de acción es `{c['primary']}` (texto encima `{c['on-primary']}`); `{c['secondary']}` y `{c['accent']}` aparecen en detalles y etiquetas.", "",
        "## Tipografía", "", f"Titulares en **{disp}** (peso {pt}, unos {h1.get('tam', '?')} en escritorio) y texto en **{cuerpo}** a {j['cuerpo']['tam']}. "
        f"Si esa fuente no está disponible, usa **{alt_disp}** como alternativa libre de Google Fonts.", "",
        "## Formas y espaciado", "", f"Radio habitual de {r['md']}; los botones son {forma_boton}. "
        "Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.", "",
        "## Qué hacer y qué no", "", f"- Haz: respeta la jerarquía de un solo color de acción (`{c['primary']}`).",
        f"- Haz: usa {disp if disp != 'Inter' else alt_disp} solo en titulares y deja el texto en {cuerpo}.",
        f"- No hagas: copiar el logotipo, las fotografías o los textos de {s['nombre']}; crea los tuyos.", ""]
  return "\n".join(y), c


GRUPOS = {
  "Finanzas": ["Banca", "Pagos"],
  "Software y productividad": ["Software", "Productividad", "Gestión", "Recursos humanos", "Colaboración", "Formularios", "Agenda",
                               "Atención al cliente", "Comunicación", "Almacenamiento", "Bases de datos", "Analítica", "Marketing"],
  "Desarrollo e IA": ["Desarrollo", "Inteligencia artificial"],
  "Diseño y creatividad": ["Diseño", "Animación", "Vídeo", "Publicación"],
  "Tiendas y consumo": ["Moda", "Deporte", "Hogar", "Comercio", "Supermercado", "Tecnología", "Reparto"],
  "Viajes y movilidad": ["Viajes", "Movilidad", "Aerolínea"],
  "Medios y ocio": ["Música", "Prensa", "Streaming", "Comunidad", "Educación"],
}
GRUPO = {sec: g for g, secs in GRUPOS.items() for sec in secs}


def tarjeta(s, c, prefijo):
  sw = "".join(f'<i style="background:{c[k]}"></i>' for k in ("primary", "secondary", "accent", "text", "background"))
  txt = esc(f"{s['nombre']} {s['sector']} web real análisis {N[s['slug']][0]}".lower())
  return (f'<a class="tarjeta tarjeta-foto" href="{prefijo}analisis/{s["slug"]}/" data-cat="{esc(GRUPO[s["sector"]])}" data-texto="{txt}">'
          f'<img src="{prefijo}analisis/{s["slug"]}/captura.webp" alt="Captura de la portada de {esc(s["nombre"])}" loading="lazy" width="960" height="600">'
          f'<div class="tarjeta-pie"><div><strong>{esc(s["nombre"])}</strong><small>{esc(s["sector"])}</small></div><span class="sw">{sw}</span></div></a>')


def ficha(s, md, c, pagina):
  sw = "".join(f'<div class="color"><i style="background:{v}"></i><b>{k}</b><code>{v}</code></div>' for k, v in c.items())
  resumen, claves = N[s["slug"]]
  prompt = (f"Crea [describe aquí tu web]. Usa el DESIGN.md que te he pasado (análisis del estilo de {s['nombre']}) como referencia visual: "
            "aplica sus colores, tipografías, radios y componentes, pero con mis textos, mi logotipo y mis imágenes.")
  cuerpo = f'''
<section class="det-cab">
  <p class="migas"><a href="../../webs/">Webs populares</a> / {esc(s["nombre"])}</p>
  <p class="eti">Análisis de web real · {esc(s["sector"])}</p>
  <h1>{esc(s["nombre"])}</h1>
  <img class="captura" src="captura.webp" alt="Captura propia de la portada de {esc(s["nombre"])}" width="960" height="600">
  <p class="intro">{esc(resumen)} {esc(claves)}</p>
  <div class="acciones"><button class="btn" data-copiar-de="md">Copiar DESIGN.md</button><button class="btn btn-claro" data-copiar-de="prompt">Copiar instrucción</button></div>
  <p class="tenue peq">Captura hecha por nosotros el 19-11-2026 en <a href="{esc(s["url"])}" rel="noopener nofollow">{esc(s["url"])}</a>. Análisis independiente, sin afiliación con {esc(s["nombre"])}.</p>
</section>
<section class="bloque"><h2>Colores extraídos</h2><div class="colores">{sw}</div></section>
<section class="bloque">
  <h2>Instrucción para tu IA</h2>
  <pre class="codigo corto" id="prompt" tabindex="0" aria-label="Instrucción para tu IA">{esc(prompt)}</pre>
  <details class="archivo"><summary>Ver el archivo DESIGN.md completo (para técnicos)</summary>
  <div class="tit-sec"><span class="tenue peq">{len(md.splitlines())} líneas</span><span><button class="btn btn-peq" data-copiar-de="md">Copiar</button> <a class="btn btn-peq btn-claro" href="DESIGN.md" download="DESIGN.md">Descargar</a></span></div>
  <pre class="codigo" id="md" tabindex="0" aria-label="Archivo DESIGN.md completo">{esc(md)}</pre></details>
</section>'''
  return pagina(f"{s['nombre']}: análisis de su estilo en DESIGN.md | diseño.md",
                f"Análisis independiente del estilo visual de {s['nombre']} en formato DESIGN.md, gratis y en español.", cuerpo, "../../")


def generar(salida, pagina, z):
  tarjetas = []
  for s in SITIOS:
    j = json.loads((RAIZ / "src/analisis" / f"{s['slug']}.json").read_text())
    md, c = design_md(s, j)
    carpeta = salida / "analisis" / s["slug"]
    carpeta.mkdir(parents=True, exist_ok=True)
    (carpeta / "DESIGN.md").write_text(md)
    (carpeta / "index.html").write_text(ficha(s, md, c, pagina))
    z.writestr(f"{s['slug']}/DESIGN.md", md)
    tarjetas.append((s, c))
  return tarjetas


def zona(tarjetas, pagina):
  html = "\n".join(tarjeta(s, c, "../") for s, c in tarjetas)
  chips = '<button class="chip activo" data-filtro="">Todas</button>' + "".join(f'<button class="chip" data-filtro="{esc(g)}">{esc(g)}</button>' for g in GRUPOS)
  cuerpo = f'''
<section class="hero">
  <p class="eti">Webs populares</p>
  <h1>DESIGN.md gratis de webs que ya conoces</h1>
  <p class="intro">{len(tarjetas)} análisis independientes del estilo de webs conocidas: colores, tipografías y componentes en formato DESIGN.md, con capturas hechas por nosotros. Úsalos como referencia para tu IA, con tus textos, tu logotipo y tus fotos.</p>
  <p><a class="btn btn-claro btn-peq" href="../descargas/disenomd-webs.zip" download>Descargar los {len(tarjetas)} DESIGN.md (zip)</a> <a class="btn btn-peq" href="../#catalogo">Ver los estilos originales</a></p>
</section>
<section class="bloque" id="catalogo">
  <input class="buscar" id="buscar" type="search" placeholder="Busca una web o un sector: banca, viajes, moda…" aria-label="Buscar webs">
  <div class="chips" id="chips">{chips}</div>
  <p class="vacio" id="vacio" hidden>Ninguna web coincide con «<span id="vacio-q"></span>». Prueba con otro nombre o sector.</p>
  <div class="rejilla" id="rejilla">{html}</div>
  <p class="tenue peq">Análisis propios y sin afiliación: los nombres y marcas son de sus dueños y solo se citan para identificar la web analizada.</p>
</section>'''
  return pagina("DESIGN.md gratis de webs populares en español | diseño.md",
                f"{len(tarjetas)} análisis independientes del estilo de webs conocidas en formato DESIGN.md, gratis y en español.", cuerpo, "../")
