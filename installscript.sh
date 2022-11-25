#!/bin/bash

#Variables
dmenu="https://github.com/DioptricDesign/dmenu.git"
dddir="$HOME/Documents/DesignDocuments/"
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

#Warning
echo                     qtile-chameleon install script
echo Backup your old configurations to avoid data loss.
echo New Software will be installed. Software configurations will be modified.
echo Please be sure you understand what this script does before you run it.
echo -n "Do you want to proceed (y/N)?"

read answer
if test "$answer" != "Y" -a "$answer" != "y";
then exit 0;
fi

#Check user
if [ "$(id -u)" = 0 ]; then
    echo "Do not run as root."
    exit 1
fi

#Update
echo Updating
sudo apt update && 
sudo apt upgrade

#Install Dependencies
echo Installing Dependencies
sudo apt install git policykit-1-gnome fonts-noto-core zenity libpangocairo-1.0-0 libnotify-bin libxinerama-dev libxft-dev khal xsel lxappearance qt5ct breeze breeze-gtk-theme breeze-cursor-theme fonts-jetbrains-mono xterm htop xserver-xorg lm-sensors pavucontrol playerctl feh rofi rxvt-unicode imagemagick i3lock scrot dunst wget redshift-gtk fonts-font-awesome libxfixes-dev xautolock python3-pip build-essential xorg-dev checkinstall vdirsyncer
sudo pip3 install cffi
sudo pip3 install xcffib
sudo pip3 install cairocffi
sudo pip3 install psutil
sudo pip3 install qtile
sudo pip3 install pywal

#Install Extra Software

echo Installing desktop software
sudo apt install qutebrowser akregator cmus emacs gpodder thunderbird vlc pcmanfm hexchat keepassxc
pip3 install adblock

echo -n "Do you want to install graphic design software (y/N)?"
read answer
if test "$answer" != "Y" -a "$answer" != "y";
then
    echo Skipping graphics software...
else
    sudo apt install inkscape gimp scribus krita blender gcolor3
fi

echo -n "Do you want to install desktop publishing software (y/N)?"
read answer
if test "$answer" != "Y" -a "$answer" != "y";
then
    echo Skipping desktop publishing software...
else
    sudo apt install zathura scribus calibre
fi

echo -n "Do you want to install photography software (y/N)?"
read answer
if test "$answer" != "Y" -a "$answer" != "y";
then
    echo Skipping photograpy software...
else
    sudo apt install darktable shotwell
fi

echo -n "Do you want to install video editing software (y/N)?"
read answer
if test "$answer" != "Y" -a "$answer" != "y";
then
    echo Skipping video editing software...
else
    sudo apt install kdenlive
fi

echo -n "Do you want to install audio editing software (y/N)?"
read answer
if test "$answer" != "Y" -a "$answer" != "y";
then
    echo Skipping audio editing software...
else
    sudo apt install ardour lmms audacity
fi

echo -n "Do you want to install game design software (y/N)?"
read answer
if test "$answer" != "Y" -a "$answer" != "y";
then
    echo Skipping game design software...
else
    sudo apt install godot3 blender krita
fi

echo -n "Do you want to install Open Broadcaster Software (y/N)?"
read answer
if test "$answer" != "Y" -a "$answer" != "y";
then
    echo Skipping Open Broadcaster Software...
else
    sudo apt install obs-studio
fi

echo -n "Do you want to install gaming software (Nonfree Software!) (y/N)?"
read answer
if test "$answer" != "Y" -a "$answer" != "y";
then
    echo Skipping gaming software...
else
    sudo apt install dosbox lutris steam mangohud discord
fi

echo -n "Do you want to configure khal calendar now? (y/N)?"
read answer
if test "$answer" != "Y" -a "$answer" != "y";
then
    echo Skipping khal configuration...
else
    khal configure
fi

#Make Directories
echo Making Directories
mkdir "$dddir"
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
git clone "$dmenu" "$qtchdl/dmenu"
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

#Build Dmenu
echo Building dmenu
cd "$qtchdl"/dmenu
sudo make
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
cp "$qtchdl"/dots/config.rasi "$rofidir"
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

#End Of Script
echo Install complete.
