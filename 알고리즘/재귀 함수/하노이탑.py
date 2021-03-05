#하노이탑 공식 2^n-1
n = int(input())
count = pow(2,n)-1
print(count)

def hanoi_loop(a,b,c,n):
	if(n==1):
		print("{0} {1}".format(a,c)) # 원판이 하나일때. 1번에서 3번으로 
	else:
		hanoi_loop(a,c,b,n-1) 	#1단계. 원판 n-1개를 2번으로 옮기기
		print("{0} {1}".format(a,c))  #2단계. 가장 큰 원판을 3번으로 옮기기
		hanoi_loop(b,a,c,n-1)   #3단계. 원판 n-1개를 3번으로 옮기기

hanoi_loop(1,2,3,n)