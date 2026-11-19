---
version: "alpha"
name: June (análisis)
description: "Análisis independiente del estilo visual de June (https://www.june.so)."
colors:
  primary: "#2A2A63"
  on-primary: "#FFFFFF"
  secondary: "#20204A"
  accent: "#636380"
  background: "#FFFFFF"
  surface: "#FAFAFA"
  text: "#151531"
  muted: "#2A2A63"
  border: "#DEDEE2"
typography:
  display-lg:
    fontFamily: SF Pro Rounded
    fontSize: 3rem
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: SF Pro Rounded
    fontSize: 1.75rem
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Inter
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

# June: análisis de su estilo visual

> Análisis independiente de la portada pública de [June](https://www.june.so), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fondo gris muy claro con titular negro centrado en una sans redondeada y muy gruesa.

Bloque de texto tipo carta sobre un panel lila pálido de esquinas de 12 px; tono sobrio y editorial.

## Colores

Fondo claro `#FFFFFF` con texto `#151531`. El color de acción es `#2A2A63` (texto encima `#FFFFFF`); `#20204A` y `#636380` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **SF Pro Rounded** (peso 900, unos 60px en escritorio) y texto en **Inter** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 12px; los botones son rectángulos con radio 12px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#2A2A63`).
- Haz: usa SF Pro Rounded solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de June; crea los tuyos.
