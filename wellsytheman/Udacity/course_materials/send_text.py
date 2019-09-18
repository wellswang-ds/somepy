from twilio.rest import Client 

account_sid = "AC61be8a1417c5caddf32f4d3138b17b46"
auth_token  = "28600fd9e1d17e24af0fbe9d03990f1c"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886937165528", 
    from_="+16193041646",
    body="You have a small Dick")

print(message.sid)
