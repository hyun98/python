K = 0
apex = []  #꼭짓점 좌표
all_point = []   #전체 좌표

def solve(t:int):
    global all_point
    c1 = 0
    c2 = all_point.index(apex[int(K/2)-1])

    change = 0

    while(t > 0):
        if(c1 == c2 or c1+1 == c2):
            change+=1

        if(c1 == len(all_point)-1):
            c1 = 0
        else:
            c1+=1
    
        if(c2 == 0):
            c2 = len(all_point)-1
        else:
            c2-=1
        t-=1
    
    if(change % 2 == 1):
        print(all_point[c2][0], all_point[c2][1])
        print(all_point[c1][0], all_point[c1][1]) 
    else:
        print(all_point[c1][0], all_point[c1][1])
        print(all_point[c2][0], all_point[c2][1])
    


import copy
def circuit():
    global apex
    global all_point
    temp = copy.deepcopy(apex)
    temp.append(temp[0])

    for i in range(len(apex)):
        all_point.append(temp[i])
        if temp[i][0] == temp[i+1][0]:
            for j in range(1, abs(temp[i+1][1] - temp[i][1])):
                if temp[i+1][1] > temp[i][1]:
                    all_point.append([temp[i][0], temp[i][1] + j])
                else:
                    all_point.append([temp[i][0], temp[i][1] - j])

        elif temp[i][1] == temp[i+1][1]:
            for j in range(1, abs(temp[i+1][0] - temp[i][0])):
                if temp[i+1][0] > temp[i][0]:
                    all_point.append([temp[i][0]+j, temp[i][1]])
                else:
                    all_point.append([temp[i][0]-j, temp[i][1]])    


K = int(input())
for _ in range(K):
    apex.append(list(map(int, input().split())))

t = int(input())
circuit()
solve(t)
