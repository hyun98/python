# 1.화살표를 한 칸 아래로 내린다. (채널 i에서 i+1로)
# 2.화살표를 위로 한 칸 올린다. (채널 i에서 i-1로)
# 3.현재 선택한 채널을 한 칸 아래로 내린다. (채널 i와 i+1의 위치를 바꾼다. 화살표는 i+1을 가리키고 있는다)
# 4.현재 선택한 채널을 위로 한 칸 올린다. (채널 i와 i-1의 위치를 바꾼다. 화살표는 i-1을 가리키고 있다)

def setting(channel):
    K1 = channel.index("KBS1")
    K2 = channel.index("KBS2")
    result = ""
    if K1 < K2:
        for _ in range(K1):
            result+="1"
        for _ in range(K1):
            result+="4"
        for _ in range(K2):
            result+="1"
        for _ in range(K2-1):
            result+="4"
    else:
        for _ in range(K1):
            result+="1"
        for _ in range(K1):
            result+="4"
        for _ in range(K2+1):
            result+="1"
        for _ in range(K2):
            result+="4"
    print(result)

if __name__ == "__main__":
    import sys
    n = int(input())
    channel = []
    for _ in range(n):
        channel.append(sys.stdin.readline().strip())
    setting(channel)
