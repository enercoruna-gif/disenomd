---
version: "alpha"
name: monday.com (análisis)
description: "Análisis independiente del estilo visual de monday.com (https://monday.com)."
colors:
  primary: "#6161FF"
  on-primary: "#FFFFFF"
  secondary: "#00CA72"
  accent: "#FF3D57"
  background: "#FFFFFF"
  surface: "#F0F0FF"
  text: "#323338"
  muted: "#676879"
  border: "#E6E9EF"
typography:
  display-lg:
    fontFamily: '"Figtree", "Inter", sans-serif'
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"Figtree", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Figtree", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Figtree", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 12px
  md: 24px
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
    padding: 12px 22px
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

# monday.com: análisis de su estilo visual

> Análisis independiente de la portada pública de [monday.com](https://monday.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Un púrpura vivo, toques de color de tablero y una tipografía cercana: el trabajo se ve como un tablero alegre, no como un ERP.

monday.com entra con el violeta #6161FF y una paleta que recuerda las columnas de un tablero. Es software, pero se viste de juego organizado.

## Colores

Fondo #FFFFFF, texto #323338, acción #6161FF. El verde #00CA72 y el rosa #FF3D57 son acentos de estado, no botones rivales. Superficie #F0F0FF.

## Tipografía

- `display-lg`: `"Figtree", "Inter", sans-serif`; tamaño `2.75rem`, peso `700`.
- `headline-md`: `"Figtree", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Figtree", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Figtree", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 12px`, `md: 24px`, `lg: 16px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: El violeta es el CTA; los otros colores, solo estados del tablero.
- Haz: Usa formas juguetonas y una retícula de columnas.
- No hagas: No copies su logotipo ni capturas literales del producto.
- No hagas: No apagues la paleta hasta volverla corporativa gris.
