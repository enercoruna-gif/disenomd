---
version: "alpha"
name: Panel SaaS
description: "Gris neutro, índigo y densidad productiva."
colors:
  primary: "#4F46E5"
  on-primary: "#FFFFFF"
  secondary: "#0EA5E9"
  accent: "#F59E0B"
  background: "#F8FAFC"
  surface: "#FFFFFF"
  text: "#0F172A"
  muted: "#64748B"
  border: "#E2E8F0"
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
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
  md: 8px
  lg: 12px
  full: 999px
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
  kpi:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.headline-md}"
    rounded: "{rounded.md}"
    padding: 16px
  tabla-fila:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
    height: 40px
    padding: 0 12px
---

# Panel SaaS — DESIGN.md

> Gris neutro, índigo y densidad productiva. Ideal para: Paneles de administración, CRMs, herramientas internas, apps B2B.

Sistema de diseño original de diseño.md. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.

## Resumen

Pensada para usarse 8 horas al día. Neutra, densa y predecible: barra lateral, cabecera con búsqueda, tablas y tarjetas de métricas. El color se reserva para estado y acción.

## Colores

- **Primario `primary` (#4F46E5):** Índigo para acciones, selección y navegación activa.
- **Secundario `secondary` (#0EA5E9):** Azul cielo para información y gráficos secundarios.
- **Acento `accent` (#F59E0B):** Ámbar para avisos y estados pendientes.
- **Fondo `background` (#F8FAFC):** Gris pizarra muy claro para el lienzo del panel.
- **Texto sobre primario `on-primary` (#FFFFFF):** color de texto e iconos dentro de botones primarios.
- **Superficie, atenuado y borde (#FFFFFF, #64748B, #E2E8F0):** tarjetas, texto secundario y divisores.

## Tipografía

Inter: 600 para títulos de página (24px), 500 para cabeceras de tabla (13px), 400 para datos (14px).

Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, `body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` (JetBrains Mono) para código y datos copiables.

## Disposición

Barra lateral colapsable de 240px, cabecera de 56px, contenido con padding de 24px. Rejilla de 4px.

Espaciado en múltiplos de 4px (tokens `spacing`), con un ritmo denso para uso diario: filas de 40px, márgenes de 16px y mucha información por pantalla. Objetivos táctiles de al menos 44px.

## Elevación y profundidad

Bordes de 1px en tarjetas; sombra pequeña (0 1px 2px rgba(15,23,42,.06)). Modales con sombra grande y fondo oscurecido al 40%.

## Formas

Esquinas de 8px en tarjetas, 6px en inputs y botones.

## Movimiento

120-180ms ease-out. Esqueletos de carga en lugar de spinners. Respeta siempre `prefers-reduced-motion`.

## Voz y contenido

Funcional. Etiquetas de una o dos palabras, mensajes de error que dicen cómo arreglarlo.

## Componentes

- **`kpi`**: Indicador con etiqueta, cifra y variación con flecha; cuatro por fila en escritorio, dos en móvil.
- **`tabla-fila`**: Fila de tabla con estado en chip, acciones al pasar el ratón y selección por casilla.
- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios 6px / 8px / 12px, etiquetas en Inter y una sola acción primaria por vista.

## Qué hacer y qué no

- Sí: Usa estados vacíos con una acción clara.
- Sí: Muestra atajos de teclado en tooltips.
- Sí: Mantén las tablas ordenables y filtrables.
- No: No uses colores de estado como decoración.
- No: No anides más de dos niveles de navegación.
- No: No uses spinners de pantalla completa.

---

Hecho por diseño.md · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.
