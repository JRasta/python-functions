""" Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from
    strings of names to the string "online" or "offline", as seen above. Your function should return the number
    of people who are online """

""" Function for above problem """
def online_count(dic):
    count = 0

    for x in dic.values():
        if "online" in x:
            count += 1
    print(count)


""" Tests for above code """
test_data_01 = {"Bill": "online",
                "Ben": "offline",}

test_data_02 = {"Bill": "online",
                "Ben": "online",
                "Jill": "offline"}

test_data_03 = {"Bill": "online",
                "Ben": "online",
                "Jill": "online",
                "Jen": "offline",
                "Emily": "offline"}

test_data_04 = {"Bill": "online",
                "Ben": "online",
                "Jill": "offline",
                "Jen": "offline"}

online_count(test_data_01)
online_count(test_data_02)
online_count(test_data_03)
online_count(test_data_04)
