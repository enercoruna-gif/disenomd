---
version: "alpha"
name: Neón Nocturno
description: "Modo oscuro con brillo cian y magenta a medianoche."
colors:
  primary: "#22D3EE"
  on-primary: "#04121A"
  secondary: "#E879F9"
  accent: "#A3E635"
  background: "#0A0B10"
  surface: "#14161F"
  text: "#E8EAF2"
  muted: "#8A90A6"
  border: "#262A38"
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Inter
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0em
rounded:
  sm: 6px
  md: 10px
  lg: 16px
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
  terminal:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.code-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  glow-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.md}"
    padding: 12px 20px
---

# Neón Nocturno — DESIGN.md

> Modo oscuro con brillo cian y magenta a medianoche. Ideal para: Herramientas para desarrolladores, gaming, eventos, música electrónica, IA.

Sistema de diseño original de diseño.md. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.

## Resumen

Oscura, técnica y con energía. El brillo se usa como luz, no como pintura: halos sutiles alrededor de lo interactivo sobre un fondo casi negro. Pensada para que el código y los datos destaquen.

## Colores

- **Primario `primary` (#22D3EE):** Cian eléctrico: la acción principal y el foco de teclado.
- **Secundario `secondary` (#E879F9):** Magenta para degradados de marca y estados destacados.
- **Acento `accent` (#A3E635):** Lima para éxito, «en directo» y contadores.
- **Fondo `background` (#0A0B10):** Negro azulado profundo, nunca #000 puro.
- **Superficie `surface` (#14161F):** Gris grafito para tarjetas y paneles.
- **Texto sobre primario `on-primary` (#04121A):** color de texto e iconos dentro de botones primarios.
- **Superficie, atenuado y borde (#14161F, #8A90A6, #262A38):** tarjetas, texto secundario y divisores.

## Tipografía

Space Grotesk 600 para titulares con tracking ligeramente negativo (-0.02em); Inter para cuerpo; JetBrains Mono para fragmentos de código, comandos y métricas.

Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, `body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` (JetBrains Mono) para código y datos copiables.

## Disposición

Secciones a pantalla completa con mucho espacio negativo. Bloques de código anchos con botón de copiar. Rejilla de 12 columnas, contenedor de 1200px.

Espaciado en múltiplos de 8px (tokens `spacing`), con un ritmo compacto en paneles y amplio en el hero; los bloques de código respiran 24px. Objetivos táctiles de al menos 44px.

## Elevación y profundidad

La profundidad se expresa con luz: box-shadow 0 0 0 1px border + 0 0 24px rgba(34,211,238,.15) en elementos activos.

## Formas

Esquinas de 10px. Bordes de 1px visibles en todas las tarjetas. Degradado cian→magenta solo en líneas finas o en el titular principal.

## Movimiento

200ms ease-out. Brillos que aparecen al pasar el cursor; respeta prefers-reduced-motion. Respeta siempre `prefers-reduced-motion`.

## Voz y contenido

Directa, técnica, con algo de actitud. «Despliega en 30 segundos». Usa verbos y números.

## Componentes

- **`terminal`**: Bloque de terminal con prompt en `primary` y salida en `muted`; botón de copiar en la esquina.
- **`glow-button`**: Botón principal con halo del mismo color (sombra difusa de 24px al 40 %), solo uno por pantalla.
- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios 6px / 10px / 16px, etiquetas en Inter y una sola acción primaria por vista.

## Qué hacer y qué no

- Sí: Mantén el texto de lectura en #E8EAF2 sobre fondos oscuros.
- Sí: Usa la tipografía mono para todo lo copiable.
- Sí: Limita los brillos a lo interactivo.
- No: No pongas texto cian sobre magenta.
- No: No uses fondos blancos en ninguna sección.
- No: No abuses de los degradados en superficies grandes.

---

Hecho por diseño.md · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.
