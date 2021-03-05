def check(g):
    if len(g)%2 == 1:
        print("NO")
        return 0
    else:
        if g[0] == ")" or ")" not in g:
            print("NO")
            return 0
        else:
            g = g.split("()")
            g = "".join(g)
            if len(g) == 0:
                print("YES")
                return 0
            else:
                check(g)
                return 0

if __name__ == "__main__":
    import sys
    N = int(input())
    for i in range(N):
        G = sys.stdin.readline().strip()
        check(G)