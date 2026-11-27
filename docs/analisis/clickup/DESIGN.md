---
version: "alpha"
name: ClickUp (análisis)
description: "Análisis independiente del estilo visual de ClickUp (https://clickup.com)."
colors:
  primary: "#7B68EE"
  on-primary: "#FFFFFF"
  secondary: "#F3F0FF"
  accent: "#7B68EE"
  background: "#FFFFFF"
  surface: "#FFFFFF"
  text: "#1E1E2A"
  muted: "#6B6B80"
  border: "#E8E6F0"
typography:
  display-lg:
    fontFamily: '"Inter", sans-serif'
    fontSize: 2.85rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 6px
  md: 12px
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

# ClickUp: análisis de su estilo visual

> Análisis independiente de la portada pública de [ClickUp](https://clickup.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Violeta de producto, titulares ambiciosos y una interfaz que promete «todo en uno» con bloques nítidos y mucho contraste de tipo.

ClickUp se apoya en el violeta #7B68EE y en titulares grandes que hablan de unificar el trabajo. El fondo es blanco y la interfaz se siente de herramienta potente.

## Colores

Fondo #FFFFFF, texto #1E1E2A, acción #7B68EE y un violeta muy claro #F3F0FF para fondos de apoyo. Bordes #E8E6F0.

## Tipografía

- `display-lg`: `"Inter", sans-serif`; tamaño `2.85rem`, peso `700`.
- `headline-md`: `"Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 6px`, `md: 12px`, `lg: 16px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Un violeta de acción y un titular que explique el producto en una línea.
- Haz: Enseña la herramienta, no solo el eslogan.
- No hagas: No copies su logotipo ni la disposición exacta del panel.
- No hagas: No uses un púrpura de lujo que lo aleje de este tono de producto.
