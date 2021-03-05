def score(mush):
    a=0
    b=0
    for i in range(10):
        a += mush[i]
        if a > 100:
            break
        elif a == 100:
            print(a)
            return 0
        b += mush[i]

    if (a-100) <= (100-b):
        print(a)
    else:
        print(b)

if __name__ == "__main__":
    mush = []
    for i in range(10):
        mush.append(int(input()))
    score(mush)