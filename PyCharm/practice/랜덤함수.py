from random import *  # random 라이브러리 안에있는 모든 자료를 사용한다.

print(random())  # 0.0~1.0사이의 임의의 값 ex)0.8421654121653
print(random()*10)  # 0.0~10.0사이의 임의의 값
print(int(random()*10))  # 0~10사이의 임의의 값
print(int(random()*10)+1)  # 1~10이하의 임의의 값

# 로또 번호 구하기
print(int(random()*45)+1)  # 1~45이하의 임의의 값
print(randrange(1,46))  # 1~46미만의 임의의 값
print(randint(1,45))  # 1~45이하의 임의의 값

# 랜덤 함수 퀴즈
print("오프라인 날짜는 매월 {0}일로 선정되었습니다".format(randint(4,28)))

a = [1,2,3,4,5]