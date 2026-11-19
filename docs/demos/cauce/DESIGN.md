# Cauce — DESIGN.md

Sistema de diseño gratuito, en español, para agentes de IA y personas que construyen interfaces. Concepto fintech independiente para el catálogo de **diseño.md / ia.cuadrantia.store**. No es una aplicación bancaria real.

## 1. Intención

**El dinero encuentra su cauce.** La interfaz debe transmitir claridad y espacio mental: una hoja blanca amplia, tipografía de buen tamaño, azul cobalto como acción y ámbar como contrapunto cálido. La tecnología queda detrás; los planes de la persona van delante.

Inspiración solicitada: la composición de las capturas de Payer proporcionadas por Jorge, con una proximidad visual orientativa del 80–85 %, no una medición ni un calco. Se conservan la superficie clara enmarcada, la jerarquía tipográfica, los botones redondos, el protagonismo móvil y los campos de luz azul/ámbar. Se crean un nombre, logotipo, textos, UI, datos y componentes propios. No reutilizar marca, fotografías, mano, testimonios, cifras comerciales ni logotipos de Payer.

**Uso:** landing de una app, producto SaaS o herramienta personal. Para una empresa real, reemplazar el concepto y las capacidades ficticias por hechos verificados. No mezclar esta identidad con Ener Coruña.

## 2. Dirección visual

- Fondo exterior fino, azul y ámbar, que enmarca una gran superficie blanca.
- Contenedor centrado; el contenido no se estira en pantallas grandes.
- Titulares geométricos, negros y compactos. Acento azul en una frase, nunca degradado en el texto.
- Escenario de producto grande, con una inclinación leve y sombra direccional.
- Una franja de luz en la base del hero, no detrás del texto de lectura.
- Tarjetas gris frío con esquinas suaves; evitar bordes y sombras a la vez.
- Píldoras flotantes de estado solo cuando aporten significado.
- Aire entre secciones y una sola familia de iconos de trazo.

**No usar:** fondos negros de estilo cripto, violeta neón, cristales borrosos, estrellas de valoración inventadas, paredes de logos ficticios, falsas descargas de App Store ni formularios que no envían nada.

## 3. Tokens de color

| Token | Valor | Uso |
|---|---|---|
| `--color-paper` | `#FFFFFF` | Superficie principal |
| `--color-page` | `#E9ECF6` | Fondo exterior frío |
| `--color-ink` | `#14171D` | Titulares y cifras |
| `--color-muted` | `#5B606A` | Texto secundario legible |
| `--color-blue` | `#2855DF` | CTA principal, selección, barras |
| `--color-blue-hover` | `#1C42BA` | Hover del CTA |
| `--color-blue-soft` | `#EDF2FF` | Fondos informativos |
| `--color-orange` | `#F2A21A` | Acento gráfico, nunca texto pequeño sobre blanco |
| `--color-orange-soft` | `#FFF2D6` | Fondo de icono cálido |
| `--color-green` | `#26744E` | Estado positivo |
| `--color-green-soft` | `#E7F5EC` | Fondo de estado positivo |
| `--color-surface` | `#F6F7F9` | Tarjetas y botones secundarios |
| `--color-line` | `#E6E8ED` | Separadores y carriles de progreso |
| `--color-selection` | `#D6E1FF` | Selección de texto |

Declarar los colores en `:root`. El fondo luminoso combina dos gradientes radiales: ámbar abajo a la izquierda, azul abajo a la derecha, sobre gris frío. No usarlo como relleno de todos los bloques. El verde significa confirmación, nunca sustituye al azul como acción principal.

## 4. Tipografía

**Manrope**, variable, pesos 400–800. Es gratuita bajo SIL Open Font License 1.1. Incluir la fuente localmente o embebida; no depender de Google Fonts al ejecutar la página. Fallback: `Arial, sans-serif`.

| Rol | Escritorio | Móvil | Peso / interlineado |
|---|---|---|---|
| H1 | 60–72 px | 41–60 px fluidos | 650 / 1.08–1.13 |
| H2 | 40–46 px | 32–33 px | 650 / 1.13 |
| H3 | 25 px | 24 px | 650 / 1.13 |
| Texto | 15–16 px | 14–16 px | 400 / 1.6 |
| Texto de apoyo | 13–14 px | 12–13 px | 400 / 1.6 |
| Botón | 13 px | 11–13 px | 600 / 1.4 |
| Etiqueta de UI ilustrativa | 10–12 px | 10–12 px | 500–700 / 1.5 |

El texto pequeño de la maqueta no es la escala para contenidos largos. Tracking de titulares entre `-.025em` y `-.04em`; cuerpo sin tracking. Cifras tabulares en saldos. Evitar titulares en mayúsculas, palabras en cursiva aisladas y párrafos excesivamente anchos.

## 5. Geometría y responsive

