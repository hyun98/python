def combination(n, r):
    return fac(n)//(fac(r)*fac(n-r))

def permutation(n, r):
    return fac(n)//fac(n-r)

def fac(n):
    if(n == 0):
        return 1
    elif(n == 1):
        return 1
    return n * fac(n-1)

n = int(input())
r = int(input())
print(f"{n} C {r} = ", combination(n, r))
print(f"{n} P {r} = ", permutation(n, r))