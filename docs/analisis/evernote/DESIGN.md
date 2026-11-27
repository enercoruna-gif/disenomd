---
version: "alpha"
name: Evernote (análisis)
description: "Análisis independiente del estilo visual de Evernote (https://evernote.com)."
colors:
  primary: "#00A82D"
  on-primary: "#FFFFFF"
  secondary: "#F3FBF5"
  accent: "#00A82D"
  background: "#FFFFFF"
  surface: "#FFFFFF"
  text: "#1A1A1A"
  muted: "#5F5F5F"
  border: "#E6E6E6"
typography:
  display-lg:
    fontFamily: '"Soleil", "Inter", sans-serif'
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  headline-md:
    fontFamily: '"Soleil", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Soleil", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Soleil", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 4px
  md: 8px
  lg: 12px
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

# Evernote: análisis de su estilo visual

> Análisis independiente de la portada pública de [Evernote](https://evernote.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Verde de libretas, una portada clara y tipografía sencilla: tomar notas se presenta como un hábito, no como un editor complejo.

Evernote se reconoce por el verde #00A82D sobre blanco. La página habla de capturar ideas, con una interfaz que recuerda una libreta digital.

## Colores

Fondo #FFFFFF, texto #1A1A1A, acción #00A82D y un verde pálido #F3FBF5 en fondos de apoyo. Bordes #E6E6E6.

## Tipografía

- `display-lg`: `"Soleil", "Inter", sans-serif`; tamaño `2.75rem`, peso `700`.
- `headline-md`: `"Soleil", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Soleil", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Soleil", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 4px`, `md: 8px`, `lg: 12px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: El verde es la única acción de marca.
- Haz: Presenta la nota como una ficha clara, con título y extracto.
- No hagas: No copies el elefante ni el logotipo.
- No hagas: No uses un verde neón que lo aleje de este tono de libretas.
