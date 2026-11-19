---
version: "alpha"
name: Mango (análisis)
description: "Análisis independiente del estilo visual de Mango (https://shop.mango.com/es/es)."
colors:
  primary: "#121212"
  on-primary: "#FFFFFF"
  secondary: "#121212"
  accent: "#FDFDFD"
  background: "#FFFFFF"
  surface: "#DADADA"
  text: "#121212"
  muted: "#131313"
  border: "#DEDEDE"
typography:
  display-lg:
    fontFamily: DefaultFontES
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: DefaultFontES
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: DefaultFontES
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: DefaultFontES
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

# Mango: análisis de su estilo visual

> Análisis independiente de la portada pública de [Mango](https://shop.mango.com/es/es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fotografía de moda a sangre con titular serif blanco superpuesto y navegación mínima en mayúsculas.

Casi sin color de interfaz: negro, blanco y la propia imagen.

## Colores

Fondo claro `#FFFFFF` con texto `#121212`. El color de acción es `#121212` (texto encima `#FFFFFF`); `#121212` y `#FDFDFD` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **DefaultFontES** (peso 700, unos 26px en escritorio) y texto en **DefaultFontES** a 13px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#121212`).
- Haz: usa DefaultFontES solo en titulares y deja el texto en DefaultFontES.
- No hagas: copiar el logotipo, las fotografías o los textos de Mango; crea los tuyos.
