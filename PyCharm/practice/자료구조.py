#리스트
subway = [10,20,30]
print(subway)

subway = ['a', 'b', 'c']
print(subway.index('a'))  # a가 어디에 있는지 위치를 알려줌

subway.append('d')  # 마지막 칸에 d를 추가함
print(subway)

subway.insert(1, 'e')  # 1 인 위치에 e를 삽입
print(subway)

print(subway.pop)  # 맨 뒤에 1개의 원소를 꺼내고, 리스트에서 제거
print(subway)

subway.append('b')
print(subway.count('b'))  # 같은 값이 몇 번 나오는지 확인

num = [5,2,4,3]
num.sort()  # 정렬.
num.reverse()  # 뒤집어서 정렬
# num.clear()  # 리스트 내용 삭제

# 다양한 자료형 함께 사용 가능

num.extend(subway)  # 리스트 확장 가능. 리스트 끼리.
print(num)

#사전
cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3])  # 3번 key 의 value를 출력함
print(cabinet.get(3))  # 3번 key 의 value를 출력함
#print(cabinet[5])  # 없는 key를 출력하려고하면 프로그램이 종료됨
print(cabinet.get(5))  # 없는 key를 출력하려고 하면 None이라는 값이 출력된다.
print(cabinet.get(5, "사용가능"))  # ""사이에 있는 값을 출력해줌

print(3 in cabinet)  # True
print(5 in cabinet)  # False

cabinet = {"A-3" : "유재석", "A-100" : "김태호"}
cabinet["C-20"]="조세호"  # C-20이라는 key를 만들고 value에 조세호를 추가함.
                         # C-20에 이미 value값이 있으면 교체됨

del cabinet["A-3"]  # A-3에 해당하는 key, value 삭제
print(cabinet)

print(cabinet.keys())  # key들만 출력
print(cabinet.values())  # value들만 출력
print(cabinet.items())  # key, value 쌍으로 출력

cabinet.clear()  # 내용 삭제

#튜플
menu=("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스")  # 튜플은 값을 추가하거나 변경 불가능

name = "조현우"
age=23
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("조현우", 23, "코딩")
print(name, age, hobby)

#집합
#중복 안된, 순서없음
m_set = {1,2,3,3,3}
print(set)

java = {'a', 'b', 'c'}
python = set(['a', 'd'])  # 리스트를 묶어서 집합으로 만들 수 있음
print(java & python)  # java와 python의 교집합
print(java.intersection(python))  # java와 python의 교집합

print(java | python)  # java와 python의 합집합
print(java.union(python))  # java와 python의 합집합

print(java-python)  # java는 할 수 있지만 python은 못하는 사람
print(java.difference(python))

python.add("c")  # 값 추가
print(python)

java.remove("c")  # 값 제거

# 자료구조의 변경
menu = {'커피', '우유', '주스'}
print(menu, type(menu))
menu=list(menu)
print(menu, type(menu))
menu=tuple(menu)
print(menu, type(menu))
menu=set(menu)
print(menu, type(menu))

#Quiz
from random import*
apply = range(1,21)  # 1~20까지 숫자를 range 타입으로 생성
apply=list(apply)  # range 타입을 list 타입으로 변환
shuffle(apply)
print("---당첨자 발표---")
winner=sample(apply,4)
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨자 : {0}".format(winner[1:]))
print("--축하합니다--")

