from random import*
# 유닛 클래스
class unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 생성되었습니다.".format(self.name))

    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0} : {1}시 방향으로 이동. [속도 : {2}]"\
              .format(self.name, location, self.speed))
    def damaged(self,dmg):
        print("")
        self.hp -= dmg
        print("{0}, {1}데미지를 공격받았습니다.\
         현재체력은 {2}입니다.".format(self.name, dmg, self.hp))
        if self.hp <= 0:
            print("{0} : die".format(self.name))

# 공격 유닛 클래스
class attakunit(unit):
    def __init__(self, name, hp, speed, dmg):
        unit.__init__(self, name, hp, speed)
        self.dmg = dmg
    def attak(self,location):
        print("{0} : {1}방향으로 공격합니다. 공격력 : {2}".\
              format(self.name, location, self.dmg))

class Marin(attakunit):
    def __init__(self):
        attakunit.__init__(self, "Marin",40, 1, 6)
    def stimpack(self):
        if self.hp>10:
            self.hp-=10
            print("{0} 스팀팩 사용. 체력 10 감소".format(self.name))
        else:
            print("{0} 체력이 부족합니다.".foramt(self.name))

class Tank(attakunit):
    seize_developed = False

    def __init__(self):
        attakunit.__init__(self, "Tank", 150, 3, 30)
        self.seizemode = False

    def set_seize(self):
        if Tank.seize_developed == False:
            return
        if self.seizemode == False:
            print("{0} 시즈모드 전환".format(self.name))
            self.dmg = 70
            self.seizemode = True
        else:
            print("{0} 퉁퉁포로 전환".format(self.name))
            self.dmg = 30
            self.seizemode = False

# 날 수 있는 유닛 클래스
class flyunit:
    def __init__(self, f_speed):
        self.f_speed = f_speed

    def fly(self, name, location):
        print("{0} : {1}시방향으로 날아갑니다 [속도 : {2}]".format(name, location, self.f_speed))

# 공중 공격유닛 클래스
class fly_attakunit(attakunit, flyunit):
    def __init__(self, name, hp, dmg, f_speed):
        attakunit.__init__(self, name, hp, 0, dmg)
        flyunit.__init__(self, f_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(fly_attakunit):
    clocking_developed = False
    def __init__(self):
        fly_attakunit.__init__(self, "Wraith", 120, 8, 10)
        self.clocking = False

    def set_clocking(self):
        if not Wraith.clocking_developed:
            return

        if not self.clocking:
            print("{0} 클로킹사용.".format(self.name))
            self.clocking = True
        else:
            print("{0} 클로킹 해제".format(self.name))
            self.clocking = False

    def damaged(self, dmg):  # 매서드 오버라이딩.
        # 레이스 클래스를 받은 객체가 damaged 매서드를 사용할 때는\
        # 부모클래스 매서드가 아닌 오버라이딩한 매서드가 출력된다.
        if self.clocking:
            print("{0} 는 클로킹 상태이므로 공격받지 않습니다.".format(self.name))



# 건물
class Building(unit):
    def __init__(self,name, hp, location):
        #unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)  # 슈퍼 일때는 self 를 생략한다
        self.location = location

def game_start():
    print("새로운 게임을 시작합니다.")

def game_over():
    print("player : GG")
    print("Player 님이 퇴장했습니다.")

game_start() # 게임 시작

m1 = Marin() #마린 3기 뽑음
m2 = Marin()
m3 = Marin()

t1 = Tank()  # 탱크 2기 뽑음
t2 = Tank()

w1 = Wraith()  # 레이스 2기 뽑음
w2 = Wraith()

attack_units = []  # 유닛들 부대지정
attack_units.append(m1) # 부대에 유닛 추가
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)
attack_units.append(w2)

for unit in attack_units: # 1시로 이동
    unit.move("1")

Tank.seize_developed = True # 시즈모드 개발
print("시즈모드 개발완료")
Wraith.clocking_developed = True # 클로킹 개발
print("클로킹 개발완료")

for unit in attack_units:  # 각 유닛의 클래스 소속을 확인해서 스팀\
    # 팩을 사용할지 다른 것을 사용할지 정하기
    if isinstance(unit, Marin):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize()
    elif isinstance(unit, Wraith):
        unit.set_clocking()

for unit in attack_units:  # 1시로 공격
    unit.attak("1")

for unit in attack_units:   # 공격을 받음  받은 데미지는 무작위
    if isinstance(unit,Wraith):
        unit.damaged(randint(5,51))
    else:
        unit.damaged(randint(5,151))

game_over()