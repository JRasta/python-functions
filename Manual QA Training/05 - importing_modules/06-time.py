# import all the functions within module datetime
from datetime import *

today = datetime.today()
print('Today is:', today)
print('Today is:', datetime.today())  # uses the function call instead of assigning to a variable

print('\nPrints out the date time details on a separate line')

# uses a for loop to print out each individual portion of time, and it's equivalent value
for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print(attr, ':\t', getattr(today, attr))

# prints out the time in a readable format
print('\nTime: ', today.hour, ':', today.minute)

# strftime abbreviations (see below)
day = today.strftime('%A')  # converts the datetime.day variable to the full weekday name
month = today.strftime('%B')  # converts the datetime.month variable to the full month name

print('\nDate: ', day, month, today.day)
print('Date: ', day, str(today.day) + 'th', month)

# strftime abbreviations (watch out for the capitalisation of some characters)
# %A - Full weekday name
# %B - Full month name
# %c - Date & Time appropriate to locale
# %d - Day of the month (1-31)
# %f - Microsecond number (0-999999)
# %H - Hour number (0-23, 24-hr clock)
# %I - Hour number (1-12, 12-hr clock)
# %j - Day of the year (0-366)
# %m - Month number (1-12)
# %M - Minute number (0-59)
# %p - AM or PM for locale
# %S - Second number (0-59)
# %w - Week day number (0,Sunday - 6,Saturday)
# %W - Week of the year (0-53)
# %X - Time appropriate for locale
# %Y - Year (0-9999)
# %y - Year (00-99)
# %z - Timezone offset from UTC
# %Z - Timezone name



