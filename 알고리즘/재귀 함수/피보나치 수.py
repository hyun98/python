def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)

if __name__=="__main__":
    n = int(input())
    print(f"{fibo(n)}")