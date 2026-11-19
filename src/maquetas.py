# Vista previa propia y componentes específicos de cada sistema del catálogo.

M = {}

M["terracota"] = dict(
  densidad="aireado, como una carta bien maquetada: secciones separadas por 64-96px",
  comps=[("menu-item", dict(backgroundColor="{colors.surface}", textColor="{colors.text}", typography="{typography.body-md}", padding="16px 0"),
          "Plato de la carta: nombre en `headline-md`, descripción en `muted` y precio alineado a la derecha con línea de puntos."),
         ("reserva-bar", dict(backgroundColor="{colors.secondary}", textColor="{colors.on-primary}", rounded="{rounded.lg}", padding="16px 20px"),
          "Barra de reserva fija abajo en móvil: fecha, personas y botón «Reservar mesa».")],
  html='''<div class="mq-nav"><b>Casa Lola</b><span>Carta</span><span class="mq-pill">Reservar</span></div>
<p class="mq-eti">Cocina de mercado · desde 1987</p><h2 class="mq-h">Arroces al fuego de leña</h2>
<div class="mq-carta"><p><b>Arroz negro con alioli</b><i></i><span>18 €</span></p><p><b>Croquetas de jamón</b><i></i><span>9 €</span></p><p><b>Tarta de queso</b><i></i><span>6 €</span></p></div>
<div class="mq-barra" style="background:var(--sec);color:var(--on)">Sáb 23 · 4 personas <span class="mq-btn">Reservar mesa</span></div>''')

M["azulejo"] = dict(
  densidad="generoso alrededor de las fotos; los textos van en columnas estrechas",
  comps=[("buscador-fechas", dict(backgroundColor="{colors.surface}", textColor="{colors.text}", rounded="{rounded.lg}", padding="12px"),
          "Buscador de fechas y huéspedes que se superpone a la foto principal."),
         ("ficha-alojamiento", dict(backgroundColor="{colors.surface}", textColor="{colors.text}", rounded="{rounded.md}", padding="0"),
          "Foto 4:3 arriba, nombre, barrio y precio por noche; el patrón de azulejo solo como borde decorativo.")],
  html='''<div class="mq-foto mq-azulejo"><span class="mq-pill">Lisboa · Alfama</span></div>
<h2 class="mq-h">Apartamento con vistas al Tajo</h2>
<div class="mq-buscar"><span>12 – 15 jun</span><span>2 huéspedes</span><span class="mq-btn">Ver disponibilidad</span></div>
<p class="mq-txt">★ 4,9 · 128 opiniones · 95 € / noche</p>''')

M["fintech-sobrio"] = dict(
  densidad="contenido y preciso: rejilla de 4px y bloques numéricos alineados a la derecha",
  comps=[("saldo", dict(backgroundColor="{colors.primary}", textColor="{colors.on-primary}", typography="{typography.display-lg}", rounded="{rounded.sm}", padding="24px"),
          "Bloque de saldo: cifra grande con cifras tabulares y variación del mes en `secondary` o `accent`."),
         ("fila-movimiento", dict(backgroundColor="{colors.surface}", textColor="{colors.text}", typography="{typography.body-md}", padding="12px 0"),
          "Movimiento: concepto y fecha a la izquierda, importe a la derecha; negativos en `accent`, nunca solo por color (signo siempre visible).")],
  html='''<div class="mq-nav"><b>Cuenta Pyme</b><span>Facturas</span><span>Impuestos</span></div>
<div class="mq-saldo"><small>Saldo disponible</small><strong>24.318,40 €</strong><span>+3,2 % este mes</span></div>
<div class="mq-movs"><p><span>Factura 2026-041<small>Hoy</small></span><b class="mq-pos">+1.210,00 €</b></p><p><span>Cuota autónomos<small>Ayer</small></span><b class="mq-neg">−294,00 €</b></p><p><span>Proveedor Gráficas Sur<small>18 nov</small></span><b class="mq-neg">−86,90 €</b></p></div>''')

