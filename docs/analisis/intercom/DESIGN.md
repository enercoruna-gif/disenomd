---
version: "alpha"
name: Intercom (análisis)
description: "Análisis independiente del estilo visual de Intercom (https://www.intercom.com)."
colors:
  primary: "#0007CB"
  on-primary: "#FFFFFF"
  secondary: "#DF2020"
  accent: "#111111"
  background: "#FFFFFF"
  surface: "#FAF9F6"
  text: "#000000"
  muted: "#111111"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: Saans
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Saans
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: ui-sans-serif
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: ui-sans-serif
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

# Intercom: análisis de su estilo visual

> Análisis independiente de la portada pública de [Intercom](https://www.intercom.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Titular centrado enorme en sans fina que combina gris claro y negro, rodeado de fotografías recortadas en los márgenes.

Fondo blanco, texto en serif para el párrafo y botones rectangulares: uno negro sólido y otro con borde.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#0007CB` (texto encima `#FFFFFF`); `#DF2020` y `#111111` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Saans** (peso 400, unos 64px en escritorio) y texto en **ui-sans-serif** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 4px; los botones son rectángulos con radio 4px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#0007CB`).
- Haz: usa Saans solo en titulares y deja el texto en ui-sans-serif.
- No hagas: copiar el logotipo, las fotografías o los textos de Intercom; crea los tuyos.
