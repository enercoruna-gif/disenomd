---
version: "alpha"
name: Max (análisis)
description: "Análisis independiente del estilo visual de Max (https://www.max.com/es)."
colors:
  primary: "#002BE7"
  on-primary: "#FFFFFF"
  secondary: "#1A1A2E"
  accent: "#B2B8FF"
  background: "#000000"
  surface: "#0D0D14"
  text: "#FFFFFF"
  muted: "#A0A0B0"
  border: "#22222E"
typography:
  display-lg:
    fontFamily: '"Max Sans", "Inter", sans-serif'
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.04em
  headline-md:
    fontFamily: '"Max Sans", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Max Sans", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Max Sans", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 2px
  md: 4px
  lg: 8px
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
    padding: 12px 24px
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

# Max: análisis de su estilo visual

> Análisis independiente de la portada pública de [Max](https://www.max.com/es), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Cine en casa: negro profundo, un azul zafiro para entrar y titulares tensos, como una cartela de estreno.

Max se presenta en negro, con un azul #002BE7 que abre la sesión. La tipografía es compacta y mayúscula en la marca; la imagen de la serie ocupa el resto.

## Colores

Fondo #000000, superficies #0D0D14, texto blanco. El azul #002BE7 es la acción; un lila #B2B8FF puede marcar detalles, no el botón principal.

## Tipografía

- `display-lg`: `"Max Sans", "Inter", sans-serif`; tamaño `3rem`, peso `700`.
- `headline-md`: `"Max Sans", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Max Sans", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Max Sans", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 2px`, `md: 4px`, `lg: 8px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Mantén el negro y un solo azul de entrada.
- Haz: Deja que el cartel de la serie llene el hero.
- No hagas: No copies claves ni títulos de sus series.
- No hagas: No uses un rojo tipo videoclub que lo aleje de este zafiro.
