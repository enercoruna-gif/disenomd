---
version: "alpha"
name: Endless Tools (análisis)
description: "Análisis independiente del estilo visual de Endless Tools (https://www.endlesstools.io)."
colors:
  primary: "#FF13B1"
  on-primary: "#000000"
  secondary: "#FF89D8"
  accent: "#B26097"
  background: "#000000"
  surface: "#0A0A0A"
  text: "#FFFFFF"
  muted: "#959595"
  border: "#242424"
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 3rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 1.75rem
    fontWeight: 400
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

# Endless Tools: análisis de su estilo visual

> Análisis independiente de la portada pública de [Endless Tools](https://www.endlesstools.io), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Negro puro con titular blanco centrado, palabras rodeadas a mano y objetos 3D flotando alrededor.

Rosa fucsia en el botón principal, anotaciones con flechas dibujadas y botones en píldora.

## Colores

Fondo oscuro `#000000` con texto `#FFFFFF`. El color de acción es `#FF13B1` (texto encima `#000000`); `#FF89D8` y `#B26097` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Inter** (peso 500, unos 42px en escritorio) y texto en **Inter** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#FF13B1`).
- Haz: usa Inter solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Endless Tools; crea los tuyos.
