def oa():
    print("new account is created")

def de(balance, money):
    print("입금 완료. 잔액은 {0}입니다.".format(balance+money))
    return balance+money
def wd(balance, money):
    if money>balance:
        print("돈없잖아")
    else:
        print("출금완료. 잔액 : {0}".format(balance-money))
        return balance-money
def wd_n(balance, money):
    com = 100  # 수수료
    if money+com > balance:
        print("돈없잖아")
    else:
        print("출금완료. 잔액 : {0}".format(balance - money-com))
        return balance - money - com

balance = 0  # 잔액
balance=de(balance, 1000)
#balance=wd(balance, 300)
balance=wd_n(balance,500)

#기본값
def profile(name, age, lang):
    print("이름 : {0}\n나이 : {1}\n주언어 : {2}"\
          .format(name, age, lang))  # 역슬래시를 붙이면 줄 바꿈 가능
profile('a', 23, 'python')
profile('b', 25, 'C')

def profile(name, age=17, lang='python'):  # 기본값을 설정한 함수
    print("이름 : {0}\n나이 : {1}\n주언어 : {2}"\
          .format(name, age, lang))
profile('a')
profile('b')

#키워드 값
def profile(name, age, lang):
    print("이름 : {0}   나이 : {1}\t주언어 : {2}".format(name, age, lang))
profile(name='a', lang='C', age=21)

#가변 인자
def profile(name, age, *lang):
    print("이름 : {0}   나이 : {1}".format(name,age), end=" ") # 끝낼때 줄바꿈을 하지않음
    for l in lang:
        print(l, end=" ")
    print()

profile("c",25,'python','java','C','C#','javascript ')
profile('e',35,'Kotlin', 'swift')

#지역변수, 전역변수
gun=10
def check(sol): # 경계근무
    global gun
    gun=gun-sol
    print("남은 총 : {0}".format(gun))
print("전체 총 : {0}".format(gun))
check(2)

def check_r(gun, sol):
    gun-=sol
    print("남은 총 : {0}".format(gun))
    return gun
gun = check_r(gun,5)

#Quiz
def std_weight(height,gender):
    if gender=='m':
        std=round((pow(height/100,2))*22,2)
        print("키 {0}cm인 남자의 표준 체중은 {1}kg입니다.".format(height,std))
    elif gender=='w':
        std = round(((height / 100) ^ 2) * 21,2)
        print("키 {0}cm인 여자의 표준 체중은 {1}kg입니다.".format(height, std))
std_weight(175,'m')