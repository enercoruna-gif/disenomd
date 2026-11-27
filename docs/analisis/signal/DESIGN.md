---
version: "alpha"
name: Signal (análisis)
description: "Análisis independiente del estilo visual de Signal (https://signal.org/es/)."
colors:
  primary: "#3A76F0"
  on-primary: "#FFFFFF"
  secondary: "#EEF3FE"
  accent: "#3A76F0"
  background: "#FFFFFF"
  surface: "#F7F9FC"
  text: "#1B1B1B"
  muted: "#5E5E5E"
  border: "#E3E6EA"
typography:
  display-lg:
    fontFamily: '"Inter", sans-serif'
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Inter", sans-serif'
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

# Signal: análisis de su estilo visual

> Análisis independiente de la portada pública de [Signal](https://signal.org/es/), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Azul de confianza, mucho blanco y una tipografía directa: la privacidad se explica sin teatralidad, con un botón claro de descarga.

Signal se presenta en azul #3A76F0 sobre blanco, con poco adorno. La página habla de una conversación privada, no de un ecosistema de funciones.

## Colores

Fondo #FFFFFF, texto #1B1B1B, acción #3A76F0 y un azul pálido #EEF3FE. Superficies #F7F9FC.

## Tipografía

- `display-lg`: `"Inter", sans-serif`; tamaño `2.75rem`, peso `700`.
- `headline-md`: `"Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 12px`, `md: 24px`, `lg: 16px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Un azul de descarga y un mensaje corto sobre privacidad.
- Haz: Mantén la interfaz tan simple como la app.
- No hagas: No copies el logotipo ni capturas literales de chats.
- No hagas: No oscurezcas el fondo ni añadas un verde de otra mensajería.
