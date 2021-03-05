a,b = map(list, input().split())
a.reverse()
b.reverse()
if len(a)!=len(b):
    if len(a)>len(b):
        print("".join(a))
    else:
        print("".join(b))
else:
    for i in range(len(a)):
        if a[i]>b[i]:
            print("".join(a))
            break
        elif b[i]>a[i]:
            print("".join(b))
            break
        else:
            continue
