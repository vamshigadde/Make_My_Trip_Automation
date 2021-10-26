# import win32com.client
# #other libraries to be used in this script
# import os
# from datetime import datetime, timedelta
# outlook = win32com.client.Dispatch('Mail.application')
# mapi = outlook.GetNamespace("MAPI")
# for account in mapi.Accounts:
# 	print(account.DeliveryStore.DisplayName)
#
# inbox = mapi.GetDefaultFolder('Outlook')
# '''
#
#
#
#
# import win32com.client
# import re
# import datetime
# # set up connection to outlook
# outlook = win32com.client.Dispatch("Mail.Application").GetNamespace("MAPI")
# inbox = outlook.GetDefaultFolder(6)
# messages = inbox.Items
# message = messages.GetFirst()
# today_date = str(datetime.date.today())
# while True:
#   try:
#     current_sender = str(message.Sender).lower()
#     current_subject = str(message.Subject).lower()
#     # find the email from a specific sender with a specific subject
#     # condition
#     if re.search('Subject Title',current_subject) != None and re.search(sender_name,current_sender) != None:
#       print(current_subject) # verify the subject
#       print(current_sender)  # verify the sender
#       attachments = message.Attachments
#       attachment = attachments.Item(1)
#       attachment_name = str(attachment).lower()
#       attachment.SaveASFile(path + '\\' + attachment_name)
#     else:
#       pass
#     message = messages.GetNext()
#   except:
#     message = messages.GetNext()
# exit
#
# '''