M["neon-nocturno"] = dict(
  densidad="compacto en paneles y amplio en el hero; los bloques de código respiran 24px",
  comps=[("terminal", dict(backgroundColor="{colors.surface}", textColor="{colors.text}", typography="{typography.code-sm}", rounded="{rounded.md}", padding="16px"),
          "Bloque de terminal con prompt en `primary` y salida en `muted`; botón de copiar en la esquina."),
         ("glow-button", dict(backgroundColor="{colors.primary}", textColor="{colors.on-primary}", typography="{typography.label-sm}", rounded="{rounded.md}", padding="12px 20px"),
          "Botón principal con halo del mismo color (sombra difusa de 24px al 40 %), solo uno por pantalla.")],
  html='''<p class="mq-eti">v2.0 · open source</p><h2 class="mq-h">Despliega tu API en <span style="color:var(--pri)">10 segundos</span></h2>
<pre class="mq-term"><span style="color:var(--pri)">$</span> npx nube deploy
<span style="color:var(--mut)">✓ build 2,1 s · ✓ edge 38 regiones</span>
<span style="color:var(--sec)">→ https://mi-api.nube.dev</span></pre>
<div class="mq-fila"><span class="mq-btn mq-glow">Empezar gratis</span><span class="mq-btn2">Docs</span></div>''')

M["papel-suizo"] = dict(
  densidad="rejilla estricta de 12 columnas; el blanco es el material principal",
  comps=[("proyecto", dict(backgroundColor="{colors.background}", textColor="{colors.text}", typography="{typography.label-sm}", rounded="{rounded.sm}", padding="0"),
          "Celda de proyecto: imagen sin bordes ni sombra, número y título alineados a la línea base."),
         ("indice", dict(backgroundColor="{colors.background}", textColor="{colors.text}", typography="{typography.body-md}", padding="8px 0"),
          "Índice numerado (01, 02…) separado por filetes de 1px en `border`.")],
  html='''<div class="mq-nav"><b>Estudio Norte</b><span>Index</span><span>Info</span></div>
<h2 class="mq-h mq-suizo">Arquitectura<br>e interiores.</h2>
<div class="mq-rejilla"><div><i style="background:var(--fg)"></i><small>01 Casa Ribeira</small></div><div><i style="background:var(--pri)"></i><small>02 Mercado</small></div><div><i style="background:var(--bd)"></i><small>03 Biblioteca</small></div></div>''')

M["bosque"] = dict(
  densidad="orgánico: bloques con mucho aire y fotos de producto grandes",
  comps=[("producto", dict(backgroundColor="{colors.surface}", textColor="{colors.text}", rounded="{rounded.lg}", padding="16px"),
          "Ficha de producto con foto sobre fondo crema, sello «eco» en `accent` y precio."),
         ("sello", dict(backgroundColor="{colors.accent}", textColor="{colors.text}", typography="{typography.label-sm}", rounded="{rounded.full}", padding="4px 10px"),
          "Sello circular de certificación o ingrediente.")],
  html='''<p class="mq-eti">Cosmética natural · Asturias</p><h2 class="mq-h">Hecho a mano con lo que da el monte</h2>
<div class="mq-prods"><div><i style="background:var(--sec)"></i><b>Jabón de avena</b><span>7,50 €</span></div><div><i style="background:var(--acc)"></i><b>Bálsamo de caléndula</b><span>12 €</span></div></div>''')

