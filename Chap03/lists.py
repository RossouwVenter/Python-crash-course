# use square brackets
# 3-1 Names :
names = ['Pieter','John','Kyla','Jason']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print('\n')

# 3-2 Greetings:
print(f'Hello how are you {names[0]}')
print(f'Hello how are you {names[1]}')
print(f'Hello how are you {names[2]}')
print(f'Hello how are you {names[3]}')

print('\n')

# 3-3 Your Own list:
transport = ['BMW','Audi','Mercedes','ferrari','lamborgini']
print(f'I would like to drive a  {transport[-1]}')

print('\n')

# 3-4 Guest List:
diner = ['Oupa','Kyla','Pappa']
message = 'I am inviting you for diner and it would be nice if you are there,'
print(f'{message} {diner[0]}')
print(f'{message} {diner[1]}')
print(f'{message} {diner[-1]}')

print('\n')

# 3-5 Changing Guest list:
print(diner[-1])
New = "Oupa Hermie"
diner[-1] = New
print(f'{message} {diner[0]}')
print(f'{message} {diner[1]}')
print(f'{message} {diner[-1]}')

print('\n')

# 3-6
print('I have found a bigger table')
diner.insert(0,"Pappa")
diner.insert(2,"Mamma")
diner.append('Leze')

print(f'{message} {diner[0]}')
print(f'{message} {diner[1]}')
print(f'{message} {diner[2]}')
print(f'{message} {diner[3]}')
print(f'{message} {diner[4]}')
print(f'{message} {diner[-1]}')

print('\n')

#3-7
print('Sorry to inform you but i can now only invite 2 people.')
print(f"Sorry you are unfortunatly uninvited  {diner[-1]}")
diner.pop()
print(f"Sorry you are unfortunatly uninvited  {diner[-1]}")
diner.pop()
print(f"Sorry you are unfortunatly uninvited  {diner[-1]}")
diner.pop()
print(f"Sorry you are unfortunatly uninvited  {diner[-1]}")
diner.pop()
del diner[0]
del diner[0]
print(diner)

#3-8
places = ['germany','amerika','england','australia','new-zeeland']
print(places)
print(sorted(places))
print(places)
print(places.reverse())
print(places)
print(places.reverse())
print(places.reverse())
print()
print(places.sort())
# print(places.sort().reverse())

# 3-9 Dinner Guests:
len(diner)

# 3-10 Every Function:
