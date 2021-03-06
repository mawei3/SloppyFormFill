#! python3
# pyinstaller --onefile --windowed --name IvantiTrump --icon=IvantiTrump.icns IvantiTrump.py

from tkinter import *
from tkinter import ttk
import pyperclip
import pyautogui
import copy
import webbrowser  # use webbrowser to open outlook mailto for listservEmailGenerator

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
    # Change NoneType to ''
    #
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
        pyautogui.typewrite(str(emailDict.get('first_name')))
        pyautogui.press('tab')
        if str(emailDict.get('no_middle_initial', '')) == 'on':
            pyautogui.press('tab')
        else:
            pyautogui.typewrite(str(emailDict.get('middle_initial')))
            pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('last_name')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('muid')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('date_of_birth')))
        pyautogui.press('tab')
        pyautogui.press('tab')  # skip Preffered Display Name
        pyautogui.typewrite(str(emailDict.get('personal_email')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('department')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('campus')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('building')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('office_or_room_number')))
        pyautogui.press('tab')
        pyautogui.press('tab')  # skip employee type
        pyautogui.typewrite(str(emailDict.get('employee_title')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('supervisor')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('start_date')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('needs_telephone_service')))
        pyautogui.press('tab')
        if str.lower(emailDict.get('needs_telephone_service', '')) == 'yes':  # start telecom rediculusness
            pyautogui.typewrite(str(emailDict.get('account_number')))
            pyautogui.press('tab')
            pyautogui.typewrite(str(emailDict.get('display_name')))
            pyautogui.press('tab')
            if str.lower(emailDict.get('using_existing_ext', '')) == 'yes':
                pyautogui.press('tab')
                pyautogui.typewrite(str(emailDict.get('existing_telephone_number')))
                pyautogui.press('tab')
            else:
                pyautogui.typewrite(str(emailDict.get('phonemodel', '')))
                pyautogui.press('tab')
            if str.lower(emailDict.get('long_distance_code', '')) == 'on':
                pyautogui.press('space')
                pyautogui.press('tab')
                if str.lower(emailDict.get('international_calling', '')) == 'on':
                    pyautogui.press('space')
                    pyautogui.press('tab')
                else:
                    pyautogui.press('tab')
            else:
                pyautogui.press('tab')
            if str.lower(emailDict.get('voice_mail', '')) == 'on':
                pyautogui.press('space')
                pyautogui.press('tab')
            else:
                pyautogui.press('tab')
            if str.lower(emailDict.get('call_forwarding', '')) == 'on':
                pyautogui.press('space')
                pyautogui.press('tab')
        # else:
        #     pyautogui.press('tab')
        pyautogui.press('tab')  # skip canvas
        buttonFrame.after(500)
        if str.lower(emailDict.get('mymercer', '')) == 'on':
            pyautogui.press('space')
            pyautogui.press('tab')
        else:
            pyautogui.press('tab')
        if str.lower(emailDict.get('CampusNexus_student', '')) == 'on':
            pyautogui.press('space')
            pyautogui.press('tab')
            pyautogui.typewrite(emailDict.get('CampusNexus_student_user_to_copy'))
            pyautogui.press('tab')
        else:
            pyautogui.press('tab')
        if str.lower(emailDict.get('campusvue_finance', '')) == 'on':
            pyautogui.press('space')
            pyautogui.press('tab')
        else:
            pyautogui.press('tab')
        if str.lower(emailDict.get('shared_folder_access', '')) == 'on':
            pyautogui.press('space')
            pyautogui.press('tab')
            pyautogui.typewrite(emailDict.get('name_of_the_share'))
            pyautogui.press('tab')
        else:
            pyautogui.press('tab')
        pyautogui.press('tab')  # SkipVPN
        if str.lower(emailDict.get('25live_access', '')) == 'on':
            pyautogui.press('space')
            pyautogui.press('tab')
        else:
            pyautogui.press('tab')

        if str(emailDict.get('computer_status', '')) == 'Using existing':
            pyautogui.typewrite('using existing computer', interval=0.5)
            pyautogui.press('tab')
            pyautogui.typewrite(emailDict.get('existing_computer_RT_number'))
        elif str(emailDict.get('computer_status', '')) == 'Using an existing Thin Client (VDI)':
            pyautogui.typewrite('Using existing thin client', interval=0.5)
            pyautogui.press('tab')
            pyautogui.typewrite(emailDict.get('previous_vdi_user'))
        elif str(emailDict.get('computer_status', '')) == 'Ordered new':
            pyautogui.typewrite('New computer', interval=0.5)
        elif str(emailDict.get('computer_status', '')) == 'Not using computer':
            pyautogui.typewrite('No computer required', interval=0.5)
        elif str(emailDict.get('computer_status', '')) == 'Using new VDI':
            pyautogui.typewrite('Thin', interval=0.5)
        pyautogui.press('tab')
        pyautogui.typewrite(emailDict.get('additional_notes', ''))
        Label(buttonFrame, text='          Done!          ', bg=bgcolor, fg='green', highlightbackground=bgcolor).grid(row=3, columnspan=2)


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
        pyautogui.typewrite(str(emailDict.get('muid')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('first_name')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('middle_initial', '')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('last_name')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('personal_email', '')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('date_of_birth')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('start_date')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('campus')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('building')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('office_or_room_number')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('supervisor')))
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('department')))
        pyautogui.press('tab')
        pyautogui.press('tab')  # skip employee type
        pyautogui.typewrite(str(emailDict.get('employee_title')))
        pyautogui.press('tab')
        pyautogui.press('tab')  # skip AD display name
        if str(emailDict.get('needs_telephone_service', '')) == 'yes':
            pyautogui.press('space')
            pyautogui.press('tab')
            pyautogui.typewrite(str(emailDict.get('account_number')))
            pyautogui.press('tab')
            pyautogui.typewrite(str(emailDict.get('existing_telephone_number')))
            pyautogui.press('tab')

        else:
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
        pyautogui.press('tab')  # skip Domain account
        pyautogui.press('space')  # Email account
        pyautogui.press('tab')
        if str(emailDict.get('25live_access', '')) == 'on':
            pyautogui.press('space')
            pyautogui.press('tab')
        else:
            pyautogui.press('tab')
        if str(emailDict.get('canvas', '')) == 'on':
            pyautogui.press('space')
            pyautogui.press('tab')
        else:
            pyautogui.press('tab')
        if str(emailDict.get('mymercer', '')) == 'on':
            pyautogui.press('space')
            pyautogui.press('tab')
        else:
            pyautogui.press('tab')
        if str(emailDict.get('CampusNexus_student', '')) == 'on':
            pyautogui.press('space')
            pyautogui.press('tab')
            pyautogui.typewrite(str(emailDict.get('CampusNexus_student_user_to_copy')))
            pyautogui.press('tab')
        else:
            pyautogui.press('tab')
        if str(emailDict.get('shared_folder_access', '')) == 'on':
            pyautogui.press('space')
            pyautogui.press('tab')
            pyautogui.typewrite(str(emailDict.get('name_of_the_share')))
            pyautogui.press('tab')
        else:
            pyautogui.press('tab')
        if str(emailDict.get('computer_status', '')) == 'Using existing':
            pyautogui.typewrite('using existing computer', interval=0.5)
            pyautogui.press('tab')
            pyautogui.typewrite(emailDict.get('existing_computer_RT_number'))
            pyautogui.press('tab')
        elif str(emailDict.get('computer_status', '')) == 'Using an existing Thin Client (VDI)':
            pyautogui.typewrite('Using existing thin client', interval=0.5)
            pyautogui.press('tab')
            pyautogui.typewrite(emailDict.get('previous_vdi_user'))
            pyautogui.press('tab')
        elif str(emailDict.get('computer_status', '')) == 'New computer has been/will be ordered':
            pyautogui.press('tab')
        elif str(emailDict.get('computer_status', '')) == 'No computer required':
            pyautogui.press('tab')
        elif str(emailDict.get('computer_status', '')) == 'Thin client has been/will be ordered':
            pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.typewrite(str(emailDict.get('additional_notes', '')))
        Label(buttonFrame, text='          Done!          ', bg=bgcolor, fg='green', highlightbackground=bgcolor).grid(row=3, columnspan=2)

