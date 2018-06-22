#! python3

from tkinter import *
from tkinter import ttk
import pyperclip
import pyautogui
import copy

emailDict = {}
# Function parses email by removing unwanted lines and turns it into dictionary(emailDict)


def parseEmail():
    global emailDict
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
        treeview.insert('', 'end', text=item, values=str(emailDict.get(item)))
        keyIndex += 1


# # Define a timer.
def countdownRequestExe():
    countdownRequest(5)


def countdownRequest(count):
    if count > 0:
        # call countdown again after 1000ms (1s)
        Label(buttonFrame, text='Pasting in ' + str(count) + ' seconds', bg=bgcolor, highlightbackground=bgcolor).grid(row=3, columnspan=2)
        buttonFrame.after(1000, countdownRequest, count - 1)
        count = count - 1
    else:
        Label(buttonFrame, text='      Pasting Now!      ', bg=bgcolor, fg='orange', highlightbackground=bgcolor).grid(row=3, columnspan=2)
        keyIndex = 0
        for item in keyList:
            pyautogui.typewrite(str(emailDict.get(item)))
            pyautogui.press('tab')
            keyIndex += 1
            # if str(emailDict.get(item)) == 'on':
            #     pyautogui.press('space')
            #     pyautogui.press('tab')
            # else:
            #     pyautogui.paste(str(emailDict.get(item))


def countdownDetailExe():
    countdownDetail(5)


def countdownDetail(count):
    if count > 0:
        # call countdown again after 1000ms (1s)
        Label(buttonFrame, text='Pasting in ' + str(count) + ' seconds', bg=bgcolor, highlightbackground=bgcolor).grid(row=3, columnspan=2)
        buttonFrame.after(1000, countdownDetail, count - 1)
        count = count - 1
    else:
        Label(buttonFrame, text='      Pasting Now!      ', bg=bgcolor, fg='orange', highlightbackground=bgcolor).grid(row=3, columnspan=2)
        keyIndex = 0
        for itemD in keyList2:
            pyautogui.typewrite(str(emailDict.get(itemD)))
            pyautogui.press('tab')
            keyIndex += 1

    # GUI Starts here
main = Tk()
main.title('Ivanti Trump v0.8')
main.geometry('460x800')

bgcolor = 'light grey'
# gives weight to the cells in the grid
rows = 0
while rows < 80:
    s = ttk.Style()
    s.theme_use('default')
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1

# Defines and places the notebook widget
nb = ttk.Notebook(main)
nb.grid(row=0, column=0, columnspan=85, rowspan=80, sticky='NESW')

# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
# page1.config(bg=bgcolor, highlightbackground=bgcolor)
nb.add(page1, text='New Employee')

# Create Button To Copy From Clipboard
pullDataFrame = Frame(page1)
pullDataFrame.config(bg=bgcolor)
pullDataFrame.grid(row=0, sticky='NESW')
fillFormButton = Button(pullDataFrame, text='Copy From Clipboard', width=46, bg=bgcolor, highlightbackground=bgcolor, command=parseEmail)
fillFormButton.grid(row=0, sticky='NESW')


# Create Treeview for keys and values
treeview = ttk.Treeview(page1)
treeview.grid(row=1, sticky='NESW')
treeview.config(height=30)
treeview.column('#0', width=230,)
treeview.heading('#0', text='Items')
treeview.config(columns=('values'))
treeview.column('values', width=230)
treeview.heading('values', text='Values')

keyList = ['first_name', 'middle_initial', 'last_name', 'muid', 'date_of_birth', 'preffered_display_name', 'personal_email', 'department', 'campus', 'building', 'office_or_room_number', 'employee_title', 'supervisor', 'start_date', 'needs_telephone_service', 'account_number', 'using_existing_ext', 'existing_telephone_number', 'display_name', 'phonemodel', 'long_distance_code', 'international_calling', 'voice_mail', 'call_forwarding', 'canvas', 'mymercer', 'CampusNexus_student', 'existing_nexus_user', 'CampusNexus_student_user_to_copy', 'nexus_requirements', 'campusvue_finance', 'shared_folder_access', 'name_of_the_share', 'vpn', 'VPN employee_type', '25live_access', 'computer_status', 'existing_computer_RT_number', 'previous_vdi_user', 'AdditonalNotes']

keyIndex = 0
for item in keyList:
    treeview.insert('', 'end', text=item)
    keyIndex += 1

keyList2 = ['muid', 'first_name', 'middle_initial', 'last_name', 'personal_email', 'date_of_birth', 'start_date', 'campus', 'building', 'office_or_room_number', 'supervisor', 'department', 'NUSEemployee_type', 'employee_title', 'NUSEad_displayname', 'needs_telephone_service', 'account_number', 'using_existing_ext', 'phonemodel', 'display_name', 'long_distance_code', 'international_calling', 'call_forwarding', 'voice_mail', 'NUSEdomain_account', 'NUSEemail_account', '25live_access', 'canvas', 'mymercer', 'CampusNexus_student', 'existing_nexus_user', 'shared_folder_access', 'name_of_the_share', 'computer_status', 'existing_computer_RT_number', 'NUSEcomputer_setup_ticket', 'NUSEad_account', 'NUSEmercer_email', 'NUSEtemp_password', 'NUSEemail_ad_button', 'AdditonalNotes', 'NUSEvoicemail_pin', 'NUSElong_distance_code', 'new_phone_extension']

# Add Frame for Button/Status
buttonFrame = Frame(page1)
buttonFrame.config(bg=bgcolor, highlightbackground=bgcolor)
buttonFrame.grid(row=2)

pasteFormRequst = Button(buttonFrame, text='Service Request', width=20, highlightbackground=bgcolor, command=countdownRequestExe)
pasteFormRequst.grid(row=0, column=0)
pasteFormDetail = Button(buttonFrame, text='Fix Detail Tab', width=20, highlightbackground=bgcolor, command=countdownDetailExe)
pasteFormDetail.grid(row=0, column=1)


# # Adds tab 2 of the notebook
# page2 = ttk.Frame(nb)
# nb.add(page2, text='Fix Details')


# # Adds tab 2 of the notebook
# page3 = ttk.Frame(nb)
# nb.add(page3, text='Guide')

main.mainloop()
