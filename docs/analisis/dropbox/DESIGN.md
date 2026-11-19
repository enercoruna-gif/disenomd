---
version: "alpha"
name: Dropbox (análisis)
description: "Análisis independiente del estilo visual de Dropbox (https://www.dropbox.com/es_ES/)."
colors:
  primary: "#0061FE"
  on-primary: "#FFFFFF"
  secondary: "#0F3D8C"
  accent: "#F7F5F2"
  background: "#FFFFFF"
  surface: "#F7F5F2"
  text: "#1E1919"
  muted: "#524A3E"
  border: "#DFDFDF"
typography:
  display-lg:
    fontFamily: Sharp Grotesk
    fontSize: 3rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Sharp Grotesk
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

# Dropbox: análisis de su estilo visual

> Análisis independiente de la portada pública de [Dropbox](https://www.dropbox.com/es_ES/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Rejilla geométrica con mucho blanco, azul corporativo y capturas de producto ordenadas en módulos.

Botones rectangulares azules, tipografía sans propia y estructura muy modular.

## Colores

Fondo claro `#FFFFFF` con texto `#1E1919`. El color de acción es `#0061FE` (texto encima `#FFFFFF`); `#0F3D8C` y `#F7F5F2` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Sharp Grotesk** (peso 500, unos 40px en escritorio) y texto en **Inter** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 16px; los botones son rectángulos con radio 16px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#0061FE`).
- Haz: usa Sharp Grotesk solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Dropbox; crea los tuyos.
