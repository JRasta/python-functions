# import all functions from the time module
from time import *

# create a variable that contains the current time in Epoch time
start_time = time()

# create an object to hold the current time object
struct_start = localtime(start_time)

# start the countdown
print('\nStarting Countdown at: ', strftime('%X', struct_start))
print()

# loop around for the amount of time required
i = 10
while i > 0:
    print(i)
    i -= 1
    sleep(1)  # wait for 1 second

# get the final end Epoch time
end_time = time()

# work out the difference between the start & end time
difference = round(end_time - start_time)

end_struct = localtime(end_time)
print('\nEnd of countdown:', strftime('%X', end_struct))

print('\nRuntime:', difference, 'seconds')
