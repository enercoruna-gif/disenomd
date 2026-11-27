---
version: "alpha"
name: Perplexity (análisis)
description: "Análisis independiente del estilo visual de Perplexity (https://www.perplexity.ai)."
colors:
  primary: "#20808D"
  on-primary: "#FFFFFF"
  secondary: "#E8F4F4"
  accent: "#22B8A0"
  background: "#FFFFFF"
  surface: "#F7F7F4"
  text: "#13343B"
  muted: "#5C6B6E"
  border: "#E3E8E8"
typography:
  display-lg:
    fontFamily: '"FK Grotesk", "Inter", sans-serif'
    fontSize: 2.5rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.03em
  headline-md:
    fontFamily: '"FK Grotesk", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"FK Grotesk", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"FK Grotesk", "Inter", sans-serif'
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

# Perplexity: análisis de su estilo visual

> Análisis independiente de la portada pública de [Perplexity](https://www.perplexity.ai), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Turquesa de consulta, un campo de pregunta en el centro y una tipografía neutra: parece un motor de respuestas, no un chat recargado.

Perplexity organiza la página alrededor de una pregunta. El turquesa #20808D es el acento, el fondo es claro y el componente es el campo de búsqueda.

## Colores

Fondo #FFFFFF, superficies en #F7F7F4, texto #13343B, acción #20808D y un acento más vivo #22B8A0. Bordes #E3E8E8.

## Tipografía

- `display-lg`: `"FK Grotesk", "Inter", sans-serif`; tamaño `2.5rem`, peso `700`.
- `headline-md`: `"FK Grotesk", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"FK Grotesk", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"FK Grotesk", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 12px`, `md: 24px`, `lg: 16px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: El campo de pregunta es el centro; el turquesa, el único acento.
- Haz: Muestra fuentes con calma, no como un muro de enlaces.
- No hagas: No copies su logotipo ni la disposición exacta del buscador.
- No hagas: No uses un morado genérico de «IA».
