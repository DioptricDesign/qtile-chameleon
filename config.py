#  ____  _   _ _         _____             __ _
# / __ \| | (_) |       / ____|           / _(_)
#| |  | | |_ _| | ___  | |     ___  _ __ | |_ _  __ _
#| |  | | __| | |/ _ \ | |    / _ \| '_ \|  _| |/ _` |
#| |__| | |_| | |  __/ | |___| (_) | | | | | | | (_| |
# \___\_\\__|_|_|\___|  \_____\___/|_| |_|_| |_|\__, |
#                                                __/ |
#                                               |___/
#This configuration is Feature Rich and comfortable.
#It depends on rofi, urxvt i3-lock, scrot, Font Awesome, pywal, dunst, redshift, polkit-gnome, compton and playerctl, For utilities and libraries.
from libqtile.config import Key, Screen, Group, Drag, Click, DropDown, ScratchPad
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook, qtile
from typing import List
import os, subprocess, json
#Hooks
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
@hook.subscribe.startup
def autorestart():
    home = os.path.expanduser('~/.config/qtile/autorestart.sh')
    subprocess.call([home])
#Pywal Colors
colors = os.path.expanduser('~/.cache/wal/colors.json')
colordict = json.load(open(colors))
ColorZ=(colordict['colors']['color0'])
ColorA=(colordict['colors']['color1'])
ColorB=(colordict['colors']['color2'])
ColorC=(colordict['colors']['color3'])
ColorD=(colordict['colors']['color4'])
ColorE=(colordict['colors']['color5'])
ColorF=(colordict['colors']['color6'])
ColorG=(colordict['colors']['color7'])
ColorH=(colordict['colors']['color8'])
ColorI=(colordict['colors']['color9'])
#Hotkeys
mod = "mod4"
keys = [
    #Layout Management
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key(["mod1"], "n", lazy.layout.normalize()),
    Key([mod], "n", lazy.next_layout()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key(["mod1"], "f", lazy.window.toggle_floating()),
    Key([mod], "Return", lazy.layout.toggle_split()),
    Key([mod], "space", lazy.layout.rotate()),
    Key(["mod1"], "b", lazy.spawn("bartoggle")),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "e", lazy.shutdown()),
    Key([mod], "q", lazy.window.kill()),
    Key ([mod], "grave", lazy.group['scratchpad'].dropdown_toggle('term')),
    #Application Hotkeys
    Key([], "Print", lazy.spawn("scrot ~/Pictures/scrots")),
    Key([mod], "w", lazy.spawn("firefox")),
    Key([mod], "e", lazy.spawn("emacs")),
    Key([mod], "r", lazy.spawn("liferea")),
    Key([mod], "c", lazy.spawn("qalculate-gtk")),
    Key([mod], "p", lazy.spawn("gpodder")),
    Key([mod], "t", lazy.spawn("urxvt")),
    Key([mod], "m", lazy.spawn("thunderbird")),
    Key([mod,"shift"], "w", lazy.spawn("walp")),
    Key([mod], "v", lazy.spawn("vlc")),
    Key([mod], "b", lazy.spawn("pcmanfm-qt")),
    Key([mod], "d", lazy.spawn("discord")),
    #Audio and Media
    Key([mod], 'Page_Down', lazy.spawn('pulseaudio-ctl down 5')),
    Key([mod], 'Page_Up', lazy.spawn('pulseaudio-ctl up 5')),
    Key([mod], 'End', lazy.spawn("amixer -q set Master toggle")),
    Key([mod], 'Left', lazy.spawn("playerctl previous")),
    Key([mod], 'Right', lazy.spawn("playerctl next")),
    Key([mod], 'Down', lazy.spawn("playerctl play-pause")),
    #Launcher & App Switcher
    Key(["mod1"], "d", lazy.spawn("dmen")),
    Key(["mod1"], "r", lazy.spawn("rofi -show run -modi run,window -show-icons -sidebar-mode")),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window -show-icons")),
    Key(["mod1"], "s", lazy.spawn("rofi -show ssh")),
    #Notification Scripts
    Key([mod], "s", lazy.spawn("sensornote")),
    Key(["mod1"], "q", lazy.spawn("hotkey")),
    #Rofi Scripts
    Key(["mod1"], "p", lazy.spawn("clipmenu")),
    Key(["mod1", "control"], "a", lazy.spawn ("xautolockmenu")),
    Key(["mod1", "control"], "p", lazy.spawn ("powermenu")),
    Key(["mod1", "control"], "s", lazy.spawn ("scrotmenu")),
    Key(["mod1", "control"], "l", lazy.spawn ("libmenu")),
    Key(["mod1", "control"], "g", lazy.spawn ("gamesmenu")),
    Key(["mod1", "control"], "c", lazy.spawn ("comptonmenu")),
    Key(["mod1", "control"], "k", lazy.spawn ("calendarmenu")),
    Key(["mod1", "control"], "o", lazy.spawn ("outputmenu")),
    Key(["mod1", "control"], "m", lazy.spawn ("chatmenu")),
    Key(["mod1", "control"], "t", lazy.spawn ("timermenu")),
    Key(["mod1", "control"], "v", lazy.spawn ("virtualmenu")),
    Key(["mod1", "control"], "x", lazy.spawn ("graphicsmenu"))
]
#Workspace Groups
group_names = [("I", {}),
               ("II", {}),
               ("III", {}),
               ("IV", {}),
               ("V", {}),
               ("VI", {}),
               ("VII", {}),
               ("VIII", {}),
               ("IX", {})]
