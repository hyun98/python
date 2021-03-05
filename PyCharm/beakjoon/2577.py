A = int(input())
B = int(input())
C = int(input())
R = A*B*C
I = list(map(int, str(R)))
for i in range(10):
    print(I.count(i))