# add items for Listboxes on page2


def add_addressSubList():
    grabSubEntry = subListEntry.get()
    addressSubListBox.insert(END, grabSubEntry)


def add_addressUnSList():
    grabUnSEntry = unsListEntry.get()
    addressUnSListBox.insert(END, grabUnSEntry)


def add_addressListServ():
    grabListServ = listServEntry.get()
    listServListBox.insert(END, grabListServ)


def pickListServ():
    pass

# Generate Email Function


def createListServEmail():
    emailBody = ''
    # i = 0
    # j = 0
    # k = 0
    # m = 0
    listServListBoxItems = []
    addressSubListBoxItems = []
    addressUnSListBoxItems = []
    listServIndex = 0
    listServSize = listServListBox.size()
    while listServSize > 0:
        listServListBoxItems.append(listServListBox.get(listServIndex))
        listServSize -= 1
        listServIndex += 1
    addressSubIndex = 0
    addressSubSize = addressSubListBox.size()
    while addressSubSize > 0:
        addressSubListBoxItems.append(addressSubListBox.get(addressSubIndex))
        addressSubSize -= 1
        addressSubIndex += 1
    addressUnSIndex = 0
    addressUnSSize = addressUnSListBox.size()
    while addressUnSSize > 0:
        addressUnSListBoxItems.append(addressUnSListBox.get(addressUnSIndex))
        addressUnSSize -= 1
        addressUnSIndex += 1

    for i in listServListBoxItems:
        for j in addressSubListBoxItems:
            emailBody = emailBody + 'Subscribe%20' + i + '%20' + j + '%0d'

    listServIndex = 0
    for k in listServListBoxItems:
        for l in addressUnSListBoxItems:
            emailBody = emailBody + 'Unsubscribe%20' + k + '%20' + l + '%0d'

    emailRecipient = 'mailserv@mercer.edu'
    emailSubject = ''

    webbrowser.open('mailto:?Content-type=text/plain&to=' + emailRecipient + '&subject=' + emailSubject + '&body=' + emailBody, new=1)


