# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
TWILIO_AUTH_TOKEN = "aa876b3bcdae2dac3d1e15ef3536f508"
TWILIO_ACCOUNT_SID = "ACea175db3e75bfcf637826dbf2a379b09"

account_sid = os.environ[TWILIO_ACCOUNT_SID]
auth_token = os.environ[TWILIO_AUTH_TOKEN]
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='How is the day Mr. Souvik?',
         from_='+15017122661',
         to='+919932903030'
     )

print(message.sid)
