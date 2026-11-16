"""Рисует иконку приложения (белое сердце на зелёном) в папку assets/."""
import math, os
from PIL import Image, ImageDraw
S = 1024
os.makedirs("assets", exist_ok=True)
def heart(d, cx, cy, size, fill):
    pts = []
    for i in range(0, 360, 2):
        t = math.radians(i)
        x = 16 * math.sin(t) ** 3
        y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
        pts.append((cx + x * size / 34, cy + y * size / 34))
    d.polygon(pts, fill=fill)
green = (47, 111, 94, 255)
im = Image.new("RGBA", (S, S), green); heart(ImageDraw.Draw(im), S / 2, S / 2 + 20, 620, (255, 255, 255, 255)); im.save("assets/icon-only.png")
fg = Image.new("RGBA", (S, S), (0, 0, 0, 0)); heart(ImageDraw.Draw(fg), S / 2, S / 2 + 15, 470, (255, 255, 255, 255)); fg.save("assets/icon-foreground.png")
Image.new("RGBA", (S, S), green).save("assets/icon-background.png")
