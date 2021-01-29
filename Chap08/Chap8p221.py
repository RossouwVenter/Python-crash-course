# 8-15. Printing Models:
def printing_models():
	models = 'new'

# 8-16. Imports:
def build_profile(first, last, **user_info):
# """Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
user_profile2 = build_profile('Rossouw','Venter',location='Pretoria',field='IT',passion='Sport' )

print(user_profile)
print(user_profile2)

# 8-17. Styling Functions:

