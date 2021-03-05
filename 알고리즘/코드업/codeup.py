n = int(input())
call = list(map(int, input().split()))
print(min(call))
attend = [0]*n
for i in range(n):
    attend[-1-i] = call[i]
attend = list(map(str, attend))
print(" ".join(attend))