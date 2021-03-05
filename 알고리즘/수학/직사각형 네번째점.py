def find_point(x,y):
    x = sorted(x, key = lambda i : x.count(i))
    y = sorted(y, key = lambda i : y.count(i))
    x_4 = x[0]
    y_4 = y[0]
    print(f"{x_4} {y_4}")

if __name__=="__main__":
    x=[]
    y=[]
    for i in range(3):
        a,b = map(int, input().split())
        x.append(a)
        y.append(b)
    find_point(x,y)
