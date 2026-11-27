---
version: "alpha"
name: YouTube (análisis)
description: "Análisis independiente del estilo visual de YouTube (https://www.youtube.com)."
colors:
  primary: "#FF0000"
  on-primary: "#FFFFFF"
  secondary: "#0F0F0F"
  accent: "#065FD4"
  background: "#FFFFFF"
  surface: "#F8F8F8"
  text: "#0F0F0F"
  muted: "#606060"
  border: "#E5E5E5"
typography:
  display-lg:
    fontFamily: '"YouTube Sans", "Inter", sans-serif'
    fontSize: 2.5rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  headline-md:
    fontFamily: '"YouTube Sans", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"YouTube Sans", "Inter", sans-serif'
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"YouTube Sans", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 9px
  md: 18px
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
    rounded: "{rounded.full}"
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

# YouTube: análisis de su estilo visual

> Análisis independiente de la portada pública de [YouTube](https://www.youtube.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Blanco de fondo, un rojo inconfundible en el botón de ver y una rejilla de miniaturas con tipografía Roboto, densa y familiar.

YouTube organiza el vídeo como un tablón: miniaturas, títulos compactos y un rojo #FF0000 que apunta a reproducir. El resto es negro, gris y mucho blanco.

## Colores

Fondo #FFFFFF, texto #0F0F0F. El rojo #FF0000 es el acento de reproducción y de marca; los enlaces informativos pueden ir en #065FD4. Superficies en #F8F8F8.

## Tipografía

- `display-lg`: `"YouTube Sans", "Inter", sans-serif`; tamaño `2.5rem`, peso `700`.
- `headline-md`: `"YouTube Sans", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"YouTube Sans", "Inter", sans-serif`; tamaño `0.875rem`, peso `400`.
- `label-sm`: `"YouTube Sans", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 9px`, `md: 18px`, `lg: 12px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Reserva el rojo al ver o publicar, no a toda la cabecera.
- Haz: Deja que las miniaturas y el título corto hagan el trabajo.
- No hagas: No copies el botón de reproducción ni la marca.
- No hagas: No uses una paleta arcoíris en la navegación.
