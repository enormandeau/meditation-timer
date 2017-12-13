#!/usr/bin/env python3
"""
Meditation timer
A tool to assist in the practice of mindfulness

use the -h option for full help and options
(eg: meditation_timer.py -h)

    Buddha sits, clouds pass
    unending meditation
    expression of bliss
"""
__VERSION__ = "0.4.0"

# Importing modules
from os.path import join, dirname
from time import time, sleep
import subprocess
import argparse
import pygame
import sys
import os

# Defining global variables
if dirname(__file__) == "/usr/local/bin":
    DATA_PATH = "/usr/share/meditation-timer/data"
else:
    DATA_PATH = dirname(os.path.realpath(__file__)) + "/data"

# Defining functions
def wait(duration=0, debug_time=False):
    """Wait a certain number of seconds
    """
    t0 = time()
    if duration <= 0:
        duration = 0

    time_end = time() + float(duration)
    time_diff = time_end - time()

    while time_diff > 0:
        sleep(0.05)
        time_diff = time_end - time()

    if debug_time:
        delta = time() - t0
        print(" Waited: " + pretty_time(delta))

def play_chime():
    """Play a chime once
    """
    pygame.mixer.init(frequency=44100)
    pygame.mixer.music.load(DATA_PATH + "/bowl-short.ogg")
    pygame.mixer.music.set_volume(args.volume)
    pygame.mixer.music.play()
    pygame.time.wait(8450)
    pygame.mixer.quit()

def play_chimes(n=1, debug_time=False):
    """Play a chime n times
    """
    for i in range(n):
        t0 = time()
        play_chime()
        if debug_time:
            delta = time() - t0
            print("  Chime " + str(i + 1) + ": " + pretty_time(delta))

def pretty_time(t):
    """Format time in minutes and seconds

    Format example: '2 min 23.9 sec'
    """
    tmin = int(t) / 60
    tsec = int(t - tmin * 60)
    trest = int((t - tmin * 60 - tsec) * 100)
    return "{} min {}.{} sec".format(tmin, tsec, trest)

def print_file(ascii_file, debug_time=False):
    """Print the content of a text file, for example ascii art
    """
    if not debug_time:
        ascii_data = open(ascii_file)
        print("\n" * 69)
        for line in ascii_data:
            print(line.rstrip())
        print("")

def meditation_timer():
    """Meditation timer
    """
    t0 = time()
    bell_duration = 8.45 # seconds

    # Preparation
    if not args.no_print:
        print_file(join(DATA_PATH, "buddha0.txt"), args.debug_time)

    wait(3, args.debug_time)

    if not args.no_print:
        print_file(join(DATA_PATH, "buddha1.txt"), args.debug_time)

    wait(args.delay, args.debug_time)

    if not args.no_print:
        print_file(join(DATA_PATH, "buddha2.txt"), args.debug_time)

    if args.quiet:
        wait(bell_duration, args.debug_time)

    else:
        play_chimes(args.start_bells, args.debug_time)

    if args.debug_time:
        delta = time() - t0
        print("--Preparation: " + pretty_time(delta))

    # Meditation
    if not args.no_print:
        print_file(join(DATA_PATH, "buddha.txt"), args.debug_time)

    t1 = time()

    if args.interval:
        num_intervals = int(args.period / args.interval_time)
        remainder = args.period - num_intervals * args.interval_time

        for i in range(num_intervals):
            wait(args.interval_time * 60 - bell_duration * args.interval_bells, args.debug_time)

            if args.quiet:
                wait(bell_duration, args.debug_time)

            else:
                play_chimes(args.interval_bells, args.debug_time)

        wait(remainder - bell_duration, args.debug_time)
        meditation_time = time() - t1

        if args.quiet:
            wait(bell_duration, args.debug_time)

        else:
            play_chimes(args.end_bells, args.debug_time)

    else:
        wait(args.period * 60 - bell_duration, args.debug_time)
        meditation_time = time() - t1

        if args.quiet:
            wait(bell_duration, args.debug_time)

        else:
            play_chimes(args.end_bells, args.debug_time)

    # End of meditation
    if not args.no_print:
        print_file(join(DATA_PATH, "buddha3.txt"), args.debug_time)

    tf = time()
    program_time = time() - t0

    if args.debug_time:
        print("--Meditation:" + pretty_time(meditation_time))
        print("--Program:" + pretty_time(program_time))

# Main loop
if __name__ == "__main__":
    # Option parser
    parser = argparse.ArgumentParser(description=
            """Meditation timer. Sound a bell after an initial delay and 
at the end of the meditation period""")
    parser.add_argument('-p', '--period', type=float, nargs='?', default=30,
        help= 'meditation period in minutes, default is 30')
    parser.add_argument('-d', '--delay',  type=int, nargs='?', default=30,
        help='initial delay in seconds, default is 30')
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
    parser.add_argument('-V', '--version', action="store_true",
        help='show version number and quit')
    parser.add_argument('-v', '--volume', type=float, default=0.3,
        help='chime sound volume, from 0 to 1, default is 0.3')
    parser.add_argument('-q', '--quiet', action="store_true",
        help='run program without sound')
    parser.add_argument('-n', '--no-print', action="store_true",
        help='run program without printing the ascii art')
    parser.add_argument('-D', '--debug-time', action="store_true",
        help='print program and meditation time')
    args = parser.parse_args()

    # Insure that option values OK
    assert args.period > 0, \
            "Meditation period (-p) must be positive"
    assert args.delay >= 0, \
            "Meditation delay (-d) must be zero or positive"
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
        print(__VERSION__)
        sys.exit(0)

    # Launch meditation period
    meditation_timer()
