cost = input()
won = cost.split(';')
won = list(map(int, won))
won.sort()
won.reverse()
for i in range(len(won)):
    print("{:9,}".format(int(won[i])))