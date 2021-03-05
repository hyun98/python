word = input('단어를 입력하세요 ')

is_pail = True
for i in range(len(word)//2):
	if word[i] != word[-1-i]:
		is_pail = False
		break

print(is_pail)

print(word == word[::-1])

print(list(word) == list(reversed(word)))

print(word == "".join(reversed(word)))
