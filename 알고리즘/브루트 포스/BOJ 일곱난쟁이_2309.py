def findwarf(dwarf9:list):
    test = dwarf9[:]        # 얕은 복사와 깊은 복사의 차이를 알아야 함
    for i in range(8):
        for k in range(i+1,9):
            test.remove(dwarf9[i])
            test.remove(dwarf9[k])
            if sum(test) == 100:
                test.sort()
                for p in test:
                    print(p)
                return 0
            test = dwarf9[:]

if __name__ == "__main__":
    dwarf = []
    for i in range(9):
        dwarf.append(int(input()))
    findwarf(dwarf)

# 얕은 복사 : a = [1,2,3]  b = a  -> 이러면 a주소값에 있는 같은 객체를 바라보는 변수가 a 와 b로 두개 생긴 것이다
# 깊은 복사 : a = [1,2,3]  b = a[:]  ->  이러면 a와 b는 서로 다른 주소값을 가지게 되고 다른 객체를 바라보는 것이 된다