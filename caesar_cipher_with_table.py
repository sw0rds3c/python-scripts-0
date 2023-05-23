# Caesar Cipher -- Encryption and Decryption functions 
# w/ testing & visualization tables

# Import Libraries
import random
import string
from prettytable import PrettyTable #python -m pip install -U prettytable

# Encryption Function
def cipher_encrypt(plain_text, key):

    encrypted = ""

    for c in plain_text:

        if c.isupper(): #check for uppercase character

            c_index = ord(c) - ord('A')

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower(): #check if its a lowecase character

            # subtract the unicode of 'a' to get index in alphabets range [0-25)
            c_index = ord(c) - ord('a') 

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        else:

            # if its not alphabetical, leave as is
            encrypted += c

    return encrypted

# Decryption Function
def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper(): 

            c_index = ord(c) - ord('A')

            # shifts current character to the left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        #check for lowercase
        elif c.islower(): 

            c_index = ord(c) - ord('a') 

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        else:

            # if its not alphabetical, leave as is
            decrypted += c

    return decrypted

#making the tables for visualization
print("These tables are for visualizing a shift of 5 ---> \n")

originalTable = PrettyTable()
newTable = PrettyTable()

originalTable.add_row(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
newTable.add_row(["f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e"])

print("This is the original alphabets order ---> \n")
print(originalTable, "\n")
print("This is the order with a shift of 5 ---> \n")
print(newTable, "\n")

#user input section for testing the encryption and decryption functions w/ user supplied input
plain_text = input("What is the letter, word or sentence you would like to pass through the caeser cipher? Please enter it here: \n")
shiftCount = int(input("\nPlease enter the desired shift count:\n"))
ciphertext = cipher_encrypt(plain_text, shiftCount)
print("\nOriginal message:\n", plain_text, "\n")
print("\nEncrypted Cipher text:\n", ciphertext, "\n")
print("\nDecrypted Cipher text:\n",cipher_decrypt(ciphertext, shiftCount))
