# Functions
def pets(PetType,PetName,PetColour,PetAge):
	print('\nmy pets are')
	print(f'I have a {PetType}')
	print(f'Her name is {PetName}')
	print(f'She has {PetColour} fur')
	print(f'She is still young at an age of {PetAge}')

pets('Dog','Nyla','White',f'6 months')
pets('Dog','luca','White',f'14 years')

print('\n')

def pets(PetType='Dog',PetName='Nyla',PetColour='White',PetAge=f'6 months'):
	print('\nMy pets are:')
	print(f'I have a {PetType}')
	print(f'Her name is {PetName}')
	print(f'She has {PetColour} fur')
	print(f'She is still young at an age of {PetAge}')

pets()

#Optional functions
print('\n')

def customer(name,surname,favstore=''):
	if favstore:
		customerDetails = f'{name} {surname} favorite store is: {favstore}'
	else:
		customerDetails = f'{name} {surname} favorite store is: unknown'
	return customerDetails.title()

customer1 = customer('John','jobs','Nike')
print(customer1)
customer2 = customer('Steve','mallic')
print(customer2)

# while loop + function

def getFullname(first_name,last_name):
	full_name = f'{first_name} {last_name}'
	return full_name.title()

while True:
	print('\n Please tell me your name:')
	print('Enter quit to quit')
	f_name = input('first name: ')
	l_name = input('last name: ')
	formatted_name = getFullname(f_name,l_name)
	if (f_name or l_name ) == "quit":
		break
	else:
	
	print(f'Hello,{formatted_name}!')

	#  Doesnt work

# Importing an entire Module
# importing: