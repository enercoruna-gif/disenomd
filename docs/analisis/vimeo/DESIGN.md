---
version: "alpha"
name: Vimeo (análisis)
description: "Análisis independiente del estilo visual de Vimeo (https://vimeo.com)."
colors:
  primary: "#00ADEF"
  on-primary: "#FFFFFF"
  secondary: "#E8F7FC"
  accent: "#00ADEF"
  background: "#FFFFFF"
  surface: "#F5FBFD"
  text: "#1A2E35"
  muted: "#5A6A70"
  border: "#DCE6EA"
typography:
  display-lg:
    fontFamily: '"Vimeo Circular", "Inter", sans-serif'
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"Vimeo Circular", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Vimeo Circular", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Vimeo Circular", "Inter", sans-serif'
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
    padding: 12px 22px
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

# Vimeo: análisis de su estilo visual

> Análisis independiente de la portada pública de [Vimeo](https://vimeo.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Cian de reproductor, tipografía redonda y un tono más editorial que un cortador de clips: el vídeo se presenta con calma.

Vimeo se pinta en cian #00ADEF sobre blanco, con un texto azul petróleo. Es una plataforma de vídeo que se siente más autor que algoritmo.

## Colores

Fondo #FFFFFF, texto #1A2E35, acción #00ADEF y un cian pálido #E8F7FC en apoyos. Superficies #F5FBFD.

## Tipografía

- `display-lg`: `"Vimeo Circular", "Inter", sans-serif`; tamaño `2.75rem`, peso `700`.
- `headline-md`: `"Vimeo Circular", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Vimeo Circular", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Vimeo Circular", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 4px`, `md: 8px`, `lg: 12px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Un solo cian de acción y el reproductor en el centro.
- Haz: Mantén un tono editorial, no de feed infinito.
- No hagas: No copies el logotipo ni players de terceros de su sitio.
- No hagas: No uses el rojo de otras plataformas de vídeo.
