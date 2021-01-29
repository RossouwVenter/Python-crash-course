# 7-4. Pizza Toppings:
print('Add a topping to the Pizza') 
prompt = 'Enter quit to stop. or enter the toppings'
toppings = []
active = True
message = ''
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		toppings.append(message)
print(f' The topics are: {toppings}')
# 7-5 Movie Tickets:
promt = 'What is your age'
active = True

while active:
	message = input(promt)
	if int(message)  < 3:
		ticket = 'free'
		print(f'The ticket wil cost you {ticket}')
	elif message <= 12:
		ticket = f'${10}'
		print(f'The ticket wil cost you {ticket}')
	elif message > 12:
		ticket = f'${15}'
		print(f'The ticket wil cost you {ticket}')

# 7-6. Three Exits:
promt = 'What is your age'
active = True

while active:
	print('Enter quit to end!')
	message = input(promt)
	if int(message)  < 3:
		ticket = 'free'
		print(f'The ticket wil cost you {ticket}')
	elif message <= 12:
		ticket = f'${10}'
		print(f'The ticket wil cost you {ticket}')
	elif message > 12:
		ticket = f'${15}'
		print(f'The ticket wil cost you {ticket}')
	elif message == 'quit':
		break

# 7-7. Infinity:
number = 7
while number > 6:
	print('Endless loop')