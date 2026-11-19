---
version: "alpha"
name: Resend (análisis)
description: "Análisis independiente del estilo visual de Resend (https://resend.com)."
colors:
  primary: "#FFFFFF"
  on-primary: "#000000"
  secondary: "#FFFFFF"
  accent: "#B2B2B2"
  background: "#000000"
  surface: "#0B0E14"
  text: "#FFFFFF"
  muted: "#A1A4A5"
  border: "#242424"
typography:
  display-lg:
    fontFamily: domaine
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: domaine
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter Website
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Inter Website
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

# Resend: análisis de su estilo visual

> Análisis independiente de la portada pública de [Resend](https://resend.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Negro total con una ilustración 3D en cristal y titular serif blanco.

Estética de herramienta para desarrolladores: bordes finos grises y botones blancos.

## Colores

Fondo oscuro `#000000` con texto `#FFFFFF`. El color de acción es `#FFFFFF` (texto encima `#000000`); `#FFFFFF` y `#B2B2B2` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **domaine** (peso 400, unos 96px en escritorio) y texto en **Inter Website** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#FFFFFF`).
- Haz: usa domaine solo en titulares y deja el texto en Inter Website.
- No hagas: copiar el logotipo, las fotografías o los textos de Resend; crea los tuyos.
