
def replace_strings(string, length):
    solution = ''
    for char in range(0, length):
        # print (char)
        if string[char] != ' ':
            solution += string[char]
        elif string[char] == ' ':
            solution += '%20'
        else:
            raise TypeError
    return solution

if __name__ == '__main__':
    print (replace_strings('Mr John Smith    ', 13))
    assert replace_strings('Mr John Smith    ', 13) == 'Mr%20John%20Smith'
    print (replace_strings('   fjs  ekjekwe ww  ddqwdq  ffw2344 1123', 40))