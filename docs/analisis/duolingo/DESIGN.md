---
version: "alpha"
name: Duolingo (análisis)
description: "Análisis independiente del estilo visual de Duolingo (https://es.duolingo.com)."
colors:
  primary: "#1CB0F6"
  on-primary: "#000000"
  secondary: "#347EA0"
  accent: "#71A5BC"
  background: "#FFFFFF"
  surface: "#F8F8F8"
  text: "#4B4B4B"
  muted: "#747474"
  border: "#E6E6E6"
typography:
  display-lg:
    fontFamily: duolingo-sans
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: duolingo-sans
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

# Duolingo: análisis de su estilo visual

> Análisis independiente de la portada pública de [Duolingo](https://es.duolingo.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Verde lima, personajes ilustrados y botones con relieve inferior que parecen de juego.

Tipografía redondeada muy gruesa y mucho blanco alrededor de un único mensaje.

## Colores

Fondo claro `#FFFFFF` con texto `#4B4B4B`. El color de acción es `#1CB0F6` (texto encima `#000000`); `#347EA0` y `#71A5BC` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **duolingo-sans** (peso 700, unos 32px en escritorio) y texto en **Inter** a 17px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#1CB0F6`).
- Haz: usa duolingo-sans solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Duolingo; crea los tuyos.
