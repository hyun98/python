with open('words.txt', 'r') as file:
	s = file.read()

words = s.split('\n')
pail=[]
for i in words:
	if i == i[::-1]:
		pail.append(i)
for i in pail:
	print(i)