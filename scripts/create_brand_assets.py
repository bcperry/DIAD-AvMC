#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "Instructor" / "Data"
LOGO_PATH = DATA_DIR / "AvMC_Logo.png"
BACKGROUND_PATH = DATA_DIR / "Background.jpg"

ARMY_GOLD = (193, 168, 117)
ARMY_GREEN = (75, 83, 32)
ARMY_BLACK = (45, 41, 38)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
    ):
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def create_logo() -> None:
    image = Image.new("RGBA", (979, 122), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 978, 121), outline=ARMY_GOLD + (255,), width=3)
    draw.rectangle((10, 10, 108, 112), fill=ARMY_GREEN + (255,))
    draw.polygon([(59, 26), (68, 50), (94, 50), (73, 65), (81, 91), (59, 75), (37, 91), (45, 65), (24, 50), (50, 50)], fill=ARMY_GOLD + (255,))
    draw.text((132, 24), "DEVCOM AvMC", fill=ARMY_GOLD + (255,), font=font(46))
    draw.text((135, 78), "Aviation & Missile Center", fill=(235, 235, 225, 255), font=font(24))
    image.save(LOGO_PATH)


def create_background() -> None:
    width, height = 1280, 720
    image = Image.new("RGB", (width, height), ARMY_BLACK)
    draw = ImageDraw.Draw(image)

    for y_position in range(height):
        blend = y_position / height
        red = int(ARMY_BLACK[0] * (1 - blend) + 28 * blend)
        green = int(ARMY_BLACK[1] * (1 - blend) + 38 * blend)
        blue = int(ARMY_BLACK[2] * (1 - blend) + 42 * blend)
        draw.line((0, y_position, width, y_position), fill=(red, green, blue))

    for x_position in range(-200, width, 95):
        draw.line((x_position, height, x_position + 520, 0), fill=(59, 69, 55), width=2)

    for y_position in range(80, height, 92):
        draw.line((0, y_position, width, y_position), fill=(51, 55, 50), width=1)

    draw.rectangle((0, height - 118, width, height), fill=(33, 38, 33))
    draw.rectangle((0, height - 118, width, height - 111), fill=ARMY_GOLD)
    draw.text((54, height - 82), "DEVCOM AvMC", fill=ARMY_GOLD, font=font(34))
    draw.text((54, height - 43), "R&D engineering analytics", fill=(218, 218, 205), font=font(22))

    image.save(BACKGROUND_PATH, quality=92)


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    create_logo()
    create_background()
    print(f"Created {LOGO_PATH}")
    print(f"Created {BACKGROUND_PATH}")


if __name__ == "__main__":
    main()
