arr = []
for i in range(10):
    arr.append(int(input()) % 42)
a = set(arr)
print(len(a))
