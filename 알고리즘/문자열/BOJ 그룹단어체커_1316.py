def checker(N):
    import sys
    word = []
    count = N
    for i in range(N):
        word.append(sys.stdin.readline().strip("\n"))
    for i in range(N):
        save=[]
        jud=0
        for j in range(len(word[i])):
            if word[i][j] in save:              # 만약 알파벳이 save에 있고
                if word[i][j]!=word[i][j-1]:    # 이전과 다르다면 jud를 1 증가 시킴으로 표시(그룹 단어에서 제외)
                    jud+=1
            save.append(word[i][j])             # 알파벳을 하나씩 확인 후 리스트 save에 추가
        if jud>=1:                              
            count-=1
    print(count)

if __name__ == "__main__":
    N = int(input())
    checker(N)