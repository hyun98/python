class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while(1):
    try:
        print("남은 치킨 : {0}".format(chicken))
        order = int(input("몇 마리 주문 하시겠습니까? : "))
        if order <= 0:
            raise ValueError
        elif order > chicken:
            print("재료 부족")
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다."\
                  .format(waiting,order))
            waiting+=1
            chicken-=order
        if chicken == 0:
            raise SoldOutError

    except ValueError:
        print("잘못된 값을 입력했어요")
    except SoldOutError:
        print("재료 소진. 판매를 종료합니다.")
        break

