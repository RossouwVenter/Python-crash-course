# 9-1. Restaurant:
class Restaurant:

	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)

	def open_restaurant(self):
		print(f'{self.restaurant_name} is open!')

restaurant1 = Restaurant('Mc Donalds','Take Out')
restaurant2 = Restaurant('Debonairs','Take Out Pizza')

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print(f'\nFirst Restaurant is: {restaurant1.restaurant_name} and it is a {restaurant1.cuisine_type} cuisine')
print(f'Second Restaurant is: {restaurant2.restaurant_name} and it is a {restaurant2.cuisine_type} cuisine')

# 9-2. Three Restaurants
restaurant2.describe_restaurant()
print(f'\nSecond Restaurant is: {restaurant2.restaurant_name} and it is a {restaurant2.cuisine_type} cuisine')

restaurant3 = Restaurant('KFC', 'Chicken')
restaurant3.describe_restaurant()
print(f'\nThird Restaurant is: {restaurant3.restaurant_name} and it is a {restaurant3.cuisine_type} cuisine')

# 9-3. Users:
class User:

	def __init__(self,firstName,lastName):
		self.firstName = firstName
		self.lastName = lastName
		# self.age = age
		# self,gender = gender

	def describe_user(self):
		print(f'First Name: {self.firstName}')
		print(f'Last Name : {self.lastNametName}')
		# print(f'Age: {self.age}')
		# print(f'Gender: {self.gender}')

	def greeter(self):
		print(f'\nHello {self.firstName} {self.lastName}! ')

John = User('John','Henry')

John.greeter()
print(f' You may take a seat where you like')