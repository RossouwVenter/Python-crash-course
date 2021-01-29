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
