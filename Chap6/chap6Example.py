# Dictionarys
shoes = {'nikes': 'fashion','asics' :'training','addidas':'racing','nikes' : 'racing'}

shoetype = shoes.get(f'nike','nike is not available')
# if statement in a dictionary
print(f'Shoe is best for: {shoetype}')


for stype, purpose in shoes.items():
	print(f'These {stype.title()} are best for {purpose.title()}.')
# exctracting all the values from the list

print('\n')
for stype in shoes.keys():
	print(f'The diffret shoes are {stype}')
# exctracting keys from the list
print('\n')

print('The purpose of the shoes:')
for purpose in set(shoes.values()) :# set is used to prevent double values.
	print(purpose)
# exctracting values from the list
print('\n')

print('Diffrent brands of shoes that are popular:')
for stype in sorted(shoes.keys()):
	print(f'\t{stype.title()}')
# Sorting the values in alphabetic.


# Places to buy the transport method
transport = {
	'buss': {
		'Pretoria': 'North',
		'JHB': 'South'	
			},
	'Car': {
		'Pretoria': 'East',
		'JHB': 'North'
	},
}
# Display
for trspt, location in transport.items():
	print(f'\n Transport method: {trspt}')
	tourJhb = f"Destination: {location['Pretoria']} and {location['JHB']}"
	tourPta = f"Destination: {location['Pretoria']} and {location['JHB']}"

	print(f'\t{tourJhb.title()}')
	print(f'\t{tourPta.title()}')