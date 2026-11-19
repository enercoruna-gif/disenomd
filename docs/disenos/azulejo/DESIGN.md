---
version: "alpha"
name: Azulejo
description: "Azul cobalto sobre blanco cal, como un patio de Lisboa o Sevilla."
colors:
  primary: "#1F4FA3"
  on-primary: "#FFFFFF"
  secondary: "#0E2A5C"
  accent: "#F2A541"
  background: "#FFFFFF"
  surface: "#F3F6FC"
  text: "#0F1B33"
  muted: "#56627A"
  border: "#D5DEEF"
typography:
  display-lg:
    fontFamily: DM Serif Display
    fontSize: 3rem
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: DM Serif Display
    fontSize: 1.75rem
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: DM Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0em
  label-sm:
    fontFamily: DM Sans
    fontSize: 0.8125rem
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  code-sm:
    fontFamily: DM Mono
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0em
rounded:
  sm: 4px
  md: 8px
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
  buscador-fechas:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: 12px
  ficha-alojamiento:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.md}"
    padding: 0
---

# Azulejo — DESIGN.md

> Azul cobalto sobre blanco cal, como un patio de Lisboa o Sevilla. Ideal para: Turismo, apartamentos vacacionales, museos, guías de ciudad.

Sistema de diseño original de diseño.md. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.

## Resumen

Luminosa, ordenada y con un punto artesanal. El blanco domina y el cobalto guía. Se permite un patrón geométrico de azulejo como textura de fondo en cabeceras, siempre al 6-10% de opacidad.

## Colores

- **Primario `primary` (#1F4FA3):** Azul cobalto del azulejo pintado a mano: acciones y enlaces.
- **Secundario `secondary` (#0E2A5C):** Azul noche para cabeceras, pies de página y bloques de contraste.
- **Acento `accent` (#F2A541):** Ocre de tejado para insignias, precios y fechas destacadas.
- **Fondo `background` (#FFFFFF):** Blanco cal, limpio y luminoso.
- **Superficie `surface` (#F3F6FC):** Azul muy pálido para tarjetas y zonas de formulario.
- **Texto sobre primario `on-primary` (#FFFFFF):** color de texto e iconos dentro de botones primarios.
- **Superficie, atenuado y borde (#F3F6FC, #56627A, #D5DEEF):** tarjetas, texto secundario y divisores.

## Tipografía

DM Serif Display para titulares grandes (nunca por debajo de 28px); DM Sans 400/500 para lectura e interfaz.

Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, `body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` (DM Mono) para código y datos copiables.

## Disposición

Rejilla de 12 columnas, contenedor de 1200px. Tarjetas de alojamiento o actividad en rejilla de 3 en escritorio, 1 en móvil, con imagen 4:3 arriba.

Espaciado en múltiplos de 8px (tokens `spacing`), con un ritmo generoso alrededor de las fotos; los textos van en columnas estrechas. Objetivos táctiles de al menos 44px.

## Elevación y profundidad

Sombra fría y difusa en tarjetas (0 6px 20px rgba(15,27,51,.08)). Al pasar el cursor, la sombra crece y la tarjeta sube 2px.

## Formas

Esquinas suaves (8px). Divisores con un patrón de azulejo en línea fina de 4px de alto como separador de secciones.

## Movimiento

160-220ms, ease-in-out. Carruseles con desplazamiento suave, sin autoplay. Respeta siempre `prefers-reduced-motion`.

## Voz y contenido

Evocadora pero útil. Primero el dato (precio, fecha, distancia), después la emoción.

## Componentes

- **`buscador-fechas`**: Buscador de fechas y huéspedes que se superpone a la foto principal.
- **`ficha-alojamiento`**: Foto 4:3 arriba, nombre, barrio y precio por noche; el patrón de azulejo solo como borde decorativo.
- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios 4px / 8px / 16px, etiquetas en DM Sans y una sola acción primaria por vista.

## Qué hacer y qué no

- Sí: Muestra precio y valoración en la tarjeta, sin obligar a entrar.
- Sí: Usa el patrón de azulejo solo como textura sutil.
- Sí: Mantén mucho blanco alrededor de las fotos.
- No: No mezcles el cobalto con otros azules ajenos a la paleta.
- No: No uses DM Serif Display en botones ni etiquetas.
- No: No pongas el patrón detrás de texto de lectura.

---

Hecho por diseño.md · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.
