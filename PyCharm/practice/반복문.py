for wn in [0,1,2,3,4]:
    print("대기번호 : {0}".format(wn))
for wn in range(1,6):
    print(wn)

sb=['a', 'b', 'c']
for cu in sb:
    print("{0}".format(cu))


cu='a'
index=5
while(index>=1):
    print("{0}, {1}".format(cu,index))
    index-=1
    if index==0:
        print("ㅗ")

cu='a'
index = 1
while(1):  # 1대신 True를 넣어도 무방
    print("{0}, {1}".format(cu,index))
    index+=1
    if index==10:
        break

# cu='b'
# pe='U'
# while pe!=cu:
#     print("{0}".format(cu))
#     pe=input("name? : ")

ab=[2,5]
nb=[7]
for st in range(1,11):
    if st in ab:
        continue
    elif st in nb:
        print("{0} die".format(st))
        break
    print("{0}".format(st))

# 한 줄로 끝내는 for문
st = [1,2,3,4,5]
st=[i+100 for i in st]
print(st)

st = ['abcd', 'geshbdf', 'fsdf hetb']
kt=[len(i) for i in st]
print(st)

st = [i.upper() for i in st]
print(st)

#Quiz
index=0
from random import*
for i in range(1,51):
    temp=randrange(5,51)
    if 5<=temp<=15:
        print("[O] {0}번째 손님 (소요시간 : {1}분 )".format(i,temp))
        index+=1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분 )".format(i,temp))
print("총 승객 {0}명".format(index))

