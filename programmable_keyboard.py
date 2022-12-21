"""
Inthis script I am usign hotkeys to
open webbrowser pages using keyboard module
"""

#pip3 install webbrowser
#pip3 install keyboard

import webbrowser                     #to browse internet
from keyboard import add_hotkey, wait #to add hotkeys and wait to be pressed

def open_web(link):
    """
    Function to open a new webpage with URL link
    """
    webbrowser.open(link)

def add_function(shortcut, link):
    """
    Function to add a new hotkey
    """
    add_hotkey(f"{shortcut}", callback=lambda:open_web(link))

def main():
    """
    Main function to manage the script
    """
    with open('input.txt', 'r') as file:                    #hotkeys are stored in a text files
        comenzi = file.readlines()                          #add commands in a list
    comenzi = [comanda.split(' ') for comanda in comenzi]   #commads are pair of hotkey and URL link
    for comanda in comenzi:
        add_function(comanda[0], comanda[1])                #create hotkey for commands
    wait()

if __name__ == "__main__":
    main()