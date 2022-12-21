"""
In this script you can both encrypt or
decrypt files from a diirectory.
"""

#pip3 install cryptography

import os
import sys
from cryptography.fernet import Fernet #to crypt/decrypt files

#Functia de criptare
def encrypt():
    """
    This function check if there are files to
    be encrypted, make a list of the and generate
    a key in order to encrypt files with that key.
    """
    list_files = os.listdir("input")                        #list files to encrypt
    key = Fernet.generate_key()                             #generate encryption key
    with open("key.key", "wb") as the_key:                  #keep key in a .key file
        the_key.write(key)
    for file in list_files:                                 #encrypt files 
        with open(f'input/{file}', 'rb') as f:
            content = f.read()
        files_content = Fernet(key).encrypt(content)
        with open(f'input/{file}', "wb") as f:
            f.write(files_content)
    print('Files encrypted!')

def decrypt():
    """
    The decrypt function will check for key if is
    valid and read files binary to decrypt them
    """
    list_files = os.listdir("input")                                     #load files
    if os.path.isfile('./key.key'):                                      #check key
        with open('./key.key', 'rb') as file:
            key = file.read()
        for file in list_files:
            with open(f'input/{file}', 'rb') as f:
                continut = f.read()
            try:
                continut_decriptat = Fernet(key).decrypt(continut)      #try to decrypt
            except:
                print('Invalid key')
                sys.exit(1) #quit script
            with open(f'input/{file}', "wb") as f:
                f.write(continut_decriptat)
        print('Fisierele au fost decriptate')
    else:
        print('Key not found')

def main():
    """
    Main function to manage the two function
    of encrytion and decryption.
    """
    if answer == '1':
        if len(os.listdir("input")) == 0:
            print("No files to encrypt")
        else:
            encrypt()
    elif answer == '2':
        if len(os.listdir("input")) == 0:
            print("No files to decrypt")
        else:
            decrypt()   

if __name__ == "__main__":
    answer = input('Encrypt/ Decrypt files (1/2) ?: ')
    main(answer)