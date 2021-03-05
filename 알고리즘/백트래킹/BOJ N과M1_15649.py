def DFS(cnt):
	if cnt == M:
		print(" ".join(map(str, result)))
		return
		
	for i in range(N):
		if not check[i]:
			check[i] = True
			result.append(num[i])
			DFS(cnt+1)
			result.pop()
			check[i] = False

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
N, M = map(int, input().split())	# (1 ≤ M ≤ N ≤ 8)

result = []

check = [False] * N
num = [i+1 for i in range(N)]
DFS(0)

# from itertools import permutations
# N, M = map(int, input().split())
# P = permutations(range(1, N+1), M)  # iter(tuple)
# for i in P:
#     print(' '.join(map(str, i)))  # tuple -> str