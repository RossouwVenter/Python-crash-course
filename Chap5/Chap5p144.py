# 5-8. Hello Admin:
names = ['leze','Rossouw','Kyla','admin','secretary']

for name  in names:
	if 'admin' in names:
		print('Hello admin, would you like to see a status report?\n')
	if name != 'admin':
		print(f'Hello {name} thanks you for logging in again!')

# 5-9. No Users:
users = []
if users:
	print('we need to find some users!')

# 5-10. Checking Usernames:
current_users = ['ben','jon','steve','kit','Amanda']
new_users = ['wian','pieter','eliza','johan','zeta']

# new_users.lower()
# current_users.lower()
if new_users in current_users:
	print('User naame has already been used.')
else:
	print('Username is available')
# 5-11. Ordinal Numbers:
print('\n')
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
	if number == 1:
		print('1st')
	elif number == 2 :
		print('2nd')
	else:
		print(f'{number}th')

