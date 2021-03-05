def v_num(N):
	num=0
	while(N>0):
		if N%5==0:
			num += N/5
			print(int(num))
			return 0
		else:
			N-=3
			num+=1
	if(N==0):
		print(int(num))
	else:
		print("-1")

N=int(input())
v_num(N)