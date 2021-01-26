# 2-1 Simple Message:
message = ' Hello world'
print(message.title())
# 2-2 Simple Message:
message = ' Hello world, lets program!'
print(message.title())
# 2-3 Personal Message:
name = "eric"
print(f' Hello {name.title()}, would you like to learn sme Python today?\n')

#2-4 famous quote:
famous_person = "Albert Einstein"

print(famous_person.lower())
print(famous_person.upper())
print(famous_person.title())

# 2-5 famous quote:
quote = "Albert Einstein once said, “A person who never made a mistake never tried anything new.”"
print(quote)
# When quoting use double quotation. or single at the end.!

# print('\n')
# quote = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
# print(quote)

#2-6 
famous_person = "Albert Einstein"
message ='A person who never made a mistake never tried anything new.'
print(f'{famous_person} once said, "{message}" ')

# 2-7
name = " John "
print(name.rstrip())
print('\n')
print(f'\n {name.lstrip()}')
# it is important to use the format here.
print(name.strip())