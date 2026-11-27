---
version: "alpha"
name: SoundCloud (análisis)
description: "Análisis independiente del estilo visual de SoundCloud (https://soundcloud.com)."
colors:
  primary: "#FF5500"
  on-primary: "#FFFFFF"
  secondary: "#FFF3ED"
  accent: "#FF5500"
  background: "#FFFFFF"
  surface: "#F8F8F8"
  text: "#121212"
  muted: "#666666"
  border: "#E5E5E5"
typography:
  display-lg:
    fontFamily: '"Interstate", "Inter", sans-serif'
    fontSize: 2.5rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  headline-md:
    fontFamily: '"Interstate", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Interstate", "Inter", sans-serif'
    fontSize: 0.9375rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Interstate", "Inter", sans-serif'
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

# SoundCloud: análisis de su estilo visual

> Análisis independiente de la portada pública de [SoundCloud](https://soundcloud.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Naranja de onda, una forma de audio que se recorre en horizontal y tipografía compacta: más estudio compartido que magazine.

SoundCloud se reconoce por el naranja #FF5500 y la onda de la pista. El resto es blanco, negro y una interfaz densa de descubrimiento.

## Colores

Fondo #FFFFFF, texto #121212, acción #FF5500 y un naranja pálido #FFF3ED. Superficies #F8F8F8.

## Tipografía

- `display-lg`: `"Interstate", "Inter", sans-serif`; tamaño `2.5rem`, peso `700`.
- `headline-md`: `"Interstate", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Interstate", "Inter", sans-serif`; tamaño `0.9375rem`, peso `400`.
- `label-sm`: `"Interstate", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 2px`, `md: 4px`, `lg: 8px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: El naranja solo en la onda y en el reproducir.
- Haz: Deja que la pista se lea como una fila, no como una card de álbum enorme.
- No hagas: No copies la nube de la marca ni ondas de artistas ajenos.
- No hagas: No uses un naranja de descuento en toda la cabecera.
