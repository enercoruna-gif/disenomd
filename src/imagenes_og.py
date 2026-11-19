"""Imágenes sociales del sitio; requiere Pillow (python3 -m pip install Pillow)."""

from PIL import Image, ImageDraw, ImageFont, ImageOps


FONDO = "#161616"
TINTA = "#EDEDED"
ACENTO = "#F5A9D6"


def fuente(tamano, mono=False):
    nombre = "DejaVuSansMono.ttf" if mono else "DejaVuSans-Bold.ttf"
    try:
        return ImageFont.truetype(nombre, tamano)
    except OSError:
        return ImageFont.load_default(size=tamano)


def logo(dibujo, xy, tamano):
    x, y = xy
    tipo = fuente(tamano, mono=True)
    dibujo.text((x, y), "diseño", font=tipo, fill=ACENTO)
    dibujo.text((x + dibujo.textlength("diseño", font=tipo), y), ".md", font=tipo, fill=TINTA)


def generar(salida, sitios):
    imagen = Image.new("RGB", (1200, 630), FONDO)
    dibujo = ImageDraw.Draw(imagen)
    logo(dibujo, (64, 42), 68)
    for y, texto, color in ((190, "Haz que la web que te crea", TINTA),
                            (272, "la IA parezca hecha", TINTA),
                            (354, "por un diseñador.", ACENTO)):
        dibujo.text((64, y), texto, font=fuente(64), fill=color)
    dibujo.line((64, 482, 1136, 482), fill=ACENTO, width=3)
    dibujo.text((64, 524), "Sistemas de diseño para tu IA · Gratis y en español", font=fuente(30), fill=TINTA)
    imagen.save(salida / "assets/og.png", optimize=True)

    for sitio in sitios:
        carpeta = salida / "analisis" / sitio["slug"]
        captura = carpeta / "captura.webp"
        if not captura.is_file():
            continue
        with Image.open(captura) as original:
            recorte = ImageOps.fit(original.convert("RGB"), (1200, 500), method=Image.Resampling.LANCZOS, centering=(0.5, 0))
        imagen = Image.new("RGB", (1200, 630), FONDO)
        imagen.paste(recorte, (0, 0))
        dibujo = ImageDraw.Draw(imagen)
        dibujo.line((0, 500, 1200, 500), fill=ACENTO, width=4)
        tamano = 44
        while tamano > 16 and dibujo.textlength(sitio["nombre"], font=fuente(tamano)) > 770:
            tamano -= 2
        dibujo.text((40, 530), sitio["nombre"], font=fuente(tamano), fill=TINTA)
        logo(dibujo, (900, 540), 38)
        imagen.save(carpeta / "og.jpg", quality=85, optimize=True, progressive=True)
