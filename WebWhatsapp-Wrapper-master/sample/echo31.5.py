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
def getUnreadMessagers():
    while True:
        time.sleep(3)
        print('Checking for more messages')
        for contact in driver.get_unread():
            print (contact)
            for message in contact.messages:
                print (message)
                #if isinstance(message, Message):  # Currently works for text messages only.
                #    contact.chat.send_message(message.safe_content)
def printJson(data):
    json_string = json.dumps(data)
    print json_string
    sys.stdout.flush()
def getStaticMessagers():
    try:
        while True:
            time.sleep(1)
            paramTime = time.strftime("%Y-%m-%d %H:%M:%S")
            data = {
                "sessionID": sessionID,
                "code": 3,
                "message": "userMessage",
                "data": {
                    # did the the action
                    "caller": myPhone,
                    # send to
                    "callee": '0524592005',
                    "timestamp": paramTime,
                    "message": 'I want a static message',
                    "group": True
                }
            }
            printJson(data)

            time.sleep(10)
            paramTime = time.strftime("%Y-%m-%d %H:%M:%S")
            data = {
                "sessionID": sessionID,
                "code": 3,
                "message": "userMessage",
                "data": {
                    # did the the action
                    "caller": myPhone,
                    # send to
                    "callee": '0524592005',
                    "timestamp": paramTime,
                    "message": 'I want a static message',
                    "group": False
                }
            }
            printJson(data)

            time.sleep(10)
            paramTime = time.strftime("%Y-%m-%d %H:%M:%S")
            data = {
                "sessionID": sessionID,
                "code": 3,
                "message": "userMessage",
                "data": {
                    # did the the action
                    "caller": '0524592005',
                    # send to
                    "callee": myPhone,
                    "timestamp": paramTime,
                    "message": 'I want a static message',
                    "group": True
                }
            }
            printJson(data)

            time.sleep(10)
            paramTime = time.strftime("%Y-%m-%d %H:%M:%S")
            data = {
                "sessionID": sessionID,
                "code": 3,
                "message": "userMessage",
                "data": {
                    # did the the action
                    "caller": '0524592005',
                    # send to
                    "callee": myPhone,
                    "timestamp": paramTime,
                    "message": 'I want a static message',
                    "group": False
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
#getStaticMessagers()
getUnreadMessagers()



