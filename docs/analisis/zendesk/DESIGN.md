---
version: "alpha"
name: Zendesk (análisis)
description: "Análisis independiente del estilo visual de Zendesk (https://www.zendesk.es)."
colors:
  primary: "#17494D"
  on-primary: "#FFFFFF"
  secondary: "#03363D"
  accent: "#1F73B7"
  background: "#FFFFFF"
  surface: "#F8F9F8"
  text: "#03363D"
  muted: "#4A5555"
  border: "#D5D8D7"
typography:
  display-lg:
    fontFamily: '"Zendesk typography", "Inter", sans-serif'
    fontSize: 2.75rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  headline-md:
    fontFamily: '"Zendesk typography", "Inter", sans-serif'
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: '"Zendesk typography", "Inter", sans-serif'
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: '"Zendesk typography", "Inter", sans-serif'
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.01em
rounded:
  sm: 12px
  md: 24px
  lg: 8px
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

# Zendesk: análisis de su estilo visual

> Análisis independiente de la portada pública de [Zendesk](https://www.zendesk.es), hecho por diseño.md el 22 de noviembre de 2026. No está afiliado ni respaldado por la marca. Úsalo como referencia de estilo para tu propia interfaz, no para copiar su identidad.

## Resumen

Un verde petróleo de servicio, mucho aire y una tipografía serena: parece un mostrador de ayuda, no un panel de tickets.

Zendesk se pinta en verdes profundos #17494D y #03363D sobre blanco. El tono es de soporte: claro, profesional y sin alardes.

## Colores

Fondo #FFFFFF, texto #03363D, botón #17494D y un azul #1F73B7 como acento de enlace. Superficies en #F8F9F8.

## Tipografía

- `display-lg`: `"Zendesk typography", "Inter", sans-serif`; tamaño `2.75rem`, peso `700`.
- `headline-md`: `"Zendesk typography", "Inter", sans-serif`; tamaño `1.75rem`, peso `600`.
- `body-md`: `"Zendesk typography", "Inter", sans-serif`; tamaño `1rem`, peso `400`.
- `label-sm`: `"Zendesk typography", "Inter", sans-serif`; tamaño `0.8125rem`, peso `500`.

Estos son los valores de la propuesta normalizada del documento, no una escala oficial ni una medición exacta de toda la web. Los tamaños en rem dependen de la raíz: con 16px, 3rem equivalen a 48px y 1rem a 16px. Las alternativas están expresadas en cada fontFamily; pueden cambiar el aspecto y las métricas. Los nombres de las fuentes de marca son referencias: no se incluyen sus archivos ni derechos de uso.

## Formas y espaciado

Radios de esta propuesta: `sm: 12px`, `md: 24px`, `lg: 8px`, `full: 9999px`. Espaciados: `xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`. Son tokens normalizados para aplicar el estilo, no mediciones universales de la marca.

## Qué hacer y qué no

- Haz: Usa el verde petróleo como acción y mantén el texto en el mismo registro.
- Haz: Diseña como un mostrador, no como un dashboard oscuro.
- No hagas: No copies su mascota ni el logotipo.
- No hagas: No uses un verde neón de startup que rompa este carácter.
