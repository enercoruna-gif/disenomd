---
version: "alpha"
name: Trello (análisis)
description: "Análisis independiente del estilo visual de Trello (https://trello.com/es)."
colors:
  primary: "#0065FF"
  on-primary: "#FFFFFF"
  secondary: "#0052CC"
  accent: "#0052CC"
  background: "#FFFFFF"
  surface: "#F4F5F7"
  text: "#091E42"
  muted: "#172B4D"
  border: "#DDDFE5"
typography:
  display-lg:
    fontFamily: Charlie Display
    fontSize: 3rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Charlie Display
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Charlie Text
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Charlie Text
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

# Trello: análisis de su estilo visual

> Análisis independiente de la portada pública de [Trello](https://trello.com/es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Blanco con azul de marca, titular grande a la izquierda e ilustración del móvil con tarjetas.

Campo de correo con botón azul, formas redondeadas y tono optimista.

## Colores

Fondo claro `#FFFFFF` con texto `#091E42`. El color de acción es `#0065FF` (texto encima `#FFFFFF`); `#0052CC` y `#0052CC` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Charlie Display** (peso 500, unos 48px en escritorio) y texto en **Charlie Text** a 20px. Si esa fuente no está disponible, usa **Source Serif 4** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 4px; los botones son rectángulos con radio 4px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#0065FF`).
- Haz: usa Charlie Display solo en titulares y deja el texto en Charlie Text.
- No hagas: copiar el logotipo, las fotografías o los textos de Trello; crea los tuyos.
