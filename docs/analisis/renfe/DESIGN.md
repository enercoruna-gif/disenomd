---
version: "alpha"
name: Renfe (análisis)
description: "Análisis independiente del estilo visual de Renfe (https://www.renfe.com/es/es)."
colors:
  primary: "#5B064B"
  on-primary: "#FFFFFF"
  secondary: "#340A2E"
  accent: "#404040"
  background: "#FFFFFF"
  surface: "#F1F2F8"
  text: "#0D0F12"
  muted: "#404040"
  border: "#DDDDDE"
typography:
  display-lg:
    fontFamily: Arial
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Arial
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Renfe Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Renfe Sans
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 20px
  md: 40px
  lg: 80px
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

# Renfe: análisis de su estilo visual

> Análisis independiente de la portada pública de [Renfe](https://www.renfe.com/es/es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fondo blanco funcional con buscador de trenes en primer plano y morado corporativo.

Formularios grandes, botones de color sólido y tipografía práctica.

## Colores

Fondo claro `#FFFFFF` con texto `#0D0F12`. El color de acción es `#5B064B` (texto encima `#FFFFFF`); `#340A2E` y `#404040` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Arial** (peso 700, unos 24px en escritorio) y texto en **Renfe Sans** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 40px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#5B064B`).
- Haz: usa Arial solo en titulares y deja el texto en Renfe Sans.
- No hagas: copiar el logotipo, las fotografías o los textos de Renfe; crea los tuyos.
