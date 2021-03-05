def prime_checker(n):
    if n==1:
        return 0
    else:
        d=2
        while(n!=d):
            if n%d != 0:
                d+=1
            else:
                return 0
        if n==d:
            return 1

def prime_collect(arr):
    count=0
    prime_list=[]
    for i in arr:
        count+=prime_checker(i)
        if prime_checker(i)==1:
            prime_list.append(i)
    if count==0:
        print("-1")
    else:
        print(sum(prime_list))
        print(min(prime_list))

if __name__=="__main__":
    M = int(input())
    N = int(input())
    arr = list(range(M,N+1))
    prime_collect(arr)