def balance(lang):
    stack = []
    for j in lang:
        if j in "([":
            stack.append(j)
        elif  j == ")":
            if not stack or stack.pop() != "(":
                print("no")
                break
        elif j == "]":
            if not stack or stack.pop() != "[":
                print("no")
                break
        elif j == ".":
            if stack:
                print("no")
                break
            else:
                print("yes")
                break
            
if __name__ == "__main__":
    import sys
    while(1):
        lang = sys.stdin.readline().strip("\n")
        if lang == ".":
            break
        else:
            balance(lang)
