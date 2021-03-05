def avg_score(W, K):
	W = sorted(W, reverse=True)
	K = sorted(K, reverse=True)
	print(sum(W[:3]), sum(K[:3]))

if __name__ == "__main__":
	import sys
	W = []
	for _ in range(10):
		W.append(int(sys.stdin.readline()))
	K = []
	for _ in range(10):
		K.append(int(sys.stdin.readline()))
	avg_score(W, K)