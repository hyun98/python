class FC:
    def __init__(self, first, second):  # 생성자 라고 함. 객체가 생성될 때
        # 자동으로 호출되는 매서드
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def div(self):
        result = self.first / self.second
class M(FC):
    def __init__(self, first, second):
        FC.__init__(self, first, second)
    def pow(self):
        result=self.first**self.second
        return result
class D(M):
    def __init__(self, first, second):
        M.__init__(self, first, second)
    def div(self):
        if self.second ==0:
            return 0
        else:
            return self.first/self.second
n1 = int(input("number 1 : "))
n2 = int(input("number 2 : "))
a = D(n1, n2)
print(a.div())


# class unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#     def move(self,location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1}시 방향으로 이동. [속도 : {2}]"\
#               .format(self.name, location, self.speed))
#
# a = unit("벌쳐", 80, 20)
# a.move("5")
#
# class attakunit(unit):
#     def __init__(self, name, hp, speed, dmg):
#         unit.__init__(self, name, hp, speed)
#         self.dmg = dmg
#     def attak(self,location):
#         print("{0} : {1}방향으로 공격합니다. 공격력 : {2}".\
#               format(self.name, location, self.dmg))
#     def damaged(self,dmg):
#         print("")
#         self.hp -= dmg
#         print("{0},공격 받았습니다. 현재체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : die".format(self.name))
#
# b = attakunit("마린",40, 5, 6)
# b.attak("5")
# b.damaged(25)
# b.move("1")