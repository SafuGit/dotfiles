from libqtile.config import Screen

from core.bar import Bar
from utils.config import cfg

screens = [
    Screen(
        wallpaper="~/.config/qtile/background.jpeg",
        wallpaper_mode="fill",
        top=Bar(cfg.bar).create(),
    ),
    Screen(
        wallpaper="~/.config/qtile/background.jpeg",
        wallpaper_mode="fill",
        top=Bar(cfg.bar2).create(),
    ),
]