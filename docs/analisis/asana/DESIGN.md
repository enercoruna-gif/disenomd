---
version: "alpha"
name: Asana (análisis)
description: "Análisis independiente del estilo visual de Asana (https://asana.com/es)."
colors:
  primary: "#F06A6A"
  on-primary: "#FFFFFF"
  secondary: "#F6F4F2"
  accent: "#F06A6A"
  background: "#FFFFFF"
  surface: "#F6F4F2"
  text: "#1E1F21"
  muted: "#6D6E6F"
  border: "#E8E6E3"
typography:
  display-lg:
    fontFamily: '"Asana Sans", "Inter", sans-serif'
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"Asana Sans", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Asana Sans", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Asana Sans", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 8px
  md: 16px
  lg: 16px
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

# Asana: análisis de su estilo visual

> Análisis independiente de la portada pública de [Asana](https://asana.com/es), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Coral humano, fondos cálidos y formas redondas: una herramienta de equipo que se presenta como cercana, no como un Gantt frío.

Asana se reconoce por el coral #F06A6A y un fondo cálido #F6F4F2. La tipografía es amable y los bloques parecen post-its ordenados.

## Colores

Fondo #FFFFFF, texto #1E1F21, acción #F06A6A y superficies en el beige #F6F4F2. El gris #6D6E6F es secundario.

## Tipografía

- `display-lg`: `"Asana Sans", "Inter", sans-serif`; tamaño `2.75rem`, peso `700`.
- `headline-md`: `"Asana Sans", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Asana Sans", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Asana Sans", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 8px`, `md: 16px`, `lg: 16px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Un solo coral de acción sobre fondos cálidos.
- Haz: Redondea las formas y deja aire entre las tareas.
- No hagas: No copies su ilustración de personajes ni la marca.
- No hagas: No uses un rojo de alarma en vez de este coral.
