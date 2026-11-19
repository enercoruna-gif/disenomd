---
version: "alpha"
name: Papel Suizo
description: "Estilo tipográfico internacional: rejilla, negro, blanco y un rojo."
colors:
  primary: "#111111"
  on-primary: "#FFFFFF"
  secondary: "#E10600"
  accent: "#E10600"
  background: "#FFFFFF"
  surface: "#F2F2F2"
  text: "#111111"
  muted: "#6B6B6B"
  border: "#111111"
typography:
  display-lg:
    fontFamily: Archivo
    fontSize: 3rem
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Archivo
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Archivo
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Archivo
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
  proyecto:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  indice:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
    padding: 8px 0
---

# Papel Suizo — DESIGN.md

> Estilo tipográfico internacional: rejilla, negro, blanco y un rojo. Ideal para: Estudios de diseño, arquitectura, portfolios, agencias, consultoras.

Sistema de diseño original de diseño.md. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.

## Resumen

Orden radical. La rejilla es visible y la tipografía hace todo el trabajo: tamaños muy contrastados, alineación a la izquierda, mucho blanco. El rojo es una decisión, no una decoración.

## Colores

- **Primario `primary` (#111111):** Negro tinta: texto, botones y reglas de la rejilla.
- **Secundario `secondary` (#E10600):** Rojo señal: un único punto de énfasis por pantalla (número, palabra, botón).
- **Fondo `background` (#FFFFFF):** Blanco papel.
- **Superficie `surface` (#F2F2F2):** Gris claro para bloques secundarios y fondos de imagen.
- **Texto sobre primario `on-primary` (#FFFFFF):** color de texto e iconos dentro de botones primarios.
- **Superficie, atenuado y borde (#F2F2F2, #6B6B6B, #111111):** tarjetas, texto secundario y divisores.

## Tipografía

Archivo en toda la web. Titulares enormes (hasta 96px) en 800 con tracking -0.03em; cuerpo en 400 a 17px. Números de sección en IBM Plex Mono.

Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, `body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` (IBM Plex Mono) para código y datos copiables.

## Disposición

Rejilla de 12 columnas con calles de 24px y líneas horizontales de 1px negras separando secciones. Texto siempre alineado a la izquierda, nunca centrado.

Espaciado en múltiplos de 8px (tokens `spacing`), con un ritmo rejilla estricta de 12 columnas; el blanco es el material principal. Objetivos táctiles de al menos 44px.

## Elevación y profundidad

Ninguna. Cero sombras. La jerarquía se construye con tamaño, peso y reglas.

## Formas

Esquinas rectas (0px) en todo. Imágenes recortadas en rectángulos exactos de la rejilla.

## Movimiento

Mínimo: 150ms lineal. Subrayados que crecen de izquierda a derecha en enlaces. Respeta siempre `prefers-reduced-motion`.

## Voz y contenido

Sobria y segura. Frases declarativas cortas. Títulos de proyecto en una sola palabra cuando sea posible.

## Componentes

- **`proyecto`**: Celda de proyecto: imagen sin bordes ni sombra, número y título alineados a la línea base.
- **`indice`**: Índice numerado (01, 02…) separado por filetes de 1px en `border`.
- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios 0px / 0px / 0px, etiquetas en Archivo y una sola acción primaria por vista.

## Qué hacer y qué no

- Sí: Deja que los titulares grandes respiren.
- Sí: Numera las secciones (01, 02, 03).
- Sí: Usa un solo elemento rojo por vista.
- No: No redondees esquinas.
- No: No centres párrafos.
- No: No uses más de una familia tipográfica además de la mono.

---

Hecho por diseño.md · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.
