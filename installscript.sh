#!/bin/bash
echo qtile-chameleon install script
echo Backup your old configurations to avoid data loss.
read -p "Press Enter to continue"

#Variables
qtile_chameleon="https://github.com/DioptricDesign/qtile-chameleon.git"
qtiledir="$HOME/.config/qtile"
scripts="https://github.com/DioptricDesign/scripts.git"
scriptsdir="$HOME/.local/share/scripts"
qtchdl="$HOME/qtilechameleon/"
bindir="/usr/local/bin/"
bgdir="$HOME/.local/share/backgrounds/"
startdir="$HOME/.local/share/start-page/"
startp="https://github.com/DioptricDesign/min-startpage.git"

#Make Directories
echo Making Directories
mkdir "$qtchdl"
mkdir "$scriptsdir"
mkdir "$qtiledir"
mkdir "$bgdir"
mkdir "$startdir"

#Clone Repos
echo Cloning Git Repos...
git clone "$qtile_chameleon" "$qtchdl/qtile-chameleon"
git clone "$scripts" "$qtchdl/scripts"
git clone "$startp" "$startdir"

#Make Binaries executable
echo Making Binaries Executable
chmod +x "/home/user/qtilechameleon/scripts/bin/"*

#Copy Files
echo Copying Files...
cp -r "$HOME/qtilechameleon/qtile-chameleon/"* "$qtiledir"
cp "$HOME/qtilechameleon/scripts/"*.sh "$scriptsdir"
sudo cp "$HOME/qtilechameleon/scripts/bin/"* "$bindir"

#Cleanup
echo Cleaning up...
rm -rf "$qtchdl"
echo Install complete.

#Enumerate Wallpaper
echo Enumerating Background Files
ls "$bgdir" | wc -l
echo Make sure you have at least one image file in ~/.local/share/backgrounds/
echo If anything seems broken make sure you have the required program.
echo To use the startpage change your browsers homepage to ~/.local/share/start-page/min.html
echo Adjust the path in min.css to direct to your users color.css
