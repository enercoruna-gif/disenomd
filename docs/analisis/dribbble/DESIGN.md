---
version: "alpha"
name: Dribbble (análisis)
description: "Análisis independiente del estilo visual de Dribbble (https://dribbble.com)."
colors:
  primary: "#EA4C89"
  on-primary: "#000000"
  secondary: "#782850"
  accent: "#A06884"
  background: "#FFFFFF"
  surface: "#F3F3F6"
  text: "#060318"
  muted: "#0D0C22"
  border: "#DCDCDF"
typography:
  display-lg:
    fontFamily: Mona Sans
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Mona Sans
    fontSize: 1.75rem
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Mona Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Mona Sans
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

# Dribbble: análisis de su estilo visual

> Análisis independiente de la portada pública de [Dribbble](https://dribbble.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Blanco limpio con titular negro grande y una palabra destacada en rosa, al servicio de las imágenes de trabajos.

Botones negros en píldora y miniaturas de proyectos con esquinas suaves.

## Colores

Fondo claro `#FFFFFF` con texto `#060318`. El color de acción es `#EA4C89` (texto encima `#000000`); `#782850` y `#A06884` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Mona Sans** (peso 600, unos 52px en escritorio) y texto en **Mona Sans** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#EA4C89`).
- Haz: usa Mona Sans solo en titulares y deja el texto en Mona Sans.
- No hagas: copiar el logotipo, las fotografías o los textos de Dribbble; crea los tuyos.
