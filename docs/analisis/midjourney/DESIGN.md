---
version: "alpha"
name: Midjourney (análisis)
description: "Análisis independiente del estilo visual de Midjourney (https://www.midjourney.com)."
colors:
  primary: "#E8E0D0"
  on-primary: "#0E0E0E"
  secondary: "#1A1A1A"
  accent: "#C4A574"
  background: "#0E0E0E"
  surface: "#161616"
  text: "#EEEAE3"
  muted: "#9A958C"
  border: "#2A2A2A"
typography:
  display-lg:
    fontFamily: '"Times New Roman", "Source Serif 4", serif'
    fontSize: 3.25rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: '"Times New Roman", "Source Serif 4", serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Times New Roman", "Source Serif 4", serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Times New Roman", "Source Serif 4", serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 1px
  md: 2px
  lg: 4px
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
    padding: 12px 22px
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

# Midjourney: análisis de su estilo visual

> Análisis independiente de la portada pública de [Midjourney](https://www.midjourney.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Oscuridad de estudio, una serif de cartel y un beige de acento: más galería que herramienta, con la imagen generada como pieza central.

Midjourney se presenta en negro #0E0E0E, con tipografía serif y un beige #E8E0D0 para la acción. Parece una sala de exposiciones, no un panel de ajustes.

## Colores

Fondo #0E0E0E, superficie #161616, texto #EEEAE3, acción #E8E0D0 (texto #0E0E0E) y un acento oro suave #C4A574. Bordes #2A2A2A.

## Tipografía

- `display-lg`: `"Times New Roman", "Source Serif 4", serif`; tamaño `3.25rem`, peso `700`.
- `headline-md`: `"Times New Roman", "Source Serif 4", serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Times New Roman", "Source Serif 4", serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Times New Roman", "Source Serif 4", serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 1px`, `md: 2px`, `lg: 4px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Fondo muy oscuro, un beige de acción y la imagen como protagonista.
- Haz: Usa una serif editorial, no una sans de dashboard.
- No hagas: No copies obras ni el wordmark de la marca.
- No hagas: No ilumines la página ni uses un morado de «IA genérica».
