matrix = []
row, col = map(int, input().split())

for i in range(row):
    matrix.append(list(input()))

bomb_number = matrix.copy()
count=0

for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		if matrix[i][j]=='*':
			continue
		else:
			if j-1>=0:
				if matrix[i][j-1]=='*':
					count+=1
			if j+1<len(matrix[i]):
				if matrix[i][j+1]=='*':
					count+=1
			if i-1>=0:
				if matrix[i-1][j]=='*':
					count+=1
			if i+1<len(matrix):
				if matrix[i+1][j]=='*':
					count+=1
			if j-1>=0 and i-1>=0:
				if matrix[i-1][j-1]=='*':
					count+=1
			if j-1>=0 and i+1<len(matrix):
				if matrix[i+1][j-1]=='*':
					count+=1
			if j+1<len(matrix[i]) and i-1>=0:
				if matrix[i-1][j+1]=='*':
					count+=1
			if j+1<len(matrix[i]) and i+1<len(matrix):
				if matrix[i+1][j+1]=='*':
					count+=1
		bomb_number[i][j] = count
		count=0

for i in bomb_number:
	i = map(str, i)
	print(''.join(i))
