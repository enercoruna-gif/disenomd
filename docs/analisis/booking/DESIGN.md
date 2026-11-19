---
version: "alpha"
name: Booking.com (análisis)
description: "Análisis independiente del estilo visual de Booking.com (https://www.booking.com/index.es.html)."
colors:
  primary: "#003B95"
  on-primary: "#FFFFFF"
  secondary: "#FFB700"
  accent: "#003B95"
  background: "#FFFFFF"
  surface: "#F5F5F5"
  text: "#1A1A1A"
  muted: "#006CE4"
  border: "#DFDFDF"
typography:
  display-lg:
    fontFamily: Avenir Next
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Avenir Next
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
    textColor: "{colors.text}"
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

# Booking.com: análisis de su estilo visual

> Análisis independiente de la portada pública de [Booking.com](https://www.booking.com/index.es.html), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Azul intenso en la cabecera con un buscador amarillo muy visible: todo empuja a buscar fechas.

Alta densidad de información, tarjetas pequeñas y etiquetas de oferta en verde y amarillo.

## Colores

Fondo claro `#FFFFFF` con texto `#1A1A1A`. El color de acción es `#003B95` (texto encima `#FFFFFF`); `#FFB700` y `#003B95` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Avenir Next** (peso 700, unos 24px en escritorio) y texto en **Inter** a 14px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#003B95`).
- Haz: usa Avenir Next solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Booking.com; crea los tuyos.
