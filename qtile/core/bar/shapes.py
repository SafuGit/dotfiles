from libqtile.bar import CALCULATED
from libqtile.lazy import lazy
from libqtile import qtile

from core.bar.base import base, powerline, rectangle, symbol
from extras import Clock, GroupBox, TextBox, modify, widget, RectDecoration
from utils.config import cfg
from utils.palette import palette

def open_htop():
    lazy.spawn("alacritty -e htop")

bar = {
    "background": palette.base,
    "border_color": palette.base,
    "border_width": 4,
    "margin": [10, 10, 0, 10],
    "opacity": 1,
    "size": 20,
}


def sep(fg, offset=0, padding=10):
    return TextBox(
        **base(None, fg),
        **symbol(11),
        offset=offset,
        padding=padding,
        text="󰇙",
    )


logo = lambda bg, fg: TextBox(
    **base(bg, fg),
    **symbol(),
    **rectangle(),
    padding=20,
    text="",
)

groups = lambda bg: GroupBox(
    **symbol(),
    background=bg,
    borderwidth=1,
    colors=[
        "#55A98E", # Cyan-Green ish
        "#6b8e23", # Nature Green
        "#0D98BA", # Green-Blue
        "#ba3c3c", # Red
        "#AA9155", # Brown ish
        "#00A38E", # Cyan-Green
        "#228B22", # Deep Green
        "#AA3C72" # Magenta
    ],
    highlight_color=palette.base,
    highlight_method="line",
    inactive=palette.surface2,
    invert=True,
    padding=6,
    rainbow=True,
)

volume = lambda bg, fg: [
    modify(
        TextBox,
        **base(bg, fg),
        **symbol(),
        **rectangle("left"),
        offset=-17,
        padding=15,
        text="",
        x=-2,
    ),
    widget.Volume(
        **base(bg, fg),
        **powerline("arrow_right"),
        check_mute_command="pamixer --get-mute",
        check_mute_string="true",
        get_volume_command="pamixer --get-volume-human",
        mute_command="pamixer --toggle-mute",
        update_interval=0.1,
        volume_down_command="pamixer --decrease 5",
        volume_up_command="pamixer --increase 5",
    ),
]

updates = lambda bg, fg: [
    TextBox(
        **base(bg, fg),
        **symbol(14),
        offset=-1,
        text="",
        x=-2,
    ),
    widget.CheckUpdates(
        **base(bg, fg),
        **rectangle("right"),
        colour_have_updates=fg,
        colour_no_updates=fg,
        custom_command=" " if cfg.is_xephyr else "checkupdates",
        display_format="{updates} updates  ",
        initial_text="No updates  ",
        no_update_string="No updates  ",
        padding=0,
        update_interval=3600,
    ),
]

window_name = lambda fg: widget.WindowName(
    **base(None, fg),
    format="{name}",
    max_chars=60,
    width=CALCULATED,
)

cpu = lambda bg, fg: [
    modify(
        TextBox,
        **base(bg, fg),
        **symbol(14),
        **rectangle("left"),
        offset=-13,
        padding=15,
        text="󰍛",
    ),
    widget.CPU(
        **base(bg, fg),
        **powerline("arrow_right"),
        format="{load_percent:.0f}%",
        mouse_callbacks={
            "Button1": open_htop,
        }
    ),
]

ram = lambda bg, fg: [
    TextBox(
        **base(bg, fg),
        **symbol(14),
        offset=-1,
        padding=5,
        text="󰘚",
    ),
    widget.Memory(
        **base(bg, fg),
        **powerline("arrow_right"),
        format="{MemUsed: .0f}{mm} ",
        padding=-3,
    ),
]

disk = lambda bg, fg: [
    TextBox(
        **base(bg, fg),
        **symbol(14),
        offset=-1,
        text="",
        x=-2,
    ),
    widget.DF(
        **base(bg, fg),
        **rectangle("right"),
        format="{f} GB  ",
        padding=0,
        partition="/",
        visible_on_warn=False,
        warn_color=fg,
    ),
]

clock = lambda bg, fg: [
    modify(
        TextBox,
        **base(bg, fg),
        **symbol(14),
        **rectangle("left"),
        offset=-14,
        padding=15,
        text="",
    ),
    modify(
        Clock,
        **base(bg, fg),
        **rectangle("right"),
        format="%A - %I:%M %p ",
        long_format="%B %-d, %Y ",
        padding=7,
    ),
]


widgets = lambda: [
    widget.Spacer(length=1),
    logo("#36454F", "#56978c"),
    sep(palette.surface2, offset=-14),
    groups(None),
    sep(palette.surface2, offset=8, padding=2),
    *volume("#36454F", "#56978c"),
    *updates("#AA9155", palette.base),
    widget.Spacer(),
    window_name(palette.text),
    widget.Spacer(),
    *cpu("#AA9155", palette.base),
    *ram("#00A38E", palette.base),
    *disk("#36454F", "#56978c"),
    sep(palette.surface2),
    *clock("#36454F", "#FBFAF5"),
    widget.Spacer(length=1),
]
