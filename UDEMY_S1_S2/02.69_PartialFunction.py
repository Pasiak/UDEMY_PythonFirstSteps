import smtplib
import sys
import functools

# def SendIntoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):
#     message = '''From: {}
#     Subject : {}
#
#     {}'''.format(mailFrom, mailSubject, mailBody)
#     try:
#         serwer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#         serwer.ehlo()
#         serwer.login(user, password)
#         serwer.sendmail(user, mailTo, message)
#         serwer.close()
#         print("mail send")
#         return True
#     except:
#         print("Error", sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
#         return False
#
#
# user = 'pytesto997@gmail.com'
# password = "Cwaniak12"
# mailFrom = 'pytesto997@gmail.com'
# mailTo = 'patryk.pasiak@gmail.com'
# mailSubject = 'Subject'
# mailBody = '''Tekst ktory zostanie wyslany mailem'''
#
# # SendIntoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)
# SendInfoEmailFromGmail = functools.partial(SendIntoEmail, user, password)
#
# SendInfoEmailFromGmail(mailFrom, mailTo, mailSubject, mailBody)

# '''

# LAB
import requests
import os


def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


msg = "Please wait - the file {} will be downloaded"
url = 'http://mobilo24.eu/spis'
dir = r'C:\Users\El Patrico\Desktop\tempTXT'
file = 'logo.png'

save_url_to_dir = functools.partial(save_url_file, dir = r'C:\Users\El Patrico\Desktop\tempTXT'
, msg = "Please wait - the file {} will be downloaded")

save_url_to_dir(url=url, file=file)
