---
version: "alpha"
name: Wix (análisis)
description: "Análisis independiente del estilo visual de Wix (https://es.wix.com)."
colors:
  primary: "#0C6EFC"
  on-primary: "#FFFFFF"
  secondary: "#F0F4FF"
  accent: "#0C6EFC"
  background: "#FFFFFF"
  surface: "#F7F8FA"
  text: "#0D0D11"
  muted: "#5C6370"
  border: "#E6E8EE"
typography:
  display-lg:
    fontFamily: '"Wix Madefor", "Inter", sans-serif'
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"Wix Madefor", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Wix Madefor", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Wix Madefor", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 9px
  md: 18px
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

# Wix: análisis de su estilo visual

> Análisis independiente de la portada pública de [Wix](https://es.wix.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Una landing de producto amable: azul vivo, titulares grandes y botones en píldora que invitan a empezar la web ya.

Wix habla en un azul #0C6EFC sobre blanco, con tipografía cercana y mucho valor de «empieza aquí». Se siente a constructor, no a revista de lujo.

## Colores

Fondo #FFFFFF, texto #0D0D11, acción #0C6EFC y una superficie fría #F7F8FA. El azul suave #F0F4FF sirve de fondo de apoyo.

## Tipografía

- `display-lg`: `"Wix Madefor", "Inter", sans-serif`; tamaño `3rem`, peso `700`.
- `headline-md`: `"Wix Madefor", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Wix Madefor", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Wix Madefor", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 9px`, `md: 18px`, `lg: 16px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Un solo azul de acción y un titular que explique el producto en una frase.
- Haz: Usa radios generosos, no una interfaz seca.
- No hagas: No copies su editor ni sus plantillas.
- No hagas: No oscurezcas toda la página: el sistema es claro y cercano.
