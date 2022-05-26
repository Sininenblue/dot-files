# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# todo, figure out a way to move and float windows, and put them back to tile
# could do this through just makeing it so that I can disable floating through a shortcut
# also floating mode border

# also change the margin of the bar and the windows
# basically I want the border to have 4 bottom margin
# and the windows no margin to make max have proper margins

import os
import subprocess
# import iwlib
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([home])


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Custom
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle Floating"),
    Key([mod], "p", lazy.spawn("rofi -show drun"), desc="Launch program launcher"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Launch run launcher"),
    # Custom Media
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Take a screenshot"),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer sset Master 5%-"),
        desc="Lower volume",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer sset Master 5%+"),
        desc="Raise volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("amixer -D default set Master toggle"),
        desc="Mute volume",
    ),
    
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "n", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "e", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "n", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "e", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "n", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "e", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "k", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

#groups = [Group(i) for i in ["★", "★", "3★", "4★", "5★"]]
groups = [Group(i) for i in ["", "", "", "", ""]]
#groups = [Group(i) for i in "12345"]
group_hotkeys = "12345"

for i, k in zip(groups, group_hotkeys):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                k,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                k,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        # border_on_single=True,
        border_focus="#575268",
        border_normal="#161320",
        border_width=2,
        margin=[0, 4, 4, 4],
        ),
    layout.Max(),
    # layout.Floating(
    #     border_focus="#575268",
    #     border_normal="#161320",
    #     border_width=4,
    #     ),
    # layout.Bsp(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    fontsize=12,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=18,
                    active="#96CDFB",
                    inactive="#6E6C7E",
                    foreground="#96CDFB",
                    rounded=False,
                    borderwidth=2,
                    margin=4,
                    highlight_method="line",
                    highlight_color="#161320",
                    other_screen_border="#6E6C7E",
                    other_current_screen_border="#96CDFB",
                    this_current_screen_border="#96CDFB",
                    this_screen_border="#6E6C7E",
                    ),
                widget.Prompt(
                    foreground="#d9e0ee",
                    ),
                widget.WindowName(
                    foreground="#d9e0ee",
                    font="jetbrainsmono nerd font medium",
                    ),
                widget.Chord(
                    foreground="#d9e0ee",
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                    ),
                # widget.Systray(icon_size=15),
                widget.Volume(
                    foreground="#96cdfb",
                    fmt="墳 {}"
                    ),
                widget.Sep(
                    foreground="#96CDFB",
                    line_width=2,
                    size_percent=50,
                    ),
                widget.Backlight(
                    foreground="#d9e0ee",
                    backlight_name="radeon_bl0",
                    fmt="☀ {}"
                    ),
                widget.Sep(
                    foreground="#96CDFB",
                    line_width=2,
                    size_percent=50,
                    ),
                # widget.Wlan(),
                widget.Battery(
                    foreground="#96CDFB",
                    low_foreground="#F28FAD",
                    low_percentage=.3,
                    format="{char} {percent:2.0%}",
                    charge_char="",
                    discharge_char="",
                    full_char="",
                    unknown_char="",
                    empty_char="",
                    ),
                widget.Sep(
                    foreground="#96CDFB",
                    line_width=2,
                    size_percent=50,
                    ),
                widget.Clock(
                    foreground="#d9e0ee",
                    format=" %a %I:%M %p"
                    ),
                widget.Sep(
                    foreground="#96CDFB",
                    line_width=2,
                    size_percent=50,
                    ),
                widget.CurrentLayout(
                    foreground="#96CDFB",
                    ),
                widget.Sep(
                    foreground="#96CDFB",
                    line_width=2,
                    size_percent=50,
                    ),
                widget.TextBox(
                    text="⏻",
                    mouse_callbacks={"Button1": lazy.spawn("systemctl poweroff"),}
                ),
                widget.TextBox(
                    text="⟳",
                    fontsize=18,
                    mouse_callbacks={"Button1": lazy.spawn("systemctl restart"),}
                ),
                widget.TextBox(
                    text="⏾",
                    mouse_callbacks={"Button1": lazy.spawn("systemctl suspend"),}
                ),
                widget.Sep(
                    foreground="#161320", # a shitty margin because I'm lazy
                    linewidth=1,
                ),
            ],
            20,
            background="#161320",
            opacity=.95,
            margin=[4, 4, 4, 4]
            # border_width=[0, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["000000", "000000", "96CDFB", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus = "#96CDFB",
    border_normal = "#161320",
    border_width = 2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