- Ancho máximo del lienzo: 1440 px; ancho máximo del contenido: 1120 px.
- Margen exterior: 18 px en escritorio, 9 px en móvil.
- Contenedor: ancho disponible menos 96 px; 64 px en tablet; 38 px en móvil.
- Radio del lienzo: 24 px; tarjetas: 18 px; controles: 999 px.
- Distancia entre secciones: 112 px en escritorio, 88 px en tablet, 72 px en móvil.
- Grid de funciones: dos columnas `minmax(0, 1fr)`, gap de 18 px; una columna desde 650 px.
- Hero: texto a la izquierda y producto a la derecha; móvil: texto, CTAs y producto, sin reducir el teléfono a una miniatura.
- En móvil se eliminan enlaces de navegación secundarios, no el CTA de descarga.
- Teléfono con inclinación de 10 grados; no debe tapar el titular ni las acciones.
- `overflow-x: clip` en `html` y `body`; arreglar los desbordamientos reales, no esconder contenido necesario.
- Las tablas de datos y los controles de producción deben conservar un tamaño legible y áreas táctiles suficientes.

Revisar 320, 390, 650, 768, 1024, 1440 y 1920 px. Ningún CTA cortado ni desplazamiento horizontal. En zoom, el contenido debe reordenarse antes de colisionar.

## 6. Componentes

### Cabecera

Wordmark de 25 px, marca circular original, tres anclas internas y CTA de descarga. Sin menú hamburguesa inútil: en móvil basta la marca y el CTA. En una web más compleja, crear un menú real con gestión de foco y `aria-expanded`.

### Botones

Primario azul con texto blanco, altura mínima 48 px. Secundario gris claro con texto tinta. Un solo CTA dominante por grupo. Hover de 2 px hacia arriba y color ligeramente más oscuro; active vuelve al plano y escala a `.98`. Estados de foco visibles al instante. Controles pequeños: área táctil mínima 44 × 44 px aunque el icono mida 17 px.

### Producto protagonista

Vista funcional de una aplicación ficticia, no una imagen descargada de una tienda de apps. Marco oscuro, superficie interior gris claro, un saldo, un objetivo y dos movimientos. La etiqueta **Datos de ejemplo** se muestra dentro de la propia UI. No dibujar una mano artificial ni simular logos del sistema operativo.

### Saldo privado

Botón de ojo que alterna cifra y máscara. `aria-pressed` describe el estado y `aria-label` cambia entre «Ocultar saldo de ejemplo» y «Mostrar saldo de ejemplo». La ocultación es visual: no es una medida de seguridad ni borra datos del DOM o la memoria. En un producto real, tratar la privacidad por separado.

### Objetivos

Nombre concreto, cantidad, destino y barra de progreso. El ejemplo es 640 € de 1.000 €; el avance es 64 %. No hacer pasar estos datos por resultados del negocio. La barra necesita una descripción equivalente accesible.

### Gráficos

Seis barras, etiquetas de meses y una barra ámbar como máximo. El acento señala el valor mayor, no siempre una columna arbitraria. Las barras y sus etiquetas representan el mismo conjunto de datos. `role="img"` y una descripción textual completa evitan que el color sea la única forma de entenderlo.

### Selector de vistas

Tres pestañas verticales. La activa revela una frase explicativa y actualiza título, total y gráfico. Implementar `tablist`, `tab`, `tabpanel`, `aria-selected`, `aria-controls` y `aria-labelledby`. Un único tab entra en la secuencia de tabulación; flechas, Home y End cambian la selección y el foco.

### Preguntas frecuentes

Usar `details` / `summary`: interacción nativa, teclado y funcionamiento sin JavaScript. Icono de más que gira al abrir; borde horizontal muy tenue. No encerrar cada pregunta en otra tarjeta.

### Descarga

Gratis y sin registro. El HTML autónomo contiene el Markdown completo y genera un Blob UTF-8 al pulsar el botón. Descargar con nombre `DESIGN.md`. También incluir el archivo suelto en el ZIP. No pedir correo ni fingir una suscripción. En Safari para iPhone, el navegador puede abrir el documento para guardarlo en Archivos o desde Compartir.

## 7. Movimiento

- Entrada única del producto: opacidad `.3` a `1`, desplazamiento vertical 24 px a 0 e inclinación 14 a 10 grados; 900 ms con curva `cubic-bezier(.22, 1, .36, 1)`.
- Microinteracciones: 180–220 ms; sin rebotes largos ni seguimiento del cursor.
- No animar `height`, `width`, `top` o `left`; nunca `transition: all`.
- Sin autoplay, carruseles, contadores comerciales o tabs que cambian solos.
- Para `prefers-reduced-motion: reduce`, eliminar animaciones y desplazamiento suave. Todo el contenido permanece visible sin JavaScript.
- Aplicar efectos hover solo en dispositivos que dispongan de hover fino.

## 8. Redacción

Español natural y directo, de tú. Calma sin paternalismo. Hablar de planes y decisiones, no prometer riqueza, rentabilidad ni seguridad bancaria.

Ejemplos: «Tus finanzas, en buena dirección»; «Tu mes, de un vistazo»; «Un objetivo que puedes ver»; «Tú eliges qué mostrar». Evitar «revoluciona tus finanzas», «confían millones de personas», «100 % seguro» y testimonios de nombres inventados.

## 9. Estructura recomendada

