strng = "Hello World"

print(strng[6])

for ch in strng:
    print(ch)

print('Length = ', len(strng))

print(strng[0:5])
print(strng[6:])
print(strng[:3])

newStr = strng[:3] + 'p'
print(newStr)
print('Hel' in strng[:3])

print(strng.upper())
print(strng.lower())

print(strng.replace('World', 'Harun'))
print(strng)