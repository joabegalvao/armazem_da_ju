#!/usr/bin/env python3
"""Gera as imagens otimizadas da landing page a partir dos arquivos originais.

Uso (na raiz do projeto):
    python3 tools/optimize-images.py

Requer Pillow (pip install pillow). Os originais nunca são alterados.
Para trocar uma foto, substitua o arquivo de origem ou edite a lista PHOTOS
e rode o script novamente.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "materiais-de-origem"
SRC = SOURCES / "fotos"
AVATAR_SRC = SOURCES / "avaliacoes"
LOGO_SRC = SOURCES / "logo" / "ju_essencias.jpg"
OUT = ROOT / "assets" / "img"

# largura -> qualidade WebP. A versão maior só é usada em telas de alta
# densidade, onde a compressão mais forte não aparece.
WIDTHS = {480: 78, 800: 72, 1000: 60}
LOGO_INK = (30, 27, 7)       # #1E1B07, contorno e letras do logo
LOGO_BUTTER = (254, 248, 170)  # #FEF8AA, fundo do rótulo
PAPER = (255, 252, 240)      # #FFFCF0, fundo claro da página

# nome de saída -> arquivo em materiais-de-origem/fotos
PHOTOS = {
    "bandeja-linha-artesanal": "foto-163336-tratada.png",
    "cantinho-da-loja": "foto-163345-tratada.png",
    "mesa-sais-de-banho": "foto-163401-tratada.png",
    "frascos-alfa-omega": "foto-163437-tratada.png",
    "vitrine-de-natal": "foto-163156-tratada.png",
}

# Fotos de perfil: nome de saída -> arquivo em materiais-de-origem/avaliacoes
AVATARS = {
    "avaliacao-ely-melo": "Ely_Melo.png",
    "avaliacao-claudia-regina": "Claudia_Regina.png",
    "avaliacao-michelle-almeida": "Michelle_Almeida.png",
}

# Recortes de borda (esquerda, topo, direita, base), em pixels do original.
# Use quando o arquivo de origem trouxer faixas nas extremidades.
CROPS = {}


def open_source(source: str) -> Image.Image:
    im = Image.open(SRC / source).convert("RGB")
    left, top, right, bottom = CROPS.get(source, (0, 0, 0, 0))
    return im.crop((left, top, im.width - right, im.height - bottom))


def resize_to_width(im: Image.Image, width: int) -> Image.Image:
    if im.width <= width:
        return im.copy()
    height = round(im.height * width / im.width)
    return im.resize((width, height), Image.LANCZOS)


def build_photos() -> None:
    for name, source in PHOTOS.items():
        im = open_source(source)
        for width, quality in WIDTHS.items():
            resize_to_width(im, width).save(
                OUT / f"{name}-{width}.webp", "WEBP", quality=quality, method=6
            )
        # fallback JPEG para navegadores sem WebP
        resize_to_width(im, 800).save(
            OUT / f"{name}-800.jpg", "JPEG", quality=80, optimize=True, progressive=True
        )
        print(f"{name}: {im.width}x{im.height}")


def cut_out_label(logo: Image.Image) -> Image.Image:
    """Separa o rótulo do fundo branco.

    O contorno do rótulo é escuro e neutro; o miolo é amarelo. Partindo dos
    cantos, a área neutra (branco, cinza da suavização e contorno) é
    preenchida até encontrar o amarelo. Nessa área, a cor vira a do contorno
    e a transparência vem do quanto o pixel é claro: branco fica invisível,
    contorno fica sólido. O miolo e as letras não são tocados."""
    rgb = logo.convert("RGB")
    width, height = rgb.size
    pixels = rgb.load()

    neutral = Image.new("L", rgb.size, 0)
    mark = neutral.load()
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if r - b < 30:
                mark[x, y] = 255

    for corner in ((0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1)):
        if mark[corner] == 255:
            ImageDraw.floodfill(neutral, corner, 128)

    out = Image.new("RGBA", rgb.size)
    target = out.load()
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if mark[x, y] == 128:
                light = (r * 299 + g * 587 + b * 114) / 1000
                alpha = max(0.0, min(1.0, (235 - light) / (235 - 45)))
                target[x, y] = LOGO_INK + (round(alpha * 255),)
            else:
                target[x, y] = (r, g, b, 255)
    return out


def build_logo() -> None:
    """O logo original tem 150x150 px, com o rótulo ocupando 140x83 px. Nada
    é redesenhado: o script amplia a imagem, recorta a margem vazia e torna
    transparente o fundo branco em volta do rótulo."""
    logo = Image.open(LOGO_SRC).convert("RGB")

    scale = 4
    big = logo.resize((logo.width * scale, logo.height * scale), Image.LANCZOS)
    big = big.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
    label = cut_out_label(big)
    label = label.crop(label.getchannel("A").getbbox())

    for width in (label.width, 280):
        out = label if width == label.width else resize_to_width(label, width)
        out.save(OUT / f"logo-armazem-da-ju-{width}.png", optimize=True)
        out.save(OUT / f"logo-armazem-da-ju-{width}.webp", "WEBP", quality=92, method=6)
    print(f"logo-armazem-da-ju: {label.width}x{label.height}")

    # Ícones: rótulo centralizado sobre o fundo claro da página
    for name, size in (("favicon-32", 32), ("apple-touch-icon", 180), ("icon-192", 192)):
        icon = Image.new("RGB", (size, size), PAPER)
        mark = resize_to_width(label, round(size * 0.92))
        icon.paste(mark, ((size - mark.width) // 2, (size - mark.height) // 2), mark)
        icon.save(OUT / f"{name}.png", optimize=True)


def build_avatars() -> None:
    """Mantém o tamanho e a transparência originais (72x72 px)."""
    for name, source in AVATARS.items():
        im = Image.open(AVATAR_SRC / source).convert("RGBA")
        im.save(OUT / f"{name}.png", optimize=True)
        im.save(OUT / f"{name}.webp", "WEBP", quality=90, method=6)
        print(f"{name}: {im.width}x{im.height}")


def build_social_card() -> None:
    """Imagem de compartilhamento (1200x630): logo à esquerda e foto à direita."""
    card = Image.new("RGB", (1200, 630), PAPER)

    photo = open_source(PHOTOS["bandeja-linha-artesanal"])
    photo = ImageOps.fit(photo, (560, 630), Image.LANCZOS, centering=(0.5, 0.8))
    card.paste(photo, (640, 0))

    logo = Image.open(next(OUT.glob("logo-armazem-da-ju-5*.png"))).convert("RGBA")
    logo = resize_to_width(logo, 480)
    card.paste(logo, ((640 - logo.width) // 2, (630 - logo.height) // 2), logo)

    card.save(OUT / "compartilhamento.jpg", "JPEG", quality=86, optimize=True, progressive=True)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    build_photos()
    build_logo()
    build_avatars()
    build_social_card()
    total = sum(f.stat().st_size for f in OUT.iterdir())
    print(f"{len(list(OUT.iterdir()))} arquivos, {total / 1024:.0f} KB no total")
