def recur(empty, c):
	if empty // c == 0:
		return 0
	drink = 0
	drink += empty // c
	empty = drink + empty % c
	return drink + recur(empty, c)

if __name__ == "__main__":
	e, f, c = map(int, input().split())
	print(recur(e+f, c))