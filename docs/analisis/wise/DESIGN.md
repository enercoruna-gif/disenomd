---
version: "alpha"
name: Wise (análisis)
description: "Análisis independiente del estilo visual de Wise (https://wise.com/es/)."
colors:
  primary: "#163300"
  on-primary: "#FFFFFF"
  secondary: "#9FE870"
  accent: "#163300"
  background: "#FFFFFF"
  surface: "#9FE870"
  text: "#0E0F0C"
  muted: "#163300"
  border: "#DDDDDD"
typography:
  display-lg:
    fontFamily: Wise Sans
    fontSize: 3rem
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Wise Sans
    fontSize: 1.75rem
    fontWeight: 700
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
  sm: 13px
  md: 27px
  lg: 54px
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

# Wise: análisis de su estilo visual

> Análisis independiente de la portada pública de [Wise](https://wise.com/es/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Verde lima brillante con titular en mayúsculas muy grueso en verde oscuro.

Botones en píldora verdes, ilustraciones planas y tono directo.

## Colores

Fondo claro `#FFFFFF` con texto `#0E0F0C`. El color de acción es `#163300` (texto encima `#FFFFFF`); `#9FE870` y `#163300` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Wise Sans** (peso 800, unos 96px en escritorio) y texto en **Inter** a 18px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 27px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#163300`).
- Haz: usa Wise Sans solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Wise; crea los tuyos.
