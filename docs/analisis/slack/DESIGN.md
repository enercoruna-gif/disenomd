---
version: "alpha"
name: Slack (análisis)
description: "Análisis independiente del estilo visual de Slack (https://slack.com/intl/es-es)."
colors:
  primary: "#730394"
  on-primary: "#FFFFFF"
  secondary: "#481A54"
  accent: "#2E0039"
  background: "#FFFFFF"
  surface: "#F9F0FF"
  text: "#1D1D1D"
  muted: "#481A54"
  border: "#DFDFDF"
typography:
  display-lg:
    fontFamily: Salesforce-Avant-Garde
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Salesforce-Avant-Garde
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Salesforce-Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Salesforce-Sans
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 16px
  md: 32px
  lg: 64px
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

# Slack: análisis de su estilo visual

> Análisis independiente de la portada pública de [Slack](https://slack.com/intl/es-es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Blanco con morado berenjena de marca, titulares muy gruesos y capturas del chat.

Botones morados rectangulares con poco radio y acentos de los cuatro colores del logo.

## Colores

Fondo claro `#FFFFFF` con texto `#1D1D1D`. El color de acción es `#730394` (texto encima `#FFFFFF`); `#481A54` y `#2E0039` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Salesforce-Avant-Garde** (peso 700, unos 64px en escritorio) y texto en **Salesforce-Sans** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 32px; los botones son rectángulos con radio 32px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#730394`).
- Haz: usa Salesforce-Avant-Garde solo en titulares y deja el texto en Salesforce-Sans.
- No hagas: copiar el logotipo, las fotografías o los textos de Slack; crea los tuyos.
