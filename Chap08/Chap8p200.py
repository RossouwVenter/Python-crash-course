# 8-3. T-Shirt:
# def make_shirt(size,text): 
#	print(f'The size of the shirt is: {size}.\n The following text will be printed on the foto: {text.title()}')

#make_shirt('M','No Pain No Gain')

# 8-4. Large Shirts:

def make_shirt(size,text='I Love Python'): 
	if size < 15:
		size = "Medium"
		print(f'The size of the shirt is: {size}.\nThe following text will be printed on the shirt: {text.title()}')
	else:
		size = "Large"
		print(f'The size of the shirt is: {size}.\nThe following text will be printed on the shirt: {text.title()}')

make_shirt(12)
# 8-5. Cities:
def describe_city(country,city):
	print(f'{city} is in {country}')
describe_city('Iceland','Reykjavik')
