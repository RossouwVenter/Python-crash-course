# 6-4. Glossary 2:
Glossary = {'variables' :'a value that is assigned to a name',
'array':'a bunch of strings that are compiled',
'comment':'Commenting out code for notes or extra information',
'numbers':'integer values in a program.',
'append':'adding a value to an array or dictionary'}

print('New words that I have learned:')
for k,v in Glossary.items():
	print(f'{k.title()}: \n\t {v.title()}')

print('\n')
# 6-5. Rivers:
rivers = {
'nile':'egypt',
'oranje':'South Africa',
'amazon':'brazil'}

for k,v in rivers.items():
	print(f'The {k.title()} flows through {v.title()}')

print('\n')
# 6-6. Polling:
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'ben': 'ruby',
'phil': 'c'
}

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")
# ????
