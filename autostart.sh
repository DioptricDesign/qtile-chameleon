#!/usr/bin/bash
exec /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
xautolock -time 5 -locker "lock" &
clipmenud &
emacs --daemon &
redshift-gtk &
nm-applet &
urxvtd -q -f -o &
walp & 
