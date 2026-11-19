---
version: "alpha"
name: OpenAI (análisis)
description: "Análisis independiente del estilo visual de OpenAI (https://openai.com/es-ES/)."
colors:
  primary: "#000000"
  on-primary: "#FFFFFF"
  secondary: "#000000"
  accent: "#4C4C4C"
  background: "#FFFFFF"
  surface: "#F5F5F5"
  text: "#000000"
  muted: "#595959"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: OpenAI Sans
    fontSize: 3rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: OpenAI Sans
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: OpenAI Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: OpenAI Sans
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 20px
  md: 40px
  lg: 80px
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

# OpenAI: análisis de su estilo visual

> Análisis independiente de la portada pública de [OpenAI](https://openai.com/es-ES/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Portada sobria y blanca con buscador central y tarjetas de imagen grandes y suaves.

Tipografía propia neutra, casi sin color de interfaz y botones negros en píldora.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#000000` (texto encima `#FFFFFF`); `#000000` y `#4C4C4C` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **OpenAI Sans** (peso 500, unos 17.6995px en escritorio) y texto en **OpenAI Sans** a 17px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 40px; los botones son rectángulos con radio 40px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#000000`).
- Haz: usa OpenAI Sans solo en titulares y deja el texto en OpenAI Sans.
- No hagas: copiar el logotipo, las fotografías o los textos de OpenAI; crea los tuyos.
