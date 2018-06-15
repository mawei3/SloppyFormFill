#! python3

import pyperclip
import keyboard
import tkinter
from pprint import pprint

#
rawEmail = str(pyperclip.paste())
splitEmail = rawEmail.split(sep='\n')
splitEmail = [i.strip() for i in splitEmail]
listEmail = list(filter(None, splitEmail))

emailDict = dict(zip(listEmail[::2], listEmail[1::2]))  # turn list into dictionary

print(emailDict)
# pprint  # pprint for testing
