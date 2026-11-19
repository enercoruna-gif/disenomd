---
version: "alpha"
name: Canva (análisis)
description: "Análisis independiente del estilo visual de Canva (https://www.canva.com/es_es/)."
colors:
  primary: "#0F1015"
  on-primary: "#FFFFFF"
  secondary: "#0F1015"
  accent: "#57585B"
  background: "#FFFFFF"
  surface: "#F5F5F6"
  text: "#0F1015"
  muted: "#8B3DFF"
  border: "#DDDEDE"
typography:
  display-lg:
    fontFamily: Canva Sans
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Canva Sans
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
  sm: 5px
  md: 10px
  lg: 20px
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

# Canva: análisis de su estilo visual

> Análisis independiente de la portada pública de [Canva](https://www.canva.com/es_es/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Degradados morado-turquesa muy vivos y titulares redondos y gruesos, pensado para un público no técnico.

Botones en píldora morados, ilustraciones y plantillas como gancho visual.

## Colores

Fondo claro `#FFFFFF` con texto `#0F1015`. El color de acción es `#0F1015` (texto encima `#FFFFFF`); `#0F1015` y `#57585B` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Canva Sans** (peso 600, unos 24px en escritorio) y texto en **Inter** a 10px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 10px; los botones son rectángulos con radio 10px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#0F1015`).
- Haz: usa Canva Sans solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Canva; crea los tuyos.
