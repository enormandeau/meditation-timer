#!/usr/bin/env python
"""Meditation timer
A tool to assist in the practice of mindfulness

    Statue sits, quiet
    unending meditation
    expression of bliss
"""
__VERSION__ = "0.3.1"

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
    print "Read the installation procedure in the README.md file."

# Defining functions
def wait(duration):
    """Wait a certain number of minutes
    """
    if duration <= 0:
        duration = 0
    time_end = time() + float(duration) * 60
    time_diff = time_end - time()
    while time_diff > 0:
        sleep(1)
        time_diff = time_end - time()

def play_chime():
    """Play a chime once
    """
    subprocess.call(["mplayer data/bowl-short.ogg -really-quiet 2> /dev/null"],
        shell=True)

def play_chimes(n):
    """Play a chime n times
    """
    for i in xrange(n):
        play_chime()

def print_file(ascii_file):
    """Print the content of a text file, for example ascii art
    """
    ascii_data = open(ascii_file)
    print "\n" * 69
    for line in ascii_data:
        print line.rstrip()
    print

def timer(period, delay, start_bells, end_bells,
        interval, interval_time, interval_bells):
    """Meditation timer. Sound a bell after an initial delay and at the end of
    the meditation period, both given in minutes
    """
    print_file(join(DATA_PATH, "buddha0.txt"))
    wait(5./60) # wait 5 seconds with initial message
    print_file(join(DATA_PATH, "buddha1.txt"))
    wait(delay)
    print_file(join(DATA_PATH, "buddha2.txt"))
    play_chimes(start_bells)
    print_file(join(DATA_PATH, "buddha.txt"))
    if interval:
        num_intervals = int(period / interval_time)
        remainder = period - num_intervals * interval_time
        for i in xrange(num_intervals):
            wait(interval_time - bell_duration)
            play_chimes(interval_bells)
        wait(remainder - bell_duration)
        play_chimes(end_bells)
    else:
        wait(period - bell_duration)
        play_chimes(end_bells)
    print_file(join(DATA_PATH, "buddha3.txt"))

# Main loop
if __name__ == "__main__":
    # Option parser
    parser = argparse.ArgumentParser(description=
            """Meditation timer. Sound a bell after an initial delay and 
at the end of the meditation period""")
    parser.add_argument('-p', '--period', type=float, nargs='?', default=30,
        help= 'meditation period in minutes, default is 30')
    parser.add_argument('-d', '--delay',  type=float, nargs='?', default=1.3,
        help='initial delay in minutes, default is 1.3')
    parser.add_argument('-s', '--start-bells', type=int, default=3,
        help='number of times bell chimes at meditation start, default is 3')
    parser.add_argument('-e', '--end-bells', type=int, default=3,
        help='number of times bell chimes at meditation end, default is 3')
    parser.add_argument('-i', '--interval', action="store_true",
        help='whether bells should be played during the meditation')
    parser.add_argument('-I', '--interval-time', type=float, default=5,
        help='interval in minutes at which to play bells during the meditation')
    parser.add_argument('-b', '--interval-bells', type=int, default=1,
        help='number of bells to play at intervals, default is 1')
    parser.add_argument('-v', '--version', action="store_true",
        help='show version number and quit')
    args = parser.parse_args()

    # Insure that option values OK
    assert args.period > 0, \
            "Meditation period (-p) must be positive"
    assert args.delay > 0, \
            "Meditation delay (-d) must be positive"
    assert args.start_bells >= 0, \
            "Number of start bells (-s) must be null or positive"
    assert args.end_bells >= 0, \
            "Number of end bells (-e) must be null or positive"
    assert args.interval_bells >= 0, \
            "Number of interval bells (-b) must be null or positive"
    assert args.interval_time > 0, \
            "Interval duration (-I) must be positive"

    # Show version or licence
    if args.version:
        print __VERSION__
        sys.exit(0)

    # Launch the program
    timer(args.period,
        args.delay,
        args.start_bells,
        args.end_bells,
        args.interval,
        args.interval_time,
        args.interval_bells)

