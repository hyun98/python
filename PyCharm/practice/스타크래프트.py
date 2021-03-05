import datetime
now = datetime.datetime.now()

class unit_prod:
    def __init__(self, name, hp, dmg, sup):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.sup = sup
        global now_supply
        global max_supply
        if (self.sup+now_supply)<=max_supply:
            now_supply+=self.sup
            print("{0} 출동준비 완료.".format(self.name))
            print("체력 : {0}, 공격력 : {1}".format(self.hp, self.dmg))
            print("인구수 {0}/{1}\n".format(now_supply, max_supply))
        elif (self.sup+now_supply)>max_supply:
            print("인구수 초과. 서플라이디팟 건설바람.\n")

class SCV(unit_prod):
    def __init__(self):
        unit_prod.__init__(self, "SCV", 60, 5, 1)

class Marin(unit_prod):
    stimpack_developed = False
    def __init__(self):
        unit_prod.__init__(self, "Marin", 40, 6, 1)

    def stimpack(self):
        if not Marin.stimpack_developed:
            return
        if self.hp > 10:
            self.hp -= 10
            print("StimPack!")
        else:
            print("not enough hp")

class Firebat(unit_prod):
    stimpack_developed = False
    def __init__(self):
        unit_prod.__init__(self, "Firebat", 50, 16, 1)

    def stimpack(self):
        if not Firebat.stimpack_developed:
            return
        if self.hp > 10:
            self.hp -= 10
            print("StimPack!")
        else:
            print("not enough hp")



# class structure_buil:
#     def __init__(self):

now_supply=0
max_supply=0
def command_center():
    print("커맨드를 선택 하였습니다.")
    print("S : SCV")
    q = input("무엇을 생산하시겠습니까?\n")
    if q == 'S' or q == 's':
        SCV()

def Barracks():
    print("{0}을 선택 하였습니다.".format("배럭"))
    print("M : marin\nF : firebat\nG : ghost\nC : medic")
    q = input("무엇을 생산하시겠습니까?\n")
    if q=='m'or q=='M':
        Marin()
    elif q == 'f' or q == 'F':
        Firebat()
    elif q=='g'or q=='G':
        unit_prod('ghost\n',45,10,1)
    elif q=='c'or q=='C':
        unit_prod('medic\n',60,0,1)

def Academy():
    print("{0}를 선택하였습니다.".format("아카데미"))
    print("무엇을 업그레이드 하시겠습니까?")
    print("t : stimpack")

def Factory():
    print("{0}을 선택 하였습니다.".format("팩토리"))
    print('V : vulture\nT : seize tank\nG : goliath')
    q=input("무엇을 생산하시겠습니까?\n")
    if q=='v'or q=='V':
        unit_prod('vulture\n',80,20,2)
    elif q=='t'or q=='T':
        unit_prod('seize tank\n',150,30,2)
    elif q=='g'or q=='G':
        unit_prod('goliath\n',120,12,2)

def Supply_depot():
    print("{0}을 건설합니다.".format("서플라이 디팟"))
    global max_supply
    max_supply+=8
    print("인구수{0}/{1}\n".format(now_supply,max_supply))

# class attack_unit:
#     def __init__(self,name,hp,dmg):
#         self.name=name
#         self.hp=hp
#         self.dmg=dmg
#
#     def attack(self,location):
#         print("{0} {1}시 방향으로 공격. 공격력 : {2}".format(self.name,\
#                                                    location,self.dmg))
mineral = 0
gas = 0
print(now)

# 블럭킹 모드 타이머
while (1):
    c = input("커맨드 : C\n배럭 : B\n팩토리 : F\n서플 : S\n")
    if (c == 'B')or(c=='b'):
        Barracks()
    elif c == 'C' or c == 'c':
        command_center()
    elif c=='S' or c=="s":
        Supply_depot()
    elif (c == 'F')or(c=='f'):
        Factory()

