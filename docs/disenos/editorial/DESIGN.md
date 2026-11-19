---
version: "alpha"
name: Editorial
description: "Revista de papel: serifas, columnas y buena lectura."
colors:
  primary: "#9B1C31"
  on-primary: "#FFFFFF"
  secondary: "#1E1E1E"
  accent: "#C9A227"
  background: "#FFFEFB"
  surface: "#F6F2EA"
  text: "#1E1E1E"
  muted: "#666057"
  border: "#E4DDCF"
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Playfair Display
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.01em
  body-md:
    fontFamily: Source Serif 4
    fontSize: 1.1875rem
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0em
  label-sm:
    fontFamily: Source Serif 4
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
  articulo-portada:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text}"
    typography: "{typography.display-lg}"
    padding: 0
  capitular:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.display-lg}"
    padding: 0 8px 0 0
---

# Editorial — DESIGN.md

> Revista de papel: serifas, columnas y buena lectura. Ideal para: Blogs, revistas digitales, newsletters, despachos, libros.

Sistema de diseño original de diseño.md. Sigue la especificación abierta DESIGN.md (tokens YAML + criterio en Markdown). Colócalo en la raíz de tu proyecto y pide a tu agente de IA que lo siga en cada pantalla.

## Resumen

Prioriza la lectura por encima de todo. Jerarquía clásica de prensa: antetítulo, titular, entradilla, cuerpo. Interfaz discreta que no compite con el texto.

## Colores

- **Primario `primary` (#9B1C31):** Granate de cabecera de periódico: secciones, enlaces y botón de suscripción.
- **Secundario `secondary` (#1E1E1E):** Negro tinta para titulares y texto.
- **Acento `accent` (#C9A227):** Dorado viejo para etiquetas «exclusiva» o «premium».
- **Fondo `background` (#FFFEFB):** Blanco hueso para lectura prolongada.
- **Texto sobre primario `on-primary` (#FFFFFF):** color de texto e iconos dentro de botones primarios.
- **Superficie, atenuado y borde (#F6F2EA, #666057, #E4DDCF):** tarjetas, texto secundario y divisores.

## Tipografía

Playfair Display 700 para titulares; Source Serif 4 a 19px/1.7 para el cuerpo; antetítulos en mayúsculas pequeñas con tracking 0.08em.

Escala: `display-lg` para el titular principal (uno por página), `headline-md` para títulos de sección, `body-md` para lectura, `label-sm` para botones, etiquetas y metadatos, `code-sm` (IBM Plex Mono) para código y datos copiables.

## Disposición

Columna de lectura de 680px centrada; portada en rejilla de 3 columnas con noticia principal a 2 columnas. Capitular opcional en la primera letra.

Espaciado en múltiplos de 8px (tokens `spacing`), con un ritmo de lectura: columna de 60-70 caracteres y márgenes amplios. Objetivos táctiles de al menos 44px.

## Elevación y profundidad

Ninguna sombra; reglas finas de 1px entre artículos.

## Formas

Esquinas casi rectas (2-4px). Imágenes con pie de foto en cursiva.

## Movimiento

Mínimo. Barra de progreso de lectura fina arriba. Respeta siempre `prefers-reduced-motion`.

## Voz y contenido

Periodística: titulares informativos, sin clickbait. Entradillas de 1-2 frases.

## Componentes

- **`articulo-portada`**: Titular a gran tamaño con antetítulo en `primary`, firma y tiempo de lectura.
- **`capitular`**: Letra capitular de tres líneas al inicio de cada artículo.
- **Base** (`button-primary`, `button-secondary`, `card`, `input`, `chip`, `badge`, `caption`, `divider`): radios 2px / 4px / 6px, etiquetas en Source Serif 4 y una sola acción primaria por vista.

## Qué hacer y qué no

- Sí: Mantén la columna de lectura por debajo de 75 caracteres.
- Sí: Usa antetítulos para la sección.
- Sí: Incluye tiempo de lectura.
- No: No pongas anuncios dentro del primer párrafo.
- No: No uses texto gris claro para el cuerpo.
- No: No mezcles más de dos serifas.

---

Hecho por diseño.md · Licencia: uso libre en proyectos personales y comerciales; no se permite revender este archivo como producto propio.