# GUI Starts here
main = Tk()
main.title('Ivanti Trump v1.1.0')
main.resizable(0, 0)
main.geometry('465x800')
s = ttk.Style()
s.theme_use('classic')

bgcolor = 'light grey'
# gives weight to the cells in the grid
rows = 0
while rows < 80:
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
pullDataFrame.config(bg=bgcolor)
pullDataFrame.grid(row=0, sticky='NESW')
fillFormButton = Button(pullDataFrame, text='Copy From Clipboard', width=48, bg=bgcolor, highlightbackground=bgcolor, command=parseEmail)
fillFormButton.grid(row=0)


# Create Treeview for keys and values
treeview = ttk.Treeview(page1)
treeview.grid(row=1, sticky='NESW')
treeview.config(height=30)
treeview.column('#0', width=230,)
treeview.heading('#0', text='Items')
treeview.config(columns=('values'))
treeview.column('values', width=230)
treeview.heading('values', text='Values')

keyList = ['first_name', 'middle_initial', 'last_name', 'muid', 'date_of_birth', 'preffered_display_name', 'personal_email', 'department', 'campus', 'building', 'office_or_room_number', 'employee_title', 'supervisor', 'start_date', 'needs_telephone_service', 'account_number', 'using_existing_ext', 'existing_telephone_number', 'display_name', 'phonemodel', 'long_distance_code', 'international_calling', 'voice_mail', 'call_forwarding', 'canvas', 'mymercer', 'CampusNexus_student', 'existing_nexus_user', 'CampusNexus_student_user_to_copy', 'nexus_requirements', 'campusvue_finance', 'shared_folder_access', 'name_of_the_share', 'vpn', 'VPN employee_type', '25live_access', 'computer_status', 'existing_computer_RT_number', 'previous_vdi_user', 'additional_notes']

keyIndex = 0
for item in keyList:
    treeview.insert('', 'end', text=item)
    keyIndex += 1

keyList2 = ['muid', 'first_name', 'middle_initial', 'last_name', 'personal_email', 'date_of_birth', 'start_date', 'campus', 'building', 'office_or_room_number', 'supervisor', 'department', 'NUSEemployee_type', 'employee_title', 'NUSEad_displayname', 'needs_telephone_service', 'account_number', 'using_existing_ext', 'phonemodel', 'display_name', 'long_distance_code', 'international_calling', 'call_forwarding', 'voice_mail', 'NUSEdomain_account', 'NUSEemail_account', '25live_access', 'canvas', 'mymercer', 'CampusNexus_student', 'existing_nexus_user', 'shared_folder_access', 'name_of_the_share', 'computer_status', 'existing_computer_RT_number', 'NUSEcomputer_setup_ticket', 'NUSEad_account', 'NUSEmercer_email', 'NUSEtemp_password', 'NUSEemail_ad_button', 'additional_notes', 'NUSEvoicemail_pin', 'NUSElong_distance_code', 'new_phone_extension']

# Add Frame for Button/Status
buttonFrame = Frame(page1)
buttonFrame.config(bg=bgcolor, highlightbackground=bgcolor)
buttonFrame.grid(row=2)

pasteFormRequst = Button(buttonFrame, text='Service Request', width=20, highlightbackground=bgcolor, command=countdownRequestExe)
pasteFormRequst.grid(row=0, column=0)
pasteFormDetail = Button(buttonFrame, text='Fix Detail Tab', width=20, highlightbackground=bgcolor, command=countdownDetailExe)
pasteFormDetail.grid(row=0, column=1)


# # Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='ListServ')

# Email Address Subscribe frame
emailAddressSubFrame = Frame(page2)
emailAddressSubFrame.config(bg=bgcolor)
emailAddressSubFrame.grid(row=0, sticky='NSEW')
addressSubLabel = Label(emailAddressSubFrame, text='Subscribe these Addresses:', bg=bgcolor, highlightbackground=bgcolor)
addressSubLabel.grid(row=0)
subListEntry = Entry(emailAddressSubFrame, width=34, highlightbackground=bgcolor)
subListEntry.grid(row=1, column=0)
subListEntryButton = Button(emailAddressSubFrame, text='Add', width=10, bg=bgcolor, highlightbackground=bgcolor, command=add_addressSubList)
subListEntryButton.grid(row=1, column=1)
addressSubListBox = Listbox(emailAddressSubFrame, width=35, highlightbackground=bgcolor)
addressSubListBox.grid(row=2, column=0)
editAddressesSubButton = Button(emailAddressSubFrame, text='Delete', width=10, bg=bgcolor, highlightbackground=bgcolor, command=lambda addressSubListBox=addressSubListBox: addressSubListBox.delete(ANCHOR))
editAddressesSubButton.grid(row=2, column=1, sticky='N')
# Email Address UnSubscribe frame
emailAddressUnSFrame = Frame(page2)
emailAddressUnSFrame.config(bg=bgcolor)
emailAddressUnSFrame.grid(row=1)
emailAddressUnSLabel = Label(emailAddressUnSFrame, text="UnSubscribe these Addresses:", bg=bgcolor, highlightbackground=bgcolor)
emailAddressUnSLabel.grid(row=0)
unsListEntry = Entry(emailAddressUnSFrame, width=34, highlightbackground=bgcolor)
unsListEntry.grid(row=1, column=0)
unsListEntryButton = Button(emailAddressUnSFrame, text='Add', width=10, bg=bgcolor, highlightbackground=bgcolor, command=add_addressUnSList)
unsListEntryButton.grid(row=1, column=1)
addressUnSListBox = Listbox(emailAddressUnSFrame, width=35, highlightbackground=bgcolor)
addressUnSListBox.grid(row=2, column=0)
editAddressesUnSButton = Button(emailAddressUnSFrame, text='Delete', width=10, bg=bgcolor, highlightbackground=bgcolor, command=lambda addressUnSListBox=addressUnSListBox: addressUnSListBox.delete(ANCHOR))
editAddressesUnSButton.grid(row=2, column=1, sticky='N')
# ListServ Selection Frame
listServFrame = Frame(page2)
listServFrame.config(bg=bgcolor)
listServFrame.grid(row=2)
listServLabel = Label(listServFrame, text="Selected Listservs:", bg=bgcolor, highlightbackground=bgcolor)
listServLabel.grid(row=0)
listServEntry = Entry(listServFrame, width=34, highlightbackground=bgcolor)
listServEntry.grid(row=1, column=0)
listServEntryButton = Button(listServFrame, text='Add', width=10, bg=bgcolor, highlightbackground=bgcolor, command=add_addressListServ)
listServEntryButton.grid(row=1, column=1)
listServListBox = Listbox(listServFrame, width=35, highlightbackground=bgcolor)
listServListBox.grid(row=2, rowspan=2)
listServEditButton = Button(listServFrame, text="Delete", width=10, bg=bgcolor, highlightbackground=bgcolor, command=lambda listServListBox=listServListBox: listServListBox.delete(ANCHOR))
listServEditButton.grid(row=2, column=1, sticky='N')
listServPickButton = Button(listServFrame, text='Pick List', width=10, bg=bgcolor, highlightbackground=bgcolor, command=pickListServ)
listServPickButton.grid(row=3, column=1, sticky='N')
# Generate Email0 Button Frame
generateListServFrame = Frame(page2)
generateListServFrame.config(bg=bgcolor)
generateListServFrame.grid(row=3, sticky='NSEW')
generateListServButton = Button(generateListServFrame, text='Generate Email', width=45, highlightbackground=bgcolor, command=createListServEmail)
generateListServButton.grid(row=0)
clearAllListBoxesButton = Button(generateListServFrame, text='!!! Start Over !!!', width=45, fg="red", highlightbackground=bgcolor)
clearAllListBoxesButton.grid(row=1, sticky='S')

# # Adds tab 2 of the notebook
# page3 = ttk.Frame(nb)
# nb.add(page3, text='Guide')

main.mainloop()
