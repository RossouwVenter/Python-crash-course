filename = 'text_folder/programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
# Writing text into the file.
	file_object.write("Python is fun\n")
	file_object.write("I love creating new programs")
	# 'w' overrides the file 
	# 'a' adds to the file!
	# 'r' reads the file.

