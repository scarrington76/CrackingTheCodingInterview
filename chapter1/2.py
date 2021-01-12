
def permcheck (string1, string2):
    string1 = sorted(string1)
    string2 = sorted(string2)
    if len(string1) != len(string2):
        return False
    if string1 == string2:
        return True
    else:
        return False

if __name__ == '__main__':
    assert permcheck('badhat', 'hatbad') == True
    assert permcheck('', '') == True
    assert permcheck('twenty', 'tweety') == False
