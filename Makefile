nothing:
	
install:
	mkdir /usr/share/meditation-timer 2> /dev/null
	chmod +x meditation_timer.py
	cp meditation_timer.py /usr/local/bin
	cp -r data /usr/share/meditation-timer
	####################################
	# meditation_timer.py is installed #
	####################################

uninstall:
	rm -rf /usr/share/meditation-timer 2> /dev/null
	rm -f /usr/local/bin/meditation_timer.py 2> /dev/null
	############################################
	# meditation_timer.py has been uninstalled #
	############################################
