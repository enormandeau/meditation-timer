###ABOUT THIS PROGRAM

Meditation timer (v0.3.2) is a simple program to assist in the practice of
mindfulness that works under Linux. It provides a meditation timer that plays
chimes at the start and the end of the meditation session.

###FEATURES

 - Set preparation and meditation periods duration
 - Choose the number of bells before and after the meditation period
 - Add optional bells at intervals during meditation 

###DEPENDENCIES

Meditation timer requires the mplayer program and currently works only under
Linux (tested on Ubuntu 12.04+) and possibly MacOSX (not tested).

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
./meditation_timer.py -h
```

####2) Installing meditation-timer via the 'install.sh' script
This will install the Python program file ('meditation_timer.py') in the
'/usr/local/bin' directory and the data in '/usr/share/meditation-timer/'. In
order to install the program, you will need to have admnistrative rights on the
computer you are using. To proceed with the installation, launch the
installation script (use 'sudo' to gain administrative rights):

```bash
sudo make install
```

The program is now installed. If there is a previous installation of meditation_timer on your computer, run the following command to remove it before doing the install:

```bash
sudo make uninstall
```


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

