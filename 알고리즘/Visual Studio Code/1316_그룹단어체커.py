N = int(input())
word = []
count = N

for i in range(N):
	word.append(input())
for i in range(N):
	save=[]
	jud=0
	for j in range(len(word[i])):
		if word[i][j] in save:
			if word[i][j]!=word[i][j-1]:
				jud+=1
		save.append(word[i][j])
	if jud>=1:
		count-=1
print(count)