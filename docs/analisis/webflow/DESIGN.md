---
version: "alpha"
name: Webflow (análisis)
description: "Análisis independiente del estilo visual de Webflow (https://webflow.com)."
colors:
  primary: "#146EF5"
  on-primary: "#FFFFFF"
  secondary: "#0E3B7E"
  accent: "#5676A5"
  background: "#FFFFFF"
  surface: "#F0F0F0"
  text: "#080808"
  muted: "#5E5E5E"
  border: "#DCDCDC"
typography:
  display-lg:
    fontFamily: WF Visual Sans Variable
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: WF Visual Sans Variable
    fontSize: 1.75rem
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: WF Visual Sans Variable
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: WF Visual Sans Variable
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

# Webflow: análisis de su estilo visual

> Análisis independiente de la portada pública de [Webflow](https://webflow.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Blanco con azul eléctrico de marca y capturas del editor visual en tarjetas.

Tipografía propia ancha, botones azules rectangulares y mucho detalle de producto.

## Colores

Fondo claro `#FFFFFF` con texto `#080808`. El color de acción es `#146EF5` (texto encima `#FFFFFF`); `#0E3B7E` y `#5676A5` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **WF Visual Sans Variable** (peso 600, unos 74.8571px en escritorio) y texto en **WF Visual Sans Variable** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#146EF5`).
- Haz: usa WF Visual Sans Variable solo en titulares y deja el texto en WF Visual Sans Variable.
- No hagas: copiar el logotipo, las fotografías o los textos de Webflow; crea los tuyos.
