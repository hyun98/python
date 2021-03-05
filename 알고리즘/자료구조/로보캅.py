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

def loc(all_c, times):
    circum = len(all_c)-1
    print(all_c)

    for t in times:
        lt = t % circum
        result = list(map(str, all_c[lt]))
        print(" ".join(result))

K = int(input())
coord = []
for i in range(K):
    coord.append(list(map(int, input().split())))
times = list(map(int, input().split()))
loc(coord_list(coord), times)
