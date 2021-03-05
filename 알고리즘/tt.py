#15686
import numpy as np
from itertools import combinations

N, M = map(int, input().split())
N_arr = [list(map(int,input().split())) for _ in range(N)]

house = [] # 1 - 집의 좌표
chicken = [] # 2 - 치킨집 좌표 , 치킨집으로부터 집까지 거리의 합


for i in range(N):
    for j in range(N):
        if N_arr[i][j] == 1:
            house.append((i,j))
        elif N_arr[i][j] == 2:
            chicken.append((i,j))

min_distance = 10000
for i in combinations(chicken, M): #튜플 형태로 나옴
    tmp = 0
    for h in house:
        m = 2*N
        for c in i:
            distance = abs(h[0]-c[0]) + abs(h[1]-c[1]) # 집과 치킨집 거리
            m = min(distance, m) # 선택된 집(h)에서 가장 가까운 치킨 집 거리 선택
        tmp += m # 선택된 집(h)에서 가장 가까운 치킨 집 거리 저장
    min_distance = min(min_distance,tmp) # 가장 작은 거리 선택

print(min_distance) # 출력