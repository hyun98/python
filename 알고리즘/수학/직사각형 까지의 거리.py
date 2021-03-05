def distance(x,y,w,h):
    if sub(x,w)>=x:
        to_x = x
    else:
        to_x = sub(x,w)
    if sub(y,h)>=y:
        to_y = y
    else:
        to_y = sub(y,h)
    a = [to_x,to_y]
    print(min(a))

def sub(a,b):
    return abs(a-b)

if __name__=="__main__":
    x,y,w,h = map(int, input().split())
    distance(x,y,w,h)