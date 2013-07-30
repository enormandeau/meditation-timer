#!/bin/bash
mkdir /usr/share/meditation_timer 2> /dev/null
chmod +x meditation_timer.py
cp meditation_timer.py /usr/local/bin
cp -r data /usr/share/meditation_timer
echo meditation_timer.py is installed
