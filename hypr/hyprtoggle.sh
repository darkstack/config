#!/usr/bin/env sh
case $4 in 
    int)
        NRV=2
        ;;
    float)
        NRV=3
        ;;
    str)
        NRV=4
        ;;
    *)
        NRV=2
esac
VALUE=$(hyprctl getoption $1 | awk -v nrv=$NRV 'NR==nrv {print $2}' | sed "s/\"//g")

if [ "$VALUE" == $2 ]; then
    hyprctl keyword $1 $3
else
    hyprctl keyword $1 $2
fi
# update waybar
pkill -RTMIN+9 waybar
