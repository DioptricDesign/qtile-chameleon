#  ___  _   _ _                  A Qtile Config With Pywal
# / _ \| |_(_) | ___  Requires:  playerctl dunst scrot clipmenu xautolock 
#| | | | __| | |/ x \ pywal rofi dmenu lm-sensors urxvt firefox
#| | | | |_| | |  __/ i3lock htop notify-send khal pavucontol feh psutil
# \__\_\\__|_|_|\___| Backgrounds should go in ~/.local/share/backgrounds
# A Link to the acompanying scripts and start page is in the readme.
from typing import List
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os, subprocess, json

# Functions
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
@hook.subscribe.startup
def autorestart():
    home = os.path.expanduser('~/.config/qtile/autorestart.sh')
    subprocess.call([home])
def htop():
    qtile.cmd_spawn('urxvtc -e htop')
def powermenu():
    qtile.cmd_spawn('powermenu')
def weather():
    qtile.cmd_spawn('xdg-open https://openweathermap.org/city/3333147')
def sound():
    qtile.cmd_spawn('pavucontrol')
def calendar():
    qtile.cmd_spawn('urxvtc -e khal interactive')
def dmen():
    qtile.cmd_spawn('dmen')
def timer():
    qtile.cmd_spawn('timermenu')

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
terminal = guess_terminal()

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
    Key([mod], "Right", lazy.next_layout()),
    Key([mod], "Left", lazy.prev_layout()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key(["mod1"], "f", lazy.window.toggle_floating()),
    Key([mod], "Return", lazy.layout.toggle_split()),
    Key(["mod1"], "b", lazy.spawn("bartoggle")),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "e", lazy.shutdown()),
    Key([mod], "x", lazy.window.kill()),
    Key([mod], "q", lazy.window.kill()),
    Key(["mod1"], "F4", lazy.window.kill()),
    Key(["mod1"], "x", lazy.spawn("xkill")),
    Key ([mod], "grave", lazy.group['scratchpad'].dropdown_toggle('term')),

    #Application Hotkeys
    Key(["mod1", "control"], "Delete", lazy.spawn ("urxvtc -e htop")),
    Key([], "Print", lazy.spawn("scrot $HOME/Pictures/scrots/")),
    Key([mod], "w", lazy.spawn("firefox")),
    Key(["mod1"], "w", lazy.spawn("qutebrowser")),
    Key([mod], "e", lazy.spawn("emacsclient -c ")),
    Key([mod], "r", lazy.spawn("akregator")),
    Key([mod], "o", lazy.spawn("pavucontrol")),
    Key([mod], "c", lazy.spawn("qalculate-gtk")),
    Key(["mod1"], "c", lazy.spawn("gcolor3")),
    Key([mod], "g", lazy.spawn("gpodder")),
    Key([mod], "t", lazy.spawn("urxvtc")),
    Key(["mod1"], "t", lazy.spawn("xterm")),
    Key([mod], "m", lazy.spawn("thunderbird")),
    Key([mod,"shift"], "w", lazy.spawn("walp")),
    Key([mod], "v", lazy.spawn("vlc")),
    Key([mod], "b", lazy.spawn("pcmanfm")),

    #Audio and Media
    Key([mod], 'minus', lazy.spawn('pulseaudio-ctl down 5')),
    Key([mod], 'equal', lazy.spawn('pulseaudio-ctl up 5')),
    Key([mod], '0', lazy.spawn("pulseaudio-ctl mute")),
    Key([mod], 'comma', lazy.spawn("playerctl previous")),
    Key([mod], 'period', lazy.spawn("playerctl next")),
    Key([mod], 'slash', lazy.spawn("playerctl play-pause")),

    #Launcher & App Switcher
    Key(["mod1"], "d", lazy.spawn("dmen")),
    Key(["mod1"], "r", lazy.spawn("rofi -show run -modi run,window -show-icons -sidebar-mode")),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window -show-icons")),
    Key(["mod1"], "s", lazy.spawn("rofi -show ssh")),

    #Notification Scripts
    Key([mod], "s", lazy.spawn("sensornote")),
    Key(["mod1", "control"], "h", lazy.spawn("hotkey")),

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
          Group("V", layout='max', matches=[Match(wm_class=["gimp","Inkscape","krita","darktable","shotwell","scribus"])]),
          Group("VI", layout='max', matches=[Match(wm_class=["VirtualBox Machine","VirtualBox Manager"])]),
          Group("VII", layout='bsp',),
          Group("VIII", layout='bsp',),
          Group("IX", layout='bsp', matches=[Match(wm_class=["Steam","Lutris","RetroArch","dosbox"])])]

layouts = [
     layout.Bsp(margin=5,
                border_focus=ColorE,
                border_normal=ColorA),
     layout.MonadTall(margin=5,
                border_focus=ColorE,
                border_normal=ColorA),
     layout.Max(),
]

#Widget Defaults
widget_defaults = dict(
    font='Source Code Pro',
    fontsize=13,
    padding=5,
    foreground=ColorG
)
extension_defaults = widget_defaults.copy()

#Screens
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(highlight_method='line',
                                urgent_border=ColorF,
                                active=ColorG,
                                inactive=ColorB,
                                this_screen_border=ColorB,
                                this_current_screen_border=ColorC,),
                widget.WindowName(mouse_callbacks = {'Button1':dmen}),
                widget.TextBox(text='',
                               mouse_callbacks = {'Button1':sound}),
                widget.PulseVolume(),
                widget.CPU(mouse_callbacks = {'Button1':htop}),
                widget.Memory(format='MEM{MemUsed: .0f}{mm}', mouse_callbacks = {'Button1':htop}),
                widget.Clock(format=' %Y-%m-%d %a', mouse_callbacks={'Button1':calendar}),
                widget.Clock(format='  %I:%M %p', mouse_callbacks={'Button1':timer}),
                widget.OpenWeather(cityid=3333147,
                                   metric=False,
                                   format=' {main_temp}°{units_temperature}',
                                   mouse_callbacks = {'Button1':weather}),
                widget.Systray(),
                widget.CurrentLayoutIcon(scale=.75),
                widget.TextBox(mouse_callbacks = {'Button1':powermenu},
                               text='',),
            ],
            20, background ='#282828'
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating( border_focus=ColorE,
                                   border_normal=ColorA,
    float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='ssh-askpass'),
    Match(title='branchdialog'),
    Match(title='pinentry'),
    Match(title='Volume Control'),
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
    Match(wm_class='toolbar'),
    Match(wm_class='gcolor3'),
    Match(wm_class='qalculate-gtk'),
    Match(wm_class='qt5ct'),])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wmname = "LG3D"
