import sys
import math
A, B, V = map(int, sys.stdin.readline().split())
a = math.ceil((V-A)/(A-B))
print("{0}".format(a+1))