import sys
def DBJ(n:int):
    not_heard_seen = []
    person = []
    for _ in range(n):
        not_heard_seen.append(sys.stdin.readline().strip("\n"))

    not_heard_seen.sort()
    for i, name in enumerate(not_heard_seen):
        try:
            if name == not_heard_seen[i+1]:
                person.append(name)
        except IndexError:
            pass
    
    print(len(person))
    for i in person:
        print(i)

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    DBJ(n+m)
