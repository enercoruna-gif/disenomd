---
version: "alpha"
name: Uber (análisis)
description: "Análisis independiente del estilo visual de Uber (https://www.uber.com/es/es/)."
colors:
  primary: "#111111"
  on-primary: "#FFFFFF"
  secondary: "#080808"
  accent: "#525252"
  background: "#FFFFFF"
  surface: "#F6F6F6"
  text: "#000000"
  muted: "#111111"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: UberMove
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: UberMove
    fontSize: 1.75rem
    fontWeight: 600
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

# Uber: análisis de su estilo visual

> Análisis independiente de la portada pública de [Uber](https://www.uber.com/es/es/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Negro y blanco absoluto, titulares gruesos y formularios de origen y destino.

Botones negros rectangulares con poco radio y fotografía de ciudad.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#111111` (texto encima `#FFFFFF`); `#080808` y `#525252` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **UberMove** (peso 700, unos 52px en escritorio) y texto en **Inter** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#111111`).
- Haz: usa UberMove solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Uber; crea los tuyos.
