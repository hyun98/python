def turret(x_1, y_1, r_1, x_2, y_2, r_2):
    import math
    dist_1_2 = math.sqrt((y_2-y_1)**2 + (x_2 - x_1)**2)
    # 두 원의 중심이 같을 때
    if dist_1_2 == 0:
        if r_1 == r_2:
            print(-1)
        else:
            print(0)
    
    # 교점이 2개일 때
    elif dist_1_2 < r_1 + r_2:
            print(2)
    
    # 한 원의 중심이 다른 한 원의 내부에 있을 때

def main():
    n = int(input())
    for i in range(n):
        x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
        turret(x_1, y_1, r_1, x_2, y_2, r_2)

if __name__ == "__main__":
    main()
