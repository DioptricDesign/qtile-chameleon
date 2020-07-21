#!/usr/bin/bash
export DISPLAY=:0
exec /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
xautolock -time 5 -locker "i3lock -c 000000" &
clipmenud &
redshift-gtk &
pamac-tray &
walp &
qtile-cmd -o cmd -f restart 
