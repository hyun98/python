import sys
sys.setrecursionlimit(1000000)
# 이게뭐람 어이가없네

def recur(n):
    if n == 1:
        return 1
    return n + recur(n-1)

if __name__ == "__main__":
    print(recur(int(input())))