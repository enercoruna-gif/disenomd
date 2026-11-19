---
version: "alpha"
name: Vercel (análisis)
description: "Análisis independiente del estilo visual de Vercel (https://vercel.com)."
colors:
  primary: "#171717"
  on-primary: "#FFFFFF"
  secondary: "#171717"
  accent: "#FFFFFF"
  background: "#FAFAFA"
  surface: "#FFFFFF"
  text: "#171717"
  muted: "#4D4D4D"
  border: "#DADADA"
typography:
  display-lg:
    fontFamily: GeistSans
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: GeistSans
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: GeistSans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: GeistSans
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

# Vercel: análisis de su estilo visual

> Análisis independiente de la portada pública de [Vercel](https://vercel.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Blanco y negro con el triángulo de marca como único gráfico y titular muy ajustado.

Rejilla con líneas finas, tipografía Geist y botones pequeños en píldora.

## Colores

Fondo claro `#FAFAFA` con texto `#171717`. El color de acción es `#171717` (texto encima `#FFFFFF`); `#171717` y `#FFFFFF` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **GeistSans** (peso 400, unos 64px en escritorio) y texto en **GeistSans** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 6px; los botones son rectángulos con radio 6px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#171717`).
- Haz: usa GeistSans solo en titulares y deja el texto en GeistSans.
- No hagas: copiar el logotipo, las fotografías o los textos de Vercel; crea los tuyos.
