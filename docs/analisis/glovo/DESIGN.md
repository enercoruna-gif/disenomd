---
version: "alpha"
name: Glovo (análisis)
description: "Análisis independiente del estilo visual de Glovo (https://glovoapp.com/es/es/)."
colors:
  primary: "#017963"
  on-primary: "#FFFFFF"
  secondary: "#FFC042"
  accent: "#035949"
  background: "#FFFFFF"
  surface: "#F9EFDC"
  text: "#000000"
  muted: "#161617"
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
    fontFamily: Glovo Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Glovo Sans
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

# Glovo: análisis de su estilo visual

> Análisis independiente de la portada pública de [Glovo](https://glovoapp.com/es/es/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Amarillo intenso de fondo, ilustraciones 3D de comida y un buscador de dirección central.

Titulares en verde oscuro, botones en píldora verdes y tono desenfadado.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#017963` (texto encima `#FFFFFF`); `#FFC042` y `#035949` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Inter** (peso 700, unos ? en escritorio) y texto en **Glovo Sans** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#017963`).
- Haz: usa Inter solo en titulares y deja el texto en Glovo Sans.
- No hagas: copiar el logotipo, las fotografías o los textos de Glovo; crea los tuyos.
