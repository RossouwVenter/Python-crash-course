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