---
version: "alpha"
name: Factorial (análisis)
description: "Análisis independiente del estilo visual de Factorial (https://factorialhr.es)."
colors:
  primary: "#E51943"
  on-primary: "#FFFFFF"
  secondary: "#851F40"
  accent: "#A25D73"
  background: "#FFFFFF"
  surface: "#E8E8ED"
  text: "#25253D"
  muted: "#515164"
  border: "#E0E0E4"
typography:
  display-lg:
    fontFamily: DM Sans
    fontSize: 3rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: DM Sans
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: DM Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: DM Sans
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 10px
  md: 21px
  lg: 42px
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

# Factorial: análisis de su estilo visual

> Análisis independiente de la portada pública de [Factorial](https://factorialhr.es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Blanco con acentos rojo frambuesa, titular centrado con palabras destacadas en color y capturas del software.

Botones en píldora rojos, tarjetas con bordes suaves y fotografía de equipos.

## Colores

Fondo claro `#FFFFFF` con texto `#25253D`. El color de acción es `#E51943` (texto encima `#FFFFFF`); `#851F40` y `#A25D73` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **DM Sans** (peso 500, unos 64px en escritorio) y texto en **DM Sans** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 21px; los botones son rectángulos con radio 21px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#E51943`).
- Haz: usa DM Sans solo en titulares y deja el texto en DM Sans.
- No hagas: copiar el logotipo, las fotografías o los textos de Factorial; crea los tuyos.
