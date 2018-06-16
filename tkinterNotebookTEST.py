#! python3

from tkinter import *
from tkinter import ttk
import pyperclip
import keyboard
import tkinter
import copy

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

main = Tk()
main.title('Form Filler 5000')
main.geometry('500x800')


# gives weight to the cells in the grid
rows = 0
while rows < 80:
    s = ttk.Style()
    s.theme_use('classic')
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1

# Defines and places the notebook widget
nb = ttk.Notebook(main)
nb.grid(row=0, column=0, columnspan=85, rowspan=80, sticky='NESW')

# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
nb.add(page1, text='Submit Request')
labelLoop = ['First Name', 'Middle Initial', 'Last Name', 'MUID', 'Date of Birth', 'Preffered Display Name', 'Personal Email', 'Department Name', 'Campus', 'Building', 'Room or Office', 'Employee Type', 'Job Title', 'Supervisor', 'Start Date', 'Phone Required', 'Account', 'Use Existing', 'Existing Extension', 'Phone Model', 'Long Distance', 'International', 'Voicemail', 'Call Forward', 'Canvas', 'MyMercer', 'Campus Nexus', 'Nexus Copy From', 'CampusVue', 'Network Drive', 'Network Path', 'VPN', 'VPN Type', '25 Live', 'Computer Requirement', 'Existing RT', 'Additonal Notes']
labelfont = ('ariel', 11, 'bold')   # Change Font
for i in labelLoop:                 # Print all labels for form
    labelLoop = Label(page1, text=(i + ':').rjust(35), width='22')
    labelLoop.config(font=labelfont)
    labelLoop.config(borderwidth=1, relief="solid")
    labelLoop.pack(side='top', anchor="w")

for i in emailDict:                 # Print all labels for form
    valueLoop = Label(page1, text=(emailDict[i]), width='22')
    valueLoop.config(font=labelfont)
    valueLoop.config(borderwidth=1, relief="solid")
    valueLoop.pack(anchor="w")

pasteFill = Button(page1, text='Form Fill Xtreme')
pasteFill.pack(side='bottom')
grabClipboard = Button(page1, text='Grab Clipboard')
grabClipboard.pack(side='bottom')

# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='Fix Details')


# Adds tab 2 of the notebook
page3 = ttk.Frame(nb)
nb.add(page3, text='Guide')

main.mainloop()
