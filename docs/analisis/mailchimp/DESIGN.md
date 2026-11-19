---
version: "alpha"
name: Mailchimp (análisis)
description: "Análisis independiente del estilo visual de Mailchimp (https://mailchimp.com/es/)."
colors:
  primary: "#FFE01B"
  on-primary: "#000000"
  secondary: "#80700E"
  accent: "#A69B56"
  background: "#FFFFFF"
  surface: "#F5F5F5"
  text: "#000000"
  muted: "#231E15"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: Means Web
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Means Web
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Tally
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Tally
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 13px
  md: 26px
  lg: 52px
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

# Mailchimp: análisis de su estilo visual

> Análisis independiente de la portada pública de [Mailchimp](https://mailchimp.com/es/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Amarillo cavendish de marca, titulares en serif propia con una palabra en cursiva y fotografía cálida.

Botones con borde negro y fondo amarillo; tono cercano y humano.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#FFE01B` (texto encima `#000000`); `#80700E` y `#A69B56` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Means Web** (peso 400, unos 64px en escritorio) y texto en **Tally** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 26px; los botones son rectángulos con radio 26px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#FFE01B`).
- Haz: usa Means Web solo en titulares y deja el texto en Tally.
- No hagas: copiar el logotipo, las fotografías o los textos de Mailchimp; crea los tuyos.
