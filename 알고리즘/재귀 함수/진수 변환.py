def any_to_de(s, r):
    if len(s)==1:
        return int(s[-1])
    else:
        return any_to_de(s[0:-1], r)*r + int(s[-1])

def de_to_any(n, r):
    if n < r:
        return str(n)
    else:
        return de_to_any(n//r, r) + de_to_any(n%r, r) 


if __name__=="__main__":
    num = input()
    print(f"{any_to_de(num,2)}")
