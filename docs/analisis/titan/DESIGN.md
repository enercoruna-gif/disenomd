---
version: "alpha"
name: Titan (análisis)
description: "Análisis independiente del estilo visual de Titan (https://titan.com)."
colors:
  primary: "#12100E"
  on-primary: "#FFFFFF"
  secondary: "#12100E"
  accent: "#585755"
  background: "#FDFEFA"
  surface: "#F4F4F1"
  text: "#12100E"
  muted: "#646361"
  border: "#DCDDD9"
typography:
  display-lg:
    fontFamily: neueMontreal
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: neueMontreal
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: neueMontreal
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: neueMontreal
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 4px
  md: 8px
  lg: 16px
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

# Titan: análisis de su estilo visual

> Análisis independiente de la portada pública de [Titan](https://titan.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Héroe fotográfico a pantalla completa con el nombre de la marca en serif gigante y texto blanco encima.

Paleta casi monocroma de negro cálido y blanco roto, botones en píldora y mucho aire entre bloques.

## Colores

Fondo claro `#FDFEFA` con texto `#12100E`. El color de acción es `#12100E` (texto encima `#FFFFFF`); `#12100E` y `#585755` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **neueMontreal** (peso 400, unos 24px en escritorio) y texto en **neueMontreal** a 14px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#12100E`).
- Haz: usa neueMontreal solo en titulares y deja el texto en neueMontreal.
- No hagas: copiar el logotipo, las fotografías o los textos de Titan; crea los tuyos.
