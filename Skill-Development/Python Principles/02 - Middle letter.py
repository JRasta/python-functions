""" Write a function named mid that takes a string as its parameter. Your function should extract and return the
middle letter. If there is no middle letter, your function should return the empty string """

""" Function for above problem """
def mid(x):
    temp = len(x)
    if temp % 2 != 0:
        len_temp = temp % 2
        result = x[len_temp]
    else:
        result = "String has an even letter count..."
    print(result)

""" Tests for above code """
mid("abc")         # "b"
mid("aaaa")        # ""
mid("fifth")       # "f"
mid("bbgghh")      # ""
mid("abcdefg")     # "d"
mid("ppiiooll")    # ""
mid("pilopilog")   # "p"
mid("pilopiloga")  # ""