---
version: "alpha"
name: Cursor (análisis)
description: "Análisis independiente del estilo visual de Cursor (https://cursor.com)."
colors:
  primary: "#26251E"
  on-primary: "#FFFFFF"
  secondary: "#26251E"
  accent: "#65645E"
  background: "#F7F7F4"
  surface: "#F2F1ED"
  text: "#26251E"
  muted: "#3A6A9F"
  border: "#DADAD6"
typography:
  display-lg:
    fontFamily: CursorGothic
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: CursorGothic
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: CursorGothic
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: CursorGothic
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

# Cursor: análisis de su estilo visual

> Análisis independiente de la portada pública de [Cursor](https://cursor.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Estética de editor de código: fondo claro y neutro, tipografía técnica y capturas grandes del propio producto.

Botones pequeños oscuros en píldora, mucho espacio y cero decoración.

## Colores

Fondo claro `#F7F7F4` con texto `#26251E`. El color de acción es `#26251E` (texto encima `#FFFFFF`); `#26251E` y `#65645E` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **CursorGothic** (peso 400, unos 26px en escritorio) y texto en **CursorGothic** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#26251E`).
- Haz: usa CursorGothic solo en titulares y deja el texto en CursorGothic.
- No hagas: copiar el logotipo, las fotografías o los textos de Cursor; crea los tuyos.