M["brutalista"] = dict(
  densidad="denso y a golpes: bloques pegados con bordes de 2px y sombras duras sin difuminar",
  comps=[("bloque-duro", dict(backgroundColor="{colors.surface}", textColor="{colors.text}", rounded="{rounded.sm}", padding="20px"),
          "Tarjeta con borde de 2px en `text` y sombra dura de 6px 6px 0 sin desenfoque."),
         ("marquee", dict(backgroundColor="{colors.accent}", textColor="{colors.text}", typography="{typography.label-sm}", padding="8px 0"),
          "Cinta de texto en movimiento para anuncios; se detiene con `prefers-reduced-motion`.")],
  html='''<div class="mq-cinta">★ DROP 03 YA DISPONIBLE ★ ENVÍO GRATIS ★ DROP 03 ★</div>
<h2 class="mq-h mq-brutal">HAZ RUIDO.</h2>
<div class="mq-duro"><b>Newsletter semanal</b><p>Cada lunes, 5 herramientas indie.</p><span class="mq-btn">Apúntate →</span></div>''')

M["pastel-suave"] = dict(
  densidad="amable: objetivos táctiles de 48px y separación amplia entre elementos",
  comps=[("curso", dict(backgroundColor="{colors.surface}", textColor="{colors.text}", rounded="{rounded.lg}", padding="20px"),
          "Tarjeta de curso o actividad con ilustración redonda, edad recomendada y barra de progreso."),
         ("progreso", dict(backgroundColor="{colors.secondary}", textColor="{colors.text}", rounded="{rounded.full}", height="10px"),
          "Barra de progreso gruesa y redondeada; celebra los hitos con el color de acento.")],
  html='''<div class="mq-nav"><b>Pequeños Pasos</b><span class="mq-pill">Entrar</span></div>
<h2 class="mq-h">Hola, Lucía 👋</h2>
<div class="mq-curso"><i style="background:var(--acc)"></i><div><b>Letras y sonidos</b><small>4-6 años · lección 7 de 12</small><span class="mq-prog"><em style="width:58%"></em></span></div></div>
<div class="mq-curso"><i style="background:var(--sec)"></i><div><b>Números jugando</b><small>4-6 años · lección 2 de 10</small><span class="mq-prog"><em style="width:20%"></em></span></div></div>''')

M["editorial"] = dict(
  densidad="de lectura: columna de 60-70 caracteres y márgenes amplios",
  comps=[("articulo-portada", dict(backgroundColor="{colors.background}", textColor="{colors.text}", typography="{typography.display-lg}", padding="0"),
          "Titular a gran tamaño con antetítulo en `primary`, firma y tiempo de lectura."),
         ("capitular", dict(backgroundColor="{colors.background}", textColor="{colors.primary}", typography="{typography.display-lg}", padding="0 8px 0 0"),
          "Letra capitular de tres líneas al inicio de cada artículo.")],
  html='''<div class="mq-nav mq-cabecera"><b>La Gaceta Lenta</b></div>
<p class="mq-eti" style="color:var(--pri)">Ensayo · 8 min</p><h2 class="mq-h">El regreso de las cartas escritas a mano</h2>
<p class="mq-txt mq-capi"><span>E</span>n una época de mensajes instantáneos, cada vez más gente vuelve al papel. No por nostalgia, sino por la atención que exige escribir despacio.</p>
<small class="mq-firma">Por Marta Ibáñez · 19 nov 2026</small>''')

M["clinico"] = dict(
  densidad="claro y predecible: un paso por pantalla y botones de ancho completo en móvil",
  comps=[("cita", dict(backgroundColor="{colors.surface}", textColor="{colors.text}", rounded="{rounded.md}", padding="16px"),
          "Selector de cita: día en chips, horas en rejilla de botones de 48px, confirmación en un paso."),
         ("aviso-salud", dict(backgroundColor="{colors.background}", textColor="{colors.text}", typography="{typography.body-md}", rounded="{rounded.sm}", padding="12px 16px"),
          "Aviso con icono y texto, nunca solo color, para urgencias o preparación de pruebas.")],
  html='''<div class="mq-nav"><b>Clínica Arcos</b><span>Especialidades</span></div>
<h2 class="mq-h">Pide cita en fisioterapia</h2>
<div class="mq-dias"><span>Lun 24</span><span class="mq-sel">Mar 25</span><span>Mié 26</span></div>
<div class="mq-horas"><span>09:00</span><span>10:30</span><span class="mq-sel">12:00</span><span>16:30</span></div>
<span class="mq-btn mq-ancho">Confirmar cita</span>''')

