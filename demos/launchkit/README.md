# LaunchKit — Demo + DESIGN.md gratuito

Entrega aislada para el mantenedor de **ia.cuadrantia.store**. No modifica el catálogo, los packs ni la navegación del sitio. Basada en IMG_0987 y la referencia española aportadas por Jorge. Implementación independiente, sin afiliación con LaunchKit.

## Abrir y entregar

- **`index.html`**: demo autónoma en español, CSS, JavaScript, fotografía y DESIGN.md integrados. Se puede abrir sin conexión; no requiere servidor para usar sus controles.
- **`DESIGN.md`**: tokens en el formato del catálogo y especificación de composición, componentes, responsive y comportamiento.
- **`og.png`**: imagen social de 1200 × 630.
- **ZIP generado**: archivos directamente en la raíz, listo para subir manualmente a Cloudflare Pages. No se publica automáticamente.

En iPhone, Archivos/Quick Look puede no ejecutar JavaScript: para probar las interacciones, abrir la vista previa en Safari o subir el ZIP a Cloudflare Pages. El HTML sigue conteniendo todo el diseño sin recursos remotos.

Desde la raíz del repositorio:

```sh
python3 demos/launchkit/empaquetar.py --output ~/kits-cuadrantia/LaunchKit-gratis.zip
python3 -m unittest discover -s demos/launchkit -p 'test_*.py' -v
python3 -m http.server 8080 --bind 0.0.0.0 --directory demos/launchkit
```

`empaquetar.py` sincroniza el DESIGN.md integrado en el HTML antes de crear el ZIP. No usa red ni dependencias externas. El ZIP contiene `index.html`, `DESIGN.md`, `og.png` y este `README.md`; excluye los scripts de trabajo y las referencias del usuario.

## Integración opcional por el otro Bot

Copiar los cuatro archivos al directorio que el mantenedor elija. La ruta propuesta es `/demos/launchkit/`, pero **no está publicada**. Si se elige otra, cambiar `og:image` en el HTML. Añadir una URL canónica solo cuando haya una ubicación pública confirmada. La demo lleva `noindex,follow`; la ficha del catálogo puede indexarse por separado.

El recurso gratuito puede presentarse como **LaunchKit — Finanzas claras**, con demo y descarga de DESIGN.md. No se han añadido fichas a `catalogo.json` ni archivos generados por `src/build.py`.

## Límites claros

No es un banco, no presta servicios financieros ni usa IA real. Precios, marcas de ejemplo, recibos, resúmenes y conversiones son ficticios. El formulario no envía ni guarda el correo; no hay cuentas, suscripciones, cookies ni seguimiento. El micrófono es una simulación y no pide permisos.

La similitud visual es una adaptación a partir de una captura, no una medición del 95 %: se conservan composición y lenguaje visual, con tipografía de sistema y recursos propios. La vista móvil es una adaptación de la composición; el usuario solo proporcionó referencia de escritorio.

Fotografía ilustrativa integrada de Unsplash: https://images.unsplash.com/photo-1472396961693-142e6e269027. Se usa con el tratamiento de fondo desaturado y desenfocado; no representa al negocio. Los nombres y marcas ajenos no se transfieren con esta entrega.
