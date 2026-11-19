---
version: "alpha"
name: Iberia (análisis)
description: "Análisis independiente del estilo visual de Iberia (https://www.iberia.com/es/)."
colors:
  primary: "#D7192D"
  on-primary: "#FFFFFF"
  secondary: "#A8191A"
  accent: "#B45556"
  background: "#EEEEEE"
  surface: "#FFFFFF"
  text: "#333333"
  muted: "#666666"
  border: "#D4D4D4"
typography:
  display-lg:
    fontFamily: iberiaheadline
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: iberiaheadline
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: verdana
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: verdana
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

# Iberia: análisis de su estilo visual

> Análisis independiente de la portada pública de [Iberia](https://www.iberia.com/es/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fotografía de destino a pantalla completa con buscador de vuelos superpuesto y rojo corporativo.

Tipografía funcional, precios grandes y botones rojos rectangulares.

## Colores

Fondo claro `#EEEEEE` con texto `#333333`. El color de acción es `#D7192D` (texto encima `#FFFFFF`); `#A8191A` y `#B45556` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **iberiaheadline** (peso 400, unos 60px en escritorio) y texto en **verdana** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 4px; los botones son rectángulos con radio 4px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#D7192D`).
- Haz: usa iberiaheadline solo en titulares y deja el texto en verdana.
- No hagas: copiar el logotipo, las fotografías o los textos de Iberia; crea los tuyos.
