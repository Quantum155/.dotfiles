#!/usr/bin/env bash
 
DIR="~/.config/polybar"
 
# Terminate already running bar instances
killall -q polybar
# polybar-msg cmd quit
 
# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done
 
# Launch the bar
echo "---" | tee -a /tmp/polybar.log
polybar main -r -c "$DIR"/config.ini 2>&1 | tee -a /tmp/polybar.log & disown
