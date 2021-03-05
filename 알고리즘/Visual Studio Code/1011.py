test_case = int(input()) # 아 모르겠다
for i in range(test_case):
    x,y=map(int,input().split())
    d=0
    k=1
    if y-1==x:
        d+=1
        print(d)
    elif y-2==x:
        d+=2
        print(d)
    else:
        d+=2
        y-=2
        while(y > x):
            if(y-x <= k or y-x <= k+1):
                d+=1
                print(d)
                break
            else:
                y=y-(k+1)
                k+=1
                d+=1