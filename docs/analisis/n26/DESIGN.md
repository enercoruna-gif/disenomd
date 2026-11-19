---
version: "alpha"
name: N26 (análisis)
description: "Análisis independiente del estilo visual de N26 (https://n26.com/es-es)."
colors:
  primary: "#003B39"
  on-primary: "#FFFFFF"
  secondary: "#088177"
  accent: "#52A7A0"
  background: "#FFFFFF"
  surface: "#FAF8F5"
  text: "#1B1B1B"
  muted: "#003B39"
  border: "#DFDFDF"
typography:
  display-lg:
    fontFamily: N26-Extended
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: N26-Extended
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: N26
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: N26
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 12px
  md: 24px
  lg: 48px
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

# N26: análisis de su estilo visual

> Análisis independiente de la portada pública de [N26](https://n26.com/es-es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Verde menta suave con titular centrado grande y fotografía de personas.

Botones negros en píldora, mucho blanco y tono minimalista europeo.

## Colores

Fondo claro `#FFFFFF` con texto `#1B1B1B`. El color de acción es `#003B39` (texto encima `#FFFFFF`); `#088177` y `#52A7A0` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **N26-Extended** (peso 400, unos 80px en escritorio) y texto en **N26** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 24px; los botones son rectángulos con radio 24px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#003B39`).
- Haz: usa N26-Extended solo en titulares y deja el texto en N26.
- No hagas: copiar el logotipo, las fotografías o los textos de N26; crea los tuyos.
