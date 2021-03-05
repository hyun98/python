class count:
    def __init__(self):
        self.count_0 = [0] * 41
        self.count_1 = [0] * 41
        self.f = [0]*41
    
    def fibo(self, n):
        if n == 0:
            self.count_0[0] = 1
            return 0
        if n == 1:
            self.count_1[1] = 1
            return 1
        
        if self.f[n] != 0:
            if self.count_0[n] == 0:
                self.count_0[n] = self.count_0[n-1] + self.count_0[n-2]
            if self.count_1[n] == 0:
                self.count_1[n] = self.count_1[n-1] + self.count_1[n-2]
            return self.f[n]

        self.f[n] = self.fibo(n-1) + self.fibo(n-2)
        self.count_0[n] = self.count_0[n-1] + self.count_0[n-2]
        self.count_1[n] = self.count_1[n-1] + self.count_1[n-2]
        return self.f[n]

if __name__ == "__main__":
    import sys
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        c = count()
        a = c.fibo(n)
        print("{0} {1}".format(c.count_0[n], c.count_1[n]))