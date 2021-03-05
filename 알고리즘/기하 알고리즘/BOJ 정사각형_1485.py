import math
class Square:
    def __init__(self, point:list):
        self.p0 = point[0]
        self.p1 = point[1]
        self.p2 = point[2]
        self.p3 = point[3]
    def is_square(self):
        stool1 = distance(self.p0, self.p1)
        stool2 = distance(self.p0, self.p2)
        stool3 = distance(self.p2, self.p3)
        stool4 = distance(self.p1, self.p3)
        if stool1 == stool2 and stool1 == stool3 and stool1 == stool4:
            if distance(self.p0, self.p3) == distance(self.p1, self.p2):
                return 1
            else:
                return 0
        else:
            return 0
        
def distance(a:list, b:list):
    D = math.sqrt(pow((b[1]-a[1]), 2) + pow((b[0]-a[0]), 2))
    return D

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        s = []
        for _ in range(4):
            s.append(list(map(int, input().split())))
        s.sort()
        sq = Square(s)
        print(sq.is_square())
