---
version: "alpha"
name: Apple (análisis)
description: "Análisis independiente del estilo visual de Apple (https://www.apple.com/es/)."
colors:
  primary: "#822704"
  on-primary: "#FFFFFF"
  secondary: "#0071E3"
  accent: "#F5F5F7"
  background: "#FFFFFF"
  surface: "#F5F5F7"
  text: "#000000"
  muted: "#1D1D1F"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: SF Pro Display
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: SF Pro Display
    fontSize: 1.75rem
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: SF Pro Text
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: SF Pro Text
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 5px
  md: 11px
  lg: 22px
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

# Apple: análisis de su estilo visual

> Análisis independiente de la portada pública de [Apple](https://www.apple.com/es/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Bloques a pantalla completa alternando negro y gris muy claro, cada uno con un producto y un titular corto centrado.

Tipografía de sistema muy pulida, enlaces azules en lugar de botones y fotografía de producto como protagonista.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#822704` (texto encima `#FFFFFF`); `#0071E3` y `#F5F5F7` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **SF Pro Display** (peso 600, unos 56px en escritorio) y texto en **SF Pro Text** a 17px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 11px; los botones son rectángulos con radio 11px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#822704`).
- Haz: usa SF Pro Display solo en titulares y deja el texto en SF Pro Text.
- No hagas: copiar el logotipo, las fotografías o los textos de Apple; crea los tuyos.
