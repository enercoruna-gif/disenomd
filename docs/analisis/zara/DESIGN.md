---
version: "alpha"
name: Zara (análisis)
description: "Análisis independiente del estilo visual de Zara (https://www.zara.com/es/)."
colors:
  primary: "#000000"
  on-primary: "#FFFFFF"
  secondary: "#F5F5F5"
  accent: "#000000"
  background: "#FFFFFF"
  surface: "#FFFFFF"
  text: "#000000"
  muted: "#666666"
  border: "#E5E5E5"
typography:
  display-lg:
    fontFamily: '"Helvetica Neue", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
  headline-md:
    fontFamily: '"Helvetica Neue", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Helvetica Neue", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Helvetica Neue", "Inter", sans-serif'
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

# Zara: análisis de su estilo visual

> Análisis independiente de la portada pública de [Zara](https://www.zara.com/es/), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Minimalismo de tienda: tipografía pequeña, a menudo en versales, fotografía de prenda y casi cero interfaz alrededor.

Zara reduce la web a la prenda y a un nombre. Fondo blanco, negro, letras menudas y sin radios. La moda se presenta en silencio, no con banners.

## Colores

Solo blanco y negro, con un gris #666666 para el secundario y un borde #E5E5E5. No hay un color de oferta que rompa la página.

## Tipografía

- `display-lg`: `"Helvetica Neue", "Inter", sans-serif`; tamaño `1.75rem`, peso `500`.
- `headline-md`: `"Helvetica Neue", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Helvetica Neue", "Inter", sans-serif`; tamaño `0.8125rem`, peso `400`.
- `label-sm`: `"Helvetica Neue", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 0px`, `md: 0px`, `lg: 0px`, `full: 0px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Deja que la foto de la prenda mande y comprime la interfaz.
- Haz: Usa tipografía pequeña y tracking en las etiquetas.
- No hagas: No copies campañas ni looks de la marca.
- No hagas: No uses colores de reclamación ni badges de descuento chillones.
