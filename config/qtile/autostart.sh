#!/usr/bin/bash

setxkbmap us -variant colemak
nitrogen --restore

lxsession &
xfce4-power-manager &
picom &
