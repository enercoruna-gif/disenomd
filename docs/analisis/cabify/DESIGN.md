---
version: "alpha"
name: Cabify (análisis)
description: "Análisis independiente del estilo visual de Cabify (https://cabify.com/es)."
colors:
  primary: "#7145D6"
  on-primary: "#FFFFFF"
  secondary: "#1F123F"
  accent: "#625979"
  background: "#FFFFFF"
  surface: "#F8F8FE"
  text: "#1A1A1C"
  muted: "#5E6088"
  border: "#DFDFDF"
typography:
  display-lg:
    fontFamily: Cabify Ciudad
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Cabify Ciudad
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Cabify Ciudad Text
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Cabify Ciudad Text
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 15px
  md: 31px
  lg: 62px
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

# Cabify: análisis de su estilo visual

> Análisis independiente de la portada pública de [Cabify](https://cabify.com/es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Morado característico con fotografía de conductores y pasajeros y titulares gruesos.

Tarjetas redondeadas sobre fondos lila suaves y CTAs en píldora.

## Colores

Fondo claro `#FFFFFF` con texto `#1A1A1C`. El color de acción es `#7145D6` (texto encima `#FFFFFF`); `#1F123F` y `#625979` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Cabify Ciudad** (peso 700, unos 40px en escritorio) y texto en **Cabify Ciudad Text** a 18px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 31px; los botones son rectángulos con radio 31px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#7145D6`).
- Haz: usa Cabify Ciudad solo en titulares y deja el texto en Cabify Ciudad Text.
- No hagas: copiar el logotipo, las fotografías o los textos de Cabify; crea los tuyos.
