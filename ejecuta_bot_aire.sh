#!/bin/bash

cd /home/odraudek99/aire/aire

NOW=$(date +"%d-%m-%Y %H:%M")


echo "\n"$NOW >> README.md
#printf "\n" >> README.md
#echo  $NOW >> README.md

python2.7 bot_aire_img.py

#git add *
git commit -m 'New changes' calidad.png README.md mapa.png
#git commit -m 'New changes' README.md
git push

