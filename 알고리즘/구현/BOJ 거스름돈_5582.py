def left(n):
	coin = [500, 100, 50, 10, 5, 1]
	count = 0
	for c in coin:
		count += n//c
		n %= c
	print(count)

if __name__ == "__main__":
	n = int(input())
	left(1000-n)
