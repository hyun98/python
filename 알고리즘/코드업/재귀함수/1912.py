def facto(n):
    if n == 1:
        return 1
    return n * facto(n-1)

if __name__ == "__main__":
    n = int(input())
    print(facto(n))
