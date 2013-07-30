###ABOUT THIS PROGRAM

Meditation timer (v0.3.1) is a simple program to assist in the practice of
mindfulness that works under Linux. It provides a meditation timer that plays
chimes at the start and the end of the meditation session. The user can define
the duration of the session, the duration of the set up period, the number of
bells to be heard at the start and end of the meditation and if there should be
periodic bells during the meditation.

###FEATURES

 - Set preparation and meditation periods duration
 - Choose how many bells you want before and after meditating
 - Decide if you want bells, and how many, at intervals during meditation 

###DEPENDENCIES

Meditation timer requires the mplayer program and currently works only under
Linux (tested) and possibly MacOSX (not tested).

###INSTALLING

In Linux, you have two options in order to use Meditation-timer:

####1) No installation

Simply put the program directory anywhere on your system. When you want to
launch the program, open a terminal and move into the directory (using 'cd').
Make sure the file 'meditation_timer.py' executable. In the console, type:

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
order to install the program, you will need to have admnistrative rights on the
computer you are using. To proceed with the installation, first make the
installation script and program file executable if ther are not already:

```bash
chmod +x install.sh meditation_timer.py
```

Then launch the installation script (use 'sudo' to gain administrative rights):

```bash
sudo ./install.sh
```

The program is now installed.


###USING THE PROGRAM

- Launch the program with the -h option information about available options.
  Open a terminal and lauch the following command:

```bash
meditation_timer.py -h
```

(Note: add './' before the command if the program was not installed)


###CONTACTING THE AUTHOR

You can send comments to the author at:

eric [dot] normandeau [dot] qc at gmail [dot] com

