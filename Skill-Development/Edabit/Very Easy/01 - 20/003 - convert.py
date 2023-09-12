"""
Convert Minutes into Seconds

Write a function that takes an integer minutes and converts it to seconds
"""

def convert_mins_into_secs(mins):
    secs_total = mins * 60
    print(f'{mins} mins converted into seconds: {secs_total} secs')


convert_mins_into_secs(5)
convert_mins_into_secs(3)
convert_mins_into_secs(2)
