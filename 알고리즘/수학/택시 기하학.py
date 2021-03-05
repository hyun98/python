pi = 3.141592653589793238462643383279

def euclid(r):
    area = r*r*pi
    print(f"{area:.6f}")
    
def taxi(r):
    area = 2*r*r
    print(f"{area:.6f}")

if __name__=="__main__":
    r = int(input())
    euclid(r)
    taxi(r)
