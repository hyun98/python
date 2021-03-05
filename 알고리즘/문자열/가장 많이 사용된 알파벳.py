a = input()
a = a.lower()
alpha = "abcdefghijklmnopqrstuvwxyz"
alpha = list(alpha)
co=[]

for i in range(len(alpha)):
    co.append(a.count(alpha[i]))
co_2 = co[:]
co.sort()

if co[-1]==co[-2]:
    print("?")  
else:
    idx = co_2.index(co[-1])
    p = alpha[idx]
    print(p.upper())