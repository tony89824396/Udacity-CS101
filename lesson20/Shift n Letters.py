
def shift_n_letters(a, n):
    if ord(a)+n >= (97+25):
        new=(ord(a)+n)-(97+25)-1+97
        return chr(new)
    elif ord(a)+n <97:
        new=(ord(a)+n) -97 +1+ (97+25)
        return chr(new)
    else:
        return chr(ord(a)+n)
