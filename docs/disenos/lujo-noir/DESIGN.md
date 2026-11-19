---
version: "alpha"
name: Lujo Noir
description: "Negro, champán y mucho espacio vacío."
colors:
  primary: "#C8A96A"
  on-primary: "#0D0D0D"
  secondary: "#F2EDE4"
  accent: "#76592F"
  background: "#0D0D0D"
  surface: "#171615"
  text: "#F2EDE4"
  muted: "#A39C90"
  border: "#2C2A27"
typography:
  display-lg:
    fontFamily: Cormorant Garamond
    fontSize: 3rem
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Cormorant Garamond
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Montserrat
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Montserrat
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  code-sm:
    fontFamily: IBM Plex Mono
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0em
rounded:
  sm: 0px
  md: 2px
  lg: 4px
  full: 999px
spacing:
  xs: 8px
  sm: 16px
  md: 32px
  lg: 48px
  xl: 80px
  2xl: 128px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.md}"
    padding: 12px 20px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: 12px 20px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: 24px
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px
    height: 44px
  chip:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.text}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 2px 10px
  caption:
    backgroundColor: "{colors.background}"
    textColor: "{colors.muted}"
    typography: "{typography.label-sm}"
  divider:
    backgroundColor: "{colors.border}"
    height: 1px
  hero-producto:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text}"
    typography: "{typography.display-lg}"
    padding: 96px 24px
  enlace-subrayado:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.label-sm}"
    padding: 4px 0
---

# Lujo Noir — DESIGN.md

> Negro, champán y mucho espacio vacío. Ideal para: Joyerías, moda, hoteles boutique, vinos, inmobiliaria premium.

Sistema de diseño original de diseño.md. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.

## Resumen

El lujo es espacio. Fondos oscuros, fotografía protagonista, tipografía con serifa de alto contraste y detalles dorados mínimos. Cada pantalla muestra poco y lo muestra bien.

## Colores

- **Primario `primary` (#C8A96A):** Champán dorado: botones y detalles finos. Úsalo con mesura.
- **Secundario `secondary` (#F2EDE4):** Marfil para titulares y texto principal.
- **Acento `accent` (#76592F):** Bronce para separadores y estados hover.
- **Fondo `background` (#0D0D0D):** Negro terciopelo.
- **Texto sobre primario `on-primary` (#0D0D0D):** color de texto e iconos dentro de botones primarios.
- **Superficie, atenuado y borde (#171615, #A39C90, #2C2A27):** tarjetas, texto secundario y divisores.

## Tipografía

Cormorant Garamond 500 para titulares grandes (hasta 80px) en mayúsculas espaciadas o minúsculas elegantes; Montserrat 400 en 14-16px con tracking 0.04em para interfaz.

Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, `body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` (IBM Plex Mono) para código y datos copiables.

## Disposición

Imágenes a pantalla completa, textos cortos superpuestos o al lado. Secciones con 120px de separación vertical en escritorio.

Espaciado en múltiplos de 8px (tokens `spacing`), con un ritmo muy espaciado: un producto por pantalla y textos cortos. Objetivos táctiles de al menos 44px.

## Elevación y profundidad

Sin sombras; capas por luminosidad (surface ligeramente más clara que el fondo).

## Formas

Esquinas rectas. Líneas doradas de 1px como separadores.

## Movimiento

Lento y elegante: 400ms ease-in-out, fundidos de imagen. Respeta siempre `prefers-reduced-motion`.

## Voz y contenido

Evocadora, breve, sin precios gritados. «Descubra la colección». Usted.

## Componentes

- **`hero-producto`**: Pieza única en el centro, nombre en serif ligera y precio discreto debajo.
- **`enlace-subrayado`**: Acción secundaria como texto en versalitas con subrayado fino, en lugar de botón.
- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios 0px / 2px / 4px, etiquetas en Montserrat y una sola acción primaria por vista.

## Qué hacer y qué no

- Sí: Deja mucho espacio vacío.
- Sí: Usa fotografía de alta calidad.
- Sí: Limita el dorado a detalles finos.
- No: No uses insignias de descuento llamativas.
- No: No pongas más de un CTA por sección.
- No: No uses texto dorado en párrafos largos.

---

Hecho por diseño.md · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.
