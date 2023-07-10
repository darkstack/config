#!/bin/env sh 

#print get running SINK 
RUNNING=$(pactl list sinks short | grep RUNNING | awk '{ print $1}')
SINKS=($(pactl list sinks short | awk '{print $1}'))
MAX_SINK=$(( ${#SINKS[@]} - 1))

for i in "${!SINKS[@]}"; do
   if [[ "${SINKS[$i]}" = "$RUNNING" ]]; then
       next=$((i+1))
       if [ $next -gt $MAX_SINK ]; then 
           next=0
       fi
       echo "Switch to  ${SINKS[$next]}"
       pactl set-default-sink ${SINKS[$next]}
       exit
   fi
done
