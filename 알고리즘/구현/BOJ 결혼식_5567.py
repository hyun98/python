def inspect(friends:list):
	sangfriend = []
	invited = []
	for i in friends:
		if "1" in i:
			sangfriend.append(i)
			invited.extend(i)
	sangfriend.sort()

	n_sangfriend = []
	for i in friends:
		if i not in sangfriend:
			n_sangfriend.append(i)
	
	count = 0
	for i in sangfriend:
		for j in n_sangfriend:
			if i[1] in j:
				count += 1
				invited.extend(j)
	invited = list(set(invited))
	print(len(invited)-1)

if __name__ == "__main__":
	import sys
	N = int(sys.stdin.readline())
	M = int(sys.stdin.readline())
	friends = []
	for i in range(M):
		friends.append(list(map(str, sys.stdin.readline().split())))
	inspect(friends)