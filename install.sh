#!/bin/bash
mkdir /usr/share/meditation-timer
chmod +x meditation_timer.py
cp meditation_timer.py /usr/local/bin
cp -r data /usr/share/meditation-timer
echo Installation completed
