# 5-1 Conditional Tests
# 1.
car = 'bmw'
if car == 'bmw':
	print(f'Your car is {car}')

print('\n')
# 2.
shoesize = 9
if shoesize >= 9:
	shoe = 'racer'
	print(f'The shoe is a {shoe}')
else:
	shoe ='trainer'
	print(f'The shoe is a {shoe}')

print('\n')
# 3. 
cars = ['bmw','merc','audi','vw']

if car.lower() in cars:
 	print(f'{car} is still available')
else:
 	print('The car is not available')

# 4.
numbers = [1,61,2,22,3,6,5,4,7,9]

for number in numbers:
	if number > 10:
		del number
	elif number < 5:
		print(numbers)

print('\n')
# 5-2 More Conditional Tests:
# 1.
auto = 'false'
if 'bmw' in cars:
	auto = 'true'
	print(auto)
else:
	print(auto)
# 2.
auto = 'false'
if 'bmw' in cars:
	auto = 'true'
	print(auto.lower())
else:
	print(auto)
# 3.

num = 5
if num < 5:
	num = num + 1
elif num < 5:
	num = num -1
elif num == 5:
	print(f'{num} is the correct number')
else:
	print(f'The number is {num}')
# 4.
numb = 7
while numb > num:
	num = num -1
if num and numb == num:
	print(f'Bothe numbers are {numb}')
#5.
if car.lower() in cars:
 	print(f'{car} is still available')
else:
 	print('The car is not available')
#6.
car = 'ferrari'
if car not in cars:
 	print(f'{car} is not available')
else:
 	print('The car is  available')