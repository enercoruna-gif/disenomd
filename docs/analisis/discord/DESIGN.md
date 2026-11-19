---
version: "alpha"
name: Discord (análisis)
description: "Análisis independiente del estilo visual de Discord (https://discord.com)."
colors:
  primary: "#5865F2"
  on-primary: "#FFFFFF"
  secondary: "#ACB2F8"
  accent: "#8D92D8"
  background: "#1A2081"
  surface: "#232986"
  text: "#FFFFFF"
  muted: "#AFB1D3"
  border: "#3A3F93"
typography:
  display-lg:
    fontFamily: Abcgintodiscordnord
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Abcgintodiscordnord
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Ggsans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Ggsans
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

# Discord: análisis de su estilo visual

> Análisis independiente de la portada pública de [Discord](https://discord.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Azul eléctrico saturado de fondo con ilustraciones de personajes y titulares en mayúsculas muy gruesas.

Botones blancos y negros en píldora; tono juvenil y de comunidad gamer.

## Colores

Fondo oscuro `#1A2081` con texto `#FFFFFF`. El color de acción es `#5865F2` (texto encima `#FFFFFF`); `#ACB2F8` y `#8D92D8` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Abcgintodiscordnord** (peso 700, unos 44px en escritorio) y texto en **Ggsans** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 16px; los botones son rectángulos con radio 16px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#5865F2`).
- Haz: usa Abcgintodiscordnord solo en titulares y deja el texto en Ggsans.
- No hagas: copiar el logotipo, las fotografías o los textos de Discord; crea los tuyos.
