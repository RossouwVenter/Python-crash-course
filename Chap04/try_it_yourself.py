# 4-1 pizzas
pizzas = ['margerita','hawaian','beef']
for pizza in pizzas:
	print(f' I like {pizza} pizza!')
print('\nI Love Pizza!')

# 4-2 Animals
animals = ['dogs','cats','Fish']
for animal in animals:
	print(f'{animals} would make great pets!')
print('Any of these animals could be pets!')

# 4-3 Counting to Twenty
print('\n')
for number in range(1,21):
	print(f' {number}')

	print('\n')

# 4-4 One Million
# numbers = []
# for number in range(1,1_000_001):
# 	numbers.append(number)

# print(numbers)
# print('\n')

# 4-5 Summing a Million
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# 4-6 Odd Numbers

print('\n')
numbers = list(range(1,21,2))
for number in numbers:
	print(number)

# 4-7 Threes
print('\n')
numbers = list(range(3,33,3))
for number in numbers:
	print(number)

# 4-8 Cubes
print('\n')

Cubes = []
for value in range(1,11):
	cube = value ** 3
	Cubes.append(cube) 

print(Cubes)

print('\n')
# 4-9 Cube Comprehension:
squares = [value**3 for value in range(1, 11)]
print(list(squares))

print('\n')
# 4-10 Slices
print(f'The first three items in the list are: \n{squares[:3]}')
print(f'\n Three items from the middel of the list are: \n {squares[4:6]}')
print(f'\n The last three items of the list are: \n {squares[-3:]}')

print('\n')

# 4-11 My Pizzas, Your Pizzas:
friend_pizzas = ['margerita','hawaian','beef']
pizzas.append("sea food")
# print(pizzas)
friend_pizzas.append("Chicken")
print(f'My favorite pizzas are:')
for pizza in pizzas:
	print(pizza)
print(f'\nMy friends favorite pizzas are:')
for friend_pizza in friend_pizzas:
	print(friend_pizza)


print('\n')


# 4-12 More Loops;
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
for foods in my_foods:
	print(foods)
print("\nMy friend's favorite foods are:")
for friend_foods in friend_foods:
	print(friend_foods)

# 4-13 Buffet
print('\n')
foods = ('buggers','pizza','pasta','salad','meat')
for food in foods:
	print(food)
# foods.append('Fish')
print('\n')
foods = ('toast' , 'dessert''buggers','pizza','pasta','meat')
for food in foods:
	print(food)

# 4-14 PEP 8:

# 4-15 Code Review

# 1.
squares = [value**3 for value in range(1, 11)]
print(list(squares)) # the code has been written in one line instead of a few lines
#  in order to save space and make it easier to read.

# 2.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for foods in my_foods:
	print(foods)

print("\nMy friend's favorite foods are:")
for friend_foods in friend_foods:
	print(friend_foods)
 #  using spaces to make readability easier

# 3.
print('\n')
foods = ('buggers','pizza','pasta','salad','meat')
for food in foods:
	print(food)
# foods.append('Fish')
print('\n')
foods = ('toast' , 'dessert''buggers','pizza','pasta','meat')
for food in foods:
	print(food)

# making open lines in my coding to seperate the outcome 
# in order to make it easier to read for the user
