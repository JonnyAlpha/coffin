# COFFIN
COFFIN (**C**omputerised **On** **l**ine **F**act **F**inding **I**nvestigation **N**ode) started out as a robot designed for a school project to imitate 
a planetary rover for a space exploration based computing topic.
This is a Raspberry Pi based robot that is operated from a web based control panel.
Web control is facilitated using WEBIOPI: http://webiopi.trouch.com/
The robot uses two files coffin.py and coffin.html.
The python script recieves commands from the web page using webiopi and sends them to a Sabertooth motor driver board using plain text serial sent over USB.
The html file is a web page which includes a control panel to operate the robot. Webiopi is used to send commands from the web page to the python script. 
A webcam connected to the robot uses mjpg-streamer to stream video to the web page to provide the user with a display from the robot. 
To start the program you need to run the coffin.py, then in a web browser navigate to your IP address followed by :8000/coffin.html
