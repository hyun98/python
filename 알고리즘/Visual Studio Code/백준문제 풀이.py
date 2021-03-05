import sys
n1 = 0
n2=0
while n1!=0 and n2!=0:
      n1, n2 = map(int, sys.stdin.readline().split())
      sum = n1+n2
      print(sum)
