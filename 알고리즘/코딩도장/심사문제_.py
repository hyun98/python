keys = input().split()
values = map(int, input().split())
 
x = dict(zip(keys, values))

del x['delta']
for i in range(len(keys)):
    if x.get(keys[i]) == 30:
        del x[keys[i]]

print(x)    