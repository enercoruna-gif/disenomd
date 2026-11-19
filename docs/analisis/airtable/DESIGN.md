---
version: "alpha"
name: Airtable (análisis)
description: "Análisis independiente del estilo visual de Airtable (https://www.airtable.com)."
colors:
  primary: "#912E1F"
  on-primary: "#FFFFFF"
  secondary: "#542622"
  accent: "#876764"
  background: "#FFFFFF"
  surface: "#F0F6FF"
  text: "#181D26"
  muted: "#333840"
  border: "#DFDFE1"
typography:
  display-lg:
    fontFamily: Haas
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Haas
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Haas Groot Disp
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Haas Groot Disp
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

# Airtable: análisis de su estilo visual

> Análisis independiente de la portada pública de [Airtable](https://www.airtable.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Portada corporativa centrada, con titular grande en una sans neutra y dos botones: uno sólido casi negro y otro con borde.

Mucho blanco, tipografía de un solo peso y color solo en ilustraciones de producto.

## Colores

Fondo claro `#FFFFFF` con texto `#181D26`. El color de acción es `#912E1F` (texto encima `#FFFFFF`); `#542622` y `#876764` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Haas** (peso 400, unos 40px en escritorio) y texto en **Haas Groot Disp** a 20px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 12px; los botones son rectángulos con radio 12px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#912E1F`).
- Haz: usa Haas solo en titulares y deja el texto en Haas Groot Disp.
- No hagas: copiar el logotipo, las fotografías o los textos de Airtable; crea los tuyos.
