---
version: "alpha"
name: Loom (análisis)
description: "Análisis independiente del estilo visual de Loom (https://www.loom.com)."
colors:
  primary: "#1868DB"
  on-primary: "#FFFFFF"
  secondary: "#FFAB00"
  accent: "#FFC44C"
  background: "#FFFFFF"
  surface: "#E9F2FE"
  text: "#000000"
  muted: "#101214"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: Charlie Display
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Charlie Display
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Charlie Text
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Charlie Text
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 2px
  md: 4px
  lg: 8px
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
    textColor: "{colors.text}"
  tag:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.text}"
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

# Loom: análisis de su estilo visual

> Análisis independiente de la portada pública de [Loom](https://www.loom.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Blanco con azul vivo de marca, titular centrado y miniaturas de vídeo como prueba del producto.

Botones en píldora azules y tarjetas con esquinas medianas.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#1868DB` (texto encima `#FFFFFF`); `#FFAB00` y `#FFC44C` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Charlie Display** (peso 700, unos 56.5385px en escritorio) y texto en **Charlie Text** a 16px. Si esa fuente no está disponible, usa **Source Serif 4** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 4px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#1868DB`).
- Haz: usa Charlie Display solo en titulares y deja el texto en Charlie Text.
- No hagas: copiar el logotipo, las fotografías o los textos de Loom; crea los tuyos.
