###ABOUT THIS PROGRAM

Meditation timer is a simple program to assist in the practice of mindfullness
that works under Linux. It provides a meditation timer that plays three chimes
at the start of the meditation session and one at the end. The user can define
both the duration of the session as well as of the duration of theset up period.


###DEPENDENCIES

Meditation timer requires the 'pygame' Python module to play the chime sound.
You should install 'pygame' before attemptint to install Meditation-timer. In
Debian, Ubuntu or Linux Mint, type:

```bash
sudo apt-get install python-pygame
```

###INSTALLING

Meditation-timer is written to work under Linux. You have two options in order
to use Meditation-timer:

####1) No installation. Simply put the program directory anywhere on your
system. When you want to lauch the program, open a terminal and move into the
directory (using 'cd'). Make sure the file 'meditation_timer.py' executable. In
the console, type:

```bash
 chmod +x meditation_timer.py
```

Launch the program:

```bash
./meditation_timer [period] [delay] 
```

####2) Installing meditation-timer is made via the 'install.sh' script. This will
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

- For a meditation period of 20 minutes, preceded by one minute to set up, open
  a terminal and lauch the following command:

```bash
meditation 20 1
```

(Note: add './' before the command if the program was not installed)

- Both the period and set up delay are in minutes and also optional. The default
  meditation period is 30 minutes and the default set up delay is 1.3 minutes,
  or 78 seconds.
  

###CONTACTING THE AUTHOR

You can send comments to the author at:

eric dot normandeau dot qc at gmail dot com

