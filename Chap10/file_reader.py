file_path = 'text_folder/pi_digits.txt'
# \\ are used when sing a window file path!

with open(file_path) as file_object:
	# contents = file_object.read()
# print(contents.rstrip())
# Reads the whole file.
	# for line in file_object:
	# 	print(line)  # Reading line for line
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()
	# makes it one line
print(pi_string)
print(len(pi_string))
# makes shure that there arn't any spaces from the right.