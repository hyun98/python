# class tile:
#     def __init__(self):
#         self.num = [1, 1, 2]
    
#     def binary(self, n):
#         if len(self.num) > n:
#             return self.num[n]
        
#         self.num.append(self.binary(n-2) + self.binary(n-1))

#         return self.num[n]

# if __name__ =="__main__":
#     import sys
#     n = int(sys.stdin.readline())
#     c = tile()
#     print(c.binary(n)%15746)


# 위 방식대로 하면 n이 21이 되는 시점부터 값이 이상하게 나옴
# 피보나치 구할 때 아래 방법이 메모리를 적게 먹는 방법임을 알고감

import sys

N = int(sys.stdin.readline())

a, b = 1, 2
for _ in range(N-1):
    a, b = b, (a+b) % 15746

print(a)