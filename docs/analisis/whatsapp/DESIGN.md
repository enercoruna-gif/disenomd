---
version: "alpha"
name: WhatsApp (análisis)
description: "Análisis independiente del estilo visual de WhatsApp (https://www.whatsapp.com)."
colors:
  primary: "#25D366"
  on-primary: "#FFFFFF"
  secondary: "#128C7E"
  accent: "#25D366"
  background: "#FFFFFF"
  surface: "#F0F2F5"
  text: "#111B21"
  muted: "#667781"
  border: "#E9EDEF"
typography:
  display-lg:
    fontFamily: '"Helvetica Neue", "Inter", sans-serif'
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"Helvetica Neue", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Helvetica Neue", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Helvetica Neue", "Inter", sans-serif'
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

# WhatsApp: análisis de su estilo visual

> Análisis independiente de la portada pública de [WhatsApp](https://www.whatsapp.com), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Verde conversación sobre un fondo muy claro, botones en píldora y una tipografía neutra que habla de algo cercano y cotidiano.

WhatsApp se explica en verde #25D366 y un texto casi negro. La portada es simple: un mensaje claro, un botón de descarga o de empezar, y poco más.

## Colores

Fondo #FFFFFF, texto #111B21. El verde #25D366 es la acción; un verde más profundo #128C7E aparece en apoyos. El gris #F0F2F5 hace de superficie de chat.

## Tipografía

- `display-lg`: `"Helvetica Neue", "Inter", sans-serif`; tamaño `2.75rem`, peso `700`.
- `headline-md`: `"Helvetica Neue", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Helvetica Neue", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Helvetica Neue", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 12px`, `md: 24px`, `lg: 16px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Usa el verde solo para la acción principal.
- Haz: Mantén la interfaz tan simple como una conversación.
- No hagas: No copies la marca ni las burbujas de su aplicación.
- No hagas: No oscurezcas el fondo hasta parecer un tema cripto.
