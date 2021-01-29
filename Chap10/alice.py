filename = 'text_folder/alice.txt'
try:
	with open(filename, encoding='utf-8') as f:
		# utf-8 gives it the ability to read the file name in any language.
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")
else:
# Count the approximate number of words in the file.
	words = contents.split()
	num_words = len(words)
	print(f"The file {filename} has about {num_words} words.")