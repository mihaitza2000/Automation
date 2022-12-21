"""
The script will check for any movement
of mouse so to alert the user someone
is using his PC.
"""

#pip3 install pyaudio

import win32api
import pyttsx3
import os.path

ALARM = "Don't touch my laptop!" #set an alarm warning

#######init engine to cnvert text to speech
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate/1.5)
#######

def alarm():
    """
    Function to convert text to speech
    """
    engine.say(ALARM)
    engine.runAndWait()

def detect_movement(x_mouse, y_mouse):
    """
    Function to detect when mouse was moved
    """
    while True:
        if win32api.GetCursorPos() != (x_mouse, y_mouse): #check if mouse coordinates changed
            alarm()
        if os.path.exists('alarm.txt'):#if alarm.txt file exists will stop the script 
            break  

def main():
    """
    Set mouse coordinates and start move detection 
    """
    (x_mouse, y_mouse) = win32api.GetCursorPos()#get mouse coordinates
    detect_movement(x_mouse, y_mouse) 

if __name__ == "__main__":
    main()         