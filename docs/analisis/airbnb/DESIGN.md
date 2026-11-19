---
version: "alpha"
name: Airbnb (análisis)
description: "Análisis independiente del estilo visual de Airbnb (https://www.airbnb.es)."
colors:
  primary: "#DA1249"
  on-primary: "#FFFFFF"
  secondary: "#7E1A36"
  accent: "#A55F72"
  background: "#FFFFFF"
  surface: "#DDDDDD"
  text: "#222222"
  muted: "#6C6C6C"
  border: "#E0E0E0"
typography:
  display-lg:
    fontFamily: Airbnb Cereal VF
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Airbnb Cereal VF
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Airbnb Cereal VF
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Airbnb Cereal VF
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 10px
  md: 20px
  lg: 40px
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
    textColor: "{colors.secondary}"
  tag:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.background}"
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

# Airbnb: análisis de su estilo visual

> Análisis independiente de la portada pública de [Airbnb](https://www.airbnb.es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Interfaz blanca y amable donde manda la fotografía: tarjetas de alojamiento con esquinas generosas y casi sin bordes.

El rosa coral se reserva para la búsqueda y las acciones de reserva; todo lo demás es gris neutro.

## Colores

Fondo claro `#FFFFFF` con texto `#222222`. El color de acción es `#DA1249` (texto encima `#FFFFFF`); `#7E1A36` y `#A55F72` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Airbnb Cereal VF** (peso 400, unos 14px en escritorio) y texto en **Airbnb Cereal VF** a 14px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 20px; los botones son rectángulos con radio 20px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#DA1249`).
- Haz: usa Airbnb Cereal VF solo en titulares y deja el texto en Airbnb Cereal VF.
- No hagas: copiar el logotipo, las fotografías o los textos de Airbnb; crea los tuyos.
