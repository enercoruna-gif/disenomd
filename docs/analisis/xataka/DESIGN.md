---
version: "alpha"
name: Xataka (análisis)
description: "Análisis independiente del estilo visual de Xataka (https://www.xataka.com)."
colors:
  primary: "#38880A"
  on-primary: "#000000"
  secondary: "#9CC484"
  accent: "#6D8A5F"
  background: "#000409"
  surface: "#1C2631"
  text: "#FFFFFF"
  muted: "#378708"
  border: "#24272B"
typography:
  display-lg:
    fontFamily: Tofino Narrow
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Tofino Narrow
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Tofino
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Tofino
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.md}"
    padding: 12px 20px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: 24px
  link:
    backgroundColor: "{colors.background}"
    textColor: "{colors.secondary}"
  tag:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: 2px 10px
  caption:
    backgroundColor: "{colors.background}"
    textColor: "{colors.muted}"
    typography: "{typography.label-sm}"
  divider:
    backgroundColor: "{colors.border}"
    height: 1px
---

# Xataka: análisis de su estilo visual

> Análisis independiente de la portada pública de [Xataka](https://www.xataka.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fondo oscuro de portada con logotipo verde y rejilla densa de noticias tecnológicas.

Titulares en sans condensada, etiquetas de sección y mucha imagen.

## Colores

Fondo oscuro `#000409` con texto `#FFFFFF`. El color de acción es `#38880A` (texto encima `#000000`); `#9CC484` y `#6D8A5F` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Tofino Narrow** (peso 700, unos 40px en escritorio) y texto en **Tofino** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#38880A`).
- Haz: usa Tofino Narrow solo en titulares y deja el texto en Tofino.
- No hagas: copiar el logotipo, las fotografías o los textos de Xataka; crea los tuyos.
