N = int(input())
s=[]
a=666
while(len(s)!=N):
	st = str(a)
	if st.count('666')>=1:
		s.append(a)
	a+=1

print(s[N-1])