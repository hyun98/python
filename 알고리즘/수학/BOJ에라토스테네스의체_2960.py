# a = []*n
# a[i] = True / False 를 활용해서 다시 풀어보기
def prime(n, k):
    array = list(range(2, n+1))
    sieved = array
    deleted = []
    while(len(deleted) != k):
        m = min(sieved)
        for i in array:
            if i%m == 0:
                deleted.append(i)
                sieved.remove(i)
                if len(deleted) == k:
                    break
    print(deleted[-1])

if __name__ == "__main__":
    N, K = map(int, input().split())
    prime(N, K)
