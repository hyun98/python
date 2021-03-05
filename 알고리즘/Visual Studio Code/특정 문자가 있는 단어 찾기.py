with open('words.txt', 'r') as file:
	s = file.read()

text = s.split()
for i in text:
	if 'c' in i:
		print(i.strip(',.'))