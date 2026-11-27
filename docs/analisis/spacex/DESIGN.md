---
version: "alpha"
name: SpaceX (análisis)
description: "Análisis independiente del estilo visual de SpaceX (https://www.spacex.com)."
colors:
  primary: "#FFFFFF"
  on-primary: "#000000"
  secondary: "#111111"
  accent: "#A7A7A7"
  background: "#000000"
  surface: "#0A0A0A"
  text: "#FFFFFF"
  muted: "#8A8A8A"
  border: "#222222"
typography:
  display-lg:
    fontFamily: '"D-DIN", "Inter", sans-serif'
    fontSize: 3.5rem
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.04em
  headline-md:
    fontFamily: '"D-DIN", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"D-DIN", "Inter", sans-serif'
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"D-DIN", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 0px
  md: 0px
  lg: 0px
  full: 0px
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
    padding: 14px 28px
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

# SpaceX: análisis de su estilo visual

> Análisis independiente de la portada pública de [SpaceX](https://www.spacex.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Negro de hangar, versales técnicas y casi ningún color: la página parece un briefing de misión, no una landing comercial.

SpaceX reduce todo a negro, blanco y tipografía en versales. El hero es una imagen de vehículo o de cielo; el cromo desaparece.

## Colores

Fondo #000000, superficie #0A0A0A, texto y acción en #FFFFFF (el botón puede ser un recuadro blanco o un trazo). El gris #A7A7A7 es secundario. No hay un color de marca vivo.

## Tipografía

- `display-lg`: `"D-DIN", "Inter", sans-serif`; tamaño `3.5rem`, peso `500`.
- `headline-md`: `"D-DIN", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"D-DIN", "Inter", sans-serif`; tamaño `0.875rem`, peso `400`.
- `label-sm`: `"D-DIN", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 0px`, `md: 0px`, `lg: 0px`, `full: 0px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Usa solo blanco sobre negro y tipografía técnica en versales.
- Haz: Deja que una sola imagen de misión llene el hero.
- No hagas: No copies logotipos, insignias ni material de misión.
- No hagas: No añadas azules o naranjas de «tecnología espacial» de stock.
