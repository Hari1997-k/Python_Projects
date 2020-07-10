/ TO DO THIS APPLICATION U NEED TO BE AUTHENTICATED BYV TWILIO "
import os
from twilio.rest import Client

client = Client()

from_num = 'whatsapp:+14155238886'
to_num = 'whatsapp:' + os.environ['My_Account_sid']

client.messages.create(body='HELLO WORLD', from_=from_num, to=to_num)
