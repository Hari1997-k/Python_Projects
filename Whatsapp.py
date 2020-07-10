"""
  ==> To do this program u need to get authenticated twilio phine number 
  ==> u need to store the twilio authentication details in environmental variable to access easily
"""
import os
from twilio.rest import Client

client = Client()

from_num = 'whatsapp:+14155238886'
to_num = 'whatsapp:' + os.environ['My_Account_sid']

client.messages.create(body='HELLO WORLD', from_=from_num, to=to_num)

# ******************************** SIMPLIFIED WHATSAPP PROGRAM  ********************************
# from twilio.rest import *
# import os
# from Python_Projects.Credentials import account_sid,auth_token,my_cell,my_twilio
#
# client = Client(account_sid, auth_token)
# msg = "Hello Hiii"
# res = client.messages.create(body=msg, from_=my_twilio, to= my_cell)
#
