from twilio.rest import TwilioRestClient

account_sid = "ACb6538b4ae2a34f3dbf794edb29ac5137" # Your Account SID from www.twilio.com/console
auth_token  = "aef40043e3f41c6becaca14495ad5b63"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+919999676446",    # Replace with your phone number
    from_="+13343399296 ") # Replace with your Twilio number

print(message.sid)
