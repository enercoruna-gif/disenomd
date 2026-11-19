---
version: "alpha"
name: Mercury (análisis)
description: "Análisis independiente del estilo visual de Mercury (https://mercury.com)."
colors:
  primary: "#5266EB"
  on-primary: "#FFFFFF"
  secondary: "#CDDDFF"
  accent: "#EDEDF3"
  background: "#FFFFFF"
  surface: "#CDDDFF"
  text: "#141414"
  muted: "#666666"
  border: "#DEDEDE"
typography:
  display-lg:
    fontFamily: arcadiaDisplay
    fontSize: 3rem
    fontWeight: 480
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: arcadiaDisplay
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: arcadia
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: arcadia
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

# Mercury: análisis de su estilo visual

> Análisis independiente de la portada pública de [Mercury](https://mercury.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Paisaje fotográfico de montaña bajo un titular blanco centrado, con un campo de correo y botón azul integrados.

Azul lavanda en el botón píldora, tipografía display propia y fondos azul tinta muy oscuros en el resto de la página.

## Colores

Fondo claro `#FFFFFF` con texto `#141414`. El color de acción es `#5266EB` (texto encima `#FFFFFF`); `#CDDDFF` y `#EDEDF3` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **arcadiaDisplay** (peso 480, unos 45.0784px en escritorio) y texto en **arcadia** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 12px; los botones son rectángulos con radio 12px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#5266EB`).
- Haz: usa arcadiaDisplay solo en titulares y deja el texto en arcadia.
- No hagas: copiar el logotipo, las fotografías o los textos de Mercury; crea los tuyos.
