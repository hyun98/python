class unit:
    def __init__(self):
        print("unit 생성자")
class flyable:
    def __init__(self):
        print("flyable 생성자")
class flyunit(unit, flyable):
    def __init__(self):
        unit.__init__(self)
        flyable.__init__(self)

#드랍쉽
dropship = flyunit()