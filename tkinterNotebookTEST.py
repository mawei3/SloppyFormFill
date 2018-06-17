#! python3

from tkinter import *
from tkinter import ttk
import pyperclip
import pyautogui
import copy
import time


# Function parses email by removing unwanted lines and turns it into dictionary(emailDict)
def parseEmail():
    emailDict = {}
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

    # Populate 2nd column
    treeview.delete(*treeview.get_children())
    keyIndex = 0
    for item in keyList:
        treeview.insert('', 'end', text=item, values=emailDict.get(item))
        keyIndex += 1

    # treeview.insert('', '0', text='first_name', values=emailDict.get('first_name'))
    # treeview.insert('', '1', values=emailDict.get('middle_initial'))
    # treeview.insert('', '2', values=emailDict.get('last_name'))
    # treeview.insert('', '3', values=emailDict.get('muid'))
    # treeview.insert('', '4', values=emailDict.get('date_of_birth'))
    # treeview.insert('', '5', values=emailDict.get('display_name'))
    # treeview.insert('', '6', values=emailDict.get('personal_email'))
    # treeview.insert('', '7', values=emailDict.get('department'))
    # treeview.insert('', '8', values=emailDict.get('campus'))
    # treeview.insert('', '9', values=emailDict.get('building'))
    # treeview.insert('', '10', values=emailDict.get('office_or_room_number'))
    # treeview.insert('', '11', values=emailDict.get('employee_type'))
    # treeview.insert('', '12', values=emailDict.get('employee_title'))
    # treeview.insert('', '13', values=emailDict.get('supervisor'))
    # treeview.insert('', '14', values=emailDict.get('start_date'))
    # treeview.insert('', '15', values=emailDict.get('needs_telephone_service'))
    # treeview.insert('', '16', values=emailDict.get('account_number'))
    # treeview.insert('', '17', values=emailDict.get('using_existing_ext'))
    # treeview.insert('', '18', values=emailDict.get('existing_telephone_number'))
    # treeview.insert('', '19', values=emailDict.get('phone_model'))
    # treeview.insert('', '20', values=emailDict.get('long_distance_code'))
    # treeview.insert('', '21', values=emailDict.get('international_calling'))
    # treeview.insert('', '22', values=emailDict.get('voice_mail'))
    # treeview.insert('', '24', values=emailDict.get('call_forwarding'))
    # treeview.insert('', '25', values=emailDict.get('canvas_unused'))
    # treeview.insert('', '26', values=emailDict.get('mymercer'))
    # treeview.insert('', '27', values=emailDict.get('CampusNexus_student'))
    # treeview.insert('', '28', values=emailDict.get('CampusNexus_student_user_to_copy'))
    # treeview.insert('', '29', values=emailDict.get('campusvue_finance'))
    # treeview.insert('', '30', values=emailDict.get('shared_folder_access'))
    # treeview.insert('', '31', values=emailDict.get('name_of_the_share'))
    # treeview.insert('', '32', values=emailDict.get('vpn'))
    # treeview.insert('', '33', values=emailDict.get('employee_type'))
    # treeview.insert('', '34', values=emailDict.get('25live_access'))
    # treeview.insert('', '35', values=emailDict.get('computer_status'))
    # treeview.insert('', '36', values=emailDict.get('existing_computer_RT_number'))
    # treeview.insert('', '37', values=emailDict.get('additional_notes'))


# GUI Starts here
main = Tk()
main.title('Form Filler 5000')
main.geometry('480x800')


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
nb.add(page1, text='New Employee')

# Create Button To Copy From Clipboard
pullDataFrame = Frame(page1)
pullDataFrame.grid(row=0)
fillFormButton = Button(pullDataFrame, text='Copy From Clipboard', width=46, command=parseEmail)
fillFormButton.grid(row=0)


# Create Treeview for keys and values
treeview = ttk.Treeview(page1)
treeview.grid(row=1)
treeview.config(height=30)
treeview.column('#0', width=230,)
treeview.heading('#0', text='Items')
treeview.config(columns=('values'))
treeview.column('values', width=230)
treeview.heading('values', text='Values')

keyList = ['first_name', 'middle_initial', 'last_name', 'muid', 'date_of_birth', 'preffered display_name', 'personal_email', 'department', 'campus', 'building', 'office_or_room_number', 'employee_type', 'employee_title', 'supervisor', 'start_date', 'needs_telephone_service', 'account_number', 'using_existing_ext', 'existing_telephone_number', 'display_name', 'phonemodel', 'long_distance_code', 'international_calling', 'voice_mail', 'call_forwarding', 'canvas', 'mymercer', 'CampusNexus_student', 'existing_nexus_user', 'CampusNexus_student_user_to_copy', 'nexus_requirements', 'campusvue_finance', 'shared_folder_access', 'name_of_the_share', 'vpn', 'VPN employee_type', '25live_access', 'computer_status', 'existing_computer_RT_number', 'previous_vdi_user', 'AdditonalNotes']

keyIndex = 0
for item in keyList:
    treeview.insert('', 'end', text=item)
    keyIndex += 1


# Add Frame for Button/Status
buttonFrame = Frame(page1)
buttonFrame.grid(row=2)

pasteFormRequst = Button(buttonFrame, text='Service Request', width=20)
pasteFormRequst.grid(row=0, column=0)
pasteFormDetail = Button(buttonFrame, text='Fix Detail Tab', width=20)
pasteFormDetail.grid(row=0, column=1)
Label(buttonFrame, text='Status').grid(row=2, columnspan=2)
Label(buttonFrame, text='CountDown Here').grid(row=3, columnspan=2)
# pasteFill = Button(page1, text='Form Fill Xtreme')
# pasteFill.pack(side='bottom')
# grabClipboard = Button(page1, text='Grab Clipboard')
# grabClipboard.pack(side='bottom')

# # Adds tab 2 of the notebook
# page2 = ttk.Frame(nb)
# nb.add(page2, text='Fix Details')


# # Adds tab 2 of the notebook
# page3 = ttk.Frame(nb)
# nb.add(page3, text='Guide')

main.mainloop()
