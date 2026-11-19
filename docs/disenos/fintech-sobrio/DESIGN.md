---
version: "alpha"
name: Fintech Sobrio
description: "Confianza, números claros y cero ruido."
colors:
  primary: "#0B3D91"
  on-primary: "#FFFFFF"
  secondary: "#0F9D74"
  accent: "#E5484D"
  background: "#F7F8FA"
  surface: "#FFFFFF"
  text: "#0B1220"
  muted: "#5B6474"
  border: "#E3E6EB"
typography:
  display-lg:
    fontFamily: IBM Plex Sans
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: IBM Plex Sans
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: IBM Plex Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: IBM Plex Sans
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
  sm: 2px
  md: 4px
  lg: 6px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  2xl: 64px
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
  saldo:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    rounded: "{rounded.sm}"
    padding: 24px
  fila-movimiento:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
    padding: 12px 0
---

# Fintech Sobrio — DESIGN.md

> Confianza, números claros y cero ruido. Ideal para: Apps de finanzas, facturación, banca, gestorías digitales, SaaS B2B.

Sistema de diseño original de diseño.md. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.

## Resumen

Densidad informativa sin agobio. Cada pantalla responde a una pregunta (¿cuánto tengo?, ¿qué debo?). El color tiene significado contable: verde entra, rojo sale, azul actúa.

## Colores

- **Primario `primary` (#0B3D91):** Azul marino institucional: acciones principales y navegación activa.
- **Secundario `secondary` (#0F9D74):** Verde para ingresos, saldos positivos y confirmaciones.
- **Acento `accent` (#E5484D):** Rojo solo para gastos, errores y saldos negativos. Nunca decorativo.
- **Fondo `background` (#F7F8FA):** Gris casi blanco para separar zonas de trabajo.
- **Atenuado `muted` (#5B6474):** Gris pizarra para etiquetas, ejes de gráficos y metadatos.
- **Texto sobre primario `on-primary` (#FFFFFF):** color de texto e iconos dentro de botones primarios.
- **Superficie, atenuado y borde (#FFFFFF, #5B6474, #E3E6EB):** tarjetas, texto secundario y divisores.

## Tipografía

IBM Plex Sans en toda la interfaz con cifras tabulares (font-feature-settings: 'tnum'). Importes grandes en 600; IBM Plex Mono para IBAN, referencias y códigos.

Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, `body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` (IBM Plex Mono) para código y datos copiables.

## Disposición

Panel con barra lateral de 248px y área principal fluida. Rejilla base de 4px. Tablas con filas de 44px y cabecera fija.

Espaciado en múltiplos de 4px (tokens `spacing`), con un ritmo contenido y preciso: rejilla de 4px y bloques numéricos alineados a la derecha. Objetivos táctiles de al menos 44px.

## Elevación y profundidad

Plana con bordes de 1px. Solo menús desplegables y modales llevan sombra (0 8px 24px rgba(11,18,32,.12)).

## Formas

Esquinas contenidas (8px en tarjetas, 4px en inputs). Gráficos con líneas de 2px y sin degradados.

## Movimiento

Rápido: 120-160ms. Los números que cambian se animan con conteo breve (300ms) solo en el resumen. Respeta siempre `prefers-reduced-motion`.

## Voz y contenido

Precisa y tranquila. «Factura enviada», «Pago pendiente: 3 días». Nada de exclamaciones.

## Componentes

- **`saldo`**: Bloque de saldo: cifra grande con cifras tabulares y variación del mes en `secondary` o `accent`.
- **`fila-movimiento`**: Movimiento: concepto y fecha a la izquierda, importe a la derecha; negativos en `accent`, nunca solo por color (signo siempre visible).
- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios 2px / 4px / 6px, etiquetas en IBM Plex Sans y una sola acción primaria por vista.

## Qué hacer y qué no

- Sí: Alinea los importes a la derecha con cifras tabulares.
- Sí: Usa verde y rojo solo con significado contable.
- Sí: Muestra siempre la moneda y la fecha del dato.
- No: No uses gráficos 3D ni degradados.
- No: No escondas comisiones en texto gris pequeño.
- No: No uses el rojo para botones de acción normales.

---

Hecho por diseño.md · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.
