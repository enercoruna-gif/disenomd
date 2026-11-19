---
version: "alpha"
name: Lattice (análisis)
description: "Análisis independiente del estilo visual de Lattice (https://lattice.com)."
colors:
  primary: "#027653"
  on-primary: "#FFFFFF"
  secondary: "#C4F7CA"
  accent: "#C4F7CA"
  background: "#FFFFFF"
  surface: "#E2F5FE"
  text: "#1A1F2E"
  muted: "#027653"
  border: "#DFE0E2"
typography:
  display-lg:
    fontFamily: Matter
    fontSize: 3rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Matter
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Matter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Matter
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 10px
  md: 21px
  lg: 42px
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

# Lattice: análisis de su estilo visual

> Análisis independiente de la portada pública de [Lattice](https://lattice.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Portada clara de software de RR. HH. con titular grande en sans geométrica a la izquierda y una tarjeta de producto con degradado pastel a la derecha.

Verde bosque en el botón principal, verde menta en los detalles y esquinas redondeadas generosas en tarjetas y botones.

## Colores

Fondo claro `#FFFFFF` con texto `#1A1F2E`. El color de acción es `#027653` (texto encima `#FFFFFF`); `#C4F7CA` y `#C4F7CA` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Matter** (peso 500, unos 70.144px en escritorio) y texto en **Matter** a 17.536px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 21px; los botones son rectángulos con radio 21px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#027653`).
- Haz: usa Matter solo en titulares y deja el texto en Matter.
- No hagas: copiar el logotipo, las fotografías o los textos de Lattice; crea los tuyos.
