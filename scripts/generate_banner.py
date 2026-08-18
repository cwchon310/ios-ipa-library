"""Generate banner.png for ios-ipa-library with pure PIL."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent.parent / "docs" / "banner.png"
W, H = 1200, 400

BG = (10, 14, 30)
TEXT = (240, 244, 255)
DIM = (150, 163, 190)
ACCENT = (96, 165, 250)
GREEN = (52, 211, 153)
AMBER = (251, 191, 36)


def _font(size: int, bold: bool = False):
    names = ["Arial Bold.ttf" if bold else "Arial.ttf",
             "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf",
             "Helvetica-Bold" if bold else "Helvetica.ttc",
             "PingFangSC-Semibold.ttf" if bold else "PingFangSC-Regular.ttf"]
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()


def main() -> None:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    title = _font(52, bold=True)
    subtitle = _font(26)
    small = _font(18)

    d.text((70, 70), "iOS IPA Library", font=title, fill=TEXT)
    d.text((70, 150), "精選可側載 IPA 收納庫 · 完整簽名教學", font=subtitle, fill=DIM)
    d.text((70, 205), "Curated sideloading IPAs · Complete signing tutorials", font=small, fill=ACCENT)

    # decorative app icons
    icons = [(900, 90, ACCENT), (1010, 90, GREEN), (900, 190, AMBER), (1010, 190, (167, 139, 250))]
    for x, y, color in icons:
        d.rounded_rectangle((x, y, x + 80, y + 80), radius=18, fill=color)
        d.rounded_rectangle((x + 20, y + 20, x + 60, y + 60), radius=10, fill=BG)
        d.text((x + 33, y + 32), "ipa", font=small, fill=color)

    # subtle bottom accent line
    d.rectangle((0, H - 6, W, H), fill=ACCENT)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG")
    print(f"written: {OUT}")


if __name__ == "__main__":
    main()