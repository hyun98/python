N = int(input())
ar=[]
for i in range(N):
	ar.append(int(input()))
ar.sort()
for i in range(N):
	print(ar[i])