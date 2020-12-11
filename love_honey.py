from twilio.rest import Client

account_sid = 'ACad3d275065fe3fd78b3d148aca8c1f34'
auth_token = '7c139ab24973c0d47d5238910a9ea65b'
client = Client(account_sid, auth_token)


def love_message():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Goodnight sweet heart',
        to='whatsapp:+233273637961'
    )

    print(message.sid)
