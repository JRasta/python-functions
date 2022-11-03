# get input of an integer
num = (input('Enter an Integer: '))

# function that accepts user input
def square(num):
    # validate input is a digit
    if not num.isdigit():
        return 'Invalid Entry'

    # cast to an integer & return the result of the calculation
    num = int(num)
    return num * num


# run the function
print(f'{num}² is:', square(num))
