class BignumberErr(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용")
    num = []
    num.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    num.append(int(input("두 번째 숫자를 입력하세요 : ")))
    num.append(int(num[0]/num[1]))
    if num[0]>=10 or num[1]>=10:
        raise BignumberErr("크와아아아앙")
    print("{0} / {1} = {2}".format(num[0],num[1],num[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except BignumberErr as er:
    print("error!")
    print(er)