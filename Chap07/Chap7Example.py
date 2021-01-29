 # prompt = 'Tell us something and we will repeat it back'
 # prompt!= 'Enter quit to stop'

 # active = True

 # while active:
	# message = input(prompt)
	# if message == 'quit':
 # 		active = false
 # 	else:
	# 	print(message)

prompt = 'Enter a number and I will tell you if it  is odd or not'
prompt != 'Enter quit to stop the program'
active = True

while active:
	number = input(prompt)
	if number == 'quit':
		break
	elif int(number) % 2 == 1:
		print(f'\n The number,{number} is odd')
	elif int(number) % 2 == 0:
		print(f'\n The number,{number} is even!')


		
		

