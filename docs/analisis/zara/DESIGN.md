---
version: "alpha"
name: Zara (análisis)
description: "Análisis independiente del estilo visual de Zara (https://www.zara.com/es/)."
colors:
  primary: "#FD2E00"
  on-primary: "#000000"
  secondary: "#7E1700"
  accent: "#A55D4C"
  background: "#FFFFFF"
  surface: "#F5F5F5"
  text: "#000000"
  muted: "#595959"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: Helvetica Now Text
    fontSize: 3rem
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Helvetica Now Text
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Helvetica Now Text
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Helvetica Now Text
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

# Zara: análisis de su estilo visual

> Análisis independiente de la portada pública de [Zara](https://www.zara.com/es/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fotografía de moda a sangre con el logotipo gigante superpuesto y una navegación casi invisible.

Sin color de interfaz: negro, blanco y tipografía muy fina.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#FD2E00` (texto encima `#000000`); `#7E1700` y `#A55D4C` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Helvetica Now Text** (peso 300, unos 13px en escritorio) y texto en **Helvetica Now Text** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#FD2E00`).
- Haz: usa Helvetica Now Text solo en titulares y deja el texto en Helvetica Now Text.
- No hagas: copiar el logotipo, las fotografías o los textos de Zara; crea los tuyos.
