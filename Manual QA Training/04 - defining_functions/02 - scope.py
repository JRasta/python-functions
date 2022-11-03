# global variable
global_var = 1

# function to print the global variable
def scope():
    print('Global Variable:', global_var)

    # initialise a local variable within function
    local_var = 2
    print('Local Variable: ', local_var)

    # coerced global variable within function
    # NB: coerced global variables must be declared and initialised separately
    global inner_var
    inner_var = 3


# runs functions
scope()
print('Coerced Global: ', inner_var)
