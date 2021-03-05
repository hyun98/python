ham = []
bev = []
for i in range(3):
    ham.append(int(input()))
for i in range(2):
    bev.append(int(input()))
s = []
for i in range(3):
    for j in range(2):
        s.append(ham[i]+bev[j])
print(min(s)-50)