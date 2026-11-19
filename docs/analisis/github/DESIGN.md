---
version: "alpha"
name: GitHub (análisis)
description: "Análisis independiente del estilo visual de GitHub (https://github.com)."
colors:
  primary: "#08872B"
  on-primary: "#FFFFFF"
  secondary: "#0969DA"
  accent: "#0969DA"
  background: "#FFFFFF"
  surface: "#F2F5F3"
  text: "#000000"
  muted: "#58635B"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: Mona Sans
    fontSize: 3rem
    fontWeight: 440
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Mona Sans
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Mona Sans VF
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Mona Sans VF
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

# GitHub: análisis de su estilo visual

> Análisis independiente de la portada pública de [GitHub](https://github.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Portada clara con titular negro grande, ilustración del octogato y campo de correo con botón verde.

Mucho blanco, tipografía Mona Sans y contraste alto para el producto técnico.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#08872B` (texto encima `#FFFFFF`); `#0969DA` y `#0969DA` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Mona Sans** (peso 440, unos 56px en escritorio) y texto en **Mona Sans VF** a 14px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#08872B`).
- Haz: usa Mona Sans solo en titulares y deja el texto en Mona Sans VF.
- No hagas: copiar el logotipo, las fotografías o los textos de GitHub; crea los tuyos.
