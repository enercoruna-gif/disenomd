# Crix — demo en español y DESIGN.md gratuito

Recreación independiente de la referencia visual IMG_0995 aportada por Jorge. Se entrega para que el mantenedor de ia.cuadrantia.store integre la demo y la guía donde corresponda. No modifica el catálogo, los generadores ni las páginas existentes del repositorio.

## Ver la demo

Abre `index.html` o ejecuta desde esta carpeta:

```sh
python3 -m http.server 4173
```

La página es estática, no tiene dependencias ni necesita instalación. El panel permite marcar tareas, filtrar vistas y añadir tareas locales. Los cambios desaparecen al recargar. No crea cuentas, no contacta con un servidor, no contrata planes y no cobra. El selector mensual/anual cambia precios ilustrativos, no ofertas reales.

## Generar la entrega

```sh
python3 build.py --output /ruta/a/entrega
```

Genera `Crix-completo.zip`, con los archivos de la web en la raíz; `Crix-autonomo.html`, con imagen, estilos, JavaScript y descarga del DESIGN.md embebidos; y una copia de `DESIGN.md`.

Para Cloudflare Pages, subir el contenido del ZIP como sitio estático, sin comando de build. En iPhone se puede abrir el HTML autónomo sin red; si el visor de archivos de iOS no ejecuta JavaScript, el contenido visual sigue disponible. Para interactuar con el panel, abrir la página servida en Safari.

## Integración

- Publicar esta carpeta en la ruta elegida por el mantenedor y enlazar `DESIGN.md` como descarga gratuita.
- Mantener los avisos de demo y el crédito fotográfico.
- Convertir `og:image` en URL absoluta y añadir canonical únicamente cuando exista la ruta final.
- No añadir el código al generador del catálogo sin coordinarlo con el Bot que mantiene el sitio.

## Validación

```sh
python3 test_delivery.py
node --check app.js
```

No se encontró configuración de pre-commit ni hooks personalizados en este repositorio.

## Créditos y alcance

Referencia: Crix, captura IMG_0995 proporcionada por el solicitante. No afiliado al autor original. Se recrean estructura y dirección visual con código propio, textos en español, interfaces de ejemplo y una fotografía de sustitución: no se afirma una coincidencia del 95 % medida.

Fotografía de archivo ilustrativa de [Unsplash](https://images.unsplash.com/photo-1454496522488-7a8e488e8606), adaptada cromáticamente; [licencia de Unsplash](https://unsplash.com/license). No se redistribuyen tipografías ni otros recursos de pago. Las miniaturas de producto, los precios y los textos editoriales son ilustrativos; no se atribuyen testimonios a personas reales.
