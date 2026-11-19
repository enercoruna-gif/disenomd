---
version: "alpha"
name: Cal.com (análisis)
description: "Análisis independiente del estilo visual de Cal.com (https://cal.com)."
colors:
  primary: "#FF5F57"
  on-primary: "#000000"
  secondary: "#883834"
  accent: "#242424"
  background: "#FFFFFF"
  surface: "#F3F4F6"
  text: "#111111"
  muted: "#242424"
  border: "#DEDEDE"
typography:
  display-lg:
    fontFamily: calSans
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: calSans
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: calSans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: calSans
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

# Cal.com: análisis de su estilo visual

> Análisis independiente de la portada pública de [Cal.com](https://cal.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Interfaz en blanco y negro con una display redondeada propia y capturas de la agenda en tarjetas con sombra suave.

Botones negros en píldora, bordes finos grises y casi nada de color.

## Colores

Fondo claro `#FFFFFF` con texto `#111111`. El color de acción es `#FF5F57` (texto encima `#000000`); `#883834` y `#242424` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **calSans** (peso 700, unos 80px en escritorio) y texto en **calSans** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 12px; los botones son rectángulos con radio 12px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#FF5F57`).
- Haz: usa calSans solo en titulares y deja el texto en calSans.
- No hagas: copiar el logotipo, las fotografías o los textos de Cal.com; crea los tuyos.
