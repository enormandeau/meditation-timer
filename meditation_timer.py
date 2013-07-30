#!/usr/bin/env python

# Metitation timer
# Version 0.3
# 2013-07-17

# Statue sits, quiet
# unending meditation
# expression of bliss

"""
Metitation timer
A tool to assist in the practice of mindfullness

The meditation period duration and the initial delay, in minutes, are optional.
If ommited, they default to a meditation period of 30 minutes and a preparation
delay of 1.3 minutes, or 78 seconds.

"""

LICENCE = """
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Importing modules
from os.path import join, dirname
from time import time, sleep
import subprocess
import argparse
import sys
import os

# Defining global variables
if dirname(__file__) == "/usr/local/bin":
    DATA_PATH = "/usr/share/meditation_timer/data"
elif dirname(__file__) == ".":
    DATA_PATH = "./data"
else:
    print "Cannot launch Meditation-timer."
    print "Read the installation procedure in the README file."

# Defining functions
def wait(duration):
    """Wait a certain number of minutes
    """
    time_end = time() + float(duration) * 60
    time_diff = time_end - time()
    while time_diff > 0:
        sleep(1)
        time_diff = time_end - time()

def _play_chime():
    """Play a sound file once
    """
    subprocess.call(["mplayer data/bowl-short.ogg -really-quiet 2> /dev/null"], shell=True)

def print_text_file(ascii_file):
    """Print the content of a text file, for example ascii art
    """
    ascii_data = open(ascii_file)
    print "\n" * 69
    for line in ascii_data:
        print line,
    print

def timer(period, delay, start_bells, end_bells):
    """Meditation timer. Sound a bell after an initial delay and at the end of
the meditation period, both given in minutes
    """
    print_text_file(join(DATA_PATH, "buddha0.txt"))
    wait(3./60)
    print_text_file(join(DATA_PATH, "buddha1.txt"))
    wait(delay)
    print_text_file(join(DATA_PATH, "buddha2.txt"))
    for i in range(start_bells):
        _play_chime()
    print_text_file(join(DATA_PATH, "buddha.txt"))
    # TODO implement optional interval bells during meditation
    wait(period)
    for i in range(end_bells):
        _play_chime()
    print_text_file(join(DATA_PATH, "buddha3.txt"))

def main():
    parser = argparse.ArgumentParser(description=
            """Meditation timer. Sound a bell after an initial delay and 
at the end of the meditation period""")
    parser.add_argument('-p', '--period', type=float, nargs='?', default=30,
            help= 'meditation period in minutes, default is 30')
    parser.add_argument('-d', '--delay',  type=float, nargs='?', default=1.3,
            help='initial delay in minutes, default is 1.3')
    parser.add_argument('-s', '--start-bells', type=int, default=3,
            help='number of times bell chimes at meditation start, default is 3')
    parser.add_argument('-e', '--end-bells', type=int, default=1,
            help='number of times bell chimes at meditation end, default is 1')
    parser.add_argument('-i', '--interval', type=float, default=None,
            help='interval in minutes at which to play bells during the meditation')
    parser.add_argument('-I', '--interval-bells', type=int, default=1,
            help='number of bells to play at intervals, default is 1')

    args = parser.parse_args()
    timer(args.period, args.delay, args.start_bells, args.end_bells)

if __name__ == "__main__":
    main()

