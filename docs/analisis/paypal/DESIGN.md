---
version: "alpha"
name: PayPal (análisis)
description: "Análisis independiente del estilo visual de PayPal (https://www.paypal.com/es/home)."
colors:
  primary: "#60CDFF"
  on-primary: "#000000"
  secondary: "#306680"
  accent: "#6E94A6"
  background: "#FFFFFF"
  surface: "#F1EFEA"
  text: "#000000"
  muted: "#595959"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: PayPal Pro
    fontSize: 3rem
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: PayPal Pro
    fontSize: 1.75rem
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: PayPal Pro Text VF
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: PayPal Pro Text VF
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

# PayPal: análisis de su estilo visual

> Análisis independiente de la portada pública de [PayPal](https://www.paypal.com/es/home), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Azul cielo de fondo con titular negro enorme y muy grueso, y una tarjeta blanca con fotografía en el centro.

Botones negros en píldora, cabecera blanca y azul marino de marca solo en el logotipo y la barra superior.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#60CDFF` (texto encima `#000000`); `#306680` y `#6E94A6` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **PayPal Pro** (peso 900, unos 82.9291px en escritorio) y texto en **PayPal Pro Text VF** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 12px; los botones son rectángulos con radio 12px. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#60CDFF`).
- Haz: usa PayPal Pro solo en titulares y deja el texto en PayPal Pro Text VF.
- No hagas: copiar el logotipo, las fotografías o los textos de PayPal; crea los tuyos.
