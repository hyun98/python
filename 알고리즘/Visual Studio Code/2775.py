def fibo(n):
    li=[]
    sum=0
    for i in range(len(n)):
        sum+=n[i]
        li.append(sum)
    return li

def floor_k_n(k,n):
    temp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    for i in range(k):
        floor_k = fibo(temp)
        temp = floor_k
    print(floor_k[n-1])

test_case = int(input())
for i in range(test_case):
    k=int(input())
    n=int(input())
    floor_k_n(k,n)
