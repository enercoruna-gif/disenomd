---
version: "alpha"
name: Raycast (análisis)
description: "Análisis independiente del estilo visual de Raycast (https://www.raycast.com)."
colors:
  primary: "#E6E6E6"
  on-primary: "#000000"
  secondary: "#F2F2F2"
  accent: "#ABACAC"
  background: "#07080A"
  surface: "#452324"
  text: "#FFFFFF"
  muted: "#9C9C9D"
  border: "#2A2B2C"
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 1.75rem
    fontWeight: 500
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
  sm: 6px
  md: 12px
  lg: 24px
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

# Raycast: análisis de su estilo visual

> Análisis independiente de la portada pública de [Raycast](https://www.raycast.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Negro profundo con un gráfico rojo diagonal y titular blanco: aspecto de app nativa premium.

Tarjetas oscuras con brillo sutil y botones pequeños en píldora.

## Colores

Fondo oscuro `#07080A` con texto `#FFFFFF`. El color de acción es `#E6E6E6` (texto encima `#000000`); `#F2F2F2` y `#ABACAC` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Inter** (peso 600, unos 64px en escritorio) y texto en **Inter** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 12px; los botones son rectángulos con radio 12px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#E6E6E6`).
- Haz: usa Inter solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Raycast; crea los tuyos.
