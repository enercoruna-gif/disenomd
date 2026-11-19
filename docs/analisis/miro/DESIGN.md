---
version: "alpha"
name: Miro (análisis)
description: "Análisis independiente del estilo visual de Miro (https://miro.com/es/)."
colors:
  primary: "#FDE050"
  on-primary: "#000000"
  secondary: "#FFC795"
  accent: "#A8F7F0"
  background: "#FBFAF7"
  surface: "#FFFFFF"
  text: "#000000"
  muted: "#0000EE"
  border: "#D8D7D4"
typography:
  display-lg:
    fontFamily: Apris Regular
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Apris Regular
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
    textColor: "{colors.text}"
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

# Miro: análisis de su estilo visual

> Análisis independiente de la portada pública de [Miro](https://miro.com/es/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fondo crema muy claro, amarillo de marca y lienzos de post-its como ilustración.

Botones negros, tarjetas flotantes con sombra y tipografía geométrica.

## Colores

Fondo claro `#FBFAF7` con texto `#000000`. El color de acción es `#FDE050` (texto encima `#000000`); `#FFC795` y `#A8F7F0` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Apris Regular** (peso 400, unos 56px en escritorio) y texto en **Inter** a 12px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 16px; los botones son rectángulos con radio 16px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#FDE050`).
- Haz: usa Apris Regular solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Miro; crea los tuyos.
