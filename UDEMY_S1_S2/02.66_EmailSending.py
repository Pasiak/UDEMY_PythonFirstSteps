import smtplib
import sys

mailFrom = 'pytesto997@gmail.com'
mailTo = 'patryk.pasiak@gmail.com'
mailSubject = 'Subject'
mailBody = '''Tekst ktory zostanie wyslany mailem'''

message = '''From: {}
Subject : {}

{}'''.format(mailFrom,mailSubject,mailBody)


user = 'pytesto997@gmail.com'
password = "test"

try:
    serwer = smtplib.SMTP_SSL('smtp.gmail.com',465)
    serwer.ehlo()
    serwer.login(user,password)
    serwer.sendmail(user,mailTo,message)
    serwer.close()
    print("mail send")
except:
    print("Error",sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])