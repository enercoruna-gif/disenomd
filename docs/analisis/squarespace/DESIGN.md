---
version: "alpha"
name: Squarespace (análisis)
description: "Análisis independiente del estilo visual de Squarespace (https://www.squarespace.com)."
colors:
  primary: "#000000"
  on-primary: "#FFFFFF"
  secondary: "#F5F4F0"
  accent: "#000000"
  background: "#FFFFFF"
  surface: "#F7F7F5"
  text: "#000000"
  muted: "#6B6B6B"
  border: "#E6E6E6"
typography:
  display-lg:
    fontFamily: '"Squarespace Sans", "Inter", sans-serif'
    fontSize: 3.25rem
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -0.04em
  headline-md:
    fontFamily: '"Squarespace Sans", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Squarespace Sans", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Squarespace Sans", "Inter", sans-serif'
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
    padding: 14px 22px
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

# Squarespace: análisis de su estilo visual

> Análisis independiente de la portada pública de [Squarespace](https://www.squarespace.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Editorial y seco: mucho blanco, un negro como única acción y titulares grandes, casi de revista, con muy poco adorno.

Squarespace vende control visual: tipografía tensa, márgenes amplios y un botón negro sobre blanco. Parece un portfolio, no un constructor de plantillas recargado.

## Colores

Blanco #FFFFFF, negro #000000 para texto y acción, un gris cálido #F7F7F5 en superficies y #6B6B6B en el texto secundario. Casi no hay un tercer color.

## Tipografía

- `display-lg`: `"Squarespace Sans", "Inter", sans-serif`; tamaño `3.25rem`, peso `500`.
- `headline-md`: `"Squarespace Sans", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Squarespace Sans", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Squarespace Sans", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 2px`, `md: 4px`, `lg: 8px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Usa el negro como único CTA y deja respirar el titular.
- Haz: Compon páginas como si fueran una revista, no un panel.
- No hagas: No copies plantillas ni fotografías de su galería.
- No hagas: No añadas una paleta de acentos que rompa el blanco y negro.
