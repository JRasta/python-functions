"""
You are given a string s.
s contains alphanumeric characters only.

Your task is to sort the string s in the following manner:
    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.
"""

# Main method
if __name__ == '__main__':
    s = input()
    lst, lower, upper, odd, even, final_lst = [], [], [], [], [], []

    for i in s:
        lst.append(i)

    for char in lst:
        if char.islower():
            lower.append(char)
            lower.sort()
        if char.isupper():
            upper.append(char)
            upper.sort()
        if char.isdigit():
            if int(char) % 2 == 0:
                even.append(char)
                even.sort()
            else:
                odd.append(char)
                odd.sort()

    if lower:
        final_lst.extend(lower)
    if upper:
        final_lst.extend(upper)
    if odd:
        final_lst.extend(odd)
    if even:
        final_lst.extend(even)

    print(''.join(final_lst))
