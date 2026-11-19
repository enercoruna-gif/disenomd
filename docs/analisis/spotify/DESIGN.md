---
version: "alpha"
name: Spotify (análisis)
description: "Análisis independiente del estilo visual de Spotify (https://www.spotify.com/es/premium/)."
colors:
  primary: "#1D75DE"
  on-primary: "#000000"
  secondary: "#1ED760"
  accent: "#9E9EFF"
  background: "#FFFFFF"
  surface: "#F5F5F5"
  text: "#000000"
  muted: "#121212"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: SpotifyMixUITitleVariable
    fontSize: 3rem
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: SpotifyMixUITitleVariable
    fontSize: 1.75rem
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: SpotifyMixUI
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: SpotifyMixUI
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

# Spotify: análisis de su estilo visual

> Análisis independiente de la portada pública de [Spotify](https://www.spotify.com/es/premium/), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Negro y verde de marca con titulares enormes y gruesos, casi carteles.

Botones en píldora verdes y blancos y degradados en bloques de campaña.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#1D75DE` (texto encima `#000000`); `#1ED760` y `#9E9EFF` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **SpotifyMixUITitleVariable** (peso 900, unos 96px en escritorio) y texto en **SpotifyMixUI** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#1D75DE`).
- Haz: usa SpotifyMixUITitleVariable solo en titulares y deja el texto en SpotifyMixUI.
- No hagas: copiar el logotipo, las fotografías o los textos de Spotify; crea los tuyos.
