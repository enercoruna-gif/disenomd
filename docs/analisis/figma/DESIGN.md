---
version: "alpha"
name: Figma (análisis)
description: "Análisis independiente del estilo visual de Figma (https://www.figma.com/es-es/)."
colors:
  primary: "#000000"
  on-primary: "#FFFFFF"
  secondary: "#000000"
  accent: "#4C4C4C"
  background: "#FFFFFF"
  surface: "#F5F5F5"
  text: "#000000"
  muted: "#595959"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: figmaSans
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: figmaSans
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: figmaSans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: figmaSans
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 8px
  md: 16px
  lg: 32px
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

# Figma: análisis de su estilo visual

> Análisis independiente de la portada pública de [Figma](https://www.figma.com/es-es/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Colores planos muy saturados por bloques (verde, morado, naranja) y titulares enormes.

Tipografía propia geométrica, botones negros en píldora y capturas del lienzo de diseño.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#000000` (texto encima `#FFFFFF`); `#000000` y `#4C4C4C` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **figmaSans** (peso 400, unos 56px en escritorio) y texto en **figmaSans** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 16px; los botones son rectángulos con radio 16px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#000000`).
- Haz: usa figmaSans solo en titulares y deja el texto en figmaSans.
- No hagas: copiar el logotipo, las fotografías o los textos de Figma; crea los tuyos.
