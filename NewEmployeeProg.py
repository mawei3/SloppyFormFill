#! python3

import pyperclip
import keyboard
import tkinter

#
rawEmail = str(pyperclip.paste())
splitEmail = rawEmail.split(sep='\n')
splitEmail = [i.strip() for i in splitEmail]
listEmail = list(filter(None, splitEmail))
i = 0
# Remove Exta Bits
emailDict = {}
for line in listEmail:
    i = i + 1
    if line == 'muid':
        emailDict = emailDict.update({'muID': listEmail[i]})
    if line == 'first_name':
        emailDict = emailDict.update({'first_name': listEmail[i]})
    if line == 'middle_initial':
        emailDict = emailDict.update({'middle_initial': listEmail[i]})
    if line == 'last_name':
        emailDict = emailDict.update({'last_name': listEmail[i]})
    if line == 'date_of_birth':
        emailDict = emailDict.update({'date_of_birth': listEmail[i]})
    if line == 'first_name':
        emailDict = emailDict.update({'first_name': listEmail[i]})
    if line == 'middle_initial':
        emailDict = emailDict.update({'middle_initial': listEmail[i]})
    if line == 'first_name':
        emailDict = emailDict.update({'last_name': listEmail[i]})
date_of_birth,personal_email,campus,building,office_or_room_number

#field_names
# requestor_email,new_mercer_employee,new_mercer_employee,H2_0,muid,first_name,middle_initial,no_middle_initial,last_name,date_of_birth,personal_email,campus,building,office_or_room_number,employee_title,department,supervisor,start_date,H2_1,needs_telephone_service,needs_telephone_service,using_existing_ext,using_existing_ext,phone_type,phone_type,phone_type,phone_type,phone_type,phone_type,existing_telephone_number,account_number,display_name,long_distance_code,international_calling,voice_mail,call_forwarding,H2_2,email_account,mymercer,campusvue_finance,CampusNexus_student,existing_nexus_user,existing_nexus_user,CampusNexus_student_user_to_copy,nexus_requirements,shared_folder_access,name_of_the_share,vpn,25live_access,H2_3,computer_status,existing_computer_RT_number,computer_status,computer_status,computer_status,previous_vdi_user,computer_status,H2_4,additional_notes,*debug,*to,*formname,*redirect,*subject,*bcc,*cc,*honeypot,*replyto
#
# checkbox_input_names
# no_middle_initial,long_distance_code,international_calling,voice_mail,call_forwarding,email_account,mymercer,campusvue_finance,CampusNexus_student,shared_folder_access,vpn,25live_access
#
# radio_input_names
# new_mercer_employee,new_mercer_employee,needs_telephone_service,needs_telephone_service,using_existing_ext,using_existing_ext,phone_type,phone_type,phone_type,phone_type,phone_type,phone_type,existing_nexus_user,existing_nexus_user,computer_status,computer_status,computer_status,computer_status,computer_status
# select_names
# campus
#
# text_input_names
# requestor_email,H2_0,muid,first_name,middle_initial,last_name,date_of_birth,personal_email,building,office_or_room_number,employee_title,department,supervisor,start_date,H2_1,existing_telephone_number,account_number,display_name,H2_2,CampusNexus_student_user_to_copy,name_of_the_share,H2_3,existing_computer_RT_number,previous_vdi_user,H2_4,*honeypot
#
# textarea_names
# nexus_requirements,additional_notes


# print(muID)
