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

def the_number_of_prime(arr):
    count=0
    for i in arr:
        count+=prime_checker(i)
    print(count)

if __name__=="__main__":
    import sys
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    the_number_of_prime(arr)