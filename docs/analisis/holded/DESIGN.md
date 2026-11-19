---
version: "alpha"
name: Holded (análisis)
description: "Análisis independiente del estilo visual de Holded (https://www.holded.com/es)."
colors:
  primary: "#1963EF"
  on-primary: "#FFFFFF"
  secondary: "#FF5454"
  accent: "#ECEAE6"
  background: "#FFFFFF"
  surface: "#FAFAF9"
  text: "#121926"
  muted: "#686F7C"
  border: "#DEDFE1"
typography:
  display-lg:
    fontFamily: inter
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: inter
    fontSize: 1.75rem
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: inter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: inter
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 9px
  md: 18px
  lg: 36px
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

# Holded: análisis de su estilo visual

> Análisis independiente de la portada pública de [Holded](https://www.holded.com/es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fondo oscuro azul noche con titular blanco grande y un botón blanco en píldora para el correo.

Acentos lila, capturas flotantes del software y sellos de valoraciones.

## Colores

Fondo claro `#FFFFFF` con texto `#121926`. El color de acción es `#1963EF` (texto encima `#FFFFFF`); `#FF5454` y `#ECEAE6` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **inter** (peso 600, unos 56px en escritorio) y texto en **inter** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 18px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#1963EF`).
- Haz: usa inter solo en titulares y deja el texto en inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Holded; crea los tuyos.
