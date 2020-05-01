import os
from twilio.rest import Client


account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)
client.messages.create(
    to=os.environ["JK_PHONE_NUM"],
    from_=os.environ["TWILIO_PHONE_NUM"], 
    body="You are a magical unicorn on your first Twilio Rainbow journey."
    )
