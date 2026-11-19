---
version: "alpha"
name: Eraser (análisis)
description: "Análisis independiente del estilo visual de Eraser (https://www.eraser.io)."
colors:
  primary: "#171717"
  on-primary: "#FFFFFF"
  secondary: "#1E1E1E"
  accent: "#FFFFFF"
  background: "#FCFBF9"
  surface: "#FFFFFF"
  text: "#242424"
  muted: "#3A3A3A"
  border: "#DEDDDB"
typography:
  display-lg:
    fontFamily: Inter var
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter var
    fontSize: 1.75rem
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter var
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Inter var
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 6px
  md: 12px
  lg: 24px
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

# Eraser: análisis de su estilo visual

> Análisis independiente de la portada pública de [Eraser](https://www.eraser.io), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Blanco cálido con titular centrado enorme en sans gris oscuro y etiquetas de colores en línea bajo el título.

Botón negro sólido y otro con borde, radios de 8 px y un diagrama técnico como imagen principal.

## Colores

Fondo claro `#FCFBF9` con texto `#242424`. El color de acción es `#171717` (texto encima `#FFFFFF`); `#1E1E1E` y `#FFFFFF` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Inter var** (peso 600, unos 78px en escritorio) y texto en **Inter var** a 14px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 12px; los botones son rectángulos con radio 12px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#171717`).
- Haz: usa Inter var solo en titulares y deja el texto en Inter var.
- No hagas: copiar el logotipo, las fotografías o los textos de Eraser; crea los tuyos.
