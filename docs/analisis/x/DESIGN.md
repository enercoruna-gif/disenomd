---
version: "alpha"
name: X (análisis)
description: "Análisis independiente del estilo visual de X (https://x.com)."
colors:
  primary: "#EFF3F4"
  on-primary: "#0F1419"
  secondary: "#1E1E1E"
  accent: "#1D9BF0"
  background: "#000000"
  surface: "#16181C"
  text: "#E7E9EA"
  muted: "#71767B"
  border: "#2F3336"
typography:
  display-lg:
    fontFamily: '"Twitter Chirp", "Inter", sans-serif'
    fontSize: 2.5rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"Twitter Chirp", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Twitter Chirp", "Inter", sans-serif'
    fontSize: 0.9375rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Twitter Chirp", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 12px
  md: 24px
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
    padding: 10px 18px
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

# X: análisis de su estilo visual

> Análisis independiente de la portada pública de [X](https://x.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Una columna de texto sobre negro, botones claros en píldora y un azul muy puntual para el enlace o el acento.

X es una noche tipográfica: fondo negro, letras claras y muy poca ornamentación. El botón principal es claro sobre oscuro; el azul #1D9BF0 aparece con mesura.

## Colores

Fondo #000000, superficie #16181C, texto #E7E9EA. El CTA principal puede ser #EFF3F4 con texto #0F1419; el acento #1D9BF0 es para enlaces e iconos activos.

## Tipografía

- `display-lg`: `"Twitter Chirp", "Inter", sans-serif`; tamaño `2.5rem`, peso `700`.
- `headline-md`: `"Twitter Chirp", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Twitter Chirp", "Inter", sans-serif`; tamaño `0.9375rem`, peso `400`.
- `label-sm`: `"Twitter Chirp", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 12px`, `md: 24px`, `lg: 16px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Trabaja en una columna estrecha de lectura, sobre negro.
- Haz: Un botón claro y un acento azul, no una paleta amplia.
- No hagas: No copies el logotipo ni la disposición exacta de su cronología.
- No hagas: No ilumines el fondo: el sistema es nocturno.
