def move(c):
    global coord_lst
    for i, s in enumerate(coord):
        if c[0] == s:
            if c[1] == '+':
                try:
                    c[0] = coord_lst[i+1]
                except:
                    c[0] = coord_lst[0]

            elif c[1] == '-':
                try:
                    c[0] = coord_lst[i-1]
                except:
                    c[0] = coord_lst[-1]
            return c

def meet(A, B):
    if A[0] == B[0]:
        return True
    else:
        return False

def near(A, B):
    if abs(A[0][0] - B[0][0]) == 1 and A[0][1]==B[0][1]:
        return True
    elif abs(A[0][1] - B[0][1]) == 1 and A[0][0]==B[0][0]:
        return True
    else:
        return False

def robot_interaction(c1, c2, c3, t):
    global coord_lst

            

    print()
    print(c2)
    print(c3)

import copy
def coord_list(coord:list):
    temp = copy.deepcopy(coord)
    temp.append(temp[0])
    all_coord = []

    for i in range(len(coord)):
        all_coord.append(temp[i])
        if temp[i][0] == temp[i+1][0]:
            for j in range(1, abs(temp[i+1][1] - temp[i][1])):
                if temp[i+1][1] > temp[i][1]:
                    all_coord.append([temp[i][0], temp[i][1] + j])
                else:
                    all_coord.append([temp[i][0], temp[i][1] - j])

        elif temp[i][1] == temp[i+1][1]:
            for j in range(1, abs(temp[i+1][0] - temp[i][0])):
                if temp[i+1][0] > temp[i][0]:
                    all_coord.append([temp[i][0]+j, temp[i][1]])
                else:
                    all_coord.append([temp[i][0]-j, temp[i][1]])    
    
    return all_coord


if __name__ == "__main__":
    K = int(input())        # K <= 50
    coord = []
    for i in range(K):
        coord.append(list(map(int, input().split())))

    coord_lst = coord_list(coord)
    robot = []
    for i in range(3):
        x, y, d = input().split()
        robot.append([[int(x), int(y)], d])
    t = int(input())

    robot_interaction(robot[0], robot[1], robot[2], t)
