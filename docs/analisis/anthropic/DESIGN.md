---
version: "alpha"
name: Anthropic (análisis)
description: "Análisis independiente del estilo visual de Anthropic (https://www.anthropic.com)."
colors:
  primary: "#141413"
  on-primary: "#FFFFFF"
  secondary: "#141413"
  accent: "#595957"
  background: "#FAF9F5"
  surface: "#F5F4ED"
  text: "#141413"
  muted: "#5E5D59"
  border: "#DAD9D5"
typography:
  display-lg:
    fontFamily: anthropicSerif
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: anthropicSerif
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: anthropicSans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: anthropicSans
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 5px
  md: 10px
  lg: 20px
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
    rounded: "{rounded.full}"
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

# Anthropic: análisis de su estilo visual

> Análisis independiente de la portada pública de [Anthropic](https://www.anthropic.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fondo crema cálido, titulares en serif y texto en sans: parece una editorial más que una tecnológica.

Paleta de tierra y negro suave, botones en píldora y casi ningún color saturado.

## Colores

Fondo claro `#FAF9F5` con texto `#141413`. El color de acción es `#141413` (texto encima `#FFFFFF`); `#141413` y `#595957` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **anthropicSerif** (peso 400, unos 38.3791px en escritorio) y texto en **anthropicSans** a 16.5817px. Si esa fuente no está disponible, usa **Source Serif 4** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 10px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#141413`).
- Haz: usa anthropicSerif solo en titulares y deja el texto en anthropicSans.
- No hagas: copiar el logotipo, las fotografías o los textos de Anthropic; crea los tuyos.