groups = [Group(name, **kwargs) for name, kwargs in group_names]
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group
groups = [ScratchPad("scratchpad",[
          DropDown("term", "urxvt", opacity=0.95)]),
          Group("I", layout='monadtall'),
          Group("II", layout='monadtall',),
          Group("III", layout='monadtall',),
          Group("IV", layout='monadtall',),
          Group("V", layout='max',),
          Group("VI", layout='bsp',),
          Group("VII", layout='bsp',),
          Group("VIII", layout='bsp',),
          Group("IX", layout='bsp',]
#Layouts
layouts = [
    layout.MonadTall(num_stacks=2,
                     margin=5,
                     border_focus=ColorC,
                     border_normal=ColorZ),
    layout.Bsp(num_stacks=2,
               margin=5,
               border_focus=ColorC,
               border_normal=ColorZ),
    layout.Max(margin=5,
               border_focus=ColorC,
               border_normal=ColorZ)
]

floating_layout = layout.Floating(
    border_focus=ColorC,
    border_normal=ColorZ,
    float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='ssh-askpass'),
    Match(title='branchdialog'),
    Match(title='pinentry'),
    Match(title='Library'),
    Match(title='Unlock Login Keyring'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='lxpolkit'),
    Match(wm_class='error'),
    Match(wm_class='pamac-manager'),
    Match(wm_class='lxappearance'),
    Match(wm_class='kvantummanager'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='gcolor2'),
    Match(wm_class='qalculate-gtk'),
    Match(wm_class='qt5ct'),
    Match(wm_class='keepassxc'),
])
#Bar
widget_defaults = dict(font='Noto Sans',
                       fontsize=14,
                       padding=3,)
extension_defaults = widget_defaults.copy()
screens = [ Screen( top=bar.Bar( [
    widget.GroupBox(highlight_method='block',
                    rounded = False,
                    background=ColorA,
                    this_current_screen_border=ColorC,
                    this_screen_border=ColorB,
                    inactive=ColorZ,
                    other_screen_border=ColorB,
                    active=ColorG,
                    urgent_text=ColorC,
                    urgent_border=ColorF,
                    other_current_screen_border=ColorC,
                    font='Noto Serif'),
    widget.TextBox(text='\uE0B0',
                   background=ColorB,
                   fontsize=20,
                   padding=0,
                   foreground=ColorA),
    widget.WindowName(mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('dmen')},
                      foreground=ColorG,
                      background=ColorB,
                      padding=10),
    widget.TextBox(text='\uE0B2',
                   background=ColorB,
                   fontsize=20,
                   padding=0,
                   foreground=ColorA),
    widget.TextBox(mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('urxvt -e nmtui')},
                   text='',
                   background=ColorA,
                   foreground=ColorG),
    widget.Wlan(interface='wlp0s19f2u1',
                update_interval=3,
                background=ColorA,
                foreground=ColorG),
    widget.TextBox(text='\uE0B2',
                   background=ColorA,
                   fontsize=20,
                   padding=0,
                   foreground=ColorB),
    widget.CPU (foreground=ColorG,
                background=ColorB),
    widget.TextBox(mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('urxvt -e htop')},
                   text='',
                   foreground=ColorG,
                   background=ColorB),
    widget.Memory(foreground=ColorG,
                  background=ColorB),
    widget.TextBox(text='\uE0B2',
                   background=ColorB,
                   fontsize=20,
                   padding=0,
                   foreground=ColorA),
    widget.TextBox(mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('pavucontrol-qt')},
                   text='',
                   foreground=ColorG,
                   background=ColorA),
    widget.Volume(foreground=ColorG,
                  background=ColorA),
    widget.TextBox(mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('urxvt -e khal interactive')},
                   text='',
                   background=ColorA,
                   foreground=ColorG),
    widget.Clock(format='%a %m-%d-%Y',
                 background=ColorA,
                 foreground=ColorG),
    widget.TextBox(mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('timermenu')},
                   text='',
                   background=ColorA,
                   foreground=ColorG),
    widget.Clock(mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('urxvt -e peaclock')},
                 format='%I:%M %p',
                 background=ColorA,
                 foreground=ColorG,
                 padding=5),
    widget.TextBox(text='\uE0B2',
                   background=ColorA,
                   fontsize=20,
                   padding=0,
                   foreground=ColorB),
    widget.Systray(background=ColorB,
                   padding=5),
    widget.CurrentLayoutIcon(scale=.7,
                             background=ColorB)
], 20, background=ColorZ )),
]
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
	"window_type = 'desktop'",
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
