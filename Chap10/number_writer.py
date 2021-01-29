import json
# Need json to use dump and load
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
# name of the file has to be.
with open(filename, 'w') as f:
	json.dump(numbers, f)
	