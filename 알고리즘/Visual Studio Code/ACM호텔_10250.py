def hotel_room_num_ord(h,w):
	room_num=[]
	for i in range(1,w+1):
		for j in range(1,h+1):
			room_num.append(j*100+i)
	return room_num

test_case = int(input())
for i in range(test_case):
	H, W, N = map(int, input().split())
	order = hotel_room_num_ord(H,W)
	print(order[N-1])