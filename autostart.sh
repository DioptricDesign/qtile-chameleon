#!/usr/bin/bash
exec /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
xautolock -time 5 -locker "lock" &
clipmenud &
redshift-gtk &
nm-applet &
mpd &
urxvtd -q -f -o &
walp & 
