# 8-12. Sandwiches:
def toppings(*sandwitch_toppings):
	print(f'Summary of the sandwitch: {sandwitch_toppings}')

toppings('cheese','egg','tomato')
toppings('cheese','bacon','onjions','tomato')
toppings('chicken','Mayo')

# 8-13. User Profile:
def build_profile(first, last, **user_info):
# """Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
user_profile2 = build_profile('Rossouw','Venter',location='Pretoria',field='IT',passion='Sport' )

print(user_profile)
print(user_profile2)

# 8-14. Cars:
def car(manufacturer,model_name,**extra_info):
	car_info['Manufacturer:'] = manufacturer
	car_info['Model:'] = model_name
	return car_info
car1 = car('Bmw','M8 Competeition',colour='oranje',horsepower=625,price='R2 800 000' )

print(car1)

