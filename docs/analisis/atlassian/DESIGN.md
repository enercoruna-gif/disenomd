---
version: "alpha"
name: Atlassian (análisis)
description: "Análisis independiente del estilo visual de Atlassian (https://www.atlassian.com)."
colors:
  primary: "#1868DB"
  on-primary: "#FFFFFF"
  secondary: "#2684FF"
  accent: "#FFC400"
  background: "#FFFFFF"
  surface: "#F4F5F7"
  text: "#172B4D"
  muted: "#626F86"
  border: "#DFE1E6"
typography:
  display-lg:
    fontFamily: '"Charlie Display", "Inter", sans-serif'
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  headline-md:
    fontFamily: '"Charlie Display", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Charlie Display", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Charlie Display", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 1px
  md: 3px
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
    padding: 10px 16px
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

# Atlassian: análisis de su estilo visual

> Análisis independiente de la portada pública de [Atlassian](https://www.atlassian.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Azul de producto Atlassian, texto en navy y una retícula de herramientas: Jira, Confluence y el resto, presentadas con rigor.

Atlassian ordena el trabajo en azul #1868DB y un navy #172B4D. La portada es de plataforma: clara, corporativa y muy de producto.

## Colores

Fondo #FFFFFF, texto #172B4D, acción #1868DB, un azul más claro #2684FF y un amarillo #FFC400 muy puntual. Superficies #F4F5F7.

## Tipografía

- `display-lg`: `"Charlie Display", "Inter", sans-serif`; tamaño `2.75rem`, peso `700`.
- `headline-md`: `"Charlie Display", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Charlie Display", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Charlie Display", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 1px`, `md: 3px`, `lg: 8px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: El azul es la acción; el amarillo, un acento mínimo.
- Haz: Presenta productos en una retícula constante y sobria.
- No hagas: No copies los logotipos de Jira, Confluence u otras herramientas.
- No hagas: No mezcles este azul con un navy de otra marca.
