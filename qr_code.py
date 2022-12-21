"""
This script willconvert any link into
a qr code tha will be saved in a folder
as png picture. Can perform multiple
convertion if add multiple links in a text
file.
"""
#pip3 install qrcode

import qrcode  #to create codes
import sys     #to quit script
import pwinput #to read password format

PASSWORD = "" #define password

def main():
    """
    Main function to manage the program
    """
    chances = 3 #define chances variable to write the password
    while True:
        password = pwinput.pwinput(prompt='Password: ', mask='*') #read password
        if password != PASSWORD:
            if chances != 0:
                chances -= 1 #decrease chances
                print(f'Incorrect password,{chances} chances left')
            else:
                sys.exit(1) #quit the script
        else:
            with open('input.txt', 'r') as file:              #read codes from input text file
                linii = file.readlines()
            linii = [linie.split(' ') for linie in linii]     #each line from file is grouped as (name, link), separate them
            for linie in linii:
                qr = qrcode.make(linie[1])                    #generate QR code
                qr.save(f"./output/{linie[0]}.jpg")           #save QR code
            break

if __name__ == "__main__":
    main()