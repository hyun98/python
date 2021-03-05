from math import *

def line():
    print("---------------------")

def mul():
    print("(실수, 허수 순서로 입력)")
    a, b = map(float, input("첫 번째 복소수를 입력하세요 : ").split())
    c, d = map(float, input("두 번째 복소수를 입력하세요 : ").split())
    I = a*c + b*d*(-1)
    J = b*c + a*d

    if(J > 0):
        line()
        print(f"|  결과 : {round(I, 5)}+{round(J, 5)}j  |")
    elif(J < 0):
        line()
        print(f" 결과 : {round(I, 5)}{round(J, 5)}j")
    else:
        line()
        print(f" 결과 : {round(I, 5)}")
    
def to_phasor():
    print("(실수, 허수 순서로 입력)")
    a, b = map(float, input("복소수를 입력하세요 : ").split())
    
    Vm = sqrt(pow(a, 2) + pow(b, 2))
    x = b/a
    degree = degrees(atan(x))

    line()
    print(f"결과 : {round(Vm, 4)} ∠ {round(degree, 4)}")
    # print(f"삼각함수로 : {round(Vm, 3)}cos(wt + {round(degree, 3)})")

def to_compound():
    print("크기, 각도 순으로 입력")
    Vm, d = map(float, input("페이저를 입력하세요 : ").split())
    i = Vm * cos(radians(d))
    j = Vm * sin(radians(d))
    if(j > 0):
        print(f"{round(i, 4)}+{round(j, 4)}j")
    else:
        print(f"{round(i, 4)}{round(j, 4)}j")
        
def cal_start():
    while(1):
        line()
        print("1. 복소수의 곱셈")
        print("2. 복소수 -> 페이저")
        print("3. 페이저 -> 복소수")
        print("4. 종료")
        line()
        pick = int(input("원하는 작업을 선택하시오 : "))

        if(pick == 1):
            try:
                mul()
            except:
                print("잘못된 입력입니다.")
        elif(pick == 2):
            try:
                to_phasor()
            except:
                print("잘못된 입력입니다.")
        elif(pick == 3):
            try:
                to_compound()
            except:
                print("잘못된 입력입니다.")
        else:
            break

cal_start()
