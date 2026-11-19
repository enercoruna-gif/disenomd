---
version: "alpha"
name: PostHog (análisis)
description: "Análisis independiente del estilo visual de PostHog (https://posthog.com)."
colors:
  primary: "#CD8407"
  on-primary: "#000000"
  secondary: "#EB9D2A"
  accent: "#111827"
  background: "#EEEFE9"
  surface: "#D3DAC6"
  text: "#111111"
  muted: "#374151"
  border: "#CFD0CB"
typography:
  display-lg:
    fontFamily: RoundHog
    fontSize: 3rem
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: RoundHog
    fontSize: 1.75rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: RoundHog
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: RoundHog
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

# PostHog: análisis de su estilo visual

> Análisis independiente de la portada pública de [PostHog](https://posthog.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Crema y marrón con un estilo de escritorio retro, ventanas y personajes de erizo.

Botones amarillos con relieve, bordes marcados y tono humorístico.

## Colores

Fondo claro `#EEEFE9` con texto `#111111`. El color de acción es `#CD8407` (texto encima `#000000`); `#EB9D2A` y `#111827` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **RoundHog** (peso 800, unos 36px en escritorio) y texto en **RoundHog** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#CD8407`).
- Haz: usa RoundHog solo en titulares y deja el texto en RoundHog.
- No hagas: copiar el logotipo, las fotografías o los textos de PostHog; crea los tuyos.
