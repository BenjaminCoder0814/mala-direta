"""
Adiciona marca d'agua diagonal (logo Zenith) em todas as imagens de produto.
Execucao: python add_watermark.py
"""
from PIL import Image
import os

LOGO_PATH  = r"C:\Users\User\Downloads\MALA DIRETA\Imagens\logo.png"
IMGS_DIR   = r"C:\Users\User\Downloads\MALA DIRETA\Imagens"
EXTENSIONS = ('.png', '.jpg', '.jpeg')

# Arquivos na raiz de Imagens que NAO sao produtos
SKIP_ROOT_FILES = {'logo.png', 'Banner.png', 'icone wpp.png',
                   'Catálogo ZENITH capa.jpg', 'Catálogo ZENITH.pdf'}

STAMP_W  = 180   # largura de cada carimbo do logo em pixels
OPACITY  = 38    # transparencia do carimbo (0-255). 38 ≈ 15%
SPACING  = 70    # espaco extra entre carimbos (px)
ANGLE    = -45   # inclinacao diagonal


def prepare_stamp(logo_path: str, stamp_w: int, opacity: int) -> Image.Image:
    """Redimensiona o logo, remove fundo branco se houver e aplica opacidade."""
    logo = Image.open(logo_path).convert("RGBA")
    ow, oh = logo.size
    stamp_h = int(stamp_w * oh / ow)
    logo = logo.resize((stamp_w, stamp_h), Image.LANCZOS)

    # Vectorizado: remove pixels brancos/quase-brancos que podem existir
    r, g, b, a = logo.split()
    import PIL.ImageChops as ic
    # Pixels com R,G,B todos > 210 → transparente
    r_data = r.getdata()
    g_data = g.getdata()
    b_data = b.getdata()
    a_data = list(a.getdata())
    for i, (rv, gv, bv) in enumerate(zip(r_data, g_data, b_data)):
        if rv > 210 and gv > 210 and bv > 210:
            a_data[i] = 0
    a.putdata(a_data)

    # Reduz opacidade de todos os pixels pelo fator desejado
    a_scaled = a.point(lambda p: int(p * opacity / 255))
    return Image.merge('RGBA', (r, g, b, a_scaled))


def build_overlay(img_size: tuple, stamp: Image.Image,
                  angle: int, spacing: int) -> Image.Image:
    """Cria uma camada RGBA do mesmo tamanho da imagem com o logo em mosaico diagonal."""
    w, h = img_size
    rotated = stamp.rotate(angle, expand=True, resample=Image.BICUBIC)
    rw, rh = rotated.size
    step_x = rw + spacing
    step_y = rh + spacing

    # Canvas maior para cobrir bordas apos corte
    canvas = Image.new('RGBA', (w + step_x * 2, h + step_y * 2), (0, 0, 0, 0))
    for cy in range(-step_y, h + step_y * 2, step_y):
        for cx in range(-step_x, w + step_x * 2, step_x):
            canvas.paste(rotated, (cx, cy), rotated)
    return canvas.crop((0, 0, w, h))


def watermark_image(img_path: str, stamp: Image.Image,
                    angle: int, spacing: int) -> None:
    img = Image.open(img_path).convert("RGBA")
    overlay = build_overlay(img.size, stamp, angle, spacing)
    result = Image.alpha_composite(img, overlay)

    if img_path.lower().endswith(('.jpg', '.jpeg')):
        result.convert("RGB").save(img_path, "JPEG", quality=92, optimize=True)
    else:
        result.save(img_path, "PNG", optimize=True)


# ─── MAIN ────────────────────────────────────────────────────────────────────
print("Preparando carimbo do logo...")
stamp = prepare_stamp(LOGO_PATH, STAMP_W, OPACITY)
print(f"  Carimbo: {stamp.size[0]}x{stamp.size[1]}px, opacidade {OPACITY}/255\n")

ok_count = 0
err_list = []

for root, dirs, files in os.walk(IMGS_DIR):
    is_root = os.path.abspath(root) == os.path.abspath(IMGS_DIR)
    for fname in files:
        if not fname.lower().endswith(EXTENSIONS):
            continue
        if is_root and fname in SKIP_ROOT_FILES:
            continue  # pula logo, banner e catalogo
        fpath = os.path.join(root, fname)
        try:
            watermark_image(fpath, stamp, ANGLE, SPACING)
            ok_count += 1
            rel = os.path.relpath(fpath, IMGS_DIR)
            print(f"  [OK] {rel}")
        except Exception as e:
            err_list.append((fname, str(e)))
            print(f"  [ERRO] {fname}: {e}")

print(f"\n{'='*50}")
print(f"Concluido: {ok_count} imagens com marca d'agua.")
if err_list:
    print(f"Erros ({len(err_list)}):")
    for n, e in err_list:
        print(f"  - {n}: {e}")
