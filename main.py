import requests
from twilio.rest import Client


Params = "&units=Imperial"


URL = "https://api.openweathermap.org/data/2.5/weather?q=Orlando" + \
    Params + "&appid=367896ff813cfe5826ffcb728cc70905"


r = requests.get(URL)

data = r.json()
weather = data['weather'][0]
description = weather['description']
Tempature = data['main']
temp = Tempature['temp']
Weathermessage = (
    f"Today is going to be a {description} with average tempature of {temp}")


account_sid = 'AC898e74f14d2d4dde9a6c4dc8ec842c3b'
auth_token = '09300f793a1822a66db5083dcddd9cb4'
client = Client(account_sid, auth_token)


phoneNumbers = ["+14077316223", "14074832151"]


for number in phoneNumbers:
    message = client.messages.create(
        body=f'Hello, this is your daily Weather Alert! {Weathermessage}',
        from_='+18559108392',  # Replace with your Twilio phone number
        to=number  # Replace with the recipient's phone number
    )

print(f"Message sent successfully. Message SID: {message.sid}")
