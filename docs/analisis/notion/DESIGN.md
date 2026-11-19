---
version: "alpha"
name: Notion (análisis)
description: "Análisis independiente del estilo visual de Notion (https://www.notion.com/es)."
colors:
  primary: "#0075DE"
  on-primary: "#000000"
  secondary: "#003A6F"
  accent: "#4C759A"
  background: "#FFFFFF"
  surface: "#F6F5F4"
  text: "#000000"
  muted: "#0075DE"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: NotionInter
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: NotionInter
    fontSize: 1.75rem
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: NotionInter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: NotionInter
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
    textColor: "{colors.background}"
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

# Notion: análisis de su estilo visual

> Análisis independiente de la portada pública de [Notion](https://www.notion.com/es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Blanco con ilustraciones de trazo negro, titular grande y acentos de color puntuales.

Botones pequeños azules y negros, iconografía de línea y mucho aire.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#0075DE` (texto encima `#000000`); `#003A6F` y `#4C759A` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **NotionInter** (peso 600, unos 96px en escritorio) y texto en **NotionInter** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#0075DE`).
- Haz: usa NotionInter solo en titulares y deja el texto en NotionInter.
- No hagas: copiar el logotipo, las fotografías o los textos de Notion; crea los tuyos.
