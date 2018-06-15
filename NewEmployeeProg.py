#! python3

import pyperclip
import keyboard
import tkinter
import copy
from pprint import pprint

rawEmail = str(pyperclip.paste())
splitEmail = rawEmail.split(sep='\n')
splitEmail = [i.strip() for i in splitEmail]
listEmaila = list(filter(None, splitEmail))

# Deletes everything before MUID
listEmailb = copy.copy(listEmaila)
for line in listEmaila:
    if line != 'muid':
        listEmailb.remove(line)
    else:
        break
listEmaila = copy.copy(listEmailb)

emailDict = dict(zip(listEmaila[::2], listEmaila[1::2]))  # turn list into dictionary

# print(emailDict)
pprint(emailDict)  # pprint for testing
