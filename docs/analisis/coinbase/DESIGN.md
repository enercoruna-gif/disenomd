---
version: "alpha"
name: Coinbase (análisis)
description: "Análisis independiente del estilo visual de Coinbase (https://www.coinbase.com/es)."
colors:
  primary: "#0052FF"
  on-primary: "#FFFFFF"
  secondary: "#EEF2FF"
  accent: "#0052FF"
  background: "#FFFFFF"
  surface: "#F4F7FF"
  text: "#0A0B0D"
  muted: "#5B616E"
  border: "#E5E8ED"
typography:
  display-lg:
    fontFamily: '"Coinbase Sans", "Inter", sans-serif'
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"Coinbase Sans", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Coinbase Sans", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Coinbase Sans", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 32px
  md: 64px
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
    padding: 14px 24px
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

# Coinbase: análisis de su estilo visual

> Análisis independiente de la portada pública de [Coinbase](https://www.coinbase.com/es), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Azul confiable de exchange, tipografía propia y botones muy redondos: cripto presentada como un banco claro, no como un casino.

Coinbase se apoya en un azul #0052FF, mucho blanco y una tipografía geométrica. Quiere parecer una entidad financiera, no un ticker nervioso.

## Colores

Fondo #FFFFFF, texto #0A0B0D, acción #0052FF y superficies en #F4F7FF. El azul pálido #EEF2FF marca estados suaves.

## Tipografía

- `display-lg`: `"Coinbase Sans", "Inter", sans-serif`; tamaño `3rem`, peso `700`.
- `headline-md`: `"Coinbase Sans", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Coinbase Sans", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Coinbase Sans", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 32px`, `md: 64px`, `lg: 16px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Un solo azul de acción y cifras muy legibles.
- Haz: Redondea los botones y mantén el fondo claro.
- No hagas: No copies su logotipo ni sus ilustraciones de monedas.
- No hagas: No uses verdes y rojos de ticker como color de marca.
