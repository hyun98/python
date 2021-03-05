n = int(input())
new = n
cy = 0
while 1:
    x = new // 10
    y = new % 10
    z = x + y
    new = (y*10) + (z % 10)
    cy += 1
    if (n == new):
        break

print(cy)