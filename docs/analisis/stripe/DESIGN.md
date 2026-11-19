---
version: "alpha"
name: Stripe (análisis)
description: "Análisis independiente del estilo visual de Stripe (https://stripe.com/es)."
colors:
  primary: "#533AFD"
  on-primary: "#FFFFFF"
  secondary: "#00D66F"
  accent: "#FFE0D1"
  background: "#FFFFFF"
  surface: "#E5EDF5"
  text: "#061B31"
  muted: "#50617A"
  border: "#DCDFE2"
typography:
  display-lg:
    fontFamily: sohne-var
    fontSize: 3rem
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: sohne-var
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: sohne-var
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: sohne-var
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 3px
  md: 6px
  lg: 12px
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

# Stripe: análisis de su estilo visual

> Análisis independiente de la portada pública de [Stripe](https://stripe.com/es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Degradados de colores fluidos detrás de un titular grande y oscuro, con cifras y logos de clientes.

Botones en píldora morado-índigo, tipografía fina y mucho detalle técnico.

## Colores

Fondo claro `#FFFFFF` con texto `#061B31`. El color de acción es `#533AFD` (texto encima `#FFFFFF`); `#00D66F` y `#FFE0D1` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **sohne-var** (peso 300, unos 44px en escritorio) y texto en **sohne-var** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 6px; los botones son rectángulos con radio 6px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#533AFD`).
- Haz: usa sohne-var solo en titulares y deja el texto en sohne-var.
- No hagas: copiar el logotipo, las fotografías o los textos de Stripe; crea los tuyos.
