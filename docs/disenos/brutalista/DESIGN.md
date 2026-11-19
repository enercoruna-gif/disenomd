---
version: "alpha"
name: Brutalista
description: "Bordes gruesos, amarillo chillón y sin pedir perdón."
colors:
  primary: "#111111"
  on-primary: "#FFE14D"
  secondary: "#FF5A36"
  accent: "#FFE14D"
  background: "#FFFBEA"
  surface: "#FFFFFF"
  text: "#111111"
  muted: "#4A4A4A"
  border: "#111111"
typography:
  display-lg:
    fontFamily: Space Mono
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Mono
    fontSize: 1.75rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Work Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: Work Sans
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  code-sm:
    fontFamily: Space Mono
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0em
rounded:
  sm: 0px
  md: 4px
  lg: 8px
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
  bloque-duro:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.sm}"
    padding: 20px
  marquee:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.text}"
    typography: "{typography.label-sm}"
    padding: 8px 0
---

# Brutalista — DESIGN.md

> Bordes gruesos, amarillo chillón y sin pedir perdón. Ideal para: Lanzamientos, newsletters, herramientas indie, eventos, marcas jóvenes.

Sistema de diseño original de diseño.md. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.

## Resumen

Honesta y ruidosa. Bordes de 2-3px negros, sombras duras desplazadas y tipografía monoespaciada en titulares. Se nota que está hecha a propósito, no por descuido.

## Colores

- **Primario `primary` (#111111):** Negro: bordes, texto y botones.
- **Secundario `secondary` (#FF5A36):** Naranja para etiquetas «nuevo» y avisos.
- **Acento `accent` (#FFE14D):** Amarillo eléctrico como fondo de bloques destacados y texto de botón.
- **Fondo `background` (#FFFBEA):** Crema amarillenta, como papel de fotocopia.
- **Texto sobre primario `on-primary` (#FFE14D):** color de texto e iconos dentro de botones primarios.
- **Superficie, atenuado y borde (#FFFFFF, #4A4A4A, #111111):** tarjetas, texto secundario y divisores.

## Tipografía

Space Mono 700 para titulares y etiquetas en mayúsculas; Work Sans 400/600 para lectura.

Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, `body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` (Space Mono) para código y datos copiables.

## Disposición

Bloques apilados con bordes visibles, como cajas. Rejilla irregular permitida en escritorio; en móvil, una columna estricta.

Espaciado en múltiplos de 8px (tokens `spacing`), con un ritmo denso y a golpes: bloques pegados con bordes de 2px y sombras duras sin difuminar. Objetivos táctiles de al menos 44px.

## Elevación y profundidad

Sombras duras sin difuminado: 4px 4px 0 #111111. Al pulsar, el botón se desplaza 4px y la sombra desaparece.

## Formas

Esquinas rectas o casi (0-4px). Bordes de 2px en todo lo interactivo.

## Movimiento

Instantáneo o 100ms lineal. Nada suave. Respeta siempre `prefers-reduced-motion`.

## Voz y contenido

Descarada, divertida, en mayúsculas cuando convenga. «HAZLO HOY». Frases de una línea.

## Componentes

- **`bloque-duro`**: Tarjeta con borde de 2px en `text` y sombra dura de 6px 6px 0 sin desenfoque.
- **`marquee`**: Cinta de texto en movimiento para anuncios; se detiene con `prefers-reduced-motion`.
- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios 0px / 4px / 8px, etiquetas en Work Sans y una sola acción primaria por vista.

## Qué hacer y qué no

- Sí: Usa bordes negros de 2px en tarjetas y botones.
- Sí: Aplica sombras duras desplazadas.
- Sí: Mantén el texto de lectura en Work Sans.
- No: No uses sombras difuminadas.
- No: No uses degradados.
- No: No escribas párrafos largos en Space Mono.

---

Hecho por diseño.md · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.
