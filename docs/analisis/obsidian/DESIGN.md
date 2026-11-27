---
version: "alpha"
name: Obsidian (análisis)
description: "Análisis independiente del estilo visual de Obsidian (https://obsidian.md)."
colors:
  primary: "#8B6CEF"
  on-primary: "#FFFFFF"
  secondary: "#2A2A2A"
  accent: "#8B6CEF"
  background: "#0D0D0D"
  surface: "#1A1A1A"
  text: "#DADADA"
  muted: "#9A9A9A"
  border: "#333333"
typography:
  display-lg:
    fontFamily: '"Inter", sans-serif'
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.15
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
  sm: 4px
  md: 8px
  lg: 10px
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

# Obsidian: análisis de su estilo visual

> Análisis independiente de la portada pública de [Obsidian](https://obsidian.md), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Oscuro de escritorio, un violeta de acento y una tipografía de editor: más taller de pensamiento que landing de consumo.

Obsidian se muestra en oscuro #0D0D0D con un violeta #8B6CEF. Parece una herramienta para escribir y enlazar ideas, no una app de notas pastel.

## Colores

Fondo #0D0D0D, superficie #1A1A1A, texto #DADADA, acción #8B6CEF y un gris #9A9A9A para lo secundario. Bordes #333333.

## Tipografía

- `display-lg`: `"Inter", sans-serif`; tamaño `2.75rem`, peso `700`.
- `headline-md`: `"Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 4px`, `md: 8px`, `lg: 10px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Mantén el oscuro y un solo violeta de acción.
- Haz: Diseña como un editor, no como una app de consumo.
- No hagas: No copies el cristal de la marca ni capturas literales del grafo.
- No hagas: No pases el fondo a blanco si quieres este carácter de taller.
