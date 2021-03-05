def prime_checker(n):
    if n==1:
        return 0
    else:
        d=2
        while n>=d*d:
            if n%d == 0:
                return 0
            d+=1
        return 1

def prime_list_to(n):
    prime_list=[]
    for i in range(2,n):
        if prime_checker(i):
            prime_list.append(i)
    return prime_list

def gold(arr,n):
    save=[]
    for i in arr:
        for j in arr:
            if i<=j and i+j==n:
                save.append([str(i),str(j)])
    print(" ".join(save[-1]))

if __name__=="__main__":
    import sys
    case = int(sys.stdin.readline())
    prime = prime_list_to(10000)
    for i in range(case):
        n = int(sys.stdin.readline())
        gold(prime,n)
