import time
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

driver = WhatsAPIDriver(username="mkhase", loadstyles=True)
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

while True:
	time.sleep(3)
    	print('Checking for more messages')
	print('test')
	for contact in driver.get_unread():
		print ('test1')
		for message in contact.messages:
			print ('test2')
			print (message)
		    	if isinstance(message, Message):  # Currently works for text messages only.
		    		contact.chat.send_message(message.safe_content)	
