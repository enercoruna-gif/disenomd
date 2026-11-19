---
version: "alpha"
name: Krepling (análisis)
description: "Análisis independiente del estilo visual de Krepling (https://krepling.com)."
colors:
  primary: "#B154F9"
  on-primary: "#000000"
  secondary: "#582A7C"
  accent: "#8A6AA3"
  background: "#FFFFFF"
  surface: "#F1F1F1"
  text: "#000000"
  muted: "#6C6B6B"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: Regular
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Regular
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Regular
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Regular
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 5px
  md: 10px
  lg: 20px
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

# Krepling: análisis de su estilo visual

> Análisis independiente de la portada pública de [Krepling](https://krepling.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Composición asimétrica sobre blanco: titular grande abajo a la izquierda y objetos 3D flotando con iconos de apps.

Morado eléctrico solo en el botón principal, texto negro y gris medio y radios pequeños de 10 px.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#B154F9` (texto encima `#000000`); `#582A7C` y `#8A6AA3` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Regular** (peso 400, unos 56.8889px en escritorio) y texto en **Regular** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 10px; los botones son rectángulos con radio 10px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#B154F9`).
- Haz: usa Regular solo en titulares y deja el texto en Regular.
- No hagas: copiar el logotipo, las fotografías o los textos de Krepling; crea los tuyos.
