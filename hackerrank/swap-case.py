def swap_case(s):
    length = len(s)
    s1 = ""
    for i in range(length):
        if s[i].islower():
            s1 += s[i].upper()
        elif s[i].isupper():  # elif here for efficiency
            s1 += s[i].lower()
        else:  # this else block to include spaces, periods, and other characters
            s1 += s[i]
    return s1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)