---
version: "alpha"
name: Medium (análisis)
description: "Análisis independiente del estilo visual de Medium (https://medium.com)."
colors:
  primary: "#191919"
  on-primary: "#FFFFFF"
  secondary: "#0C0C0C"
  accent: "#242424"
  background: "#FFFFFF"
  surface: "#F7F4ED"
  text: "#000000"
  muted: "#6B6B6B"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: gt-super
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: gt-super
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Inter
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

# Medium: análisis de su estilo visual

> Análisis independiente de la portada pública de [Medium](https://medium.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Crema cálido, titular serif gigante y una ilustración verde de trazo libre.

Botón negro en píldora y mucha tipografía: es una web para leer.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#191919` (texto encima `#FFFFFF`); `#0C0C0C` y `#242424` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **gt-super** (peso 400, unos 120px en escritorio) y texto en **Inter** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#191919`).
- Haz: usa gt-super solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Medium; crea los tuyos.
