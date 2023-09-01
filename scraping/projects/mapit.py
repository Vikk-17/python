# Gets a street address from sys import argv
# import webbrowser
# from the command line args or clipboard
# Opens the browser to the Google map page for the address
# > Read the command line args from the sys.argv
# > Call the webbrowser.open() function to open the browser

#! python3

from audioop import add
import webbrowser, sys
import pyperclip
# 1. Handling the command line args

if len(sys.argv) > 1:
    # Get address from the command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()
# print(address)
webbrowser.open('https://www.google.com/maps/place/' + address)

# 2. Handling the clipboard content and launch the browser


