def sequence(data):
    cal = []
    make_s = []
    temp = []
    count = 0
    for i in range(1, data[0]+1):       # 첫 번째 데이터 먼저 스택에 넣음
        temp.append(i)      # 임시 수열에 i까지 숫자를 추가하며
        cal.append("+")
        count+=1            # 현재 숫자의 위치를 표시
        if i == data[0]:       # 임시 수열에 추가하는 숫자i가 데이터의 첫 번째 값이면 
            make_s.append(temp.pop())   # 그 숫자 i를 결과수열에 추가하고 i를 임시 수열에서 삭제
            cal.append("-")
    # 두 번째부터
    for i in range(1, len(data)):   # 1번 인덱스부터 데이터의 마지막 인덱스까지
        if data[i] > data[i-1]:     # i번 데이터가 바로 전 data보다 크면
            for j in range(count+1, data[i]+1):     # 현재 숫자의 위치+1 부터 data의 i번 값까지 증가
                temp.append(j)
                cal.append("+")
                count+=1
                if j == data[i]:        # i번 데이터와 j가 같아지면
                    make_s.append(temp.pop())   #temp 의 마지막원소를 결과수열에 추가
                    cal.append("-")
        else:
            if temp[-1] == data[i]:     # temp의 마지막 원소가 데이터의 현재 값 일때만
                make_s.append(temp.pop())   # temp에서 추출한 값을 결과수열에 추가
                cal.append("-")
            else:
                print("NO")
                return 0
    print("\n".join(cal))

if __name__ =="__main__":
    import sys
    n = int(input())
    data = []
    for i in range(n):
        data.append(int(sys.stdin.readline()))
    sequence(data)