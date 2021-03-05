# 다이나믹 프로그래밍 : 하나의 문제를 단 한번만 풀도록 하는 알고리즘
a = [0] * 91
def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if a[n] != 0:
        return a[n]
    a[n] = fibo(n-1) + fibo(n-2)
    return a[n]

if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    print(fibo(n))
