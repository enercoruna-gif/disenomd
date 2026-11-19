(function () {
  'use strict';
  var datos = JSON.parse(document.getElementById('contenido').textContent);
  var marco = document.getElementById('sitio');
  function clave(path) {
    path = path.replace(/index\.html$/, '');
    return datos.paginas[path] ? path : (datos.paginas[path + '/'] ? path + '/' : '/404.html');
  }
  function mostrar() {
    var destino = location.hash.indexOf('#!/') === 0 ? location.hash.slice(2) : '/';
    var url = new URL(destino, datos.dominio), pagina = clave(url.pathname);
    marco.onload = function () {
      var doc = marco.contentDocument, ventana = marco.contentWindow;
      document.title = doc.title;
      ventana.fetch = function (ruta, opciones) {
        var recurso = new URL(ruta, datos.dominio + pagina.slice(1));
        return fetch(datos.recursos[recurso.pathname] || recurso.href, opciones);
      };
      doc.addEventListener('click', function (evento) {
        var enlace = evento.target.closest('a[href]');
        if (!enlace || evento.defaultPrevented || evento.button !== 0 || evento.metaKey || evento.ctrlKey || evento.shiftKey || evento.altKey) return;
        var href = enlace.getAttribute('href');
        if (href.indexOf('data:') === 0 || href.indexOf('mailto:') === 0) return;
        var siguiente = new URL(href, datos.dominio + pagina.slice(1));
        if (siguiente.origin === new URL(datos.dominio).origin) {
          evento.preventDefault();
          var hash = '#!' + siguiente.pathname + siguiente.search + siguiente.hash;
          if (location.hash === hash) mostrar();
          else location.hash = hash;
        } else {
          enlace.target = '_blank';
          enlace.rel = 'noopener';
        }
      });
      if (url.hash) {
        var ancla = doc.getElementById(decodeURIComponent(url.hash.slice(1)));
        if (ancla) {
          Promise.resolve(doc.fonts && doc.fonts.ready).then(function () {
            doc.documentElement.style.scrollBehavior = 'auto';
            ancla.scrollIntoView();
          });
        }
      }
    };
    marco.srcdoc = datos.paginas[pagina].replace(/@@recurso:(.*?)@@/g, function (_, nombre) {
      return datos.recursos[nombre];
    });
  }
  window.addEventListener('hashchange', mostrar);
  mostrar();
})();
