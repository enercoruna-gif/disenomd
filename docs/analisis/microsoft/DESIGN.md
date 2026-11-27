---
version: "alpha"
name: Microsoft (análisis)
description: "Análisis independiente del estilo visual de Microsoft (https://www.microsoft.com/es-es)."
colors:
  primary: "#0078D4"
  on-primary: "#FFFFFF"
  secondary: "#50E6FF"
  accent: "#FFB900"
  background: "#FFFFFF"
  surface: "#F5F5F5"
  text: "#1A1A1A"
  muted: "#605E5C"
  border: "#EDEBE9"
typography:
  display-lg:
    fontFamily: '"Segoe UI", "Inter", sans-serif'
    fontSize: 2.75rem
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.02em
  headline-md:
    fontFamily: '"Segoe UI", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Segoe UI", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Segoe UI", "Inter", sans-serif'
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
    padding: 10px 20px
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

# Microsoft: análisis de su estilo visual

> Análisis independiente de la portada pública de [Microsoft](https://www.microsoft.com/es-es), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Una portada clara, de producto: azul Fluent, mosaicos ordenados y tipografía Segoe que se lee como un sistema operativo, no como una campaña.

Microsoft se presenta en blanco, con un azul #0078D4 para la acción y bloques de producto bien alineados. La página parece un escritorio ordenado más que una landing de moda.

## Colores

Fondo #FFFFFF y texto #1A1A1A. El azul #0078D4 es la acción; #50E6FF y #FFB900 aparecen en acentos de producto, no en el botón principal. Superficies en #F5F5F5.

## Tipografía

- `display-lg`: `"Segoe UI", "Inter", sans-serif`; tamaño `2.75rem`, peso `600`.
- `headline-md`: `"Segoe UI", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Segoe UI", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Segoe UI", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 2px`, `md: 4px`, `lg: 8px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Mantén el azul como única acción principal.
- Haz: Alinea productos en una rejilla constante, con mucho blanco.
- No hagas: No uses el logotipo de las cuatro casillas ni iconos oficiales.
- No hagas: No mezcles ese azul con otros azules ajenos a la paleta.
