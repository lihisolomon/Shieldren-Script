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

def printJson(data):
    json_string = json.dumps(data)
    print json_string
    sys.stdout.flush()

def getUnreadMessagers(sessionID,myPhone):
	try:
	    while True:
		time.sleep(3)
		for contact in driver.get_unread():
		    for message in contact.messages:
			paramTime = time.strftime("%Y-%m-%d %H:%M:%S")
			contactNumber = message.sender.id
			if "@g.us" in message.chat_id:
		            isGroup = True
			    ContactName = contact.chat.name
		        else:
		            isGroup = False
			    ContactName = contact.chat.id
			phoneNumber = contactNumber[0:12]
			Message = message.content
			#print("Phone:" + message.sender.id + "|Message Type: " + message.type + " chat is : "+ message.chat_id)
			#print("MyPhone:" + myPhone + " phonenumber: " + phoneNumber + " contactNumber : "+ ContactName)
			if (phoneNumber == myPhone and isGroup == False):
				caller = myPhone
				callee = ContactName[0:12]
			elif (phoneNumber == myPhone and isGroup == True):
				caller = myPhone
				callee = ContactName
			elif (isGroup == True):
				caller = phoneNumber
				callee = ContactName
			else:
				caller = phoneNumber
				callee = myPhone
			data = {
		                    "sessionID": sessionID,
		                    "code": 3,
		                    "message": "userMessage",
		                    "data": {
		                        # did the the action
		                        "caller": caller,
		                        # send to
		                        "callee": callee,
		                        "timestamp": paramTime,
		                        "message": Message,
		                        "group": isGroup
		                    }
		                }
			printJson(data)
	except:
		e = sys.exc_info()[0]
		data = {
			"sessionID": sessionID,
			"code": -1,
			"message": str(e),
			"data": "null"
		}
		printJson(data)
			

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
printJson(data)

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
    printJson(data)
    sys.exit()

driver = WhatsAPIDriver(username="mkhase", loadstyles=True)
#print("Waiting for QR")
#QR Code
driver.get_qr(sessionID)
try:
    driver.wait_for_login()
    data = {
    "sessionID": sessionID,
    "code": 2,
    "message": "Scan Succeeded",
    "data": "null"
    }
    printJson(data)
except:
    data = {
    "sessionID": sessionID,
    "code": -1,
    "message": "Failed to Scan QR",
    "data": "null"
    }
    printJson(data)
    sys.exit()
getUnreadMessagers(sessionID,myPhone)



