N=int(input())
k=1
i=0
if N==1:
	print(1)
else:
	while(k<N):
		i+=1
		k = k+6*i
	print(i+1)
