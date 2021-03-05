def recur(n):
    if n == 0:
        return 0
    print(n)
    return recur(n-1)

if __name__ == "__main__":
    n = int(input())
    recur(n)
