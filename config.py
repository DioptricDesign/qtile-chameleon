#  ___  _   _ _                  A Qtile Config With Pywal
# / _ \| |_(_) | ___  Requires:  playerctl dunst scrot clipmenu xautolock 
#| | | | __| | |/ x \ pywal rofi dmenu lm-sensors urxvt firefox
#| | | | |_| | |  __/ i3lock htop notify-send khal pavucontol feh psutil
# \__\_\\__|_|_|\___| Backgrounds should go in ~/.local/share/backgrounds
# A Link to the acompanying scripts and start page is in the readme.
from typing import List
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, ScratchPad, DropDown
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
    #Navigation
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    #Movement
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod], "Return", lazy.layout.toggle_split()),
    #Size
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key(["mod1"], "n", lazy.layout.normalize()),
    #Layout
    Key([mod], "Right", lazy.next_layout()),
    Key([mod], "Left", lazy.prev_layout()),
    #Windows
    Key([], "F11", lazy.window.toggle_fullscreen()),
    Key([], "F10", lazy.window.toggle_floating()),
    Key(["mod1"], "x", lazy.spawn("xkill")),
    Key([mod], "x", lazy.window.kill()),
    #Qtile
    Key([mod], "grave",lazy.group["scratchpad"].dropdown_toggle("term")),
    KeyChord([mod], "q",[
        Key([], "b", lazy.spawn("bartoggle")),
        Key([], "w", lazy.spawn("walp")),
        Key([], "c", lazy.spawn("clipmenu")),
        Key([], "Delete", lazy.spawn("clipdel -d \".*\" ")),
        Key([], "r", lazy.restart()),
        Key([], "q", lazy.shutdown()),]),
    #Audio and Media
    Key([mod], 'minus', lazy.spawn('amixer -q sset Master 3%-')),
    Key([mod], 'equal', lazy.spawn('amixer -q sset Master 3%+')),
    Key([mod], '0', lazy.spawn("amixer -q sset Master toggle")),
    Key([mod], 'comma', lazy.spawn("playerctl previous")),
    Key([mod], 'period', lazy.spawn("playerctl next")),
    Key([mod], 'slash', lazy.spawn("playerctl play-pause")),
    #Applications
    Key(["mod1", "control"], "Delete", lazy.spawn ("urxvtc -e htop")),
    Key([], "Print", lazy.spawn("scrot $HOME/Pictures/scrots/")),
    Key([mod], "w", lazy.spawn("qutebrowser")),
    Key([mod], "e", lazy.spawn("emacsclient -c ")),
    Key([mod], "r", lazy.spawn("akregator")),
    Key([mod], "o", lazy.spawn("pavucontrol")),
    Key([mod], "c", lazy.spawn("qalculate-gtk")),
    Key([mod], "g", lazy.spawn("gpodder")),
    Key([mod], "t", lazy.spawn("urxvtc")),
    Key([mod], "m", lazy.spawn("thunderbird")),
    Key([mod], "v", lazy.spawn("vlc")),
    Key([mod], "f", lazy.spawn("pcmanfm")),
    KeyChord([mod], "a", [
        Key([], "d", lazy.spawn("discord")),
        Key([], "w", lazy.spawn("firefox")),
        Key([], "c", lazy.spawn("gcolor3")),
        Key([], "t", lazy.spawn("xterm")),
        Key([], "p", lazy.spawn("keepassxc"))]),
    #Launcher
    Key([mod], "d", lazy.spawn("dmen")),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window -show-icons")),
    Key([mod], "s", lazy.spawn("dmsearch")),
    #Scripts
    Key(["mod1", "control"], "o", lazy.spawn ("outputmenu")),
    Key(["mod1", "control"], "c", lazy.spawn ("comptonmenu")),
    Key(["mod1", "control"], "p", lazy.spawn ("powermenu")),
    Key(["mod1", "control"], "l", lazy.spawn ("xautolockmenu")),
    Key(["mod1", "control"], "s", lazy.spawn("sensornote")),
    Key(["mod1", "control"], "g", lazy.spawn ("gamesmenu")),
    KeyChord([mod], "space", [
        Key([], "h", lazy.spawn ("hotkey")),
        Key([], "s", lazy.spawn ("scrotmenu")),
        Key([], "l", lazy.spawn ("libmenu")),
        Key([], "c", lazy.spawn ("calendarmenu")),
        Key([], "m", lazy.spawn ("chatmenu")),
        Key([], "t", lazy.spawn ("timermenu")),
        Key([], "g", lazy.spawn ("graphicsmenu"))])
]

#Workspace Groups
group_names = [("I", {}),
               ("II", {}),
               ("III", {}),
               ("IV", {}),
               ("V", {}),]
groups = [Group(name, **kwargs) for name, kwargs in group_names]
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group
groups = [ScratchPad("scratchpad",[
          DropDown("term", "urxvt", opacity=0.95)]),
          Group("I", layout='monadtall', matches=[Match(wm_class=["qutebrowser",
                                                                  "Thunderbird",
                                                                  "akregator",])]),
          Group("II", layout='monadtall', matches=[Match(wm_class=["vlc",
                                                                   "gpodder"])]),
          Group("III", layout='bsp', matches=[Match(wm_class=["Steam",
                                                             "Lutris",
                                                             "RetroArch",
                                                              "dosbox"])]),
          Group("IV", layout='max', matches=[Match(wm_class=["VirtualBox Machine",
                                                             "virt-manager",
                                                             "VirtualBox Manager",
                                                             "VirtualBoxVM"])]),
          Group("V", layout='max', matches=[Match(wm_class=["gimp",
                                                            "Inkscape",
                                                            "krita",
                                                            "darktable",
                                                            "shotwell",
                                                            "scribus",
                                                            "Blender"])]),]

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
    font='Noto Sans',
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
             widget.Spacer(length = bar.STRETCH),
             widget.Clock(format='%a %b %d',
                          font='Noto Sans Bold',
                          padding=0,
                          mouse_callbacks={'Button1':calendar}),
             widget.Clock(format='%I:%M %p',
                          font='Noto Sans Bold',
                          mouse_callbacks={'Button1':timer}),
             widget.Spacer(length = bar.STRETCH),
             widget.KhalCalendar(foreground="#282828",
                                 remindertime=1440,
                                 reminder_color=ColorG,
                                 mouse_callbacks={'Button1':calendar}),
             widget.OpenWeather(cityid=3333147,
                               metric=False,
                               format=' {main_temp}°{units_temperature}',
                               mouse_callbacks = {'Button1':weather}),
             widget.TextBox(text='',
                            mouse_callbacks = {'Button1':sound}),
             widget.PulseVolume(),
             widget.TextBox(mouse_callbacks = {'Button1':powermenu},
                            text='',),
             widget.Spacer(length=5)
           ],
            22,
            background ='#282828',
        ),
        bottom=bar.Bar(
        [
            widget.CurrentLayoutIcon(scale=.75),
            widget.WindowName(font='Noto Sans Bold'),
            widget.Cmus(play_color=ColorG,
                        noplay_color=ColorB),
            widget.TextBox(text='', mouse_callbacks = {'Button1':htop}),
            widget.CPU(mouse_callbacks = {'Button1':htop}),
            widget.Memory(format='MEM{MemUsed: .0f}{mm}',
                          mouse_callbacks = {'Button1':htop}),
            widget.Systray(),
        ],
            22,
            background='#282828',
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
    Match(title='khal'),
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