M["lujo-noir"] = dict(
  densidad="muy espaciado: un producto por pantalla y textos cortos",
  comps=[("hero-producto", dict(backgroundColor="{colors.background}", textColor="{colors.text}", typography="{typography.display-lg}", padding="96px 24px"),
          "Pieza única en el centro, nombre en serif ligera y precio discreto debajo."),
         ("enlace-subrayado", dict(backgroundColor="{colors.background}", textColor="{colors.primary}", typography="{typography.label-sm}", padding="4px 0"),
          "Acción secundaria como texto en versalitas con subrayado fino, en lugar de botón.")],
  html='''<div class="mq-nav mq-centro"><b>MAISON ÓR</b></div>
<div class="mq-joya"><i></i></div>
<h2 class="mq-h mq-centro">Anillo Aurora</h2><p class="mq-txt mq-centro">Oro de 18 k · 1.450 €</p>
<p class="mq-centro"><span class="mq-sub">Descubrir la colección</span></p>''')

M["panel-saas"] = dict(
  densidad="denso para uso diario: filas de 40px, márgenes de 16px y mucha información por pantalla",
  comps=[("kpi", dict(backgroundColor="{colors.surface}", textColor="{colors.text}", typography="{typography.headline-md}", rounded="{rounded.md}", padding="16px"),
          "Indicador con etiqueta, cifra y variación con flecha; cuatro por fila en escritorio, dos en móvil."),
         ("tabla-fila", dict(backgroundColor="{colors.surface}", textColor="{colors.text}", typography="{typography.body-md}", height="40px", padding="0 12px"),
          "Fila de tabla con estado en chip, acciones al pasar el ratón y selección por casilla.")],
  html='''<div class="mq-nav"><b>▦ Panel</b><span class="mq-buscador">Buscar…</span></div>
<div class="mq-kpis"><div><small>Ingresos</small><b>48,2 k€</b><em class="mq-pos">▲ 12 %</em></div><div><small>Clientes</small><b>1.284</b><em class="mq-pos">▲ 3 %</em></div></div>
<div class="mq-tabla"><p><span>Acme S.L.</span><em class="mq-est">Activo</em><b>1.200 €</b></p><p><span>Hostal Mar</span><em class="mq-est mq-pend">Pendiente</em><b>340 €</b></p><p><span>Gráficas Sur</span><em class="mq-est">Activo</em><b>780 €</b></p></div>''')

M["retro-pixel"] = dict(
  densidad="en múltiplos de 4px para respetar la rejilla de píxeles",
  comps=[("hud", dict(backgroundColor="{colors.surface}", textColor="{colors.text}", typography="{typography.label-sm}", rounded="{rounded.sm}", padding="8px 12px"),
          "Barra tipo marcador con vidas, puntos y nivel en la fuente pixelada."),
         ("pixel-button", dict(backgroundColor="{colors.primary}", textColor="{colors.on-primary}", typography="{typography.label-sm}", rounded="{rounded.sm}", padding="12px 16px"),
          "Botón con borde escalonado de 4px (sombra dura en dos pasos) que se hunde al pulsar.")],
  html='''<div class="mq-hud"><span>♥♥♥</span><span>1UP 004200</span></div>
<h2 class="mq-h">PRESS START</h2>
<div class="mq-pixeles"><i style="background:var(--pri)"></i><i style="background:var(--acc)"></i><i style="background:var(--sec)"></i><i style="background:var(--pri)"></i></div>
<div class="mq-fila"><span class="mq-btn mq-pix">Jugar</span><span class="mq-btn2">Ranking</span></div>''')
