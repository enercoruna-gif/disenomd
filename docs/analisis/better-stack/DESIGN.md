---
version: "alpha"
name: Better Stack (análisis)
description: "Análisis independiente del estilo visual de Better Stack (https://betterstack.com)."
colors:
  primary: "#939DB8"
  on-primary: "#000000"
  secondary: "#C9CEDC"
  accent: "#C9D3EE"
  background: "#0B0C14"
  surface: "#0F101A"
  text: "#FFFFFF"
  muted: "#939DB8"
  border: "#2D2E35"
typography:
  display-lg:
    fontFamily: Helvetica Now Display
    fontSize: 3rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Helvetica Now Display
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
  sm: 21px
  md: 43px
  lg: 86px
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

# Better Stack: análisis de su estilo visual

> Análisis independiente de la portada pública de [Better Stack](https://betterstack.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fondo azul noche casi negro con titular blanco grande y una captura del panel de producto difuminada detrás.

Botón índigo con texto blanco, gris azulado para el texto secundario y un campo de correo integrado en el héroe.

## Colores

Fondo oscuro `#0B0C14` con texto `#FFFFFF`. El color de acción es `#939DB8` (texto encima `#000000`); `#C9CEDC` y `#C9D3EE` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Helvetica Now Display** (peso 500, unos 53px en escritorio) y texto en **Helvetica Now Text** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 43px; los botones son rectángulos con radio 43px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#939DB8`).
- Haz: usa Helvetica Now Display solo en titulares y deja el texto en Helvetica Now Text.
- No hagas: copiar el logotipo, las fotografías o los textos de Better Stack; crea los tuyos.
