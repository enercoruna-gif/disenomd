---
version: "alpha"
name: Netflix (análisis)
description: "Análisis independiente del estilo visual de Netflix (https://www.netflix.com/es)."
colors:
  primary: "#E50914"
  on-primary: "#FFFFFF"
  secondary: "#B3B3B3"
  accent: "#E50914"
  background: "#141414"
  surface: "#1F1F1F"
  text: "#FFFFFF"
  muted: "#B3B3B3"
  border: "#2F2F2F"
typography:
  display-lg:
    fontFamily: '"Netflix Sans", "Inter", sans-serif'
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"Netflix Sans", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Netflix Sans", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Netflix Sans", "Inter", sans-serif'
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
    padding: 12px 24px
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

# Netflix: análisis de su estilo visual

> Análisis independiente de la portada pública de [Netflix](https://www.netflix.com/es), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fondo casi negro y un único rojo de acción. Los titulares ocupan la pantalla; las series se recorren en carriles horizontales de carteles.

Una sala a oscuras: fondo #141414, tipografía grande y un rojo #E50914 que solo sirve para reproducir o contratar. El resto de la interfaz se apaga para que mande la imagen.

## Colores

Fondo #141414 y texto blanco. El único color de acción es #E50914 (texto encima #FFFFFF). El gris #B3B3B3 se reserva a metadatos y a la navegación inactiva.

## Tipografía

- `display-lg`: `"Netflix Sans", "Inter", sans-serif`; tamaño `3rem`, peso `700`.
- `headline-md`: `"Netflix Sans", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Netflix Sans", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Netflix Sans", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 2px`, `md: 4px`, `lg: 8px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Deja un solo rojo de acción y apaga el resto de la interfaz.
- Haz: Usa tipografía grande y pesada en el titular, nunca en las etiquetas.
- No hagas: No copies el logotipo ni las claves visuales de series ajenas.
- No hagas: No llenes la portada de botones de colores distintos al rojo.
