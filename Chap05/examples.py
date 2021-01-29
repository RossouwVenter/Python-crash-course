sports = ['soccer','rugby','tennis','Swimming','Running']
for sport in sports:
	if sport == 'tennis':
		print(sport.upper())
	else:
		print(sport.lower())

print('\n')

if 'rugby' in sports:
		print(f'this is the sport: rugby')

if 'Triathlon' not in sports:
	print('there is not triathlon')


print('\n')
# if Statement

age = 12
if age < 4:
	print('admission is free')
elif age <= 18:
	print('Pay $25 admission fee') # else if statement!
else:
	print('Pay $40 admission fee')

# Multiple arrays

transport = ['bus','vw','motorbike','train','bmw','boat']
cars = ['vw','bmw']

for car in cars:
	if car in transport:
		print(cars[1])
	else:
		print(f'{car} is not available ')




