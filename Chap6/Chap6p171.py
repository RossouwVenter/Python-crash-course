# 6-7. People:
user = {
	'Leze': {
	 'first_name':'Leze',
	 'last_name':'Taylor',
	 'age': 18,
	 'city':'midstream',}
	 },'Bob': {
{'first_name':'Bob',
'last_name':'jay',
'age': 25,
'city':'Pretoria'}
}
'Matty':{
{'first_name':'matty',
'last_name':'gary',
'age': 21,
'city':'Centurion'}}

for k,v in user.items():
	print(f'{k.title()}:{v}')

print('\n')
# 6-8. Pets:
pets = {'dog':{
	'breed': 'Retriever',
	'age': 10,
	'color' : 'gold',
},'cat':{
	'breed': 'unknown',
	'age': 7,
	'color' : 'grey',
}
}

for petType in pets.item():
	print(f'\n Type of pet:{petType}')
	age = pets['age']
	breed = pets['breed']
	print(f' Breed: {breed} is {age} years old')

# 6-9. Favorite Places:
favorite_places = ['germany','Italy','USA']
for places in user.items():
	favorite_places := user[favorite_places]

# 6-10. Favorite Numbers:
favNum = {'simone' : 2,'John' : 8,'Matt' : 2100,'piet' : 7,
'sam' : 75}
print('Favorite Numbers of my friends:')
for k,v in favNum.items():
	print(f'{k.title()}: {v}')

# 6-11. Cities:
cities = {'Durban','Pretoria','Bloemfontein'}
