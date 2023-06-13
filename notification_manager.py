from twilio.rest import Client

#Enter custom twilio sid and token
account_sid = ''
auth_token = ''


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            #Enter private twilio phone number
            from_='',
            #Enter personal phone number
            to=''
        )
        print(message)
