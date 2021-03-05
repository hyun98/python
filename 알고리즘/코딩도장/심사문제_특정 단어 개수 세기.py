s = input()
word = s.split()
c=0
for i in range(len(word)):
    if 'the' in word[i]:
        a = word[i].strip(',.')
        if a=="the":
            c+=1
print(c)