1. Hero con mensaje claro, CTA real, UI de producto y aviso de concepto.
2. Banda de principios sin logos prestados ni prueba social falsa.
3. Dos funciones: objetivos y lectura visual del mes.
4. Módulo ancho con control de privacidad que funciona.
5. Selector interactivo de vistas y datos sintéticos coherentes.
6. Bloque editorial que explica el recurso descargable.
7. CTA de descarga gratuita con fondo luminoso.
8. FAQ real y pie de página con atribución y alcance del concepto.

No añadir precios, reseñas, insignias, tiendas de apps ni datos de clientes que nadie haya proporcionado.

## 10. Bibliotecas y referencias consultadas

Las siete bibliotecas indicadas por Jorge se consultaron en sus webs públicas. Esta demo **adapta sus patrones de interacción con código original en HTML/CSS/JS**; no instala sus paquetes React ni redistribuye sus componentes o activos premium. Las semejanzas son de patrón y acabado, no una afirmación de integración oficial.

| Referencia | Elemento llevado al diseño |
|---|---|
| [HorizonX](https://horizonx.so/) | Presentación de producto y campos de luz cálida/fría, reinterpretados con CSS propio; sin activos premium |
| [Bencho](https://bencho.dev/) | Patrón público «Private balance»: alternar visibilidad con un botón de ojo |
| [Transitions.dev](https://transitions.dev/) | Entrada breve del producto y respuesta contenida de botones; curvas y estados escritos para esta demo |
| [BoardUI](https://boardui.com/) | Gramática de gráficos compactos: barras, una selección cálida y jerarquía de cifras |
| [ObsidianUI](https://obsidianui.dev/) | Selector con panel activo y microinteracción; composición propia, sin copiar testimonios |
| [Aceternity UI](https://ui.aceternity.com/components/background-gradient) | Idea de fondo luminoso para enfatizar un bloque, simplificada a dos gradientes radiales estáticos |
| [Astryx](https://astryx.atmeta.com/) | Organización por tokens, controles coherentes y estados accesibles, implementados sin StyleX ni React |

Payer es la referencia visual aportada por el solicitante; no hay relación, patrocinio ni cesión de marca. No convertir las capturas de referencia en activos de la web.

## 11. Accesibilidad y calidad

- `lang="es"`, un H1, encabezados ordenados, landmarks y enlace de salto.
- Contraste mínimo 4.5:1 para texto normal y 3:1 para texto grande.
- Foco visible, no tapado, también en enlaces, pestañas y `summary`.
- Interacciones utilizables con teclado y sin depender de hover.
- Iconos decorativos con `aria-hidden`; controles de icono con nombre accesible.
- Ningún movimiento esencial ni contenido oculto hasta que ejecute JavaScript.
- Aviso junto a la UI y los gráficos: datos ficticios, no conexión bancaria.
- No trackers, cookies, analítica, peticiones a terceros ni captura de datos.
- El HTML es autónomo: CSS, JavaScript, fuente y Markdown integrados.

## 12. SEO, AEO, GEO y entrega

Incluir título, descripción, idioma, favicon, Open Graph, Twitter Card y JSON-LD `CreativeWork`. La imagen social mide 1200 × 630 px con zona de seguridad. La FAQ visible responde al alcance y uso del recurso; sus respuestas deben coincidir con cualquier dato estructurado publicado.

La demo se entrega con `noindex,follow`: es un concepto, no un servicio financiero real. El catálogo definitivo puede indexar su ficha. No inventar dirección, `LocalBusiness`, coordenadas, reseñas ni información comercial para GEO; explicar claramente la entidad creadora y el idioma. La URL pública final debe decidirla quien integra el recurso: completar canonical y las URLs absolutas de OG al integrarlo. El paquete no se despliega por sí solo.

Entregables: `index.html`, `DESIGN.md`, `og-cauce.png`, `LEEME.txt`, `LICENSE.txt` y `Manrope-OFL.txt` en la raíz del ZIP para Cloudflare Pages. El HTML autónomo es el mismo documento completo, con otro nombre para abrirlo por separado. No se necesita compilación ni suscripción.

## 13. Prompt listo para usar

> Crea una landing para [mi proyecto] siguiendo este DESIGN.md. Conserva el sistema claro, Manrope, cobalto y ámbar, el ritmo espacial y la composición con producto protagonista, pero adapta la marca, el contenido y las funciones a mi negocio. Usa solo datos y capacidades que te proporcione. No inventes clientes, testimonios, métricas ni precios. Si faltan datos, omítelos o identifícalos como ilustrativos. Implementa responsive de 320 a 1920 px, teclado, foco visible y movimiento reducido. Los CTAs deben tener una acción real. Entrega una web estática funcional sin servicios de pago y no la publiques por mí.

## 14. Licencias

El contenido original de este DESIGN.md se ofrece bajo **CC0 1.0**: https://creativecommons.org/publicdomain/zero/1.0/ . El código original de la demo se ofrece bajo MIT, incluido en `LICENSE.txt`. Manrope conserva su SIL OFL 1.1. Las marcas y referencias externas no se incluyen en estas licencias y no implican afiliación. No se incluyen fotografías ni activos de pago.
