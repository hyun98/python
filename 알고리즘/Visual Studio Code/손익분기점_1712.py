import sys
a, b, c = map(int, sys.stdin.readline().split())
p=0
if b>=c:
	print("-1")
else:
	while((c-b)*p<=a):
		p+=1
	print(p)