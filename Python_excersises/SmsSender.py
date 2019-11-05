from twilio.rest import Client
import twilio


class GsmApi:
    # Connection to twillo Api
    account_sid = "AC2a2701f346f056c6b18dbe4119a4fad0"
    # Your Account SID from twilio.com/console
    auth_token = "16233519a2852af9edd428df6766e331"
    # Your Auth Token from twilio.com/console
    fromNumber = "+12028836432"
    client = Client(account_sid, auth_token)

    def __init__(self, number, message):
        self.number = number
        self.message = message

    def SendMessage(self):
        try:
            message = GsmApi.client.messages.create(
                to=self.number,
                from_=GsmApi.fromNumber,
                body=self.message)
        except twilio.rest.TwilioException as e:
            print(e)
        return print("Your Message has been sended ;)")

    def MakeCall(self):
        try:
            call =GsmApi.client.calls.create(
                to=self.number,
                from_=GsmApi.fromNumber,
                url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient"
            )
        except twilio.rest.TwilioException as e:
            print(e)
        return print("Your Call has been made ;)")

Patryk = GsmApi("+3547798709","Your veryfication code is")
#Patryk.SendMessage()
Patryk.MakeCall()