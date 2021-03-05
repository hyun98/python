a,b = map(list, input().split())
a.reverse()
b.reverse()
A = 0
B = 0
for i in a:
	A = A*10 + int(i)
for i in b:
	B = B*10 + int(i)
if(A>B):
	print(A)
else:
	print(B)