---
version: "alpha"
name: Calendly (análisis)
description: "Análisis independiente del estilo visual de Calendly (https://calendly.com)."
colors:
  primary: "#006BFF"
  on-primary: "#FFFFFF"
  secondary: "#F2F8FF"
  accent: "#006BFF"
  background: "#FFFFFF"
  surface: "#FFFFFF"
  text: "#0B0B0D"
  muted: "#6B6B76"
  border: "#E8E8ED"
typography:
  display-lg:
    fontFamily: '"Proxima Nova", "Inter", sans-serif'
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"Proxima Nova", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Proxima Nova", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Proxima Nova", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 20px
  md: 40px
  lg: 12px
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

# Calendly: análisis de su estilo visual

> Análisis independiente de la portada pública de [Calendly](https://calendly.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Una portada de reserva: azul limpio, mucho blanco y un calendario que se entiende en un vistazo, sin ruido de marketing.

Calendly invita a elegir una hora. El azul #006BFF es la única acción, el fondo es blanco y el componente estrella es la parrilla de horarios.

## Colores

Fondo y superficies blancos, texto #0B0B0D, acción #006BFF y un azul muy pálido #F2F8FF para estados seleccionados. Bordes #E8E8ED.

## Tipografía

- `display-lg`: `"Proxima Nova", "Inter", sans-serif`; tamaño `2.75rem`, peso `700`.
- `headline-md`: `"Proxima Nova", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Proxima Nova", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Proxima Nova", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 20px`, `md: 40px`, `lg: 12px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Un azul de confirmar y un calendario muy legible.
- Haz: Deja márgenes amplios; la reserva no debe parecer un formulario denso.
- No hagas: No copies su widget ni su logotipo.
- No hagas: No uses verdes de «éxito» que compitan con el azul de reserva.
