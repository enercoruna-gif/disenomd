---
version: "alpha"
name: Todoist (análisis)
description: "Análisis independiente del estilo visual de Todoist (https://www.todoist.com/es)."
colors:
  primary: "#E44332"
  on-primary: "#FFFFFF"
  secondary: "#FAF5F4"
  accent: "#E44332"
  background: "#FFFFFF"
  surface: "#FFFFFF"
  text: "#1F1F1F"
  muted: "#6B6B6B"
  border: "#EDEDED"
typography:
  display-lg:
    fontFamily: '"Graphik", "Inter", sans-serif'
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"Graphik", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Graphik", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Graphik", "Inter", sans-serif'
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

# Todoist: análisis de su estilo visual

> Análisis independiente de la portada pública de [Todoist](https://www.todoist.com/es), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Rojo de tarea sobre blanco, una lista nítida y tipografía neutra: la productividad se reduce a marcar lo que toca hoy.

Todoist se explica con un rojo #E44332 y una lista. El fondo es blanco, el ruido es mínimo y el componente es la tarea, no un tablero recargado.

## Colores

Fondo #FFFFFF, texto #1F1F1F, acción #E44332 y un rojo muy pálido #FAF5F4 en apoyos. Bordes #EDEDED.

## Tipografía

- `display-lg`: `"Graphik", "Inter", sans-serif`; tamaño `2.75rem`, peso `700`.
- `headline-md`: `"Graphik", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Graphik", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Graphik", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 4px`, `md: 8px`, `lg: 10px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Un rojo de acción y una lista que se lee de un vistazo.
- Haz: Deja mucho blanco; no conviertas la home en un panel de métricas.
- No hagas: No copies el logotipo ni su karma visual.
- No hagas: No uses un rojo de alarma en todos los botones secundarios.
