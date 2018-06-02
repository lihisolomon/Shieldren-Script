import time
import json
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
import datetime
import sys
import json
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# set unicode
reload(sys)
sys.setdefaultencoding('Windows-1255')
sessionID = random_with_N_digits(10)
data = {
    "sessionID": sessionID,
    "code": 5,
    "message": "Start",
    "data": "null"
}
json_string = json.dumps(data)
print json_string
sys.stdout.flush()

try:
    myPhone = sys.argv[1]
except:
    e = sys.exc_info()[0]
    data = {
        "sessionID": sessionID,
        "code": -1,
        "message": "phone number is empty ,exit.",
        "data": "null"
    }
    json_string = json.dumps(data)
    print json_string
    sys.stdout.flush()
    sys.exit()

driver = WhatsAPIDriver(username="mkhase", loadstyles=True)
#print("Waiting for QR")
driver.get_qr(sessionID)
driver.wait_for_login()

data = {
    "sessionID": sessionID,
    "code": 2,
    "message": "Scan Succeeded",
    "data": "null"
}
json_string = json.dumps(data)
print json_string
sys.stdout.flush()

#while True:
#	time.sleep(3)
#   	print('Checking for more messages')
#	for contact in driver.get_unread():
#		print ('test1')
#		for message in contact.messages:
#		print ('test2')
#			print (message)
#		    	if isinstance(message, Message):  # Currently works for text messages only.
#		    		contact.chat.send_message(message.safe_content)	
		
	
