def fn(N): #N까지의 수의 합
	k=0
	for i in range(N):
		k+=i+1
	return k

def fibo_f(N): #N이 몇 번째 층에 있는지 알아내는 함수
	i=0 #층
	k=0
	while(k<N):
		i+=1
		k+=i
	# N은 i층에 있다.
	return i

def frac(N): #분수를 찾아 출력하는 함수
	if(fibo_f(N)%2==0): # 층이 짝수일 때
		de = fn(fibo_f(N)) - N + 1 #몇 번째 열 인지. n열 일때 분모는 n
		nu = N - fn(fibo_f(N)-1)  #몇 번째 행 인지. n행 일때 분자는 n
		print("{0}/{1}".format(nu,de))
	else: #층이 홀수일 때
		de = N - fn(fibo_f(N)-1) #몇 번째 열 인지. n열 일때 분모는 n
		nu = fn(fibo_f(N)) - N + 1  #몇 번째 행 인지. n행 일때 분자는 n
		print("{0}/{1}".format(nu,de))

N = int(input())
frac(N)