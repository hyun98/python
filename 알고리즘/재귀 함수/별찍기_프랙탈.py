def line(a,b):             
    return ["".join(i) for i in zip(a,b,a)]

def map(n):
    if n==1:
        return ['*']
    n//=3
    f = map(n)
    a = line(f,f)
    b = line(f, [" "*n]*n)
    return a+b+a

if __name__=="__main__":
    n = int(input())
    print("\n".join(map(n)))