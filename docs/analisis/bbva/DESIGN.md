---
version: "alpha"
name: BBVA (análisis)
description: "Análisis independiente del estilo visual de BBVA (https://www.bbva.es)."
colors:
  primary: "#001391"
  on-primary: "#FFFFFF"
  secondary: "#0C6DFF"
  accent: "#070E46"
  background: "#F7F8F8"
  surface: "#FFFFFF"
  text: "#000000"
  muted: "#001391"
  border: "#D4D5D5"
typography:
  display-lg:
    fontFamily: Benton Sans BBVA
    fontSize: 3rem
    fontWeight: 350
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Benton Sans BBVA
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Benton Sans BBVA
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Benton Sans BBVA
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 8px
  md: 16px
  lg: 32px
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

# BBVA: análisis de su estilo visual

> Análisis independiente de la portada pública de [BBVA](https://www.bbva.es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Banca clara y directa: azul corporativo profundo, cabeceras con cifras grandes y fotografía de personas.

Botones rectangulares con poco radio y un tono turquesa secundario para destacar ofertas.

## Colores

Fondo claro `#F7F8F8` con texto `#000000`. El color de acción es `#001391` (texto encima `#FFFFFF`); `#0C6DFF` y `#070E46` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Benton Sans BBVA** (peso 350, unos 15.008px en escritorio) y texto en **Benton Sans BBVA** a 15.008px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 16px; los botones son rectángulos con radio 16px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#001391`).
- Haz: usa Benton Sans BBVA solo en titulares y deja el texto en Benton Sans BBVA.
- No hagas: copiar el logotipo, las fotografías o los textos de BBVA; crea los tuyos.
