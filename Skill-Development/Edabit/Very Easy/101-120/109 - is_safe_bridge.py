def is_safe_bridge(blocks):
    # single line if statement
    # value_when_true if condition else value_when_false

    print("True") if " " not in blocks else print("False")

is_safe_bridge("####") # True
is_safe_bridge("## ####") # False
is_safe_bridge("#") # True
is_safe_bridge("# #") # False
