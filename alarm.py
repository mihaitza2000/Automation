"""
In this application the script will check
if the battery is under a threshold value
an if so and the PC is not pluged in
a voice alarm will warn you untill you plug
it in.
"""
#pip3 install pyttsx3
#pip3 install psutil
import pyttsx3 #to convert text to speech
import psutil  #to have access to battery 
               #information and other components
LEVEL = 20     #threshold
engine = pyttsx3.init()             #init the engine
rate = engine.getProperty('rate')   #get voice rate to slow it down
engine.setProperty('rate', rate/1.5)#slow voice rate by 50%
def main():
    """
    The main function that checks for battery level
    and start alarm when the conditions are satisfied
    TODO:
    1. When plug in but the alarm is talking
       have to wait till the alarm stops
    2. Solution to stop the alarm in case you
       don't have a charger to plug in 
    """
    while True:
        baterie = psutil.sensors_battery()                               #battery object
        if baterie.percent < LEVEL and not baterie.power_plugged:        #check conditions
            engine.say(f'Battery is {baterie.percent} percent, plug in!')#start alarm
            engine.runAndWait()
if __name__ == "__main__":
    main()