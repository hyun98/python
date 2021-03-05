def r_triag(side):
    side.sort()
    if side[2]**2 == side[0]**2 + side[1]**2:
        print("right")
    else:
        print("wrong")

if __name__=="__main__":
    while(1):
        side = list(map(int, input().split()))
        if side[0]==0:
            break
        else:
            r_triag(side)