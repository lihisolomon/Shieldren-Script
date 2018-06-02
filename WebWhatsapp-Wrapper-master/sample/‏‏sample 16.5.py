import time
import datetime
import sys
import json
from webwhatsapi import WhatsAPIDriver
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

# start to read new messages
# print "waiting for QR"
driver = WhatsAPIDriver()
driver.firstrun(sessionID)

data = {
    "sessionID": sessionID,
    "code": 2,
    "message": "Scan Succeeded",
    "data": "null"
}
json_string = json.dumps(data)
print json_string
#print "Scan Succeeded"

sys.stdout.flush()
driver.view_unread()
# print "bot started"
# print 'my phone number: ', sys.argv[1]
myPhone = sys.argv[1]
while True:
    time.sleep(1)
    # print('checking for more messages')
    for contact in driver.view_unread():
        for message in contact[u'messages']:
            # driver.send_to_whatsapp_id(contact[u'id'],message[u'message'])
            # write into file the information
            contactNumber = (contact[u'id'])
            if "@g.us" in contactNumber:
                isGroup = True

            else:
                isGroup = False

            messageS = (message[u'message'])

            if (' -_x_isSentByMe' in messageS):
                messageS = messageS.replace(" -_x_isSentByMe", "")
                # print messageS
                phoneNumber = myPhone
            else:
                phoneNumber = contactNumber[0:12]

            paramTime = time.strftime("%Y-%m-%d %H:%M:%S")

            if 'undefined' != messageS:
                # create json file
                # data = {phoneNumber: {'group': isGroup, 'timestamp': paramTime, 'message': messageS}}
                #data = {'caller': myPhone, 'callee': phoneNumber, 'timestamp': paramTime, 'message': messageS,
                #        'group': isGroup}
                data = {
                    "sessionID": sessionID,
                    "code": 3,
                    "message": "userMessage",
                    "data": {
                        "caller": myPhone,
                        "callee" : phoneNumber,
                        "timestamp" : paramTime,
                        "message" : messageS,
                        "group" : isGroup
                    }
                }
                json_string = json.dumps(data)
                print json_string

            sys.stdout.flush()