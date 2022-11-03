# import all functions from the regex expressions module
from re import *

pattern = compile('(^|\s)[-a-z/d_.]+@([-a-z/d]+\.)+[a-z]{1,6}(\s|$)]')

def get_address():
    address = input('Enter your email address: ')
    is_valid = pattern.match(address)

    if is_valid:
        print('Valid email address: ', is_valid.group())
    else:
        print('Invalid email address! Please re-try...\n')


get_address()
