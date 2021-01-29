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