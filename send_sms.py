from twilio.rest import Client

account_sid = 'AC39152bacb7fd3e8e358738c34c80fd35'
auth_token = 'ef4f1563ebef954226fcc7dc03ce8d6b'
client = Client(account_sid, auth_token)

#message = client.messages \
 #   .create(
  #       body='First Sms from the pycharm',
   #      from_='+15017122661',
    #     to='+8801752625560'
     #)

message = client.messages.create(
                              body='This is utpal. He has come to your home. Get home quickly.',
                              from_='+12025179046',
                              to='+8801842515838'
                          )


print(message.sid)
