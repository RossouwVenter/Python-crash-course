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