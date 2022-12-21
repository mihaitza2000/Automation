"""
This script will take automatically screenshots of 
your PC screen, continously, with a delay set by user
The script is password protected.
"""
# pip3 install pwinput
# pip3 install pyautogui
import pyautogui #to take screenshot
import os        #to read file name
import sys       #to close the program
import pwinput   #to write passworrd format 
import time      #to create delay
PASSWORD = ""    #set a password

def screenshot(interval, number_images):
    """
    Function that takes screenshot automaticaly
    and save pictures in output folder
    """
    while True:
        camera = pyautogui.screenshot()                     #take a screenshot
        number_images += 1                                  #increment number of images
        camera.save(f'output/{number_images + 1}.png')      #save screenshot
        time.sleep(interval)                                #wait a number of seconds

def main(number_images):
    """
    Main function that manage everything
    """
    chances = 3                                                           #number of chances to write the password
    while True:                                               
        password = pwinput.pwinput(prompt='Password: ', mask='*')         #password format
        if password == PASSWORD:                                          #check password
            interval = input('Delay in seconds: ')                        #set delay
            if interval.isdigit():                                        #check delay to be number
                if int(interval) > 0:                                     #check delay to be positive
                    screenshot(int(interval), number_images)              #call screenshot function
                else:
                    print('Delay must be positive')          
            else:
                print('Delay must be integer')  
        elif chances != 0:
                chances -= 1
                print(f'Incorrect password, have {chances} more chaces')    
        else:
            sys.exit(1)  #exit the program

if __name__ == "__main__":
    number_images = len(os.listdir('output'))#count images in output folder
    main(number_images)