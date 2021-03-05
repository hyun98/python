def yootnori(yoot):
	if yoot.count(0) == 0:
		print("E")
	elif yoot.count(0) == 1:
		print("A")
	elif yoot.count(0) == 2:
		print("B")
	elif yoot.count(0) == 3:
		print("C")
	else:
		print("D")

if __name__ =="__main__":
	import sys
	for i in range(3):
		yoot = list(map(int, sys.stdin.readline().split()))
		yootnori(yoot)
