
def uniqueCheck (string):
    if len(string) > 128:
        return False
    char_set = [128]
    for i in string:
        if i in char_set:
            return False
        char_set.append(i)
    return True

if __name__ == '__main__':
    assert uniqueCheck('abcdefgh') == True
    assert uniqueCheck('aaaaabbbb') == False
    assert uniqueCheck('') == True
    assert uniqueCheck('abcdefgha') == False





