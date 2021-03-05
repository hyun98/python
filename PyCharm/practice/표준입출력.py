print("python","java", sep=" vs ", end='?\n')
#sep : 문장 사이에 무엇이 들어갈지 설정해줌
#end : 문장이 끝나면 기본적으로 \n이 설정되어있는데 end를 사용하면 \n대신 ?나
# 공백을 사용할 수 있음
# import sys
# print("python","java",file=sys.stdout)
# print("python","java",file=sys.stderr)  # 표준 에러

scores={"수학":0, "영어":80, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8),str(score).rjust(4),sep=":")  # ljust(n) 왼쪽으로 n 칸 정렬

#for num in range(1,21):
    #print("대기번호 : "+str(num).zfill(3))  # zfill(n) : n자리로 숫자 출력.
                                                    # 입력되지않은 칸은 0으로 채움

#answer=input("아무노래나 그냥 틀어 : ")
#print("노래는 "+answer+"입니다.")

print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0:_<+10}".format(500))

#3자리마다 콤마를 찍어주기
print("{0:,}".format(10000000000))
print("{0:+,}".format(10000000000))  # 부호도 같이나옴

print("{0:^<+30,}".format(10000000000))

print("{0:.3f}".format(5/3))

