A = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
B = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

row, col = map(int, input().split())
chess = []
for i in range(row):
	chess.append(list(input()))

t=64
for c in range(0,col-7):
	for r in range(0,row-7):
		temp_num = 0
		for i in range(r,r+8,2):
			for p in range(8):
				if chess[i][c+p] != A[p]:
					temp_num+=1
		for j in range(r+1,r+8,2):
			for k in range(8):
				if chess[j][c+k] != B[k]:
					temp_num+=1
		if temp_num < t:
			t = temp_num
		
		temp_num=0
		for i in range(r,r+8,2):
			for p in range(8):
				if chess[i][c+p] != B[p]:
					temp_num+=1	
		for j in range(r+1,r+8,2):
			for k in range(8):
				if chess[j][c+k] != A[k]:
					temp_num+=1
		if temp_num < t:
			t = temp_num

print(t)