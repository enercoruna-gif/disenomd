---
version: "alpha"
name: Twitch (análisis)
description: "Análisis independiente del estilo visual de Twitch (https://www.twitch.tv)."
colors:
  primary: "#9147FF"
  on-primary: "#FFFFFF"
  secondary: "#EB0400"
  accent: "#5C16C5"
  background: "#F7F7F8"
  surface: "#EFEFF1"
  text: "#0E0E10"
  muted: "#3B3B44"
  border: "#D6D6D8"
typography:
  display-lg:
    fontFamily: Roobert
    fontSize: 3rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Roobert
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
  sm: 3px
  md: 6px
  lg: 12px
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

# Twitch: análisis de su estilo visual

> Análisis independiente de la portada pública de [Twitch](https://www.twitch.tv), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Morado de marca con miniaturas de directos en rejilla densa y fondo gris muy claro.

Etiquetas rojas de «en directo», tarjetas pequeñas y mucha información.

## Colores

Fondo claro `#F7F7F8` con texto `#0E0E10`. El color de acción es `#9147FF` (texto encima `#FFFFFF`); `#EB0400` y `#5C16C5` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Roobert** (peso 500, unos 18px en escritorio) y texto en **Inter** a 14px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 6px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#9147FF`).
- Haz: usa Roobert solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Twitch; crea los tuyos.
