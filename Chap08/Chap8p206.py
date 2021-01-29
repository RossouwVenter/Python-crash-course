# 8-6. City Names:
def city_country(city,country):
	print(f'{city.title()}, {country.title()}')

city_country("Santiago"," Chile")

# 8-7. Album:
print('\n')
def make_album(artistName,artistTitle):
	album ={'Name':artistName,'Title': artistTitle}
	return album
album = make_album('jimi','singer')
print(album)

# 8-8 User Albums:
print('\n')
def make_album(artistName,artistTitle):
	album ={'Name':artistName,'Title': artistTitle}
	return album
album = make_album('jimi','singer')
print(album)
print(album)

while True:
	print('Enter q to quit')
	artistName = input('Enter an artists name:')
	artistTitle = input('Enter an album name:')

	if (artistName or artistTitle == 'q'):
		break
	else:
		album = make_album(artistName,artistTitle)
