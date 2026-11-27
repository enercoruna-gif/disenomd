---
version: "alpha"
name: HubSpot (análisis)
description: "Análisis independiente del estilo visual de HubSpot (https://www.hubspot.com)."
colors:
  primary: "#FF7A59"
  on-primary: "#FFFFFF"
  secondary: "#2D3E50"
  accent: "#FF7A59"
  background: "#FFFFFF"
  surface: "#FFF5F2"
  text: "#2D3E50"
  muted: "#516F90"
  border: "#E6E6E6"
typography:
  display-lg:
    fontFamily: '"Avenir Next", "Inter", sans-serif'
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  headline-md:
    fontFamily: '"Avenir Next", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Avenir Next", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Avenir Next", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 12px
  md: 24px
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
    rounded: "{rounded.full}"
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

# HubSpot: análisis de su estilo visual

> Análisis independiente de la portada pública de [HubSpot](https://www.hubspot.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Naranja coral de marketing sobre un azul pizarra en el texto: cercano, de producto, con botones redondos que piden una demo.

HubSpot se reconoce por el coral #FF7A59 y un texto en azul pizarra #2D3E50. Es una web de software que quiere parecer accesible, no fría.

## Colores

Fondo #FFFFFF, texto #2D3E50, acción #FF7A59 y una superficie cálida #FFF5F2. El gris azulado #516F90 es el secundario.

## Tipografía

- `display-lg`: `"Avenir Next", "Inter", sans-serif`; tamaño `2.75rem`, peso `700`.
- `headline-md`: `"Avenir Next", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Avenir Next", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Avenir Next", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 12px`, `md: 24px`, `lg: 12px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: El coral es el único CTA; el texto se queda en pizarra.
- Haz: Usa formas amables y bloques de producto fáciles de escanear.
- No hagas: No copies sus ilustraciones ni el sprocket de marca.
- No hagas: No sustituyas el coral por un naranja genérico de oferta.
