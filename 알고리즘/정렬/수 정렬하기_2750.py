#오름차순 정렬 함수 구현(정수만)
def sort(ar,n):
	for i in range(n-1):
		for j in range(i+1,n):
			if ar[i]>ar[j]:
				temp = ar[i]
				ar[i] = ar[j]
				ar[j] = temp
	for i in range(n):
		print(ar[i])

if __name__ =="__main__":
	N = int(input())
	ar=[]
	for i in range(N):
		ar.append(int(input()))
	sort(ar,N)