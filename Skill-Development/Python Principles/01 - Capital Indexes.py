"""Write a function named capital_indexes. The function takes a single parameter, which is a string.
Your function should return a list of all the indexes in the string that have capital letters"""

"""Function for above problem"""
def capital_indexes(x):
    index_lst = []
    for index, letter in enumerate(x):
        if letter.isupper():
            index_lst.append(index)
    print(index_lst)

"""Tests for above code"""
capital_indexes("HeLlO")     # [0, 2, 4]
capital_indexes("BiLLyBoB")  # [0, 2, 3, 5, 7]
capital_indexes("GoodBYE")   # [0, 4, 5, 6]
capital_indexes("ThAnks")    # [0, 2]
capital_indexes("JaMeSSS")   # [0, 2, 4, 5, 6]
