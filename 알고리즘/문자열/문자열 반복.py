def repeat():
    a = list(input().split())
    n = int(a[0])
    st = "".join(a[1:])
    word=""
    for i in range(len(st)):
        word+=st[i]*n
    print(word)

case = int(input())
for i in range(case):
    repeat()