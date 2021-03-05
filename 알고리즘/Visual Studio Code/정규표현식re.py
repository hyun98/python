def unix_match(filename: str, pattern: str) -> bool:
    import re
    pat = pattern.replace('.', '\.').replace('?', '.').replace('*', ".*")\
        .replace("[!", "[^").replace("[]", "[^.]").replace("[^]", "\[!\]")
    return re.match(pat, filename) is not None


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
