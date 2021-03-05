def han_num(N):
    count = 0
    if (N<100):
        print("{0}".format(N))
    else:
        count+=99
        for i in range(100,N+1):
            if(i//100-(i%100)//10)==((i%100)//10-i%10):
                count+=1
        print("%d" %count)

n = int(input())
han_num(n)