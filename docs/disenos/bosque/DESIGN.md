---
version: "alpha"
name: Bosque
description: "Verde musgo, papel reciclado y calma."
colors:
  primary: "#2F5D3A"
  on-primary: "#F4F1E8"
  secondary: "#8A6A3D"
  accent: "#D98E32"
  background: "#F4F1E8"
  surface: "#FFFDF7"
  text: "#1F2A22"
  muted: "#66705F"
  border: "#DDD6C3"
typography:
  display-lg:
    fontFamily: Source Serif 4
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Source Serif 4
    fontSize: 1.75rem
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Outfit
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Outfit
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
  sm: 8px
  md: 14px
  lg: 24px
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
  producto:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: 16px
  sello:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.text}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
---

# Bosque — DESIGN.md

> Verde musgo, papel reciclado y calma. Ideal para: Marcas eco, huertos, cosmética natural, ONGs, turismo rural.

Sistema de diseño original de diseño.md. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.

## Resumen

Natural y honesta. Texturas suaves, tipografía con serifa para contar historias y una sans geométrica amable para la interfaz. Debe sentirse sin prisa.

## Colores

- **Primario `primary` (#2F5D3A):** Verde musgo: acciones, enlaces y sello de marca.
- **Secundario `secondary` (#8A6A3D):** Marrón corteza para etiquetas, iconos y detalles de origen.
- **Acento `accent` (#D98E32):** Naranja otoño para avisos amables y destacados de temporada.
- **Fondo `background` (#F4F1E8):** Papel reciclado cálido.
- **Texto sobre primario `on-primary` (#F4F1E8):** color de texto e iconos dentro de botones primarios.
- **Superficie, atenuado y borde (#FFFDF7, #66705F, #DDD6C3):** tarjetas, texto secundario y divisores.

## Tipografía

Source Serif 4 para titulares y citas (600); Outfit 400/500 para interfaz y texto corrido.

Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, `body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` (IBM Plex Mono) para código y datos copiables.

## Disposición

Secciones alternas texto/imagen en dos columnas; en móvil, imagen arriba. Contenedor de 1080px, márgenes generosos.

Espaciado en múltiplos de 8px (tokens `spacing`), con un ritmo orgánico: bloques con mucho aire y fotos de producto grandes. Objetivos táctiles de al menos 44px.

## Elevación y profundidad

Sombras cálidas y muy suaves (0 4px 16px rgba(31,42,34,.06)). Preferir separación por color.

## Formas

Esquinas generosas (14px) y formas orgánicas en ilustraciones; botones en píldora.

## Movimiento

240ms ease-out. Apariciones con fundido lento al hacer scroll, sin desplazamientos bruscos. Respeta siempre `prefers-reduced-motion`.

## Voz y contenido

Cálida, transparente con los datos (origen, huella, ingredientes). Evita el «greenwashing» y los superlativos.

## Componentes

- **`producto`**: Ficha de producto con foto sobre fondo crema, sello «eco» en `accent` y precio.
- **`sello`**: Sello circular de certificación o ingrediente.
- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios 8px / 14px / 24px, etiquetas en Outfit y una sola acción primaria por vista.

## Qué hacer y qué no

- Sí: Muestra el origen y los datos del producto.
- Sí: Usa fotografía de exterior con luz natural.
- Sí: Prefiere botones en píldora.
- No: No uses verdes fluorescentes.
- No: No satures de iconos de hojas.
- No: No uses negro puro.

---

Hecho por diseño.md · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.
