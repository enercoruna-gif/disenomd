---
version: "alpha"
name: Typeform (análisis)
description: "Análisis independiente del estilo visual de Typeform (https://www.typeform.com/es/)."
colors:
  primary: "#A057BB"
  on-primary: "#FFFFFF"
  secondary: "#653C73"
  accent: "#83698C"
  background: "#FAF9FB"
  surface: "#FFFFFF"
  text: "#2A222B"
  muted: "#3C323E"
  border: "#DDDBDE"
typography:
  display-lg:
    fontFamily: Tobias
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Tobias
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Twklausanne 400
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Twklausanne 400
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 6px
  md: 12px
  lg: 24px
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

# Typeform: análisis de su estilo visual

> Análisis independiente de la portada pública de [Typeform](https://www.typeform.com/es/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fondo blanco, titular serif grande centrado y ejemplos de formularios en colores suaves.

Botones negros con esquinas suaves y una experiencia muy editorial.

## Colores

Fondo claro `#FAF9FB` con texto `#2A222B`. El color de acción es `#A057BB` (texto encima `#FFFFFF`); `#653C73` y `#83698C` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Tobias** (peso 400, unos 64px en escritorio) y texto en **Twklausanne 400** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 12px; los botones son rectángulos con radio 12px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#A057BB`).
- Haz: usa Tobias solo en titulares y deja el texto en Twklausanne 400.
- No hagas: copiar el logotipo, las fotografías o los textos de Typeform; crea los tuyos.
