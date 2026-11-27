---
version: "alpha"
name: Hugging Face (análisis)
description: "Análisis independiente del estilo visual de Hugging Face (https://huggingface.co)."
colors:
  primary: "#FFD21E"
  on-primary: "#0A0A0A"
  secondary: "#FFFBEA"
  accent: "#FF9D00"
  background: "#FFFFFF"
  surface: "#FFFBEA"
  text: "#0A0A0A"
  muted: "#5C5C5C"
  border: "#E8E8E8"
typography:
  display-lg:
    fontFamily: '"Source Sans 3", "Inter", sans-serif'
    fontSize: 2.5rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  headline-md:
    fontFamily: '"Source Sans 3", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Source Sans 3", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Source Sans 3", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 5px
  md: 10px
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

# Hugging Face: análisis de su estilo visual

> Análisis independiente de la portada pública de [Hugging Face](https://huggingface.co), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Amarillo amable, tipografía clara y una comunidad de modelos: se siente a laboratorio abierto, no a producto cerrado.

Hugging Face se distingue por el amarillo #FFD21E sobre blanco y un tono de comunidad. La portada parece un directorio de modelos, no una campaña de lujo.

## Colores

Fondo #FFFFFF, texto #0A0A0A, acción #FFD21E (texto #0A0A0A), un acento #FF9D00 y superficies en #FFFBEA.

## Tipografía

- `display-lg`: `"Source Sans 3", "Inter", sans-serif`; tamaño `2.5rem`, peso `700`.
- `headline-md`: `"Source Sans 3", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Source Sans 3", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Source Sans 3", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 5px`, `md: 10px`, `lg: 12px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: El amarillo es el CTA, con texto oscuro encima.
- Haz: Organiza modelos en tarjetas claras, fáciles de escanear.
- No hagas: No copies la mascota ni el logotipo.
- No hagas: No sustituyas el amarillo por un negro corporativo que apague el carácter.
