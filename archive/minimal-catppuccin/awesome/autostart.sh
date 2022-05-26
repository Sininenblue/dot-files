#!/bin/sh

run() {
  if ! pgrep -f "$1" ;
  then
    "$@"&
  fi
}

run lxsession
run xfce4-power-manager
run picom
run nitrogen --restore
run setxkbmap us -variant colemak
run xinput set-prop "SynPS/2 Synaptics TouchPad" "libinput Tapping Enabled" 1
