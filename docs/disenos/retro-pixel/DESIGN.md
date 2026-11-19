---
version: "alpha"
name: Retro Pixel
description: "Recreativa de los 80: píxeles, CRT y colores primarios."
colors:
  primary: "#FF3366"
  on-primary: "#120A1F"
  secondary: "#33CCFF"
  accent: "#FFD23F"
  background: "#120A1F"
  surface: "#1E1433"
  text: "#F5F0FF"
  muted: "#A99BC7"
  border: "#3A2A5C"
typography:
  display-lg:
    fontFamily: Press Start 2P
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Press Start 2P
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: IBM Plex Mono
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: IBM Plex Mono
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
  md: 0px
  lg: 0px
  full: 0px
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
    textColor: "{colors.background}"
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
  hud:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  pixel-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
---

# Retro Pixel — DESIGN.md

> Recreativa de los 80: píxeles, CRT y colores primarios. Ideal para: Juegos indie, ludotecas, eventos gaming, tiendas de cómics, streamers.

Sistema de diseño original de diseño.md. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.

## Resumen

Nostalgia jugable. Titulares en fuente pixelada, bordes escalonados, sombras de 4px en bloque y un leve efecto de líneas CRT opcional. La lectura larga sigue siendo cómoda gracias a la mono.

## Colores

- **Primario `primary` (#FF3366):** Rosa arcade para el botón START y acciones principales.
- **Secundario `secondary` (#33CCFF):** Cian para enlaces y puntuaciones.
- **Acento `accent` (#FFD23F):** Amarillo moneda para premios, vidas y destacados.
- **Fondo `background` (#120A1F):** Púrpura noche de salón recreativo.
- **Texto sobre primario `on-primary` (#120A1F):** color de texto e iconos dentro de botones primarios.
- **Superficie, atenuado y borde (#1E1433, #A99BC7, #3A2A5C):** tarjetas, texto secundario y divisores.

## Tipografía

Press Start 2P solo para titulares cortos y botones (máximo 6 palabras); IBM Plex Mono 400 para todo lo demás.

Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, `body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` (IBM Plex Mono) para código y datos copiables.

## Disposición

Tarjetas tipo «cartucho» en rejilla. Marcadores y barras de progreso pixeladas.

Espaciado en múltiplos de 8px (tokens `spacing`), con un ritmo en múltiplos de 4px para respetar la rejilla de píxeles. Objetivos táctiles de al menos 44px.

## Elevación y profundidad

Sombras en bloque sin difuminado (4px 4px 0 #000) y bordes de 3px.

## Formas

Píxel puro: esquinas rectas o escalonadas con clip-path.

## Movimiento

Pasos discretos (steps(4)) en lugar de transiciones suaves. Parpadeo «PRESS START» lento. Respeta siempre `prefers-reduced-motion`.

## Voz y contenido

Juguetona, con guiños gamer. «¡Nivel desbloqueado!», «Inserta moneda para continuar».

## Componentes

- **`hud`**: Barra tipo marcador con vidas, puntos y nivel en la fuente pixelada.
- **`pixel-button`**: Botón con borde escalonado de 4px (sombra dura en dos pasos) que se hunde al pulsar.
- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios 0px / 0px / 0px, etiquetas en IBM Plex Mono y una sola acción primaria por vista.

## Qué hacer y qué no

- Sí: Limita Press Start 2P a textos cortos.
- Sí: Usa sombras en bloque.
- Sí: Ofrece desactivar el efecto CRT.
- No: No escribas párrafos con fuente pixelada.
- No: No uses esquinas redondeadas.
- No: No animes nada de forma suave.

---

Hecho por diseño.md · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.
