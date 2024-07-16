from libqtile.config import Group, Key
from libqtile.lazy import lazy

from core.keys import keys, mod
from utils.match import wm_class

groups: list[Group] = []

for key, label, layout, matches in [
    ("1", "󰇄", None, wm_class()),
    ("2", "", None, wm_class("qterminal", "alacritty", "github-desktop")),
    ("3", "", None, wm_class("code")),
    ("4", "", None, wm_class("insomnia", "obs", "evince", "pcmanfm-qt")),
    ("5", "󰈹", None, wm_class("brave-browser", "firefox")),
    ("6", "󰭻", None, wm_class("discord", "telegram-desktop")),
    ("7", "", None, wm_class("spotify", "vlc")),
    ("8", "", None, wm_class("instagram", "whatsapp-web")),
]:
    groups.append(Group(key, matches, label=label, layout=layout))

    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], key, lazy.group[key].toscreen(toggle=True)),

        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], key, lazy.window.togroup(key)),
    ])  # fmt: skip
