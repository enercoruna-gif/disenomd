---
version: "alpha"
name: Oura (análisis)
description: "Análisis independiente del estilo visual de Oura (https://ouraring.com/es)."
colors:
  primary: "#2A72DE"
  on-primary: "#FFFFFF"
  secondary: "#15396F"
  accent: "#5B749A"
  background: "#FFFFFF"
  surface: "#F7F1E8"
  text: "#000000"
  muted: "#4A4741"
  border: "#DBDBDB"
typography:
  display-lg:
    fontFamily: Editorial New
    fontSize: 3rem
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Editorial New
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: AkkuratLL
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: AkkuratLL
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
    rounded: "{rounded.full}"
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

# Oura: análisis de su estilo visual

> Análisis independiente de la portada pública de [Oura](https://ouraring.com/es), hecho por diseño.md el 19 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Fondo crema cálido con titular en serif fina de gran tamaño y la foto del producto centrada.

Azul intenso solo en el botón píldora, texto marrón grisáceo y una franja superior de aviso discreta.

## Colores

Fondo claro `#FFFFFF` con texto `#000000`. El color de acción es `#2A72DE` (texto encima `#FFFFFF`); `#15396F` y `#5B749A` aparecen en detalles y etiquetas.

## Tipografía

Titulares en **Editorial New** (peso 300, unos 80px en escritorio) y texto en **AkkuratLL** a 16px. Si esa fuente no está disponible, usa **Inter** como alternativa libre de Google Fonts.

## Formas y espaciado

Radio habitual de 8px; los botones son píldoras. Espaciado en múltiplos de 8px, con bloques de 64px entre secciones.

## Qué hacer y qué no

- Haz: respeta la jerarquía de un solo color de acción (`#2A72DE`).
- Haz: usa Editorial New solo en titulares y deja el texto en AkkuratLL.
- No hagas: copiar el logotipo, las fotografías o los textos de Oura; crea los tuyos.
