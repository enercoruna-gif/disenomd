---
version: "alpha"
name: Revolut (análisis)
description: "Análisis independiente del estilo visual de Revolut (https://www.revolut.com/es-ES/)."
colors:
  primary: "#1F1F1F"
  on-primary: "#FFFFFF"
  secondary: "#101010"
  accent: "#F4F4F4"
  background: "#FFFFFF"
  surface: "#F7F7F7"
  text: "#000000"
  muted: "#1F1F1F"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: Aeonik Pro
    fontSize: 3rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Aeonik Pro
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

# Revolut: análisis de su estilo visual

> Análisis independiente de la portada pública de [Revolut](https://www.revolut.com/es-ES/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Azul de marca con fotografía de estilo de vida y titulares blancos enormes.

Botones en píldora blancos, tarjetas redondeadas y contraste alto.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#1F1F1F` (texto encima `#FFFFFF`); `#101010` y `#F4F4F4` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Aeonik Pro** (peso 500, unos 84.6578px en escritorio) y texto en **Inter** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 20px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#1F1F1F`).
- Haz: usa Aeonik Pro solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Revolut; crea los tuyos.
