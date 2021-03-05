def rank(nation:list, K:int):
    count = 0
    for i in nation:
        if i[0] == K:
            for j in nation:
                count += compare(i, j)
    print(count+1)

def compare(i, j):
    for k in range(1, 4):
        if j[k] > i[k]:
            return 1
        elif i[k] > j[k]:
            return 0
    return 0

if __name__ == "__main__":
    N, K = map(int, input().split())
    nation = []
    for i in range(N):
        nation.append(list(map(int, input().split())))
    rank(nation, K)