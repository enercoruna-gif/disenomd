---
version: "alpha"
name: Pastel Suave
description: "Lavanda, menta y formas redondas que abrazan."
colors:
  primary: "#6D4FD8"
  on-primary: "#FFFFFF"
  secondary: "#2BB39A"
  accent: "#FF9DB0"
  background: "#FAF8FF"
  surface: "#FFFFFF"
  text: "#2A2440"
  muted: "#6E6888"
  border: "#E7E2F7"
typography:
  display-lg:
    fontFamily: Nunito
    fontSize: 3rem
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Nunito
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Nunito
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Nunito
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
  sm: 10px
  md: 18px
  lg: 28px
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
  curso:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: 20px
  progreso:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.text}"
    rounded: "{rounded.full}"
    height: 10px
---

# Pastel Suave — DESIGN.md

> Lavanda, menta y formas redondas que abrazan. Ideal para: Apps educativas, guarderías, salud mental, productos para bebés, coaching.

Sistema de diseño original de diseño.md. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.

## Resumen

Amable y segura. Todo es redondo, el contraste del texto se mantiene alto aunque los fondos sean suaves, y los logros se celebran con color y pequeñas ilustraciones.

## Colores

- **Primario `primary` (#6D4FD8):** Lavanda intensa: acciones principales (suficiente contraste con blanco).
- **Secundario `secondary` (#2BB39A):** Menta para progreso, logros y confirmaciones.
- **Acento `accent` (#FF9DB0):** Rosa chicle para ilustraciones y celebraciones, nunca para texto.
- **Fondo `background` (#FAF8FF):** Blanco lavanda muy suave.
- **Texto sobre primario `on-primary` (#FFFFFF):** color de texto e iconos dentro de botones primarios.
- **Superficie, atenuado y borde (#FFFFFF, #6E6888, #E7E2F7):** tarjetas, texto secundario y divisores.

## Tipografía

Nunito en toda la interfaz: 800 para titulares, 400 para lectura a 17px con interlineado 1.6.

Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, `body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` (IBM Plex Mono) para código y datos copiables.

## Disposición

Tarjetas grandes y táctiles (mínimo 48px de alto en controles). Una idea por pantalla en móvil.

Espaciado en múltiplos de 8px (tokens `spacing`), con un ritmo amable: objetivos táctiles de 48px y separación amplia entre elementos. Objetivos táctiles de al menos 44px.

## Elevación y profundidad

Sombras suaves teñidas de lavanda (0 8px 24px rgba(109,79,216,.12)).

## Formas

Esquinas muy redondeadas (18px tarjetas, píldora en botones). Iconos con trazo redondeado.

## Movimiento

220ms con ligero rebote (cubic-bezier(.34,1.56,.64,1)) solo en celebraciones; el resto ease-out. Respeta siempre `prefers-reduced-motion`.

## Voz y contenido

Animosa y clara. «¡Lo has conseguido!», «Paso 2 de 4». Frases cortas, sin tecnicismos.

## Componentes

- **`curso`**: Tarjeta de curso o actividad con ilustración redonda, edad recomendada y barra de progreso.
- **`progreso`**: Barra de progreso gruesa y redondeada; celebra los hitos con el color de acento.
- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios 10px / 18px / 28px, etiquetas en Nunito y una sola acción primaria por vista.

## Qué hacer y qué no

- Sí: Mantén el texto en #2A2440 para buena lectura.
- Sí: Celebra el progreso con menta.
- Sí: Usa controles grandes y redondos.
- No: No pongas texto sobre rosa o menta claros.
- No: No uses esquinas rectas.
- No: No satures la pantalla de opciones.

---

Hecho por diseño.md · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.
