(function () {
  var toast = document.getElementById('toast'), t;
  function aviso(msg) {
    toast.textContent = msg; toast.classList.add('ver');
    clearTimeout(t); t = setTimeout(function () { toast.classList.remove('ver'); }, 1800);
  }
  function copiar(texto, msg) {
    var ok = function () { aviso(msg || 'Copiado'); };
    var fallo = function () { aviso('No se pudo copiar: mantén pulsado el texto para copiarlo'); };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(texto).then(ok, function () { respaldo(texto) ? ok() : fallo(); });
    } else { respaldo(texto) ? ok() : fallo(); }
  }
  function respaldo(texto) {
    var a = document.createElement('textarea');
    a.value = texto; a.setAttribute('readonly', ''); a.style.position = 'fixed'; a.style.opacity = '0';
    document.body.appendChild(a); a.select(); a.setSelectionRange(0, texto.length);
    var hecho = false;
    try { hecho = document.execCommand('copy'); } catch (e) {}
    document.body.removeChild(a);
    return hecho;
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-copiar],[data-copiar-de]');
    if (!b) return;
    if (b.dataset.copiar) return copiar(b.dataset.copiar, b.dataset.copiar + ' copiado');
    var el = document.getElementById(b.dataset.copiarDe);
    if (el) copiar(el.textContent, b.dataset.copiarDe === 'md' ? 'DESIGN.md copiado' : 'Prompt copiado');
  });

  document.addEventListener('click', function (e) {
    if (e.target.closest('a') && document.body.classList.contains('menu-abierto')) {
      document.body.classList.remove('menu-abierto');
      var m = document.querySelector('.menu-btn'); if (m) m.setAttribute('aria-expanded', 'false');
    }
  });

  var rejilla = document.getElementById('rejilla');
  if (!rejilla) return;
  var buscar = document.getElementById('buscar'), chips = document.getElementById('chips'), vacio = document.getElementById('vacio'), cat = '';
  function norm(t) { return (t || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, ''); }
  var sin = { dark: 'oscuro', hosteleria: 'restaurante bar', minimal: 'minimalista', clinica: 'clinica' };
  function filtrar() {
    var q = norm(buscar.value).trim(), n = 0, tarjetas = rejilla.querySelectorAll('.tarjeta');
    var palabras = q ? (sin[q] || q).split(' ') : [];
    tarjetas.forEach(function (c) {
      var t = norm(c.dataset.texto);
      var ver = (!cat || c.dataset.cat === cat) && (!palabras.length || palabras.some(function (p) { return t.indexOf(p) !== -1; }));
      c.hidden = !ver; if (ver) n++;
    });
    if (n === 0) { tarjetas.forEach(function (c) { c.hidden = cat && c.dataset.cat !== cat; }); document.getElementById('vacio-q').textContent = buscar.value.trim(); }
    vacio.hidden = n > 0;
  }
  buscar.addEventListener('input', filtrar);
  chips.addEventListener('click', function (e) {
    var b = e.target.closest('.chip'); if (!b) return;
    chips.querySelectorAll('.chip').forEach(function (x) { x.classList.toggle('activo', x === b); });
    cat = b.dataset.filtro; filtrar();
  });
})();
