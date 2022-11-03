file = open('example.txt', 'w')

print('\nFile Name:', file.name)
print('File Open Mode:', file.mode)

print('Readable:', file.readable())
print('Writeable:', file.writable())

def get_status(f):
    if f.closed:
        return 'Closed'
    else:
        return 'Open'


print('File status:', get_status(file))
file.close()
print('\nFile Status:', get_status(file))
