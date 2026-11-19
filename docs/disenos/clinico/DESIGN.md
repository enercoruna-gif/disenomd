---
version: "alpha"
name: Clínico
description: "Accesible, limpio y tranquilizador."
colors:
  primary: "#0A7C86"
  on-primary: "#FFFFFF"
  secondary: "#1D3557"
  accent: "#F4A261"
  background: "#F6FAFB"
  surface: "#FFFFFF"
  text: "#12202B"
  muted: "#4F6270"
  border: "#D6E4E8"
typography:
  display-lg:
    fontFamily: Atkinson Hyperlegible
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Atkinson Hyperlegible
    fontSize: 1.75rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Atkinson Hyperlegible
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Atkinson Hyperlegible
    fontSize: 0.8125rem
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  code-sm:
    fontFamily: IBM Plex Mono
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
  cita:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: 16px
  aviso-salud:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
---

# Clínico — DESIGN.md

> Accesible, limpio y tranquilizador. Ideal para: Clínicas, fisioterapia, dentistas, farmacias, servicios públicos.

Sistema de diseño original de diseño.md. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.

## Resumen

Diseñada para que cualquiera, a cualquier edad, encuentre lo que busca y pida cita sin ayuda. Accesibilidad WCAG AA como mínimo, tipografía muy legible y un flujo de reserva de pocos pasos.

## Colores

- **Primario `primary` (#0A7C86):** Verde azulado sanitario: pedir cita y acciones principales.
- **Secundario `secondary` (#1D3557):** Azul marino para cabeceras e información importante.
- **Acento `accent` (#F4A261):** Melocotón para avisos amables (recordatorios, horarios especiales).
- **Fondo `background` (#F6FAFB):** Blanco con un toque frío, higiénico sin ser hospitalario.
- **Texto sobre primario `on-primary` (#FFFFFF):** color de texto e iconos dentro de botones primarios.
- **Superficie, atenuado y borde (#FFFFFF, #4F6270, #D6E4E8):** tarjetas, texto secundario y divisores.

## Tipografía

Atkinson Hyperlegible en toda la web, cuerpo a 18px mínimo, titulares 700.

Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, `body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` (IBM Plex Mono) para código y datos copiables.

## Disposición

Botón de «Pedir cita» siempre visible (fijo abajo en móvil). Información en bloques: servicios, equipo, horarios, ubicación.

Espaciado en múltiplos de 8px (tokens `spacing`), con un ritmo claro y predecible: un paso por pantalla y botones de ancho completo en móvil. Objetivos táctiles de al menos 44px.

## Elevación y profundidad

Sombras suaves y frías (0 4px 14px rgba(18,32,43,.07)) en tarjetas de servicio.

## Formas

Esquinas medias (10px). Iconos lineales de trazo 2px.

## Movimiento

Discreto: 180ms ease-out. Sin animaciones automáticas. Respeta siempre `prefers-reduced-motion`.

## Voz y contenido

Tranquila, respetuosa y clara. Usted o tú según la marca, pero coherente. Sin jerga médica innecesaria.

## Componentes

- **`cita`**: Selector de cita: día en chips, horas en rejilla de botones de 48px, confirmación en un paso.
- **`aviso-salud`**: Aviso con icono y texto, nunca solo color, para urgencias o preparación de pruebas.
- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios 6px / 10px / 16px, etiquetas en Atkinson Hyperlegible y una sola acción primaria por vista.

## Qué hacer y qué no

- Sí: Muestra teléfono, horario y dirección en la primera pantalla.
- Sí: Usa etiquetas visibles en todos los campos.
- Sí: Mantén contraste AA o superior.
- No: No uses imágenes de stock genéricas de batas.
- No: No escondas el precio de la primera visita.
- No: No uses solo color para indicar errores.

---

Hecho por diseño.md · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.
