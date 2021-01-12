def palperm (string):
    counts = {}
    for char in string:
        if char in counts:
            counts[char] = counts[char] + 1
        elif char != ' ':
            counts[char] = 1
    print (counts)
    decider = 0
    for key, value in counts.items():
        if value % 2 == 1:
            decider += 1
    if decider != 1:
        return False
    return True


if __name__ == '__main__':
    print (palperm('tact coa'))
    print (palperm('2342 34ad'))
    print (palperm('aaffgghher'))
    print (palperm('hhggrreoett'))
