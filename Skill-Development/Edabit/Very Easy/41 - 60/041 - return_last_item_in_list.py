"""
Return the Last Element in a List

Create a function that accepts a list and returns the last item in the list.
The list can be either homogeneous or heterogeneous
"""

def get_last_item(lst):
    last_item = lst.pop()
    print(last_item)


get_last_item([1, 2, 3])
get_last_item(["cat", "dog", "duck"])
get_last_item([True, False, True])
get_last_item([7, "string", False])
