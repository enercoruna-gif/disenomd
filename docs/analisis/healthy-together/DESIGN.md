---
version: "alpha"
name: Healthy Together (análisis)
description: "Análisis independiente del estilo visual de Healthy Together (https://healthytogether.io)."
colors:
  primary: "#4541FE"
  on-primary: "#FFFFFF"
  secondary: "#A2A0FE"
  accent: "#7D7EBF"
  background: "#101722"
  surface: "#1A202B"
  text: "#FFFFFF"
  muted: "#C3C5C7"
  border: "#313741"
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
    fontFamily: ui-sans-serif
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: ui-sans-serif
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

# Healthy Together: análisis de su estilo visual

> Análisis independiente de la portada pública de [Healthy Together](https://healthytogether.io), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Azul marino profundo a toda la pantalla con titular blanco centrado en sans muy gruesa.

Acento rosa coral y azul eléctrico en botones píldora; fila de sellos institucionales en gris claro.

## Colores

Fondo oscuro `#101722` con texto `#FFFFFF`. El color de acción es `#4541FE` (texto encima `#FFFFFF`); `#A2A0FE` y `#7D7EBF` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Inter** (peso 700, unos ? en escritorio) y texto en **ui-sans-serif** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#4541FE`).
- Haz: usa Inter solo en titulares y deja el texto en ui-sans-serif.
- No hagas: copiar el logotipo, las fotografías o los textos de Healthy Together; crea los tuyos.
