name = input('Enter the filename: ')
handle = open(name)

counts = dict()
for line in handle:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1

print(counts['World'])