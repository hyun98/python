arr = []
for i in range(9):
    arr.append(int(input()))
MAX = max(arr)
INDEX = arr.index(MAX)
print(MAX)
print(INDEX+1)