---
version: "alpha"
name: IKEA (análisis)
description: "Análisis independiente del estilo visual de IKEA (https://www.ikea.com/es/es/)."
colors:
  primary: "#CA5008"
  on-primary: "#000000"
  secondary: "#FFDB00"
  accent: "#484848"
  background: "#FFFFFF"
  surface: "#F5F5F5"
  text: "#111111"
  muted: "#484848"
  border: "#DEDEDE"
typography:
  display-lg:
    fontFamily: Omani Rial
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Omani Rial
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Omani Rial
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Omani Rial
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

# IKEA: análisis de su estilo visual

> Análisis independiente de la portada pública de [IKEA](https://www.ikea.com/es/es/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Azul y amarillo de marca solo en el logo y detalles; el resto es blanco con fotografía de hogar.

Chips redondeados para categorías, botones negros en píldora y textos cortos.

## Colores

Fondo claro `#FFFFFF` con texto `#111111`. El color de acción es `#CA5008` (texto encima `#000000`); `#FFDB00` y `#484848` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Omani Rial** (peso 700, unos 24px en escritorio) y texto en **Omani Rial** a 14px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#CA5008`).
- Haz: usa Omani Rial solo en titulares y deja el texto en Omani Rial.
- No hagas: copiar el logotipo, las fotografías o los textos de IKEA; crea los tuyos.
