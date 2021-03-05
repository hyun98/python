import sys
N, X = map(int, sys.stdin.readline().split())
A = map(int, sys.stdin.readline().split())
a = []
count = 0
for i in A:
    if i < X:
        a.append(i)
for i in range(len(a)):
    print("%d" %a[i], end=' ')


print(" ".join(map(str, a)))  # join 함수 : 68쪽

