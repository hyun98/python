def generator(K):
	P=K
	N = list(str(K))
	sum = 0
	for i in N:
		sum+=int(i)
	new_number = P+sum
	return new_number

X = int(input())
min_num = 1000000
for i in range(X):
	if generator(i)==X and generator(i)<min_num:
		min_num = i
if min_num==1000000:
	print(0)
else:
	print(min_num)

