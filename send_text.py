from twilio.rest import TwilioRestClient

account_sid = "" # Your Account SID from www.twilio.com/console
auth_token  = ""  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="My name is Ron Burgundy?",
    to="1234567890",    # Replace with your phone number
    from_="1234567890") # Replace with your Twilio number

print(message.sid)
