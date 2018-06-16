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
labelfont = ('ariel', 12, 'bold')   # Change Font

labelIndex = 0
for i in labelLoop:
    Label(page1, text=i + ':', font=labelfont).grid(row=labelIndex, column=0, sticky=E)
    labelIndex += 1

# Populate 2nd column
Label(page1, text=emailDict.get('first_name'), relief=SUNKEN, width=20, justify=LEFT).grid(row=0, column=1, sticky=W)
Label(page1, text=emailDict.get('middle_initial'), relief=SUNKEN, width=20, justify=LEFT).grid(row=1, column=1, sticky=W)
Label(page1, text=emailDict.get('last_name'), relief=SUNKEN, width=20, justify=LEFT).grid(row=2, column=1, sticky=W)
Label(page1, text=emailDict.get('muid'), relief=SUNKEN, width=20, justify=LEFT).grid(row=3, column=1, sticky=W)
Label(page1, text=emailDict.get('date_of_birth'), relief=SUNKEN, width=20, justify=LEFT).grid(row=4, column=1, sticky=W)
Label(page1, text=emailDict.get('display_name'), relief=SUNKEN, width=20, justify=LEFT).grid(row=5, column=1, sticky=W)
Label(page1, text=emailDict.get('personal_email'), relief=SUNKEN, width=20, justify=LEFT).grid(row=6, column=1, sticky=W)
Label(page1, text=emailDict.get('department'), relief=SUNKEN, width=20, justify=LEFT).grid(row=7, column=1, sticky=W)
Label(page1, text=emailDict.get('campus'), relief=SUNKEN, width=20, justify=LEFT).grid(row=8, column=1, sticky=W)
Label(page1, text=emailDict.get('building'), relief=SUNKEN, width=20, justify=LEFT).grid(row=9, column=1, sticky=W)
Label(page1, text=emailDict.get('office_or_room_number'), relief=SUNKEN, width=20, justify=LEFT).grid(row=10, column=1, sticky=W)
Label(page1, text=emailDict.get('employee_type'), relief=SUNKEN, width=20, justify=LEFT).grid(row=11, column=1, sticky=W)
Label(page1, text=emailDict.get('employee_title'), relief=SUNKEN, width=20, justify=LEFT).grid(row=12, column=1, sticky=W)
Label(page1, text=emailDict.get('supervisor'), relief=SUNKEN, width=20, justify=LEFT).grid(row=13, column=1, sticky=W)
Label(page1, text=emailDict.get('start_date'), relief=SUNKEN, width=20, justify=LEFT).grid(row=14, column=1, sticky=W)
Label(page1, text=emailDict.get('needs_telephone_service'), relief=SUNKEN, width=20, justify=LEFT).grid(row=15, column=1, sticky=W)
Label(page1, text=emailDict.get('account_number'), relief=SUNKEN, width=20, justify=LEFT).grid(row=16, column=1, sticky=W)
Label(page1, text=emailDict.get('using_existing_ext'), relief=SUNKEN, width=20, justify=LEFT).grid(row=17, column=1, sticky=W)
Label(page1, text=emailDict.get('existing_telephone_number'), relief=SUNKEN, width=20, justify=LEFT).grid(row=18, column=1, sticky=W)
Label(page1, text=emailDict.get('phone_model'), relief=SUNKEN, width=20, justify=LEFT).grid(row=19, column=1, sticky=W)
Label(page1, text=emailDict.get('long_distance_code'), relief=SUNKEN, width=20, justify=LEFT).grid(row=20, column=1, sticky=W)
Label(page1, text=emailDict.get('international_calling'), relief=SUNKEN, width=20, justify=LEFT).grid(row=21, column=1, sticky=W)
Label(page1, text=emailDict.get('voice_mail'), relief=SUNKEN, width=20, justify=LEFT).grid(row=22, column=1, sticky=W)
Label(page1, text=emailDict.get('call_forwarding'), relief=SUNKEN, width=20, justify=LEFT).grid(row=23, column=1, sticky=W)
Label(page1, text=emailDict.get('canvas_unused'), relief=SUNKEN, width=20, justify=LEFT).grid(row=24, column=1, sticky=W)
Label(page1, text=emailDict.get('mymercer'), relief=SUNKEN, width=20, justify=LEFT).grid(row=25, column=1, sticky=W)
Label(page1, text=emailDict.get('CampusNexus_student'), relief=SUNKEN, width=20, justify=LEFT).grid(row=26, column=1, sticky=W)
Label(page1, text=emailDict.get('CampusNexus_student_user_to_copy'), relief=SUNKEN, width=20, justify=LEFT).grid(row=27, column=1, sticky=W)
Label(page1, text=emailDict.get('campusvue_finance'), relief=SUNKEN, width=20, justify=LEFT).grid(row=28, column=1, sticky=W)
Label(page1, text=emailDict.get('shared_folder_access'), relief=SUNKEN, width=20, justify=LEFT).grid(row=29, column=1, sticky=W)
Label(page1, text=emailDict.get('name_of_the_share'), relief=SUNKEN, width=20, justify=LEFT).grid(row=30, column=1, sticky=W)
Label(page1, text=emailDict.get('vpn'), relief=SUNKEN, width=20, justify=LEFT).grid(row=31, column=1, sticky=W)
Label(page1, text=emailDict.get('employee_type'), relief=SUNKEN, width=20, justify=LEFT).grid(row=32, column=1, sticky=W)
Label(page1, text=emailDict.get('25live_access'), relief=SUNKEN, width=20, justify=LEFT).grid(row=33, column=1, sticky=W)
Label(page1, text=emailDict.get('computer_status'), relief=SUNKEN, width=20, justify=LEFT).grid(row=34, column=1, sticky=W)
Label(page1, text=emailDict.get('existing_computer_RT_number'), relief=SUNKEN, width=20, justify=LEFT).grid(row=35, column=1, sticky=W)
Label(page1, text=emailDict.get('additional_notes'), relief=SUNKEN, width=20, justify=LEFT).grid(row=36, column=1, sticky=W)


# pasteFill = Button(page1, text='Form Fill Xtreme')
# pasteFill.pack(side='bottom')
# grabClipboard = Button(page1, text='Grab Clipboard')
# grabClipboard.pack(side='bottom')

# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='Fix Details')


# Adds tab 2 of the notebook
page3 = ttk.Frame(nb)
nb.add(page3, text='Guide')

main.mainloop()
