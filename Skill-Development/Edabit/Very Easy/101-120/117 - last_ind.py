def last_ind(lst):
    if not lst or lst is "":
        print("None")
    else:
        print(lst[-1])

last_ind([0, 4, 19, 34, 50, -9, 2]) # 2
last_ind(["Hello", "There", "Python", "User"]) # "User"
last_ind([]) # None
last_ind([True, False, False, True]) # True
last_ind([(5, 0), (0, 5, 6, 7), (3, 5, 67, 7), (0, -9, 3, 45, 5)]) # (0, -9, 3, 45, 5)
last_ind("Python is a great programming langauge.") # "."
last_ind(["H", "E", "L", "L", "O"]) # "O"
last_ind("The quick brown fox jumped over the lazy dog") # "g"
last_ind([{"name": "batman"}, {"kids": "none"}, {"parents": "also none"}]) # {"parents": "also none"}
last_ind("") # None