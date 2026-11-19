---
version: "alpha"
name: DJI (análisis)
description: "Análisis independiente del estilo visual de DJI (https://www.dji.com/es)."
colors:
  primary: "#0070D5"
  on-primary: "#FFFFFF"
  secondary: "#0060E7"
  accent: "#4C90EE"
  background: "#FFFFFF"
  surface: "#EDEDED"
  text: "#000000"
  muted: "#303233"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Open Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Open Sans
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
    rounded: "{rounded.full}"
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
    textColor: "{colors.text}"
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

# DJI: análisis de su estilo visual

> Análisis independiente de la portada pública de [DJI](https://www.dji.com/es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fotografía de producto a pantalla completa con el nombre del modelo en sans fina blanca centrada.

Azul corporativo en el botón de tienda, botones con borde fino en píldora y rejilla de tarjetas grises debajo.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#0070D5` (texto encima `#FFFFFF`); `#0060E7` y `#4C90EE` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Inter** (peso 700, unos ? en escritorio) y texto en **Open Sans** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 4px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#0070D5`).
- Haz: usa Inter solo en titulares y deja el texto en Open Sans.
- No hagas: copiar el logotipo, las fotografías o los textos de DJI; crea los tuyos.
