def recur(a, b):
    if a > b:
        return 0

    if a%2 == 1:
        print(a, end=" ")
    return recur(a+1, b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    recur(a,b)
