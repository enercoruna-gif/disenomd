---
version: "alpha"
name: El País (análisis)
description: "Análisis independiente del estilo visual de El País (https://elpais.com)."
colors:
  primary: "#F7CF3C"
  on-primary: "#000000"
  secondary: "#7C681E"
  accent: "#111111"
  background: "#FFFFFF"
  surface: "#F7CF3C"
  text: "#000000"
  muted: "#111111"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: MajritTx
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: MajritTx
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: MajritTx
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: MajritTx
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 2px
  md: 2px
  lg: 4px
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

# El País: análisis de su estilo visual

> Análisis independiente de la portada pública de [El País](https://elpais.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Cabecera de periódico clásica con logotipo serif centrado, columnas de noticias y fotografía documental.

Titulares en serif propia, texto denso, filetes finos y el azul solo en etiquetas.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#F7CF3C` (texto encima `#000000`); `#7C681E` y `#111111` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **MajritTx** (peso 700, unos 32px en escritorio) y texto en **MajritTx** a 16px. Si esa fuente no está disponible, usa **Source Serif 4** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 2px; los botones son rectángulos con radio 2px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#F7CF3C`).
- Haz: usa MajritTx solo en titulares y deja el texto en MajritTx.
- No hagas: copiar el logotipo, las fotografías o los textos de El País; crea los tuyos.
