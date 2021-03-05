def recur(n, i):
    if i > n:
        return 0
    print(i)
    return recur(n, i+1)

if __name__ == "__main__":
    n = int(input())
    recur(n, 1)