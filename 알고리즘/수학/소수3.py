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

if __name__=="__main__":
    M,N = map(int, input().split())
    for i in range(M,N+1):
        if prime_checker(i):
            print(i)

def is_primary(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i==0:
            return False

        i += 1
    return True

start, end = map(int, input().split())
for i in range(start, end + 1):
    if is_primary(i):
        print(i)