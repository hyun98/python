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

def prime_count(a):
    count=0
    for i in range(a+1,2*a+1):
        count+=prime_checker(i)

    print(count)

if __name__=="__main__":
    while (1):
        a = int(input())
        if a==0:
            break
        prime_count(a)
        
