x = 5
c = 10
i = 0

while i < c:
	if i < x:
		print(i, '<', x)
	elif i == x:
		print(i, '=', x)
	else:
		print(i, '>', x)
	i+=1;

word = input("input a word: ")
print(word)