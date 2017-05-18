#!/bin/bash

cd /home/odraudek99/aire/

NOW=$(date +"%d-%m-%Y %H:%M")


echo "|"$NOW >> README.md
#printf "\n" >> README.md
#echo  $NOW >> README.md

python2.7 bot_aire_img.py

#git add *
#comment = New changes NOW
echo  'inicia commit'
git commit -m 'update images' .
#git commit -m 'update images' calidad.png README.md mapa.png hora1.png
#git commit -m 'New changes' README.md
git push origin master

pgrep phantomjs | xargs kill

