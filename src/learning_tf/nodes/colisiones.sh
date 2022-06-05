#!/bin/bash
# Este es nuestro primer progrma
rostopic echo rosout_agg | grep msg > colisiones.txt
sleep 30
wc -l colisiones.txt
exit
