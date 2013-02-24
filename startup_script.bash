#!/bin/bash
cd /home/pi/25c-to-continue/
sudo python LED_flash_5.py &
cd /home/pi/25c-to-continue/monsters_and_mushrooms-master/
sudo python game.py &
