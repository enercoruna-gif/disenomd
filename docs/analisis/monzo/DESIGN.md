---
version: "alpha"
name: Monzo (análisis)
description: "Análisis independiente del estilo visual de Monzo (https://monzo.com)."
colors:
  primary: "#091723"
  on-primary: "#FFFFFF"
  secondary: "#040C12"
  accent: "#4F5559"
  background: "#FFFFFF"
  surface: "#F2F8F3"
  text: "#000000"
  muted: "#091723"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: MonzoSansDisplay
    fontSize: 3rem
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: MonzoSansDisplay
    fontSize: 1.75rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: MonzoSansText
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: MonzoSansText
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

# Monzo: análisis de su estilo visual

> Análisis independiente de la portada pública de [Monzo](https://monzo.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Azul marino oscuro con acentos coral, titulares grandes y fotografía de la tarjeta.

Tipografía propia redondeada, botones en píldora claros sobre fondo oscuro.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#091723` (texto encima `#FFFFFF`); `#040C12` y `#4F5559` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **MonzoSansDisplay** (peso 800, unos 48.8288px en escritorio) y texto en **MonzoSansText** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 10px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#091723`).
- Haz: usa MonzoSansDisplay solo en titulares y deja el texto en MonzoSansText.
- No hagas: copiar el logotipo, las fotografías o los textos de Monzo; crea los tuyos.
