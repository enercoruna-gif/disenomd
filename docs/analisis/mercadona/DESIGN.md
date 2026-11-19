---
version: "alpha"
name: Mercadona (análisis)
description: "Análisis independiente del estilo visual de Mercadona (https://www.mercadona.es)."
colors:
  primary: "#00AB61"
  on-primary: "#000000"
  secondary: "#005630"
  accent: "#4C896E"
  background: "#FFFFFF"
  surface: "#F8F5EC"
  text: "#000000"
  muted: "#3B3935"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: PlayfairDisplay-ExtraBold
    fontSize: 3rem
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: PlayfairDisplay-ExtraBold
    fontSize: 1.75rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Muli
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Muli
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

# Mercadona: análisis de su estilo visual

> Análisis independiente de la portada pública de [Mercadona](https://www.mercadona.es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Verde corporativo con fotografía de producto fresco y un campo grande para el código postal.

Formas sencillas, botones verdes y pocos elementos por pantalla.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#00AB61` (texto encima `#000000`); `#005630` y `#4C896E` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **PlayfairDisplay-ExtraBold** (peso 800, unos 44.8px en escritorio) y texto en **Muli** a 16px. Si esa fuente no está disponible, usa **Source Serif 4** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#00AB61`).
- Haz: usa PlayfairDisplay-ExtraBold solo en titulares y deja el texto en Muli.
- No hagas: copiar el logotipo, las fotografías o los textos de Mercadona; crea los tuyos.
