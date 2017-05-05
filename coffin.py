#########################################################################################
# This is a programme to add a web based control of a Sabertooth 2 x 32Amp Motor Driver #
# Commands are sent to Raspberry Pi over a web page using webiopi                       #
# and interpretted within this program for transmission to the motor driver             # 
# In the initial setup serial commands are being sent over USB                          #
# If you wish send serial using the GPIO you need to install pigpio and                 #
# start the pigpio daemon by either entering pigpiod at a command prompt                #
# or running it automatically at startup                                                #
# as a CRON job                                                                         #
# Bill Harvey 05/05/17                                                                  #                                                                         
#########################################################################################

#!/usr/bin/python3

# import the neccessary libraries 
import webiopi # Import webiopi - software to communicate with a Rapsberry Pi over a web interface
from webiopi.devices.serial import Serial 
from time import sleep
import os

# configure the serial communications port (you may need to change this based on your port name / number
serial = Serial('ttyACM0', 9600) # this was the baud rate used in my test - poss could be higher

# Uncomment the following two lines if using the Pi GPIO
# import pigpio # pigpio is a custom module for controlling GPIO pins 
# pi = pigpio.pi #declare psuedo for pigpio commands

# define the webio macros which are needed to interpret commands from the web control panel

#@webiopi.macro
def stop():
        #number = 0
        serial.writeString("M1: 0\r\n")
        serial.writeString("M2: 0\r\n")
        print("M1 and M2 off") # print to terminal for debugging
        sleep(1) #not sure if the sleep is required so needs to be tested
        
#@webiopi.macro
def forward():
        number = 1
        serial.writeString("M1: -1023\r\n") # half speed
        serial.writeString("M2: -1023\r\n")
        print("M1 and M2 forward") # print to terminal for debugging
        sleep(1)
        
#@webiopi.macro
def left():
        number = 2
        serial.writeString("M1: -1023\r\n") # motor 1 forward full speed
        serial.writeString("M2: 1023\r\n") # motor 2 reverse full speed
        print("M1 forward and M2 reverse") # print to terminal for debugging
        sleep(1)
        
#@webiopi.macro
def right():
        number = 3
        serial.writeString("M1: 1023\r\n") # motor 1 reverse half speed
        serial.writeString("M2: -1023\r\n") # motor 2 forward half speed
        print("M1 reverse and M2 forward") # print to terminal for debugging
        sleep(1)
        
#@webiopi.macro
def backward():
        number = 4
        serial.writeString("M1: 1023\r\n") # motor 1 reverse half speed
        serial.writeString("M2: 1023\r\n") # motor 2 reverse half speed
        print("M1 and M2 reverse") # print to terminal for debugging
        sleep(1)

#@webiopi.macro
def servo_centre():
        number = 5
        print("servo centre") #print to terminal for debugging
        sleep(1)

#@webiopi.macro
def servo_left():
        number = 6
        print("servo left") #print to terminal for debugging
        sleep(1)

#@webiopi.macro
def servo_right():
        number = 7
        print("servo right") #print to terminal for debugging
        sleep(1)        
        
#@webiopi.macro
def led_on():
   number = 8
   print("LED on if fitted") #print to terminal for debugging
   sleep(1)
   
#@webiopi.macro
def led_off():
   number = 9
   print("LED off if fitted") #print to terminal for debugging
   sleep(1)
   
# Start the webiopi server
server = webiopi.Server(port=8000, login="coffin", password="coffin")

# Start the webcam video stream
# os.system("./streamer.sh")

# Register the macros
server.addMacro(stop)
server.addMacro(forward)
server.addMacro(left)
server.addMacro(right)
server.addMacro(backward)
server.addMacro(stop)
server.addMacro(servo_centre)
server.addMacro(servo_left)
server.addMacro(servo_right)
server.addMacro(led_on)
server.addMacro(led_off)

# Run default loop

webiopi.runLoop()

# Cleanly stop the server
server.stop()
