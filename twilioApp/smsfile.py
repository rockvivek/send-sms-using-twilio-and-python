#from twilio.rest import TwilioRestClient
from twilio.rest import Client
account_sid = 'AC8d28314ac48ab1659f59fe666118b7b7'
auth_token = 'c13f6f1383d0aedc52017a614c249d32'
my_cell = '+916392634784'
my_twilio ='+12058512752'
client = Client(account_sid, auth_token)
my_msg = "hello this is a demo message from vivek side.dont penic"
message = client.messages.create(
                     body = my_msg ,
                     from_= my_twilio,
                     to= my_cell
                 )

print(message.sid)