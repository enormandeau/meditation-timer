###ABOUT THIS PROGRAM

Meditation timer is a simple program to assist in the practice of mindfullness
that works under Linux. It provides a meditation timer that plays three chimes
at the start of the meditation session and one at the end. The user can define
both the duration of the session as well as of the duration of theset up period.

###DEPENDENCIES

Meditation timer requires the mplayer program and currently (v0.3.0) works only
under Linux (tested) and possibly MacOSX (not tested). It is planned to make it
work under Windows in the next version (v0.4.0).

###INSTALLING

Meditation-timer is written to work under Linux. When Windows support will be
added, the only option will be to run it without installation, the first option
listed in the next option. In linux, you have two options in order to use
Meditation-timer:

####1) No installation. Simply put the program directory anywhere on your
system. When you want to lauch the program, open a terminal and move into the
directory (using 'cd'). Make sure the file 'meditation_timer.py' executable. In
the console, type:

```bash
 chmod +x meditation_timer.py
```

Launch the program:

```bash
./meditation_timer.py
```

####2) Installing meditation-timer is made via the 'install.sh' script.This will
install the Python program file ('meditation_timer.py') in the '/usr/local/bin'
directory and the 'data' folder in '/usr/share/meditation-timer/' directory. In
order to install the program, you will need to have admnistrative rights on your
computer. To proceed with the installation, first make the installation script
and program file executable if it is not already:

```bash
chmod +x install.sh meditation_timer.py
```

Then launch the installation script with 'sudo' to gain administrative rights:

```bash
sudo ./install.sh
```

The program is now installed.


###USING THE PROGRAM

- Launch the program without options for quick help and information about
  available options, a terminal and lauch the following command:

```bash
meditation_timer.py
```

(Note: add './' before the command if the program was not installed)

- Launch the following command for the full help:

```bash
meditation_timer.py -h
```

- Both the period and set up delay are in minutes and also optional. The default
  meditation period is 30 minutes and the default set up delay is 1.3 minutes,
  or 78 seconds.
  

###CONTACTING THE AUTHOR

You can send comments to the author at:

eric [dot] normandeau [dot] qc at gmail [dot] com

