"""
a = this is a string
a = a.split("") # a is converted to a list of strings.
print a
['this', 'is', 'a', 'string']

a = "-".join(a)
print a
this-is-a-string
"""

# Function
def split_and_join(s):
    return s.replace(" ", "-")


# # Main method
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
