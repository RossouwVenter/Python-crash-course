# 6-1. Person:
person = {'first_name':'Leze','last_name':'Taylor','age': 18,
'city':'midstream'}

for k,v in person.items():
	print(f'{k.title()}:{v}')

print('\n')
# 6-2. Favorite Numbers:
favNum = {'simone' : 2,'John' : 8,'Matt' : 2100,'piet' : 7,
'sam' : 75}
print('Favorite Numbers of my friends:')
for k,v in favNum.items():
	print(f'{k.title()}: {v}')

# 6-3. Glossary:
print('\n')

Glossary = {'variables' :'a value that is assigned to a name',
'array':'a bunch of strings that are compiled',
'comment':'Commenting out code for notes or extra information',
'numbers':'integer values in a program.',
'append':'adding a value to an array or dictionary'}

print('New words that I have learned:')
for k,v in Glossary.items():
	print(f'{k.title()}: \n\t {v.title()}')

