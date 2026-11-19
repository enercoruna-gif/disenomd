---
version: "alpha"
name: Passionfroot (análisis)
description: "Análisis independiente del estilo visual de Passionfroot (https://www.passionfroot.me)."
colors:
  primary: "#190922"
  on-primary: "#FFFFFF"
  secondary: "#160E1B"
  accent: "#5C565F"
  background: "#FFFFFF"
  surface: "#F6F6F6"
  text: "#141414"
  muted: "#666666"
  border: "#DEDEDE"
typography:
  display-lg:
    fontFamily: new-kansas
    fontSize: 3rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: new-kansas
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Nunito Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Nunito Sans
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

# Passionfroot: análisis de su estilo visual

> Análisis independiente de la portada pública de [Passionfroot](https://www.passionfroot.me), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Titular centrado en serif expresiva sobre un cielo morado ilustrado con un personaje 3D.

Botones píldora blancos con borde, barra de búsqueda tipo chat y logotipos de clientes en blanco.

## Colores

Fondo claro `#FFFFFF` con texto `#141414`. El color de acción es `#190922` (texto encima `#FFFFFF`); `#160E1B` y `#5C565F` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **new-kansas** (peso 500, unos 64px en escritorio) y texto en **Nunito Sans** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#190922`).
- Haz: usa new-kansas solo en titulares y deja el texto en Nunito Sans.
- No hagas: copiar el logotipo, las fotografías o los textos de Passionfroot; crea los tuyos.
