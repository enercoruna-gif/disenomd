---
version: "alpha"
name: Sketch (análisis)
description: "Análisis independiente del estilo visual de Sketch (https://www.sketch.com)."
colors:
  primary: "#F7B500"
  on-primary: "#000000"
  secondary: "#F7F7F7"
  accent: "#F7B500"
  background: "#FFFFFF"
  surface: "#FFFFFF"
  text: "#171717"
  muted: "#6B6B6B"
  border: "#E8E8E8"
typography:
  display-lg:
    fontFamily: '"Eina", "Inter", sans-serif'
    fontSize: 2.85rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"Eina", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Eina", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Eina", "Inter", sans-serif'
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

# Sketch: análisis de su estilo visual

> Análisis independiente de la portada pública de [Sketch](https://www.sketch.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Amarillo de diamante, mucho blanco y una tipografía de producto Mac: limpia, precisa, con el lienzo como promesa.

Sketch se identifica con el amarillo #F7B500 y un negro de texto sobre blanco. Es una portada de herramienta de diseño, nítida y contenida.

## Colores

Fondo #FFFFFF, texto #171717, acción #F7B500 (texto #000000) y superficies #F7F7F7. El amarillo no se usa como fondo masivo.

## Tipografía

- `display-lg`: `"Eina", "Inter", sans-serif`; tamaño `2.85rem`, peso `700`.
- `headline-md`: `"Eina", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Eina", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Eina", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 4px`, `md: 8px`, `lg: 12px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: El amarillo es el CTA, con texto negro.
- Haz: Muestra el lienzo; no recargues la portada de features.
- No hagas: No copies el diamante de la marca ni la UI literal.
- No hagas: No sustituyas el amarillo por un naranja genérico de oferta.
