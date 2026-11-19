---
version: "alpha"
name: Antimetal (análisis)
description: "Análisis independiente del estilo visual de Antimetal (https://antimetal.com)."
colors:
  primary: "#D77435"
  on-primary: "#000000"
  secondary: "#C35E49"
  accent: "#D28C7B"
  background: "#F5F6F1"
  surface: "#ECEDE8"
  text: "#1A1614"
  muted: "#676461"
  border: "#D6D7D2"
typography:
  display-lg:
    fontFamily: signifier
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: signifier
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: GeistSans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: GeistSans
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 10px
  md: 20px
  lg: 40px
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

# Antimetal: análisis de su estilo visual

> Análisis independiente de la portada pública de [Antimetal](https://antimetal.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fondo hueso casi blanco con titular centrado en serif fina y un único botón negro en píldora.

Debajo, una ventana de producto oscura con texto monoespaciado; el contraste entre papel claro y terminal oscura es todo el estilo.

## Colores

Fondo claro `#F5F6F1` con texto `#1A1614`. El color de acción es `#D77435` (texto encima `#000000`); `#C35E49` y `#D28C7B` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **signifier** (peso 400, unos 51.0272px en escritorio) y texto en **GeistSans** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 20px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#D77435`).
- Haz: usa signifier solo en titulares y deja el texto en GeistSans.
- No hagas: copiar el logotipo, las fotografías o los textos de Antimetal; crea los tuyos.
