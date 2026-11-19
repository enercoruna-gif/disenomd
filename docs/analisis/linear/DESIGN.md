---
version: "alpha"
name: Linear (análisis)
description: "Análisis independiente del estilo visual de Linear (https://linear.app)."
colors:
  primary: "#E5E5E6"
  on-primary: "#000000"
  secondary: "#DADEE3"
  accent: "#F7F8F8"
  background: "#08090A"
  surface: "#090A0B"
  text: "#D0D6E0"
  muted: "#8A8F98"
  border: "#242628"
typography:
  display-lg:
    fontFamily: Inter Variable
    fontSize: 3rem
    fontWeight: 510
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter Variable
    fontSize: 1.75rem
    fontWeight: 410
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter Variable
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Inter Variable
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 4px
  md: 9px
  lg: 18px
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

# Linear: análisis de su estilo visual

> Análisis independiente de la portada pública de [Linear](https://linear.app), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Modo oscuro casi negro, tipografía neutra muy afinada y capturas del producto con brillo sutil.

Grises por capas para separar superficies; el color solo aparece en estados e iconos.

## Colores

Fondo oscuro `#08090A` con texto `#D0D6E0`. El color de acción es `#E5E5E6` (texto encima `#000000`); `#DADEE3` y `#F7F8F8` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Inter Variable** (peso 510, unos 64px en escritorio) y texto en **Inter Variable** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 9px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#E5E5E6`).
- Haz: usa Inter Variable solo en titulares y deja el texto en Inter Variable.
- No hagas: copiar el logotipo, las fotografías o los textos de Linear; crea los tuyos.
