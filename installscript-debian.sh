#!/bin/bash

#Variables
qtilevenv="$HOME/.local/src/qtile_venv"
pywalvenv="$HOME/.local/src/pywal_venv"
adblockvenv="$HOME/.local/src/adblock_venv"
dmenu="https://github.com/DioptricDesign/dmenu.git"
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
rofidir="$HOME/.config/rofi"
spacemacs="https://github.com/syl20bnr/spacemacs"
clipmenu="https://github.com/cdown/clipmenu.git"
clipnotify="https://github.com/cdown/clipnotify.git"
xsession="https://raw.githubusercontent.com/qtile/qtile/master/resources/qtile.desktop"
xdir="/usr/share/xsessions"
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
echo Updating and Upgrading
sudo apt update &&
sudo apt upgrade &&

#Install Dependencies
echo Installing Dependencies
sudo apt install git cargo python3 python3-venv python3-v-sim python-dbus-dev python3-cairo python3-psutil policykit-1-gnome fonts-noto zenity libpangocairo-1.0-0 libnotify-bin libxinerama-dev libxft-dev khal xsel lxappearance qt5ct breeze breeze-gtk-theme fonts-jetbrains-mono xterm htop xserver-xorg lm-sensors pavucontrol playerctl feh rofi rxvt-unicode imagemagick i3lock scrot dunst wget redshift fonts-font-awesome xautolock python3-pip build-essential vdirsyncer 

#Install qtile
echo Installing qtile
python3 -m venv $qtilevenv
mkdir ~/.local/bin/
git clone https://github.com/qtile/qtile.git $qtilevenv/qtile
$qtilevenv/bin/pip install $qtilevenv/qtile/.
$qtilevenv/bin/pip install psutil
ln -sf $qtilevenv/bin/qtile ~/.local/bin/

#Install Pywal
echo installing Pywal
python3 -m venv $pywalvenv
git clone https://github.com/dylanaraps/pywal $pywalvenv/pywal
$pywalvenv/bin/pip install --use-pep517 $pywalvenv/pywal
ln -sf $pywalvenv/bin/wal ~/.local/bin/

#Install Extra Software
echo Installing desktop software
sudo apt install qutebrowser liferea cmus emacs gpodder thunderbird vlc pcmanfm hexchat keepassxc 


echo -n "Do you want to install graphic design software (y/N)?"
read answer
if test "$answer" != "Y" -a "$answer" != "y";
then
    echo Skipping graphics software...
else
    sudo apt install inkscape gimp scribus krita blender gcolor3
fi
:
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
    sudo apt install godot blender krita
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
    sudo dpkg --add-architecture i386
    sudo apt install dosbox lutris steam-installer mangohud discord
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
wget "$xsession" -P "$qtchdl"

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
echo Adjusting Qutebrowser
sed -i "s/placeholder/${USER}/" "$qutedir/config.py"

#Wall
echo Running walp
walp

#End Of Script
echo Install complete.
