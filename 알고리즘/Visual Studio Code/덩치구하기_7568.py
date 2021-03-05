def size_rank(people):
	rank=[]
	
	for i in range(len(people)):
		p=0
		for j in range(len(people)):
			if people[j][0]>people[i][0] and people[j][1]>people[i][1]:
				p+=1
		rank.append(p+1)
	rank = map(str, rank)  #rank의 각 요소들을 str로 변환
	R = ' '.join(rank)	#rank의 각 요소들을 공백을 사이에 넣어 str로 변환
	print(R)

if __name__ =="__main__":
	N = int(input())
	people=[]
	for i in range(N):
		stat = list(map(int, input().split()))		
		people.append(stat)
	size_rank(people)