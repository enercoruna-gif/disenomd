---
version: "alpha"
name: Terracota
description: "Calidez mediterránea, barro cocido y sobremesa larga."
colors:
  primary: "#B4532A"
  on-primary: "#FFF8F1"
  secondary: "#5E7A4F"
  accent: "#E9B44C"
  background: "#FBF5EC"
  surface: "#FFFFFF"
  text: "#2B1D14"
  muted: "#7A6455"
  border: "#EADBC8"
typography:
  display-lg:
    fontFamily: Fraunces
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Fraunces
    fontSize: 1.75rem
    fontWeight: 500
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
  md: 12px
  lg: 20px
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
  menu-item:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
    padding: 16px 0
  reserva-bar:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
    padding: 16px 20px
---

# Terracota — DESIGN.md

> Calidez mediterránea, barro cocido y sobremesa larga. Ideal para: Restaurantes, bodegas, casas rurales, marcas de producto local.

Sistema de diseño original de diseño.md. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.

## Resumen

Una interfaz que huele a horno de leña. Superficies cremosas, titulares con serifa expresiva y un único color de acción: la terracota. Debe transmitir producto artesano y trato cercano, nunca lujo frío.

## Colores

- **Primario `primary` (#B4532A):** Terracota cocida: botones, enlaces activos y el único color que pide acción.
- **Secundario `secondary` (#5E7A4F):** Verde olivo para estados de éxito, etiquetas de producto y detalles botánicos.
- **Acento `accent` (#E9B44C):** Amarillo azafrán, solo para destacar (ofertas, valoraciones). Nunca como fondo de texto largo.
- **Fondo `background` (#FBF5EC):** Crema de cal: el lienzo de toda la página, más cálido que el blanco.
- **Texto `text` (#2B1D14):** Marrón casi negro, como tinta de menú escrito a mano.
- **Texto sobre primario `on-primary` (#FFF8F1):** color de texto e iconos dentro de botones primarios.
- **Superficie, atenuado y borde (#FFFFFF, #7A6455, #EADBC8):** tarjetas, texto secundario y divisores.

## Tipografía

Fraunces para titulares (peso 600, con su contraste óptico generoso); Inter para todo lo funcional. Los precios y horarios van en Inter con cifras tabulares.

Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, `body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` (JetBrains Mono) para código y datos copiables.

## Disposición

Columnas amplias y respiradas: contenedor de 1120px, márgenes de 24px en móvil. Fotografía grande a sangre en las secciones clave; el texto nunca supera 68 caracteres por línea.

Espaciado en múltiplos de 8px (tokens `spacing`), con un ritmo aireado, como una carta bien maquetada: secciones separadas por 64-96px. Objetivos táctiles de al menos 44px.

## Elevación y profundidad

Casi plana. Las tarjetas se separan del fondo por color (surface sobre background) y un borde de 1px; sombra suave solo en elementos flotantes (carrito, modales).

## Formas

Esquinas redondeadas medias (12px) que recuerdan a la cerámica. Las imágenes pueden usar arco superior (border-radius grande solo arriba) como guiño a ventanas andaluzas.

## Movimiento

Transiciones de 200ms ease-out. Nada rebota; todo se asienta, como un plato que se deja en la mesa. Respeta siempre `prefers-reduced-motion`.

## Voz y contenido

Cercana y concreta. Tutea. Frases cortas: «Reserva tu mesa», «Hecho aquí, cada mañana». Evita anglicismos.

## Componentes

- **`menu-item`**: Plato de la carta: nombre en `headline-md`, descripción en `muted` y precio alineado a la derecha con línea de puntos.
- **`reserva-bar`**: Barra de reserva fija abajo en móvil: fecha, personas y botón «Reservar mesa».
- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios 6px / 12px / 20px, etiquetas en Inter y una sola acción primaria por vista.

## Qué hacer y qué no

- Sí: Usa fotografía real de producto con luz natural.
- Sí: Reserva la terracota para una sola acción principal por pantalla.
- Sí: Combina titulares en serifa con cuerpo en sans.
- No: No uses negro puro (#000) ni blanco puro como fondo.
- No: No pongas texto largo sobre el amarillo azafrán.
- No: No uses más de dos pesos de Fraunces en la misma vista.

---

Hecho por diseño.md · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.
