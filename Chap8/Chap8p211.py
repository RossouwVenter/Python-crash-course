# 8-9. Messages:
Messages =['Hello world','Python is fun','Programming is fun']

def show_messages():
	print(Messages)

show_messages()
# 8-10. Sending Messages:
Messages =['Hello world','Python is fun','Programming is fun']
sent_message = []

def send_messages():
	print(Messages)
	for message in Messages:
		sent_message(Messages)
		print(f'message sent: {sent_message()}')

# 8-11. Archived Messages:
Messages =['Hello world','Python is fun','Programming is fun']
sent_message = []

def send_messages():
	print(Messages)
	for message in Messages:
		sent_message(Messages)
		print(f'message sent: {sent_message()}')
		print(f'Origional message: {Messages}')