---
version: "alpha"
name: Supabase (análisis)
description: "Análisis independiente del estilo visual de Supabase (https://supabase.com)."
colors:
  primary: "#A9F1CA"
  on-primary: "#000000"
  secondary: "#3FCF8E"
  accent: "#79DDB0"
  background: "#FFFFFF"
  surface: "#A9F1CA"
  text: "#141414"
  muted: "#666666"
  border: "#DEDEDE"
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 3rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Manrope
    fontSize: 1.75rem
    fontWeight: 400
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
  sm: 4px
  md: 8px
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
    textColor: "{colors.on-primary}"
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

# Supabase: análisis de su estilo visual

> Análisis independiente de la portada pública de [Supabase](https://supabase.com), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fondo blanco u oscuro según sistema, verde esmeralda de marca y capturas de consola.

Tarjetas con bordes finos, tipografía técnica y botones pequeños verdes.

## Colores

Fondo claro `#FFFFFF` con texto `#141414`. El color de acción es `#A9F1CA` (texto encima `#000000`); `#3FCF8E` y `#79DDB0` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Manrope** (peso 500, unos 46px en escritorio) y texto en **Inter** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son rectángulos con radio 8px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#A9F1CA`).
- Haz: usa Manrope solo en titulares y deja el texto en Inter.
- No hagas: copiar el logotipo, las fotografías o los textos de Supabase; crea los tuyos.
