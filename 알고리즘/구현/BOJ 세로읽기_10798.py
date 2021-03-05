def read_vertical(wordlist: list):
    word = ""
    longword = ""
    for i in wordlist:
        if len(i) > len(longword):
            longword = i
    
    for i in range(len(longword)):
        for w in wordlist:
            try:
                word += w[i]
            except IndexError:
                pass
    
    print(word)

if __name__ == "__main__":
    wordlist = []
    for i in range(5):
        wordlist.append(input())
    read_vertical(wordlist)
    # wordlist = sorted(wordlist, key=lambda x : len(x[0]))
