---
version: "alpha"
name: Substack (análisis)
description: "Análisis independiente del estilo visual de Substack (https://substack.com)."
colors:
  primary: "#FF6719"
  on-primary: "#FFFFFF"
  secondary: "#FFF3EC"
  accent: "#FF6719"
  background: "#FFFFFF"
  surface: "#FFFFFF"
  text: "#1A1A1A"
  muted: "#6B6B6B"
  border: "#E6E6E6"
typography:
  display-lg:
    fontFamily: '"Source Serif 4", serif'
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  headline-md:
    fontFamily: '"Source Serif 4", serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Source Serif 4", serif'
    fontSize: 1.125rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Source Serif 4", serif'
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
    padding: 12px 18px
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

# Substack: análisis de su estilo visual

> Análisis independiente de la portada pública de [Substack](https://substack.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Naranja de suscripción y una serif de lectura: parece una newsletter, no una red social, con el texto en el centro.

Substack se lee como una publicación: serif en el título, un naranja #FF6719 para suscribirse y una columna de lectura estrecha.

## Colores

Fondo blanco, texto #1A1A1A, acción #FF6719 y un naranja pálido #FFF3EC en fondos de apoyo. Casi no hay más color.

## Tipografía

- `display-lg`: `"Source Serif 4", serif`; tamaño `3rem`, peso `700`.
- `headline-md`: `"Source Serif 4", serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Source Serif 4", serif`; tamaño `1.125rem`, peso `400`.
- `label-sm`: `"Source Serif 4", serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 2px`, `md: 4px`, `lg: 8px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Pon la lectura en el centro y el naranja solo en suscribirse.
- Haz: Usa una serif editorial, no una display decorativa.
- No hagas: No copies cabeceras ni nombres de boletines ajenos.
- No hagas: No conviertas la portada en un feed de cards coloridas.
