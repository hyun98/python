def han_num(N):
    count = 0
    if (N<100):     # 길이가 2 이하인 수열은 모두 등차수열이라고 할 수 있다
        print(N)
    else:
        count+=99   # N 이 100보다 크면 99 개의 한수를 가지고 시작한다
        for i in range(100,N+1):
            if(i//100-(i%100)//10)==((i%100)//10-i%10):     # 100의자리와 10의자리 수의 차이와 10의 자리와 1의자리 수의 차이가 같으면 
                count+=1
        print(count)

if __name__ == "__main__":
    n = int(input())
    han_num(n)