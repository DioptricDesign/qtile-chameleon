#!/bin/bash

#Variables
dots="https://github.com/DioptricDesign/dot-files.git"
orgdir="$HOME/.org/"
zatdir="$HOME/.config/zathura/"
qutedir="$HOME/.config/qutebrowser/"
dunstdir="$HOME/.config/dunst/"
qtile_chameleon="https://github.com/DioptricDesign/qtile-chameleon.git"
qtiledir="$HOME/.config/qtile"
scripts="https://github.com/DioptricDesign/scripts.git"
scriptsdir="$HOME/.local/share/scripts"
qtchdl="$HOME/qtilechameleon"
bindir="/usr/local/bin/"
bgdir="$HOME/.local/share/backgrounds/"
startdir="$HOME/.local/share/start-page/"
startp="https://github.com/DioptricDesign/min-startpage.git"
wallpapers="https://github.com/DioptricDesign/Wallpapers.git"
scrotsdir="$HOME/Pictures/scrots/"
xsession="https://raw.githubusercontent.com/qtile/qtile/master/resources/qtile.desktop"
xdir="/usr/share/xsessions"
rofidir="$HOME/.config/rofi"
spacemacs="https://github.com/syl20bnr/spacemacs"
clipmenu="https://github.com/cdown/clipmenu.git"
clipnotify="https://github.com/cdown/clipnotify.git"

echo qtile-chameleon install script
echo Backup your old configurations to avoid data loss. Qtile, Rofi, Dmenu, Emacs, Xdefaults, Zathura, and QuteBrowser will be modified.

#Install Dependencies
echo Installing Dependencies
sudo apt install git policykit-1-gnome libpangocairo-1.0-0 khal xsel lxappearance qt5ct breeze breeze-gtk-theme breeze-cursor-theme fonts-jetbrains-mono xterm vdirsyncer htop xserver-xorg lm-sensors pavucontrol playerctl feh rofi dmenu rxvt-unicode imagemagick i3lock scrot dunst wget redshift-gtk fonts-font-awesome libxfixes-dev xautolock pip 
sudo pip3 install cffi
sudo pip3 install xcffib
sudo pip3 install cairocffi
sudo pip3 install psutil
sudo pip3 install qtile
sudo pip3 install pywal

#Install Extra Software
echo Installing extra software
sudo apt install qutebrowser zathura akregator cmus emacs gcolor3 gpodder thunderbird vlc pcmanfm dosbox calibre inkscape gimp scribus krita darktable hexchat
pip3 install adblock

#Make Directories
echo Making Directories
mkdir "$qtchdl"
mkdir "$orgdir"
mkdir "$zatdir"
mkdir "$qutedir"
mkdir "$scriptsdir"
mkdir "$qtiledir"
mkdir "$bgdir"
mkdir "$startdir"
mkdir "$scrotsdir"
mkdir "$rofidir"
mkdir "$dunstdir"

#Clone Repos
echo Cloning Git Repos...
git clone "$qtile_chameleon" "$qtchdl/qtile-chameleon"
git clone "$dots" "$qtchdl/dots"
git clone "$scripts" "$qtchdl/scripts"
git clone "$wallpapers" "$qtchdl/wallpapers"
git clone "$startp" "$startdir"
git clone "$spacemacs" $HOME/.emacs.d
git clone "$clipmenu" "$qtchdl/clipmenu"
git clone "$clipnotify" "$qtchdl/clipnotify"
wget "$xsession" -P"$qtchdl"

#Make Binaries executable
echo Making Scripts Executable
chmod +x "$qtchdl"/scripts/bin/*
chmod +x "$qtchdl"/scripts/*.sh

#Build Clipmenu
echo Building Clipmenu
cd "$qtchdl"/clipnotify
sudo make install
cd "$qtchdl"/clipmenu
sudo make install
 
#Copy Files
echo Copying Files...
cp -r "$qtchdl"/qtile-chameleon/* "$qtiledir"
cp "$qtchdl"/scripts/*.sh "$scriptsdir"
cp "$qtchdl"/scripts/.Xdefaults "$HOME"
cp "$qtchdl"/wallpapers/*.png "$bgdir"
cp "$qtchdl"/wallpapers/*.jpg "$bgdir"
cp "$qtchdl"/dots/Xdefaults ~/.Xdefaults
cp "$qtchdl"/dots/spacemacs ~/.spacemacs
cp "$qtchdl"/dots/dunstrc "$dunstdir"
cp "$qtchdl"/dots/config.py "$qutedir"
cp "$qtchdl"/dots/zathurarc "$zatdir"
sudo cp "$qtchdl"/scripts/bin/* "$bindir"
sudo cp "$qtchdl"/qtile.desktop "$xdir"

#Cleanup
echo Cleaning up...
rm -rf "$qtchdl"

#Adjust CSS to user
echo Adjusting Style Sheet
sed -i "s/user/${USER}/" "$startdir/min.css"

#Adjusting Qute Browser Config
echo Adjusting Start Page
sed -i "s/user/${USER}/" "$qutedir/config.py"

#Adjust Clipmenu for Rofi
echo changing CM_LAUNCHER to rofi
sudo sed -i s/CM_LAUNCHER=dmenu/CM_LAUNCHER=rofi/ /usr/bin/clipmenu
sudo sed -i "s/-dmenu "$@"/-dmenu -p "Clipboard" "$@"/" /usr/bin/clipmenu

#Wall
echo Running walp
walp

#Rofi theme
echo Linking Rofi Theme
ln  ~/.cache/wal/colors-rofi-dark.rasi ~/.config/rofi/config.rasi

#End Of Script
echo Install complete.
