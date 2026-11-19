---
version: "alpha"
name: Nike (análisis)
description: "Análisis independiente del estilo visual de Nike (https://www.nike.com/es/)."
colors:
  primary: "#111111"
  on-primary: "#FFFFFF"
  secondary: "#111111"
  accent: "#585858"
  background: "#FFFFFF"
  surface: "#F5F5F5"
  text: "#111111"
  muted: "#707072"
  border: "#DEDEDE"
typography:
  display-lg:
    fontFamily: Helvetica Now Display Medium
    fontSize: 3rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Helvetica Now Display Medium
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Helvetica Now Text
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Helvetica Now Text
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

# Nike: análisis de su estilo visual

> Análisis independiente de la portada pública de [Nike](https://www.nike.com/es/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fotografía deportiva a pantalla completa con titulares en mayúsculas condensadas y negras.

Interfaz blanca y negra, botones en píldora y el color lo pone la foto.

## Colores

Fondo claro `#FFFFFF` con texto `#111111`. El color de acción es `#111111` (texto encima `#FFFFFF`); `#111111` y `#585858` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Helvetica Now Display Medium** (peso 500, unos 16px en escritorio) y texto en **Helvetica Now Text** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 24px; los botones son rectángulos con radio 24px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#111111`).
- Haz: usa Helvetica Now Display Medium solo en titulares y deja el texto en Helvetica Now Text.
- No hagas: copiar el logotipo, las fotografías o los textos de Nike; crea los tuyos.
